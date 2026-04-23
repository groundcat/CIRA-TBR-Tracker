# CIRA TBR Tracker

> Automated archive and analytics for CIRA **To-Be-Released (TBR)** `.CA` domain
> drop sessions. Updated every **Wednesday ≈ 19:30 UTC** via GitHub Actions.

**Last updated:** 2026-04-23 &nbsp;|&nbsp; **Total sessions tracked:** 2

---

## What is TBR?

CIRA releases expired `.CA` domains every **Wednesday at 19:00 UTC** via a
first-come, first-served process. Whichever registrar submits a registration
request first wins the domain (one connection, one request per 5 s per registrar).

Capture latency is measured from the official session open at **19:00:00.000 UTC**.

---

## Last Session

- **Date:** 2026-04-22
- **Domains released:** 194
- **Domains registered:** 194
- **Registration rate:** 100.0%
- **Unique registrars:** 8
- **Session duration:** 128,256 ms
- **Market concentration (HHI):** 4,740.2

**Capture latency across all registrars:**
- Min: 0 ms | Median: 10144 ms | Mean: 10031.0 ms | P95: 16521 ms | Max: 128256 ms

**Per-registrar latency breakdown:**

| Registrar | Domains | Min (ms) | Median (ms) | Mean (ms) | P95 (ms) | Max (ms) | StdDev (ms) |
|-----------|--------:|---------:|------------:|----------:|---------:|---------:|------------:|
| WHC Online Solutions Inc. | 126 | 0 | 10216 | 9719.1 | 16476 | 16568 | 4594.5 |
| BareMetal.com inc | 41 | 21 | 10915 | 10078.2 | 15960 | 16274 | 5138.4 |
| MyID.ca INC. | 16 | 6 | 4943 | 4352 | 9950 | 9950 | 2481.4 |
| Grape Inc. | 3 | 0 | 17 | 1689.3 | 5051 | 5051 | 2911.3 |
| DomainePlus.com (3612040 CANADA inc.) | 3 | 37 | 11529 | 9469 | 16841 | 16841 | 8589.3 |
| Register.ca Inc. | 2 | 0 | 10 | 10.5 | 21 | 21 | 14.8 |
| Webnames.ca Inc. | 2 | 53031 | 90643 | 90643.5 | 128256 | 128256 | 53192.1 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 1 | 23781 | 23781 | 23781 | 23781 | 23781 | 0 |

**Timing distribution (captures by second offset from 19:00:00 UTC):**

| Offset (s) | Domains Captured |
|-----------:|-----------------:|
| +0 | 22 |
| +4 | 11 |
| +5 | 28 |
| +6 | 19 |
| +7 | 2 |
| +8 | 1 |
| +9 | 3 |
| +10 | 25 |
| +11 | 27 |
| +12 | 8 |
| +13 | 2 |
| +14 | 1 |
| +15 | 27 |
| +16 | 15 |
| +23 | 1 |
| +53 | 1 |
| +128 | 1 |

![Last Session Market Share](charts/last_session_market_share.png)


![Last Session Latency Distribution](charts/last_session_latency_histogram.png)


![Last Session Latency by Registrar](charts/last_session_latency_by_registrar.png)


![Last Session Timing Distribution](charts/last_session_timing_distribution.png)


---

## Rolling Windows

### Last 4 Sessions

- **Sessions covered:** 2  (2026-04-15 → 2026-04-22)
- **Total domains registered:** 449
- **Avg domains/session:** 224.5
- **Unique registrars (ever active):** 11
- **Avg registrars/session:** 9.5
- **Market concentration HHI:** 4,648.4

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 290 | 64.59% | 2 | 10839.7 |
| BareMetal.com inc | 93 | 20.71% | 2 | 11702.5 |
| MyID.ca INC. | 23 | 5.12% | 2 | 4765.9 |
| Webnames.ca Inc. | 18 | 4.01% | 2 | 124051.9 |
| Grape Inc. | 6 | 1.34% | 2 | 2587.7 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 5 | 1.11% | 2 | 19106.1 |
| DomainePlus.com (3612040 CANADA inc.) | 5 | 1.11% | 2 | 5106.5 |
| Register.ca Inc. | 3 | 0.67% | 2 | 5020.8 |
| Namespro Solutions Inc. | 2 | 0.45% | 1 | 12229 |
| PlanetHoster | 2 | 0.45% | 1 | 4720 |
| easyDNS Technologies Inc. | 2 | 0.45% | 1 | 11814 |

![Last 4 Sessions Market Share](charts/last_4_sessions_market_share.png)


---

### Last ~6 Months (26 Weeks)

- **Sessions covered:** 2  (2026-04-15 → 2026-04-22)
- **Total domains registered:** 449
- **Avg domains/session:** 224.5
- **Unique registrars (ever active):** 11
- **Avg registrars/session:** 9.5
- **Market concentration HHI:** 4,648.4

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 290 | 64.59% | 2 | 10839.7 |
| BareMetal.com inc | 93 | 20.71% | 2 | 11702.5 |
| MyID.ca INC. | 23 | 5.12% | 2 | 4765.9 |
| Webnames.ca Inc. | 18 | 4.01% | 2 | 124051.9 |
| Grape Inc. | 6 | 1.34% | 2 | 2587.7 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 5 | 1.11% | 2 | 19106.1 |
| DomainePlus.com (3612040 CANADA inc.) | 5 | 1.11% | 2 | 5106.5 |
| Register.ca Inc. | 3 | 0.67% | 2 | 5020.8 |
| Namespro Solutions Inc. | 2 | 0.45% | 1 | 12229 |
| PlanetHoster | 2 | 0.45% | 1 | 4720 |
| easyDNS Technologies Inc. | 2 | 0.45% | 1 | 11814 |

