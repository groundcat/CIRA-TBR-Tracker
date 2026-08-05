# CIRA TBR Tracker

> Automated archive and analytics for CIRA **To-Be-Released (TBR)** `.CA` domain
> drop sessions. Updated every **Wednesday ≈ 19:30 UTC** via GitHub Actions.

**Last updated:** 2026-08-05 &nbsp;|&nbsp; **Total sessions tracked:** 17

---

## What is TBR?

CIRA releases expired `.CA` domains every **Wednesday at 19:00 UTC** via a
first-come, first-served process. Whichever registrar submits a registration
request first wins the domain (one connection, one request per 5 s per registrar).

Capture latency is measured from the official session open at **19:00:00.000 UTC**.

---

## Last Session

- **Date:** 2026-08-05
- **Domains released:** 265
- **Domains registered:** 265
- **Registration rate:** 100.0%
- **Unique registrars:** 8
- **Session duration:** 213,419 ms
- **Market concentration (HHI):** 4,367.3

**Capture latency across all registrars:**
- Min: 5 ms | Median: 11987 ms | Mean: 16185.4 ms | P95: 21542 ms | Max: 213424 ms

**Per-registrar latency breakdown:**

| Registrar | Domains | Min (ms) | Median (ms) | Mean (ms) | P95 (ms) | Max (ms) | StdDev (ms) |
|-----------|--------:|---------:|------------:|----------:|---------:|---------:|------------:|
| WHC Online Solutions Inc. | 163 | 8 | 12076 | 12373.3 | 21206 | 21542 | 5665.2 |
| BareMetal.com inc | 61 | 7 | 15251 | 12218.3 | 20782 | 21135 | 6800.7 |
| MyID.ca INC. | 12 | 10 | 3458 | 2783.4 | 5407 | 5407 | 2618.4 |
| Register.ca Inc. | 10 | 5 | 43 | 2056.8 | 10269 | 10269 | 4257.6 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 10 | 2478 | 100698 | 83667.1 | 141720 | 141720 | 53590.1 |
| Webnames.ca Inc. | 5 | 42851 | 62912 | 116094.8 | 213424 | 213424 | 86866.8 |
| Grape Inc. | 3 | 43 | 10265 | 11924 | 25464 | 25464 | 12791.4 |
| Namespro Solutions Inc. | 1 | 20088 | 20088 | 20088 | 20088 | 20088 | 0 |

**Timing distribution (captures by second offset from 19:00:00 UTC):**

| Offset (s) | Domains Captured |
|-----------:|-----------------:|
| +0 | 28 |
| +1 | 2 |
| +2 | 3 |
| +5 | 27 |
| +6 | 19 |
| +7 | 9 |
| +8 | 3 |
| +9 | 1 |
| +10 | 18 |
| +11 | 23 |
| +12 | 12 |
| +13 | 5 |
| +14 | 1 |
| +15 | 19 |
| +16 | 28 |
| +17 | 14 |
| +18 | 5 |
| +19 | 2 |
| +20 | 21 |
| +21 | 12 |
| +25 | 1 |
| +42 | 1 |
| +52 | 1 |
| +62 | 1 |
| +87 | 1 |
| +97 | 1 |
| +103 | 1 |
| +109 | 1 |
| +130 | 1 |
| +136 | 1 |
| +141 | 1 |
| +208 | 1 |
| +213 | 1 |

![Last Session Market Share](charts/last_session_market_share.png)


![Last Session Latency Distribution](charts/last_session_latency_histogram.png)


![Last Session Latency by Registrar](charts/last_session_latency_by_registrar.png)


![Last Session Timing Distribution](charts/last_session_timing_distribution.png)


---

## Rolling Windows

### Last 4 Sessions

