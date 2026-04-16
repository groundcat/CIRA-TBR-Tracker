#!/usr/bin/env python3
"""
CIRA TBR Tracker - Chart Generation

Generates publication-quality visualizations for TBR session analytics.
All charts are saved to the ``charts/`` directory and referenced in README.md.

Uses only matplotlib (no seaborn/plotly) for minimal dependencies.
"""

from __future__ import annotations

import math
from pathlib import Path
from collections import defaultdict

import matplotlib
matplotlib.use("Agg")  # headless backend — must be set before pyplot import
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# ──────────────────────────────────────────────────────────────────────────────
# Style constants
# ──────────────────────────────────────────────────────────────────────────────

# Professional 12-color palette (colorblind-safe, print-friendly)
PALETTE = [
    "#4E79A7", "#F28E2B", "#E15759", "#76B7B2", "#59A14F",
    "#EDC948", "#B07AA1", "#FF9DA7", "#9C755F", "#BAB0AC",
    "#86BCB6", "#8CD17D",
]
OTHER_COLOR = "#D4D4D4"

BG_COLOR      = "#FAFAFA"
GRID_COLOR    = "#E0E0E0"
TEXT_COLOR     = "#333333"
SUBTITLE_COLOR = "#666666"

FIG_DPI  = 150
FIG_W    = 10   # inches
FIG_H_SM = 5
FIG_H_MD = 6
FIG_H_LG = 7


def _apply_style(ax: plt.Axes, title: str, subtitle: str = "") -> None:
    """Apply a clean, consistent style to any axis."""
    ax.set_facecolor(BG_COLOR)
    ax.figure.set_facecolor("white")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(GRID_COLOR)
    ax.spines["bottom"].set_color(GRID_COLOR)
    ax.tick_params(colors=TEXT_COLOR, labelsize=9)
    ax.yaxis.set_tick_params(length=0)
    ax.xaxis.set_tick_params(length=3)
    ax.set_axisbelow(True)
    ax.grid(axis="y", color=GRID_COLOR, linewidth=0.5)
    ax.set_title(title, fontsize=13, fontweight="bold", color=TEXT_COLOR,
                 loc="left", pad=12)
    if subtitle:
        ax.text(0, 1.02, subtitle, transform=ax.transAxes,
                fontsize=9, color=SUBTITLE_COLOR, va="bottom")


def _save(fig: plt.Figure, path: Path) -> None:
    fig.savefig(path, dpi=FIG_DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"    chart: {path.name}")


def _short_name(name: str, max_len: int = 28) -> str:
    """Abbreviate long registrar names for chart labels."""
    replacements = [
        ("Online Solutions Inc.", ""),
        ("Technologies Inc.", "Tech"),
        ("Solutions Inc.", ""),
        (" Inc.", ""),
        (" inc", ""),
        (" O/A ", " / "),
        ("(3612040 CANADA inc.)", ""),
        ("8648255 CANADA LTD. / ", ""),
    ]
    s = name
    for old, new in replacements:
        s = s.replace(old, new)
    s = s.strip().rstrip(".")
    if len(s) > max_len:
        s = s[:max_len - 1] + "\u2026"
    return s


# ──────────────────────────────────────────────────────────────────────────────
# Chart 1 — Last session: registrar market share (donut)
# ──────────────────────────────────────────────────────────────────────────────