![Last 26 Weeks Market Share](charts/last_26_weeks_market_share.png)


---

### Last 52 Weeks

- **Sessions covered:** 2  (2026-04-15 → 2026-04-22)
- **Total domains registered:** 449
- **Avg domains/session:** 224.5
- **Unique registrars (ever active):** 11
- **Avg registrars/session:** 9.5
- **Market concentration HHI:** 4,648.4

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 290 | 64.59% | 2 | 10839.7 |
| BareMetal.com inc | 93 | 20.71% | 2 | 11702.5 |
| MyID.ca INC. | 23 | 5.12% | 2 | 4765.9 |
| Webnames.ca Inc. | 18 | 4.01% | 2 | 124051.9 |
| Grape Inc. | 6 | 1.34% | 2 | 2587.7 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 5 | 1.11% | 2 | 19106.1 |
| DomainePlus.com (3612040 CANADA inc.) | 5 | 1.11% | 2 | 5106.5 |
| Register.ca Inc. | 3 | 0.67% | 2 | 5020.8 |
| Namespro Solutions Inc. | 2 | 0.45% | 1 | 12229 |
| PlanetHoster | 2 | 0.45% | 1 | 4720 |
| easyDNS Technologies Inc. | 2 | 0.45% | 1 | 11814 |

![Last 52 Weeks Market Share](charts/last_52_weeks_market_share.png)


---

## All Time

- **Sessions covered:** 2  (2026-04-15 → 2026-04-22)
- **Total domains registered:** 449
- **Avg domains/session:** 224.5
- **Unique registrars (ever active):** 11
- **Avg registrars/session:** 9.5
- **Market concentration HHI:** 4,648.4

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 290 | 64.59% | 2 | 10839.7 |
| BareMetal.com inc | 93 | 20.71% | 2 | 11702.5 |
| MyID.ca INC. | 23 | 5.12% | 2 | 4765.9 |
| Webnames.ca Inc. | 18 | 4.01% | 2 | 124051.9 |
| Grape Inc. | 6 | 1.34% | 2 | 2587.7 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 5 | 1.11% | 2 | 19106.1 |
| DomainePlus.com (3612040 CANADA inc.) | 5 | 1.11% | 2 | 5106.5 |
| Register.ca Inc. | 3 | 0.67% | 2 | 5020.8 |
| Namespro Solutions Inc. | 2 | 0.45% | 1 | 12229 |
| PlanetHoster | 2 | 0.45% | 1 | 4720 |
| easyDNS Technologies Inc. | 2 | 0.45% | 1 | 11814 |

![All Time Market Share](charts/all_time_market_share.png)


---

## Trends

![Domains Per Session Trend](charts/trend_domains_per_session.png)


![Market Share Trend](charts/trend_market_share.png)


![HHI Trend](charts/trend_hhi.png)


![Latency Trend by Registrar](charts/trend_latency_by_registrar.png)


---

## By Year

### 2026

- **Sessions covered:** 2  (2026-04-15 → 2026-04-22)
- **Total domains registered:** 449
- **Avg domains/session:** 224.5
- **Unique registrars (ever active):** 11
- **Avg registrars/session:** 9.5
- **Market concentration HHI:** 4,648.4

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 290 | 64.59% | 2 | 10839.7 |
| BareMetal.com inc | 93 | 20.71% | 2 | 11702.5 |
| MyID.ca INC. | 23 | 5.12% | 2 | 4765.9 |
| Webnames.ca Inc. | 18 | 4.01% | 2 | 124051.9 |
| Grape Inc. | 6 | 1.34% | 2 | 2587.7 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 5 | 1.11% | 2 | 19106.1 |
| DomainePlus.com (3612040 CANADA inc.) | 5 | 1.11% | 2 | 5106.5 |
| Register.ca Inc. | 3 | 0.67% | 2 | 5020.8 |
| Namespro Solutions Inc. | 2 | 0.45% | 1 | 12229 |
| PlanetHoster | 2 | 0.45% | 1 | 4720 |
| easyDNS Technologies Inc. | 2 | 0.45% | 1 | 11814 |

![Market share 2026](charts/year_2026_market_share.png)


---

## By Month

#### 2026-04

- **Sessions covered:** 2  (2026-04-15 → 2026-04-22)
- **Total domains registered:** 449
- **Avg domains/session:** 224.5
- **Unique registrars (ever active):** 11
- **Avg registrars/session:** 9.5
- **Market concentration HHI:** 4,648.4

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 290 | 64.59% | 2 | 10839.7 |
| BareMetal.com inc | 93 | 20.71% | 2 | 11702.5 |
| MyID.ca INC. | 23 | 5.12% | 2 | 4765.9 |
| Webnames.ca Inc. | 18 | 4.01% | 2 | 124051.9 |
| Grape Inc. | 6 | 1.34% | 2 | 2587.7 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 5 | 1.11% | 2 | 19106.1 |
| DomainePlus.com (3612040 CANADA inc.) | 5 | 1.11% | 2 | 5106.5 |
| Register.ca Inc. | 3 | 0.67% | 2 | 5020.8 |
| Namespro Solutions Inc. | 2 | 0.45% | 1 | 12229 |
| PlanetHoster | 2 | 0.45% | 1 | 4720 |
| easyDNS Technologies Inc. | 2 | 0.45% | 1 | 11814 |


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
