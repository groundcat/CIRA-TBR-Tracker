#!/usr/bin/env python3
"""
CIRA TBR Tracker - Analysis Script

Fetches the latest CIRA TBR (To-Be-Released) session results, archives the raw
JSON, recomputes all aggregate statistics across the full history, updates
tally.json, and regenerates README.md.

Run: python scripts/analyze.py
"""

import json
import sys
import statistics
from datetime import datetime, timezone, timedelta
from pathlib import Path
from collections import defaultdict
from urllib.request import urlopen
from urllib.error import URLError

from charts import generate_all_charts

API_URL = "https://api.ca.fury.ca/api/tbr/lastSessionResults"
ROOT = Path(__file__).parent.parent
DATA_DIR = ROOT / "data"

# ──────────────────────────────────────────────────────────────────────────────
# Data fetching & storage
# ──────────────────────────────────────────────────────────────────────────────

def fetch_session() -> dict:
    """Fetch latest TBR session results from API."""
    try:
        with urlopen(API_URL, timeout=30) as resp:
            return json.loads(resp.read())
    except URLError as e:
        print(f"[ERROR] Could not fetch {API_URL}: {e}", file=sys.stderr)
        sys.exit(1)


def save_raw(data: dict) -> Path:
    """Archive raw session data to data/YYYY/MM/DD.json. Idempotent."""
    dt = _parse_dt(data["releaseDate"])
    path = DATA_DIR / f"{dt.year:04d}" / f"{dt.month:02d}" / f"{dt.day:02d}.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False))
    return path


def load_all_sessions() -> list:
    """Return all archived session dicts sorted chronologically."""
    return [
        json.loads(p.read_text())
        for p in sorted(DATA_DIR.rglob("*.json"))
    ]


# ──────────────────────────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────────────────────────

def _parse_dt(s: str) -> datetime:
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def _session_start(release_dt: datetime) -> datetime:
    """Official session open time: same date at 19:00:00.000 UTC."""
    return release_dt.replace(hour=19, minute=0, second=0, microsecond=0)


def _session_date(session: dict) -> str:
    return _parse_dt(session["releaseDate"]).strftime("%Y-%m-%d")


def _percentile(sorted_vals: list, p: float):
    """Return the p-th percentile (0–1) of an already-sorted list."""
    if not sorted_vals:
        return None
    idx = min(int(len(sorted_vals) * p), len(sorted_vals) - 1)
    return sorted_vals[idx]


# ──────────────────────────────────────────────────────────────────────────────
# Per-session statistics
# ──────────────────────────────────────────────────────────────────────────────

