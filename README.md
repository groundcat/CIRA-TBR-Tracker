# CIRA TBR Tracker

> Automated archive and analytics for CIRA **To-Be-Released (TBR)** `.CA` domain
> drop sessions. Updated every **Wednesday ≈ 19:30 UTC** via GitHub Actions.

**Last updated:** 2026-04-17 &nbsp;|&nbsp; **Total sessions tracked:** 1

---

## What is TBR?

CIRA releases expired `.CA` domains every **Wednesday at 19:00 UTC** via a
first-come, first-served process. Whichever registrar submits a registration
request first wins the domain (one connection, one request per 5 s per registrar).

Capture latency is measured from the official session open at **19:00:00.000 UTC**.

---

## Last Session

- **Date:** 2026-04-15
- **Domains released:** 255
- **Domains registered:** 255
- **Registration rate:** 100.0%
- **Unique registrars:** 11
- **Session duration:** 299,678 ms
- **Market concentration (HHI):** 4,604.8

**Capture latency across all registrars:**
- Min: 0 ms | Median: 11841 ms | Mean: 20969.9 ms | P95: 63796 ms | Max: 299678 ms

**Per-registrar latency breakdown:**

| Registrar | Domains | Min (ms) | Median (ms) | Mean (ms) | P95 (ms) | Max (ms) | StdDev (ms) |
|-----------|--------:|---------:|------------:|----------:|---------:|---------:|------------:|
| WHC Online Solutions Inc. | 164 | 0 | 11732 | 11960.3 | 20555 | 21193 | 6011.6 |
| BareMetal.com inc | 52 | 1 | 15050 | 13326.7 | 20430 | 20793 | 5823.1 |
| Webnames.ca Inc. | 16 | 6547 | 166721 | 157460.3 | 299678 | 299678 | 92623.3 |
| MyID.ca INC. | 7 | 4882 | 4961 | 5179.7 | 6324 | 6324 | 519.8 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 4 | 1245 | 13157 | 14431.2 | 30166 | 30166 | 12869.5 |
| Grape Inc. | 3 | 99 | 5143 | 3486 | 5216 | 5216 | 2933.5 |
| Namespro Solutions Inc. | 2 | 83 | 12229 | 12229 | 24375 | 24375 | 17177.0 |
| DomainePlus.com (3612040 CANADA inc.) | 2 | 395 | 744 | 744 | 1093 | 1093 | 493.6 |
| PlanetHoster | 2 | 4717 | 4720 | 4720 | 4723 | 4723 | 4.2 |
| easyDNS Technologies Inc. | 2 | 8009 | 11814 | 11814 | 15619 | 15619 | 5381.1 |
| Register.ca Inc. | 1 | 10031 | 10031 | 10031 | 10031 | 10031 | 0 |

**Timing distribution (captures by second offset from 19:00:00 UTC):**

| Offset (s) | Domains Captured |
|-----------:|-----------------:|
| +0 | 21 |
| +1 | 2 |
| +4 | 10 |
| +5 | 19 |
| +6 | 18 |
| +7 | 3 |
| +8 | 1 |
| +9 | 2 |
| +10 | 30 |
| +11 | 25 |
| +12 | 5 |
| +13 | 1 |
| +14 | 2 |
| +15 | 30 |
| +16 | 25 |
| +17 | 8 |
| +19 | 2 |
| +20 | 31 |
| +21 | 4 |
| +24 | 1 |
| +28 | 1 |
| +30 | 1 |
| +63 | 1 |
| +114 | 1 |
| +134 | 1 |
| +159 | 1 |
| +164 | 1 |
| +169 | 1 |
| +189 | 1 |
| +199 | 1 |
| +209 | 1 |
| +234 | 1 |
| +239 | 1 |
| +294 | 1 |
| +299 | 1 |

![Last Session Market Share](charts/last_session_market_share.png)


![Last Session Latency Distribution](charts/last_session_latency_histogram.png)


![Last Session Latency by Registrar](charts/last_session_latency_by_registrar.png)


![Last Session Timing Distribution](charts/last_session_timing_distribution.png)


---

## Rolling Windows

### Last 4 Sessions

- **Sessions covered:** 1  (2026-04-15 → 2026-04-15)
- **Total domains registered:** 255
- **Avg domains/session:** 255.0
- **Unique registrars (ever active):** 11
- **Avg registrars/session:** 11
- **Market concentration HHI:** 4,604.8

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 164 | 64.31% | 1 | 11960.3 |
| BareMetal.com inc | 52 | 20.39% | 1 | 13326.7 |
| Webnames.ca Inc. | 16 | 6.27% | 1 | 157460.3 |
| MyID.ca INC. | 7 | 2.75% | 1 | 5179.7 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 4 | 1.57% | 1 | 14431.2 |
| Grape Inc. | 3 | 1.18% | 1 | 3486 |
| Namespro Solutions Inc. | 2 | 0.78% | 1 | 12229 |
| DomainePlus.com (3612040 CANADA inc.) | 2 | 0.78% | 1 | 744 |
| PlanetHoster | 2 | 0.78% | 1 | 4720 |
| easyDNS Technologies Inc. | 2 | 0.78% | 1 | 11814 |
| Register.ca Inc. | 1 | 0.39% | 1 | 10031 |

![Last 4 Sessions Market Share](charts/last_4_sessions_market_share.png)


---

### Last ~6 Months (26 Weeks)