- **Sessions covered:** 4  (2026-07-15 → 2026-08-05)
- **Total domains registered:** 1,083
- **Avg domains/session:** 270.8
- **Unique registrars (ever active):** 10
- **Avg registrars/session:** 8.5
- **Market concentration HHI:** 4,329.7

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 657 | 60.66% | 4 | 11423.2 |
| BareMetal.com inc | 264 | 24.38% | 4 | 15309.4 |
| MyID.ca INC. | 66 | 6.09% | 4 | 3356.2 |
| Webnames.ca Inc. | 28 | 2.59% | 4 | 79794.4 |
| Register.ca Inc. | 28 | 2.59% | 4 | 2774.6 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 23 | 2.12% | 4 | 62297.8 |
| Grape Inc. | 7 | 0.65% | 2 | 7235.9 |
| PlanetHoster | 4 | 0.37% | 3 | 960.7 |
| Namespro Solutions Inc. | 4 | 0.37% | 3 | 22405.7 |
| easyDNS Technologies Inc. | 2 | 0.18% | 2 | 6449.5 |

![Last 4 Sessions Market Share](charts/last_4_sessions_market_share.png)


---

### Last ~6 Months (26 Weeks)

- **Sessions covered:** 17  (2026-04-15 → 2026-08-05)
- **Total domains registered:** 3,911
- **Avg domains/session:** 230.1
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 9.1
- **Market concentration HHI:** 4,428.2

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 2,430 | 62.13% | 17 | 10249.2 |
| BareMetal.com inc | 892 | 22.81% | 17 | 12567.6 |
| MyID.ca INC. | 210 | 5.37% | 16 | 8150.0 |
| Webnames.ca Inc. | 121 | 3.09% | 17 | 82397.5 |
| Register.ca Inc. | 92 | 2.35% | 14 | 3090.8 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 60 | 1.53% | 15 | 37660.7 |
| Grape Inc. | 32 | 0.82% | 13 | 2237.1 |
| DomainePlus.com (3612040 CANADA inc.) | 22 | 0.56% | 12 | 4218.0 |
| Namespro Solutions Inc. | 19 | 0.49% | 10 | 27391.1 |
| PlanetHoster | 17 | 0.43% | 11 | 1365.9 |
| easyDNS Technologies Inc. | 11 | 0.28% | 8 | 10928.4 |
| CanSpace Solutions Inc. | 3 | 0.08% | 3 | 160067.3 |
| FastWebServer Internet Services Inc. | 2 | 0.05% | 2 | 3029.5 |

![Last 26 Weeks Market Share](charts/last_26_weeks_market_share.png)


---

### Last 52 Weeks

- **Sessions covered:** 17  (2026-04-15 → 2026-08-05)
- **Total domains registered:** 3,911
- **Avg domains/session:** 230.1
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 9.1
- **Market concentration HHI:** 4,428.2

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 2,430 | 62.13% | 17 | 10249.2 |
| BareMetal.com inc | 892 | 22.81% | 17 | 12567.6 |
| MyID.ca INC. | 210 | 5.37% | 16 | 8150.0 |
| Webnames.ca Inc. | 121 | 3.09% | 17 | 82397.5 |
| Register.ca Inc. | 92 | 2.35% | 14 | 3090.8 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 60 | 1.53% | 15 | 37660.7 |
| Grape Inc. | 32 | 0.82% | 13 | 2237.1 |
| DomainePlus.com (3612040 CANADA inc.) | 22 | 0.56% | 12 | 4218.0 |
| Namespro Solutions Inc. | 19 | 0.49% | 10 | 27391.1 |
| PlanetHoster | 17 | 0.43% | 11 | 1365.9 |
| easyDNS Technologies Inc. | 11 | 0.28% | 8 | 10928.4 |
| CanSpace Solutions Inc. | 3 | 0.08% | 3 | 160067.3 |
| FastWebServer Internet Services Inc. | 2 | 0.05% | 2 | 3029.5 |

![Last 52 Weeks Market Share](charts/last_52_weeks_market_share.png)


---

## All Time