def compute_session_stats(session: dict) -> dict:
    """
    Compute comprehensive statistics for a single TBR session.

    Latency is measured from the official session open time (19:00:00.000 UTC)
    to each domain's registration timestamp.
    """
    release_dt = _parse_dt(session["releaseDate"])
    session_open = _session_start(release_dt)
    domains = session.get("domains", [])
    n = len(domains)

    # ── Build per-registrar latency lists ────────────────────────────────────
    reg_latencies: dict[str, list] = defaultdict(list)
    all_latencies: list[int] = []

    for d in domains:
        ts = _parse_dt(d["timestamp"])
        lat_ms = int((ts - session_open).total_seconds() * 1000)
        all_latencies.append(lat_ms)
        reg_latencies[d["registrarName"]].append(lat_ms)

    all_latencies.sort()

    # ── Registrar breakdown ───────────────────────────────────────────────────
    registrar_breakdown = {}
    for reg, lats in sorted(reg_latencies.items(), key=lambda x: -len(x[1])):
        s_lats = sorted(lats)
        count = len(lats)
        registrar_breakdown[reg] = {
            "domain_count": count,
            "market_share_pct": round(count / n * 100, 2) if n else 0,
            "capture_latency_min_ms":    s_lats[0],
            "capture_latency_median_ms": int(statistics.median(s_lats)),
            "capture_latency_mean_ms":   round(statistics.mean(s_lats), 1),
            "capture_latency_p95_ms":    _percentile(s_lats, 0.95),
            "capture_latency_max_ms":    s_lats[-1],
            "capture_latency_stdev_ms":  round(statistics.stdev(s_lats), 1) if count >= 2 else 0,
        }

    # ── Timing distribution (captures binned by second from session open) ────
    timing_dist_by_second: dict[int, int] = defaultdict(int)
    for lat in all_latencies:
        timing_dist_by_second[lat // 1000] += 1

    # ── Market concentration: Herfindahl-Hirschman Index ─────────────────────
    shares = [v["market_share_pct"] for v in registrar_breakdown.values()]
    hhi = round(sum(s ** 2 for s in shares), 1)

    return {
        "date": _session_date(session),
        "release_timestamp": session["releaseDate"],
        "domains_released":     session.get("numberOfDomainNames", n),
        "domains_registered":   n,
        "registration_rate_pct": round(n / session.get("numberOfDomainNames", n) * 100, 2)
                                 if session.get("numberOfDomainNames", n) else 0,
        "unique_registrars":    len(registrar_breakdown),
        # Session-wide latency summary
        "capture_latency_min_ms":    all_latencies[0]  if all_latencies else None,
        "capture_latency_median_ms": int(statistics.median(all_latencies)) if all_latencies else None,
        "capture_latency_mean_ms":   round(statistics.mean(all_latencies), 1) if all_latencies else None,
        "capture_latency_p95_ms":    _percentile(all_latencies, 0.95),
        "capture_latency_max_ms":    all_latencies[-1] if all_latencies else None,
        # Total span first→last capture
        "session_duration_ms": (all_latencies[-1] - all_latencies[0]) if len(all_latencies) >= 2 else 0,
        # Market concentration
        "market_concentration_hhi": hhi,
        "top_registrar": next(iter(registrar_breakdown)) if registrar_breakdown else None,
        "registrar_breakdown": registrar_breakdown,
        # Timing histogram (second offset from 19:00:00 → domain count)
        "timing_distribution_by_second": {
            str(k): v for k, v in sorted(timing_dist_by_second.items())
        },
    }


# ──────────────────────────────────────────────────────────────────────────────
# Aggregate statistics (across multiple sessions)
# ──────────────────────────────────────────────────────────────────────────────

def aggregate_stats(session_stats_list: list, label: str) -> dict:
    """
    Aggregate per-session stats into a multi-session summary.

    Note: cross-session latency figures are computed as the mean of per-session
    means (weighted by domain count where possible).
    """
    if not session_stats_list:
        return {"label": label, "session_count": 0}

    n_sessions = len(session_stats_list)
    total_domains = sum(s["domains_registered"] for s in session_stats_list)

    # Registrar aggregation
    reg_counts: dict[str, int] = defaultdict(int)
    reg_mean_latencies: dict[str, list] = defaultdict(list)
    reg_sessions_active: dict[str, int] = defaultdict(int)

    for s in session_stats_list:
        for reg, rb in s["registrar_breakdown"].items():
            reg_counts[reg] += rb["domain_count"]
            reg_mean_latencies[reg].append(rb["capture_latency_mean_ms"])
            reg_sessions_active[reg] += 1

    registrar_breakdown = {}
    for reg in sorted(reg_counts, key=lambda r: -reg_counts[r]):
        count = reg_counts[reg]
        means = reg_mean_latencies[reg]
        registrar_breakdown[reg] = {
            "domain_count":       count,
            "market_share_pct":   round(count / total_domains * 100, 2) if total_domains else 0,
            "sessions_active":    reg_sessions_active[reg],
            "session_presence_pct": round(reg_sessions_active[reg] / n_sessions * 100, 1),
            "capture_latency_mean_of_means_ms": round(statistics.mean(means), 1) if means else None,
        }

    hhi = round(sum(r["market_share_pct"] ** 2 for r in registrar_breakdown.values()), 1)

    # Session-level variability
    domain_counts = [s["domains_registered"] for s in session_stats_list]
    registrar_counts = [s["unique_registrars"] for s in session_stats_list]

    return {
        "label":           label,
        "session_count":   n_sessions,
        "date_range":      {
            "from": session_stats_list[0]["date"],
            "to":   session_stats_list[-1]["date"],
        },
        "total_domains_registered":  total_domains,
        "avg_domains_per_session":   round(total_domains / n_sessions, 1),
        "min_domains_in_session":    min(domain_counts),
        "max_domains_in_session":    max(domain_counts),
        "stdev_domains_per_session": round(statistics.stdev(domain_counts), 1) if n_sessions >= 2 else 0,
        "unique_registrars":         len(registrar_breakdown),
        "avg_registrars_per_session": round(statistics.mean(registrar_counts), 1),
        "market_concentration_hhi":  hhi,
        "registrar_breakdown":       registrar_breakdown,
    }


# ──────────────────────────────────────────────────────────────────────────────
# Full tally
# ──────────────────────────────────────────────────────────────────────────────

def compute_tally(all_stats: list) -> dict:
    """Build the full hierarchical tally from all session stats."""
    now = datetime.now(timezone.utc)

    # Group by year and by year-month
    by_year:  dict[str, list] = defaultdict(list)
    by_month: dict[str, list] = defaultdict(list)

    for s in all_stats:
        y, m, _ = s["date"].split("-")
        by_year[y].append(s)
        by_month[f"{y}-{m}"].append(s)

    def within_days(days: int) -> list:
        cutoff = now - timedelta(days=days)
        return [
            s for s in all_stats
            if _parse_dt(s["release_timestamp"]) >= cutoff
        ]

    return {
        "generated_at":   now.isoformat(),
        "total_sessions": len(all_stats),
        # Rolling windows
        "last_1_session":  aggregate_stats(all_stats[-1:],  "Last Session"),
        "last_4_sessions": aggregate_stats(all_stats[-4:],  "Last 4 Sessions"),
        "last_26_weeks":   aggregate_stats(within_days(182), "Last ~6 Months (26 Weeks)"),
        "last_52_weeks":   aggregate_stats(within_days(365), "Last 52 Weeks"),
        # Historical breakdowns
        "all_time": aggregate_stats(all_stats, "All Time"),
        "by_year":  {y: aggregate_stats(ss, f"Year {y}")  for y, ss in sorted(by_year.items())},
        "by_month": {ym: aggregate_stats(ss, f"Month {ym}") for ym, ss in sorted(by_month.items())},
        # Full per-session detail (keyed by date for O(1) lookup)
        "sessions": {s["date"]: s for s in all_stats},
    }


# ──────────────────────────────────────────────────────────────────────────────
# README generation
# ──────────────────────────────────────────────────────────────────────────────

def _fmt_registrar_table(breakdown: dict, top_n: int = 15) -> str:
    rows = ["| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |",
            "|-----------|--------:|------:|----------------:|------------------:|"]
    for reg, rb in list(breakdown.items())[:top_n]:
        lat = rb.get("capture_latency_mean_of_means_ms") or rb.get("capture_latency_mean_ms", "—")
        sessions_active = rb.get("sessions_active", "—")
        rows.append(
            f"| {reg} "
            f"| {rb['domain_count']:,} "
            f"| {rb['market_share_pct']}% "
            f"| {sessions_active} "
            f"| {lat} |"
        )
    return "\n".join(rows)


def _fmt_latency_table(breakdown: dict, top_n: int = 15) -> str:
    rows = ["| Registrar | Domains | Min (ms) | Median (ms) | Mean (ms) | P95 (ms) | Max (ms) | StdDev (ms) |",
            "|-----------|--------:|---------:|------------:|----------:|---------:|---------:|------------:|"]
    for reg, rb in list(breakdown.items())[:top_n]:
        rows.append(
            f"| {reg} "
            f"| {rb['domain_count']:,} "
            f"| {rb.get('capture_latency_min_ms','—')} "
            f"| {rb.get('capture_latency_median_ms','—')} "
            f"| {rb.get('capture_latency_mean_ms','—')} "
            f"| {rb.get('capture_latency_p95_ms','—')} "
            f"| {rb.get('capture_latency_max_ms','—')} "
            f"| {rb.get('capture_latency_stdev_ms','—')} |"
        )
    return "\n".join(rows)


def _fmt_timing_dist(dist_by_second: dict) -> str:
    if not dist_by_second:
        return "_No timing data_"
    rows = ["| Offset (s) | Domains Captured |",
            "|-----------:|-----------------:|"]
    for sec, count in sorted((int(k), v) for k, v in dist_by_second.items()):
        rows.append(f"| +{sec:,} | {count:,} |")
    return "\n".join(rows)


def _agg_section(agg: dict) -> str:
    if not agg or agg.get("session_count", 0) == 0:
        return "_No data yet._"
    dr = agg.get("date_range", {})
    date_range = f"{dr.get('from','?')} → {dr.get('to','?')}" if dr else "—"
    lines = [
        f"- **Sessions covered:** {agg['session_count']}  ({date_range})",
        f"- **Total domains registered:** {agg.get('total_domains_registered', 0):,}",
        f"- **Avg domains/session:** {agg.get('avg_domains_per_session', '—')}",
        f"- **Unique registrars (ever active):** {agg.get('unique_registrars', '—')}",
        f"- **Avg registrars/session:** {agg.get('avg_registrars_per_session', '—')}",
        f"- **Market concentration HHI:** {agg.get('market_concentration_hhi', '—'):,}",
        "",
        _fmt_registrar_table(agg.get("registrar_breakdown", {})),
    ]
    return "\n".join(lines)


def _last_session_detail(s: dict) -> str:
    if not s:
        return "_No data yet._"
    lines = [
        f"- **Date:** {s.get('date', '—')}",
        f"- **Domains released:** {s.get('domains_released', '—'):,}",
        f"- **Domains registered:** {s.get('domains_registered', '—'):,}",
        f"- **Registration rate:** {s.get('registration_rate_pct', '—')}%",
        f"- **Unique registrars:** {s.get('unique_registrars', '—')}",
        f"- **Session duration:** {s.get('session_duration_ms', '—'):,} ms",
        f"- **Market concentration (HHI):** {s.get('market_concentration_hhi', '—'):,}",
        "",
        "**Capture latency across all registrars:**",
        f"- Min: {s.get('capture_latency_min_ms','—')} ms | "
        f"Median: {s.get('capture_latency_median_ms','—')} ms | "
        f"Mean: {s.get('capture_latency_mean_ms','—')} ms | "
        f"P95: {s.get('capture_latency_p95_ms','—')} ms | "
        f"Max: {s.get('capture_latency_max_ms','—')} ms",
        "",
        "**Per-registrar latency breakdown:**",
        "",
        _fmt_latency_table(s.get("registrar_breakdown", {})),
        "",
        "**Timing distribution (captures by second offset from 19:00:00 UTC):**",
        "",
        _fmt_timing_dist(s.get("timing_distribution_by_second", {})),
    ]
    return "\n".join(lines)


def _chart_img(charts: dict, key: str, alt: str = "") -> str:
    """Return a markdown image tag if the chart exists, else empty string."""
    fname = charts.get(key, "")
    if not fname:
        return ""
    return f"\n![{alt}](charts/{fname})\n"


def generate_readme(tally: dict, charts: dict | None = None) -> str:
    if charts is None:
        charts = {}
    generated   = tally.get("generated_at", "")[:10]
    n_sessions  = tally.get("total_sessions", 0)
    sessions    = tally.get("sessions", {})
    last_s      = list(sessions.values())[-1] if sessions else {}

    # ── Build trend charts section ──────────────────────────────────────────
    trend_section = ""
    trend_charts = [
        ("trend_domains_per_session", "Domains Per Session Trend"),
        ("trend_market_share", "Market Share Trend"),
        ("trend_hhi", "HHI Trend"),
        ("trend_latency_by_registrar", "Latency Trend by Registrar"),
    ]
    rendered_trends = [_chart_img(charts, k, a) for k, a in trend_charts if k in charts]
    if rendered_trends:
        trend_section = "\n---\n\n## Trends\n" + "\n".join(rendered_trends)

    # ── Build per-year chart refs ────────────────────────────────────────────
    by_year_sections_out = ""
    for yr, agg in sorted(tally.get("by_year", {}).items()):
        by_year_sections_out += f"\n### {yr}\n\n{_agg_section(agg)}\n"
        by_year_sections_out += _chart_img(charts, f"year_{yr}_market_share",
                                           f"Market share {yr}")

    by_month_sections_out = ""
    for ym, agg in sorted(tally.get("by_month", {}).items()):
        by_month_sections_out += f"\n#### {ym}\n\n{_agg_section(agg)}\n"

    return f"""\
# CIRA TBR Tracker

> Automated archive and analytics for CIRA **To-Be-Released (TBR)** `.CA` domain
> drop sessions. Updated every **Wednesday ≈ 19:30 UTC** via GitHub Actions.

**Last updated:** {generated} &nbsp;|&nbsp; **Total sessions tracked:** {n_sessions}

---

## What is TBR?

CIRA releases expired `.CA` domains every **Wednesday at 19:00 UTC** via a
first-come, first-served process. Whichever registrar submits a registration
request first wins the domain (one connection, one request per 5 s per registrar).

Capture latency is measured from the official session open at **19:00:00.000 UTC**.

---

## Last Session

{_last_session_detail(last_s)}
{_chart_img(charts, "last_session_market_share", "Last Session Market Share")}
{_chart_img(charts, "last_session_latency_histogram", "Last Session Latency Distribution")}
{_chart_img(charts, "last_session_latency_by_registrar", "Last Session Latency by Registrar")}
{_chart_img(charts, "last_session_timing_distribution", "Last Session Timing Distribution")}

---

## Rolling Windows

### Last 4 Sessions

{_agg_section(tally.get('last_4_sessions', {}))}
{_chart_img(charts, "last_4_sessions_market_share", "Last 4 Sessions Market Share")}

---

### Last ~6 Months (26 Weeks)

{_agg_section(tally.get('last_26_weeks', {}))}
{_chart_img(charts, "last_26_weeks_market_share", "Last 26 Weeks Market Share")}

---

### Last 52 Weeks

{_agg_section(tally.get('last_52_weeks', {}))}
{_chart_img(charts, "last_52_weeks_market_share", "Last 52 Weeks Market Share")}

---

## All Time

{_agg_section(tally.get('all_time', {}))}
{_chart_img(charts, "all_time_market_share", "All Time Market Share")}
{trend_section}

---

## By Year
{by_year_sections_out}

---

## By Month
{by_month_sections_out}

---

## Data & Files

| Path | Description |
|------|-------------|
| `data/YYYY/MM/DD.json` | Raw API response for each session |
| `tally.json` | Machine-readable aggregate statistics |
| `charts/` | Auto-generated visualizations (PNG) |
| `README.md` | This file — auto-generated each week |

---

## Metrics Glossary

| Metric | Description |
|--------|-------------|
| **Market Share %** | Percentage of session domains captured by a registrar |
| **HHI (Herfindahl-Hirschman Index)** | Market concentration; 10,000 = monopoly, <1,500 = competitive |
| **Capture Latency (ms)** | Milliseconds from session open (19:00:00.000 UTC) to domain registration timestamp |
| **Session Duration (ms)** | Time elapsed between the first and last domain captured in a session |
| **P95 Latency** | 95th-percentile capture latency — 95% of captures happened at or below this value |
| **StdDev Latency** | Standard deviation of capture latencies; lower = more consistent timing |
| **Session Presence %** | Share of sessions in which a registrar captured at least one domain |
| **Mean of Means Latency** | Average of per-session mean latencies across multiple sessions |
| **Timing Distribution** | Histogram of domain captures bucketed by second offset from session open |
| **Registration Rate %** | Fraction of released domains that were actually registered in the session |
"""


# ──────────────────────────────────────────────────────────────────────────────
# Entry point
# ──────────────────────────────────────────────────────────────────────────────

def main() -> None:
    # 1. Fetch latest session
    print("Fetching latest TBR session data...")
    raw = fetch_session()
    date_str = _session_date(raw)
    n_domains = raw.get("numberOfDomainNames", len(raw.get("domains", [])))
    print(f"  Session: {date_str}  |  Domains: {n_domains}")

    # 2. Archive raw data
    path = save_raw(raw)
    print(f"  Archived to: {path.relative_to(ROOT)}")

    # 3. Load complete history & compute per-session stats
    all_sessions = load_all_sessions()
    print(f"  Total sessions in archive: {len(all_sessions)}")
    all_stats = [compute_session_stats(s) for s in all_sessions]

    # 4. Compute tally
    tally = compute_tally(all_stats)
    tally_path = ROOT / "tally.json"
    tally_path.write_text(json.dumps(tally, indent=2, ensure_ascii=False))
    print(f"  Wrote {tally_path.relative_to(ROOT)}")

    # 5. Generate charts
    charts_dir = ROOT / "charts"
    charts = generate_all_charts(tally, all_stats, all_sessions, charts_dir)
    print(f"  Generated {len(charts)} charts")

    # 6. Regenerate README
    readme = generate_readme(tally, charts)
    (ROOT / "README.md").write_text(readme, encoding="utf-8")
    print("  Updated README.md")


if __name__ == "__main__":
    main()