- **Sessions covered:** 1  (2026-04-15 → 2026-04-15)
- **Total domains registered:** 255
- **Avg domains/session:** 255.0
- **Unique registrars (ever active):** 11
- **Avg registrars/session:** 11
- **Market concentration HHI:** 4,604.8

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 164 | 64.31% | 1 | 11960.3 |
| BareMetal.com inc | 52 | 20.39% | 1 | 13326.7 |
| Webnames.ca Inc. | 16 | 6.27% | 1 | 157460.3 |
| MyID.ca INC. | 7 | 2.75% | 1 | 5179.7 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 4 | 1.57% | 1 | 14431.2 |
| Grape Inc. | 3 | 1.18% | 1 | 3486 |
| Namespro Solutions Inc. | 2 | 0.78% | 1 | 12229 |
| DomainePlus.com (3612040 CANADA inc.) | 2 | 0.78% | 1 | 744 |
| PlanetHoster | 2 | 0.78% | 1 | 4720 |
| easyDNS Technologies Inc. | 2 | 0.78% | 1 | 11814 |
| Register.ca Inc. | 1 | 0.39% | 1 | 10031 |

![Last 26 Weeks Market Share](charts/last_26_weeks_market_share.png)


---

### Last 52 Weeks

- **Sessions covered:** 1  (2026-04-15 → 2026-04-15)
- **Total domains registered:** 255
- **Avg domains/session:** 255.0
- **Unique registrars (ever active):** 11
- **Avg registrars/session:** 11
- **Market concentration HHI:** 4,604.8

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 164 | 64.31% | 1 | 11960.3 |
| BareMetal.com inc | 52 | 20.39% | 1 | 13326.7 |
| Webnames.ca Inc. | 16 | 6.27% | 1 | 157460.3 |
| MyID.ca INC. | 7 | 2.75% | 1 | 5179.7 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 4 | 1.57% | 1 | 14431.2 |
| Grape Inc. | 3 | 1.18% | 1 | 3486 |
| Namespro Solutions Inc. | 2 | 0.78% | 1 | 12229 |
| DomainePlus.com (3612040 CANADA inc.) | 2 | 0.78% | 1 | 744 |
| PlanetHoster | 2 | 0.78% | 1 | 4720 |
| easyDNS Technologies Inc. | 2 | 0.78% | 1 | 11814 |
| Register.ca Inc. | 1 | 0.39% | 1 | 10031 |

![Last 52 Weeks Market Share](charts/last_52_weeks_market_share.png)


---

## All Time

- **Sessions covered:** 1  (2026-04-15 → 2026-04-15)
- **Total domains registered:** 255
- **Avg domains/session:** 255.0
- **Unique registrars (ever active):** 11
- **Avg registrars/session:** 11
- **Market concentration HHI:** 4,604.8

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 164 | 64.31% | 1 | 11960.3 |
| BareMetal.com inc | 52 | 20.39% | 1 | 13326.7 |
| Webnames.ca Inc. | 16 | 6.27% | 1 | 157460.3 |
| MyID.ca INC. | 7 | 2.75% | 1 | 5179.7 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 4 | 1.57% | 1 | 14431.2 |
| Grape Inc. | 3 | 1.18% | 1 | 3486 |
| Namespro Solutions Inc. | 2 | 0.78% | 1 | 12229 |
| DomainePlus.com (3612040 CANADA inc.) | 2 | 0.78% | 1 | 744 |
| PlanetHoster | 2 | 0.78% | 1 | 4720 |
| easyDNS Technologies Inc. | 2 | 0.78% | 1 | 11814 |
| Register.ca Inc. | 1 | 0.39% | 1 | 10031 |

![All Time Market Share](charts/all_time_market_share.png)



---

## By Year

### 2026

- **Sessions covered:** 1  (2026-04-15 → 2026-04-15)
- **Total domains registered:** 255
- **Avg domains/session:** 255.0
- **Unique registrars (ever active):** 11
- **Avg registrars/session:** 11
- **Market concentration HHI:** 4,604.8

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 164 | 64.31% | 1 | 11960.3 |
| BareMetal.com inc | 52 | 20.39% | 1 | 13326.7 |
| Webnames.ca Inc. | 16 | 6.27% | 1 | 157460.3 |
| MyID.ca INC. | 7 | 2.75% | 1 | 5179.7 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 4 | 1.57% | 1 | 14431.2 |
| Grape Inc. | 3 | 1.18% | 1 | 3486 |
| Namespro Solutions Inc. | 2 | 0.78% | 1 | 12229 |
| DomainePlus.com (3612040 CANADA inc.) | 2 | 0.78% | 1 | 744 |
| PlanetHoster | 2 | 0.78% | 1 | 4720 |
| easyDNS Technologies Inc. | 2 | 0.78% | 1 | 11814 |
| Register.ca Inc. | 1 | 0.39% | 1 | 10031 |

![Market share 2026](charts/year_2026_market_share.png)


---

## By Month

#### 2026-04

- **Sessions covered:** 1  (2026-04-15 → 2026-04-15)
- **Total domains registered:** 255
- **Avg domains/session:** 255.0
- **Unique registrars (ever active):** 11
- **Avg registrars/session:** 11
- **Market concentration HHI:** 4,604.8

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 164 | 64.31% | 1 | 11960.3 |
| BareMetal.com inc | 52 | 20.39% | 1 | 13326.7 |
| Webnames.ca Inc. | 16 | 6.27% | 1 | 157460.3 |
| MyID.ca INC. | 7 | 2.75% | 1 | 5179.7 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 4 | 1.57% | 1 | 14431.2 |
| Grape Inc. | 3 | 1.18% | 1 | 3486 |
| Namespro Solutions Inc. | 2 | 0.78% | 1 | 12229 |
| DomainePlus.com (3612040 CANADA inc.) | 2 | 0.78% | 1 | 744 |
| PlanetHoster | 2 | 0.78% | 1 | 4720 |
| easyDNS Technologies Inc. | 2 | 0.78% | 1 | 11814 |
| Register.ca Inc. | 1 | 0.39% | 1 | 10031 |


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