def chart_market_share_donut(session_stats: dict, out_dir: Path) -> str:
    """Donut chart of registrar market share for a single session."""
    rb = session_stats.get("registrar_breakdown", {})
    if not rb:
        return ""

    # Aggregate small registrars into "Other"
    labels, sizes, colors = [], [], []
    other = 0.0
    for i, (reg, data) in enumerate(rb.items()):
        if data["market_share_pct"] >= 2.0 and i < 10:
            labels.append(_short_name(reg))
            sizes.append(data["domain_count"])
            colors.append(PALETTE[i % len(PALETTE)])
        else:
            other += data["domain_count"]
    if other:
        labels.append("Other")
        sizes.append(other)
        colors.append(OTHER_COLOR)

    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H_MD))
    wedges, texts, autotexts = ax.pie(
        sizes, labels=None, autopct=lambda p: f"{p:.1f}%" if p >= 3 else "",
        colors=colors, startangle=90, pctdistance=0.78,
        wedgeprops=dict(width=0.45, edgecolor="white", linewidth=1.5),
    )
    for at in autotexts:
        at.set_fontsize(8)
        at.set_color(TEXT_COLOR)

    ax.legend(labels, loc="center left", bbox_to_anchor=(1.0, 0.5),
              fontsize=9, frameon=False)
    date = session_stats.get("date", "")
    n = session_stats.get("domains_registered", 0)
    ax.set_title(f"Registrar Market Share — {date}",
                 fontsize=13, fontweight="bold", color=TEXT_COLOR, pad=16)
    ax.text(0, 0, f"{n}\ndomains", ha="center", va="center",
            fontsize=16, fontweight="bold", color=TEXT_COLOR)

    fname = "last_session_market_share.png"
    _save(fig, out_dir / fname)
    return fname


# ──────────────────────────────────────────────────────────────────────────────
# Chart 2 — Last session: capture latency histogram
# ──────────────────────────────────────────────────────────────────────────────

def chart_latency_histogram(session_stats: dict, raw_session: dict, out_dir: Path) -> str:
    """Histogram of capture latencies (ms from 19:00:00.000 UTC)."""
    from datetime import datetime

    domains = raw_session.get("domains", [])
    if not domains:
        return ""

    release_dt = datetime.fromisoformat(raw_session["releaseDate"].replace("Z", "+00:00"))
    session_open = release_dt.replace(hour=19, minute=0, second=0, microsecond=0)

    latencies_s = []
    for d in domains:
        ts = datetime.fromisoformat(d["timestamp"].replace("Z", "+00:00"))
        latencies_s.append((ts - session_open).total_seconds())

    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H_SM))

    # Adaptive binning
    max_lat = max(latencies_s)
    if max_lat <= 30:
        bins = [i for i in range(int(max_lat) + 2)]
        xlabel = "Capture Latency (seconds from 19:00:00 UTC)"
    elif max_lat <= 120:
        bins = list(range(0, int(max_lat) + 5, 5))
        xlabel = "Capture Latency (seconds from 19:00:00 UTC)"
    else:
        latencies_s = [l / 60 for l in latencies_s]
        max_lat_min = max(latencies_s)
        bins = [i * 0.5 for i in range(int(max_lat_min * 2) + 2)]
        xlabel = "Capture Latency (minutes from 19:00:00 UTC)"

    ax.hist(latencies_s, bins=bins, color=PALETTE[0], edgecolor="white",
            linewidth=0.5, alpha=0.85)
    _apply_style(ax, f"Capture Latency Distribution — {session_stats.get('date','')}",
                 f"n = {len(latencies_s)} domains")
    ax.set_xlabel(xlabel, fontsize=10, color=TEXT_COLOR)
    ax.set_ylabel("Number of Domains Captured", fontsize=10, color=TEXT_COLOR)

    fname = "last_session_latency_histogram.png"
    _save(fig, out_dir / fname)
    return fname


# ──────────────────────────────────────────────────────────────────────────────
# Chart 3 — Last session: latency by registrar (horizontal bar with ranges)
# ──────────────────────────────────────────────────────────────────────────────