- **Sessions covered:** 17  (2026-04-15 → 2026-08-05)
- **Total domains registered:** 3,911
- **Avg domains/session:** 230.1
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 9.1
- **Market concentration HHI:** 4,428.2

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 2,430 | 62.13% | 17 | 10249.2 |
| BareMetal.com inc | 892 | 22.81% | 17 | 12567.6 |
| MyID.ca INC. | 210 | 5.37% | 16 | 8150.0 |
| Webnames.ca Inc. | 121 | 3.09% | 17 | 82397.5 |
| Register.ca Inc. | 92 | 2.35% | 14 | 3090.8 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 60 | 1.53% | 15 | 37660.7 |
| Grape Inc. | 32 | 0.82% | 13 | 2237.1 |
| DomainePlus.com (3612040 CANADA inc.) | 22 | 0.56% | 12 | 4218.0 |
| Namespro Solutions Inc. | 19 | 0.49% | 10 | 27391.1 |
| PlanetHoster | 17 | 0.43% | 11 | 1365.9 |
| easyDNS Technologies Inc. | 11 | 0.28% | 8 | 10928.4 |
| CanSpace Solutions Inc. | 3 | 0.08% | 3 | 160067.3 |
| FastWebServer Internet Services Inc. | 2 | 0.05% | 2 | 3029.5 |

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

- **Sessions covered:** 17  (2026-04-15 → 2026-08-05)
- **Total domains registered:** 3,911
- **Avg domains/session:** 230.1
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 9.1
- **Market concentration HHI:** 4,428.2

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 2,430 | 62.13% | 17 | 10249.2 |
| BareMetal.com inc | 892 | 22.81% | 17 | 12567.6 |
| MyID.ca INC. | 210 | 5.37% | 16 | 8150.0 |
| Webnames.ca Inc. | 121 | 3.09% | 17 | 82397.5 |
| Register.ca Inc. | 92 | 2.35% | 14 | 3090.8 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 60 | 1.53% | 15 | 37660.7 |
| Grape Inc. | 32 | 0.82% | 13 | 2237.1 |
| DomainePlus.com (3612040 CANADA inc.) | 22 | 0.56% | 12 | 4218.0 |
| Namespro Solutions Inc. | 19 | 0.49% | 10 | 27391.1 |
| PlanetHoster | 17 | 0.43% | 11 | 1365.9 |
| easyDNS Technologies Inc. | 11 | 0.28% | 8 | 10928.4 |
| CanSpace Solutions Inc. | 3 | 0.08% | 3 | 160067.3 |
| FastWebServer Internet Services Inc. | 2 | 0.05% | 2 | 3029.5 |

![Market share 2026](charts/year_2026_market_share.png)


---

## By Month

#### 2026-04

- **Sessions covered:** 3  (2026-04-15 → 2026-04-29)
- **Total domains registered:** 746
- **Avg domains/session:** 248.7
- **Unique registrars (ever active):** 12
- **Avg registrars/session:** 10
- **Market concentration HHI:** 5,094.3

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 512 | 68.63% | 3 | 11691.0 |
| BareMetal.com inc | 140 | 18.77% | 3 | 12138.8 |
| MyID.ca INC. | 31 | 4.16% | 3 | 5312.3 |
| Webnames.ca Inc. | 24 | 3.22% | 3 | 91027.8 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 8 | 1.07% | 3 | 23467.1 |
| DomainePlus.com (3612040 CANADA inc.) | 8 | 1.07% | 3 | 5592 |
| Grape Inc. | 7 | 0.94% | 3 | 1755.4 |
| Namespro Solutions Inc. | 5 | 0.67% | 2 | 21235.8 |
| PlanetHoster | 4 | 0.54% | 2 | 2473.2 |
| easyDNS Technologies Inc. | 3 | 0.4% | 2 | 9532.5 |
| Register.ca Inc. | 3 | 0.4% | 2 | 5020.8 |
| CanSpace Solutions Inc. | 1 | 0.13% | 1 | 472283 |

#### 2026-05