def chart_latency_by_registrar(session_stats: dict, out_dir: Path) -> str:
    """Horizontal bar chart: median latency per registrar with min–max whiskers."""
    rb = session_stats.get("registrar_breakdown", {})
    if not rb:
        return ""

    regs, medians, mins, maxs, counts = [], [], [], [], []
    for reg, data in list(rb.items())[:12]:
        regs.append(_short_name(reg, 30))
        medians.append(data["capture_latency_median_ms"] / 1000)
        mins.append(data["capture_latency_min_ms"] / 1000)
        maxs.append(data["capture_latency_max_ms"] / 1000)
        counts.append(data["domain_count"])

    # Reverse for top-down display
    regs.reverse(); medians.reverse(); mins.reverse(); maxs.reverse(); counts.reverse()

    fig, ax = plt.subplots(figsize=(FIG_W, max(FIG_H_SM, len(regs) * 0.45 + 1.5)))
    y_pos = range(len(regs))

    # Error bars: min to max
    xerr_low = [m - mn for m, mn in zip(medians, mins)]
    xerr_high = [mx - m for m, mx in zip(medians, maxs)]

    colors = [PALETTE[i % len(PALETTE)] for i in range(len(regs))]
    colors.reverse()

    ax.barh(y_pos, medians, height=0.55, color=colors, alpha=0.85,
            edgecolor="white", linewidth=0.5)
    ax.errorbar(medians, y_pos, xerr=[xerr_low, xerr_high], fmt="none",
                ecolor="#888888", elinewidth=1, capsize=3, capthick=1)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(regs, fontsize=9)

    # Annotate domain count
    for i, (med, count) in enumerate(zip(medians, counts)):
        ax.text(med + (max(maxs) * 0.02), i, f"n={count}",
                va="center", fontsize=8, color=SUBTITLE_COLOR)

    _apply_style(ax, f"Capture Latency by Registrar — {session_stats.get('date','')}",
                 "Bar = median | Whiskers = min\u2013max")
    ax.set_xlabel("Capture Latency (seconds from 19:00:00 UTC)", fontsize=10,
                  color=TEXT_COLOR)
    ax.grid(axis="x", color=GRID_COLOR, linewidth=0.5)
    ax.grid(axis="y", visible=False)

    fname = "last_session_latency_by_registrar.png"
    _save(fig, out_dir / fname)
    return fname


# ──────────────────────────────────────────────────────────────────────────────
# Chart 4 — Last session: timing distribution (captures per second)
# ──────────────────────────────────────────────────────────────────────────────

def chart_timing_distribution(session_stats: dict, out_dir: Path) -> str:
    """Bar chart: domains captured per second offset from session open."""
    dist = session_stats.get("timing_distribution_by_second", {})
    if not dist:
        return ""

    seconds = sorted(int(k) for k in dist)
    counts = [dist[str(s)] for s in seconds]

    # If the range is large and sparse, only show the first dense portion
    # plus a note about tail
    show_all = max(seconds) <= 60
    if not show_all:
        # Show first 30s in detail, summarize rest
        cutoff = 30
        sec_main = [s for s in seconds if s <= cutoff]
        cnt_main = [dist[str(s)] for s in sec_main]
        tail_count = sum(dist[str(s)] for s in seconds if s > cutoff)
        tail_note = f"+{tail_count} domains captured after +{cutoff}s"
    else:
        sec_main, cnt_main = seconds, counts
        tail_note = ""

    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H_SM))
    ax.bar(sec_main, cnt_main, width=0.8, color=PALETTE[0], edgecolor="white",
           linewidth=0.5, alpha=0.85)

    _apply_style(ax, f"Capture Timing Distribution — {session_stats.get('date','')}",
                 "Domains captured per second from session open (19:00:00 UTC)")
    ax.set_xlabel("Seconds After Session Open", fontsize=10, color=TEXT_COLOR)
    ax.set_ylabel("Domains Captured", fontsize=10, color=TEXT_COLOR)
    ax.yaxis.set_major_locator(mticker.MaxNLocator(integer=True))

    if tail_note:
        ax.text(0.98, 0.95, tail_note, transform=ax.transAxes,
                ha="right", va="top", fontsize=9, color=SUBTITLE_COLOR,
                fontstyle="italic")

    fname = "last_session_timing_distribution.png"
    _save(fig, out_dir / fname)
    return fname


# ──────────────────────────────────────────────────────────────────────────────
# Chart 5 — Trend: domains per session over time
# ──────────────────────────────────────────────────────────────────────────────

def chart_domains_trend(all_stats: list, out_dir: Path) -> str:
    """Line chart of domains registered per session over time."""
    if len(all_stats) < 2:
        return ""

    dates = [s["date"] for s in all_stats]
    domains = [s["domains_registered"] for s in all_stats]

    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H_SM))
    ax.plot(dates, domains, marker="o", color=PALETTE[0], linewidth=2,
            markersize=5, markerfacecolor="white", markeredgewidth=1.5)
    ax.fill_between(range(len(dates)), domains, alpha=0.08, color=PALETTE[0])

    _apply_style(ax, "Domains Registered per Session",
                 "Weekly TBR session totals over time")
    ax.set_ylabel("Domains Registered", fontsize=10, color=TEXT_COLOR)

    # Rotate labels if many sessions
    if len(dates) > 12:
        ax.set_xticks(range(0, len(dates), max(1, len(dates) // 12)))
        ax.set_xticklabels([dates[i] for i in range(0, len(dates), max(1, len(dates) // 12))],
                           rotation=45, ha="right", fontsize=8)
    else:
        ax.set_xticks(range(len(dates)))
        ax.set_xticklabels(dates, rotation=45, ha="right", fontsize=8)

    ax.yaxis.set_major_locator(mticker.MaxNLocator(integer=True))

    fname = "trend_domains_per_session.png"
    _save(fig, out_dir / fname)
    return fname


# ──────────────────────────────────────────────────────────────────────────────
# Chart 6 — Trend: market concentration (HHI) over time
# ──────────────────────────────────────────────────────────────────────────────

def chart_hhi_trend(all_stats: list, out_dir: Path) -> str:
    """Line chart of HHI (market concentration) over time."""
    if len(all_stats) < 2:
        return ""

    dates = [s["date"] for s in all_stats]
    hhis = [s["market_concentration_hhi"] for s in all_stats]

    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H_SM))
    ax.plot(dates, hhis, marker="o", color=PALETTE[2], linewidth=2,
            markersize=5, markerfacecolor="white", markeredgewidth=1.5)

    # Reference bands
    ax.axhspan(0, 1500, alpha=0.06, color="#59A14F", label="Competitive (<1,500)")
    ax.axhspan(1500, 2500, alpha=0.06, color="#EDC948", label="Moderate (1,500\u20132,500)")
    ax.axhspan(2500, 10000, alpha=0.06, color="#E15759", label="Concentrated (>2,500)")

    _apply_style(ax, "Market Concentration (HHI) Over Time",
                 "Herfindahl-Hirschman Index per session")
    ax.set_ylabel("HHI", fontsize=10, color=TEXT_COLOR)
    ax.legend(fontsize=8, loc="upper right", framealpha=0.9)

    if len(dates) > 12:
        ax.set_xticks(range(0, len(dates), max(1, len(dates) // 12)))
        ax.set_xticklabels([dates[i] for i in range(0, len(dates), max(1, len(dates) // 12))],
                           rotation=45, ha="right", fontsize=8)
    else:
        ax.set_xticks(range(len(dates)))
        ax.set_xticklabels(dates, rotation=45, ha="right", fontsize=8)

    fname = "trend_hhi.png"
    _save(fig, out_dir / fname)
    return fname


# ──────────────────────────────────────────────────────────────────────────────
# Chart 7 — Trend: registrar market share over time (stacked area)
# ──────────────────────────────────────────────────────────────────────────────

def chart_market_share_trend(all_stats: list, out_dir: Path) -> str:
    """Stacked area chart of top registrars' market share over sessions."""
    if len(all_stats) < 2:
        return ""

    # Determine top N registrars by total domain count across all sessions
    reg_totals: dict[str, int] = defaultdict(int)
    for s in all_stats:
        for reg, rb in s["registrar_breakdown"].items():
            reg_totals[reg] += rb["domain_count"]
    top_regs = sorted(reg_totals, key=lambda r: -reg_totals[r])[:8]

    dates = [s["date"] for s in all_stats]
    series: dict[str, list[float]] = {r: [] for r in top_regs}
    other_series: list[float] = []

    for s in all_stats:
        n = s["domains_registered"]
        top_sum = 0
        for reg in top_regs:
            rb = s["registrar_breakdown"].get(reg, {})
            pct = rb.get("market_share_pct", 0)
            series[reg].append(pct)
            top_sum += pct
        other_series.append(max(0, 100 - top_sum))

    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H_MD))

    stacks = [series[r] for r in top_regs] + [other_series]
    stack_labels = [_short_name(r) for r in top_regs] + ["Other"]
    stack_colors = [PALETTE[i % len(PALETTE)] for i in range(len(top_regs))] + [OTHER_COLOR]

    ax.stackplot(range(len(dates)), *stacks, labels=stack_labels,
                 colors=stack_colors, alpha=0.85, edgecolor="white", linewidth=0.5)

    _apply_style(ax, "Registrar Market Share Over Time",
                 "Stacked percentage of domains captured per session")
    ax.set_ylabel("Market Share (%)", fontsize=10, color=TEXT_COLOR)
    ax.set_ylim(0, 100)
    ax.legend(loc="center left", bbox_to_anchor=(1.0, 0.5), fontsize=8, frameon=False)

    if len(dates) > 12:
        step = max(1, len(dates) // 12)
        ax.set_xticks(range(0, len(dates), step))
        ax.set_xticklabels([dates[i] for i in range(0, len(dates), step)],
                           rotation=45, ha="right", fontsize=8)
    else:
        ax.set_xticks(range(len(dates)))
        ax.set_xticklabels(dates, rotation=45, ha="right", fontsize=8)

    fname = "trend_market_share.png"
    _save(fig, out_dir / fname)
    return fname


# ──────────────────────────────────────────────────────────────────────────────
# Chart 8 — Trend: mean capture latency by registrar over time
# ──────────────────────────────────────────────────────────────────────────────

def chart_latency_trend(all_stats: list, out_dir: Path) -> str:
    """Line chart of mean capture latency per top registrar over sessions."""
    if len(all_stats) < 2:
        return ""

    reg_totals: dict[str, int] = defaultdict(int)
    for s in all_stats:
        for reg, rb in s["registrar_breakdown"].items():
            reg_totals[reg] += rb["domain_count"]
    top_regs = sorted(reg_totals, key=lambda r: -reg_totals[r])[:6]

    dates = [s["date"] for s in all_stats]

    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H_SM))

    for i, reg in enumerate(top_regs):
        latencies = []
        for s in all_stats:
            rb = s["registrar_breakdown"].get(reg, {})
            lat = rb.get("capture_latency_mean_ms")
            latencies.append(lat / 1000 if lat is not None else None)

        # Plot only non-None values
        x_vals = [j for j, v in enumerate(latencies) if v is not None]
        y_vals = [v for v in latencies if v is not None]

        ax.plot(x_vals, y_vals, marker="o", color=PALETTE[i % len(PALETTE)],
                linewidth=1.5, markersize=4, markerfacecolor="white",
                markeredgewidth=1.2, label=_short_name(reg, 25))

    _apply_style(ax, "Mean Capture Latency by Registrar Over Time",
                 "Per-session mean latency (seconds from 19:00:00 UTC)")
    ax.set_ylabel("Mean Capture Latency (s)", fontsize=10, color=TEXT_COLOR)
    ax.legend(fontsize=8, loc="upper right", framealpha=0.9)

    if len(dates) > 12:
        step = max(1, len(dates) // 12)
        ax.set_xticks(range(0, len(dates), step))
        ax.set_xticklabels([dates[i] for i in range(0, len(dates), step)],
                           rotation=45, ha="right", fontsize=8)
    else:
        ax.set_xticks(range(len(dates)))
        ax.set_xticklabels(dates, rotation=45, ha="right", fontsize=8)

    fname = "trend_latency_by_registrar.png"
    _save(fig, out_dir / fname)
    return fname


# ──────────────────────────────────────────────────────────────────────────────
# Chart 9 — Aggregate: market share bar chart (for any rolling window)
# ──────────────────────────────────────────────────────────────────────────────

def chart_aggregate_market_share(agg: dict, slug: str, out_dir: Path) -> str:
    """Horizontal bar chart of registrar market share for an aggregate window."""
    rb = agg.get("registrar_breakdown", {})
    if not rb or agg.get("session_count", 0) == 0:
        return ""

    regs = list(rb.keys())[:12]
    shares = [rb[r]["market_share_pct"] for r in regs]
    labels = [_short_name(r, 30) for r in regs]

    labels.reverse(); shares.reverse()
    colors = [PALETTE[i % len(PALETTE)] for i in range(len(regs))]
    colors.reverse()

    fig, ax = plt.subplots(figsize=(FIG_W, max(FIG_H_SM, len(regs) * 0.4 + 1.5)))
    bars = ax.barh(range(len(labels)), shares, height=0.6, color=colors,
                   alpha=0.85, edgecolor="white", linewidth=0.5)

    ax.set_yticks(range(len(labels)))
    ax.set_yticklabels(labels, fontsize=9)

    for i, (share, bar) in enumerate(zip(shares, bars)):
        ax.text(share + 0.5, i, f"{share:.1f}%", va="center", fontsize=8,
                color=TEXT_COLOR)

    label = agg.get("label", slug)
    dr = agg.get("date_range", {})
    sub = f"{dr.get('from','?')} \u2192 {dr.get('to','?')}, n={agg.get('session_count',0)} sessions" if dr else ""

    _apply_style(ax, f"Registrar Market Share \u2014 {label}", sub)
    ax.set_xlabel("Market Share (%)", fontsize=10, color=TEXT_COLOR)
    ax.grid(axis="x", color=GRID_COLOR, linewidth=0.5)
    ax.grid(axis="y", visible=False)

    fname = f"{slug}_market_share.png"
    _save(fig, out_dir / fname)
    return fname


# ──────────────────────────────────────────────────────────────────────────────
# Public entry point
# ──────────────────────────────────────────────────────────────────────────────

def generate_all_charts(
    tally: dict,
    all_stats: list,
    raw_sessions: list,
    out_dir: Path,
) -> dict[str, str]:
    """
    Generate all charts and return a mapping of logical name → filename.

    Returns only non-empty filenames (charts that were actually produced).
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    charts: dict[str, str] = {}

    print("  Generating charts...")

    # ── Last session charts ──────────────────────────────────────────────────
    sessions = tally.get("sessions", {})
    last_stats = list(sessions.values())[-1] if sessions else {}
    last_raw = raw_sessions[-1] if raw_sessions else {}

    if last_stats:
        c = chart_market_share_donut(last_stats, out_dir)
        if c: charts["last_session_market_share"] = c

        c = chart_latency_histogram(last_stats, last_raw, out_dir)
        if c: charts["last_session_latency_histogram"] = c

        c = chart_latency_by_registrar(last_stats, out_dir)
        if c: charts["last_session_latency_by_registrar"] = c

        c = chart_timing_distribution(last_stats, out_dir)
        if c: charts["last_session_timing_distribution"] = c

    # ── Trend charts (need >=2 sessions) ─────────────────────────────────────
    if len(all_stats) >= 2:
        c = chart_domains_trend(all_stats, out_dir)
        if c: charts["trend_domains_per_session"] = c

        c = chart_hhi_trend(all_stats, out_dir)
        if c: charts["trend_hhi"] = c

        c = chart_market_share_trend(all_stats, out_dir)
        if c: charts["trend_market_share"] = c

        c = chart_latency_trend(all_stats, out_dir)
        if c: charts["trend_latency_by_registrar"] = c

    # ── Aggregate window charts ──────────────────────────────────────────────
    for slug, key in [
        ("last_4_sessions", "last_4_sessions"),
        ("last_26_weeks",   "last_26_weeks"),
        ("last_52_weeks",   "last_52_weeks"),
        ("all_time",        "all_time"),
    ]:
        agg = tally.get(key, {})
        if agg.get("session_count", 0) > 0:
            c = chart_aggregate_market_share(agg, slug, out_dir)
            if c: charts[f"{slug}_market_share"] = c

    # ── Per-year aggregate charts ────────────────────────────────────────────
    for yr, agg in sorted(tally.get("by_year", {}).items()):
        if agg.get("session_count", 0) > 0:
            c = chart_aggregate_market_share(agg, f"year_{yr}", out_dir)
            if c: charts[f"year_{yr}_market_share"] = c

    return charts