- **Sessions covered:** 4  (2026-05-06 → 2026-05-27)
- **Total domains registered:** 863
- **Avg domains/session:** 215.8
- **Unique registrars (ever active):** 12
- **Avg registrars/session:** 8.2
- **Market concentration HHI:** 4,411.2

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 530 | 61.41% | 4 | 9509.0 |
| BareMetal.com inc | 210 | 24.33% | 4 | 11662.0 |
| Webnames.ca Inc. | 40 | 4.63% | 4 | 97153.4 |
| MyID.ca INC. | 39 | 4.52% | 3 | 15531.4 |
| Register.ca Inc. | 19 | 2.2% | 2 | 999.5 |
| Grape Inc. | 5 | 0.58% | 3 | 49.7 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 5 | 0.58% | 2 | 47995.1 |
| DomainePlus.com (3612040 CANADA inc.) | 5 | 0.58% | 4 | 735.9 |
| Namespro Solutions Inc. | 3 | 0.35% | 2 | 17200.2 |
| PlanetHoster | 3 | 0.35% | 2 | 2718.8 |
| easyDNS Technologies Inc. | 3 | 0.35% | 2 | 12175.8 |
| CanSpace Solutions Inc. | 1 | 0.12% | 1 | 7370 |

#### 2026-06

- **Sessions covered:** 4  (2026-06-03 → 2026-06-24)
- **Total domains registered:** 794
- **Avg domains/session:** 198.5
- **Unique registrars (ever active):** 11
- **Avg registrars/session:** 8.8
- **Market concentration HHI:** 4,202.1

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 477 | 60.08% | 4 | 9082.6 |
| BareMetal.com inc | 183 | 23.05% | 4 | 10680.8 |
| MyID.ca INC. | 49 | 6.17% | 4 | 12134.8 |
| Register.ca Inc. | 28 | 3.53% | 4 | 3083.2 |
| Webnames.ca Inc. | 19 | 2.39% | 4 | 61415.4 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 13 | 1.64% | 4 | 21115.8 |
| Grape Inc. | 8 | 1.01% | 3 | 1671.7 |
| Namespro Solutions Inc. | 6 | 0.76% | 2 | 21410.8 |
| DomainePlus.com (3612040 CANADA inc.) | 5 | 0.63% | 3 | 4468.5 |
| PlanetHoster | 4 | 0.5% | 2 | 571.8 |
| easyDNS Technologies Inc. | 2 | 0.25% | 1 | 30047.5 |

#### 2026-07

- **Sessions covered:** 5  (2026-07-01 → 2026-07-29)
- **Total domains registered:** 1,243
- **Avg domains/session:** 248.6
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 9.8
- **Market concentration HHI:** 4,255.0

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 748 | 60.18% | 5 | 10484.8 |
| BareMetal.com inc | 298 | 23.97% | 5 | 15128.8 |
| MyID.ca INC. | 79 | 6.36% | 5 | 3309.2 |
| Webnames.ca Inc. | 33 | 2.65% | 5 | 75460.8 |
| Register.ca Inc. | 32 | 2.57% | 5 | 3368.1 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 24 | 1.93% | 5 | 46077.7 |
| Grape Inc. | 9 | 0.72% | 3 | 2242.8 |
| PlanetHoster | 6 | 0.48% | 5 | 699.4 |
| DomainePlus.com (3612040 CANADA inc.) | 4 | 0.32% | 2 | 8745.8 |
| Namespro Solutions Inc. | 4 | 0.32% | 3 | 44709.7 |
| easyDNS Technologies Inc. | 3 | 0.24% | 3 | 4654.3 |
| FastWebServer Internet Services Inc. | 2 | 0.16% | 2 | 3029.5 |
| CanSpace Solutions Inc. | 1 | 0.08% | 1 | 549 |

#### 2026-08

- **Sessions covered:** 1  (2026-08-05 → 2026-08-05)
- **Total domains registered:** 265
- **Avg domains/session:** 265.0
- **Unique registrars (ever active):** 8
- **Avg registrars/session:** 8
- **Market concentration HHI:** 4,367.3

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 163 | 61.51% | 1 | 12373.3 |
| BareMetal.com inc | 61 | 23.02% | 1 | 12218.3 |
| MyID.ca INC. | 12 | 4.53% | 1 | 2783.4 |
| Register.ca Inc. | 10 | 3.77% | 1 | 2056.8 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 10 | 3.77% | 1 | 83667.1 |
| Webnames.ca Inc. | 5 | 1.89% | 1 | 116094.8 |
| Grape Inc. | 3 | 1.13% | 1 | 11924 |
| Namespro Solutions Inc. | 1 | 0.38% | 1 | 20088 |


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
