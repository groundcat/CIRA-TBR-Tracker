# CIRA TBR Tracker

> Automated archive and analytics for CIRA **To-Be-Released (TBR)** `.CA` domain
> drop sessions. Updated every **Wednesday ≈ 19:30 UTC** via GitHub Actions.

**Last updated:** 2026-07-15 &nbsp;|&nbsp; **Total sessions tracked:** 14

---

## What is TBR?

CIRA releases expired `.CA` domains every **Wednesday at 19:00 UTC** via a
first-come, first-served process. Whichever registrar submits a registration
request first wins the domain (one connection, one request per 5 s per registrar).

Capture latency is measured from the official session open at **19:00:00.000 UTC**.

---

## Last Session

- **Date:** 2026-07-15
- **Domains released:** 283
- **Domains registered:** 283
- **Registration rate:** 100.0%
- **Unique registrars:** 9
- **Session duration:** 102,847 ms
- **Market concentration (HHI):** 4,358.0

**Capture latency across all registrars:**
- Min: 33 ms | Median: 11412 ms | Mean: 12946.4 ms | P95: 25411 ms | Max: 102880 ms

**Per-registrar latency breakdown:**

| Registrar | Domains | Min (ms) | Median (ms) | Mean (ms) | P95 (ms) | Max (ms) | StdDev (ms) |
|-----------|--------:|---------:|------------:|----------:|---------:|---------:|------------:|
| WHC Online Solutions Inc. | 171 | 363 | 11397 | 11236.3 | 20543 | 21297 | 5853.6 |
| BareMetal.com inc | 73 | 70 | 15763 | 15930.9 | 25517 | 25913 | 7254.6 |
| MyID.ca INC. | 14 | 35 | 4945 | 2986.8 | 5895 | 5895 | 2636.6 |
| Webnames.ca Inc. | 7 | 503 | 31827 | 30225.4 | 51950 | 51950 | 18386.7 |
| Register.ca Inc. | 6 | 46 | 5030 | 3442.8 | 5067 | 5067 | 2480.6 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 6 | 1181 | 34533 | 47168.5 | 102880 | 102880 | 41378.9 |
| Grape Inc. | 4 | 33 | 2544 | 2547.8 | 5069 | 5069 | 2894.0 |
| PlanetHoster | 1 | 489 | 489 | 489 | 489 | 489 | 0 |
| easyDNS Technologies Inc. | 1 | 11712 | 11712 | 11712 | 11712 | 11712 | 0 |

**Timing distribution (captures by second offset from 19:00:00 UTC):**

| Offset (s) | Domains Captured |
|-----------:|-----------------:|
| +0 | 27 |
| +1 | 8 |
| +4 | 3 |
| +5 | 33 |
| +6 | 25 |
| +7 | 2 |
| +10 | 24 |
| +11 | 25 |
| +12 | 13 |
| +15 | 26 |
| +16 | 27 |
| +17 | 15 |
| +18 | 1 |
| +20 | 24 |
| +21 | 7 |
| +24 | 1 |
| +25 | 15 |
| +31 | 1 |
| +41 | 1 |
| +45 | 1 |
| +46 | 1 |
| +51 | 1 |
| +91 | 1 |
| +102 | 1 |

![Last Session Market Share](charts/last_session_market_share.png)


![Last Session Latency Distribution](charts/last_session_latency_histogram.png)


![Last Session Latency by Registrar](charts/last_session_latency_by_registrar.png)


![Last Session Timing Distribution](charts/last_session_timing_distribution.png)


---

## Rolling Windows

### Last 4 Sessions

- **Sessions covered:** 4  (2026-06-24 → 2026-07-15)
- **Total domains registered:** 917
- **Avg domains/session:** 229.2
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 9.8
- **Market concentration HHI:** 4,398.8

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 567 | 61.83% | 4 | 9976.4 |
| BareMetal.com inc | 211 | 23.01% | 4 | 12866.0 |
| MyID.ca INC. | 46 | 5.02% | 4 | 2263.8 |
| Register.ca Inc. | 26 | 2.84% | 4 | 3463.9 |
| Webnames.ca Inc. | 24 | 2.62% | 4 | 63515.8 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 20 | 2.18% | 4 | 31582.9 |
| Grape Inc. | 9 | 0.98% | 3 | 2242.8 |
| DomainePlus.com (3612040 CANADA inc.) | 5 | 0.55% | 3 | 9880.2 |
| PlanetHoster | 3 | 0.33% | 3 | 368 |
| easyDNS Technologies Inc. | 2 | 0.22% | 2 | 6388 |
| FastWebServer Internet Services Inc. | 2 | 0.22% | 2 | 3029.5 |
| CanSpace Solutions Inc. | 1 | 0.11% | 1 | 549 |
| Namespro Solutions Inc. | 1 | 0.11% | 1 | 87000 |

![Last 4 Sessions Market Share](charts/last_4_sessions_market_share.png)


---

### Last ~6 Months (26 Weeks)

- **Sessions covered:** 14  (2026-04-15 → 2026-07-15)
- **Total domains registered:** 3,111
- **Avg domains/session:** 222.2
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 9.3
- **Market concentration HHI:** 4,457.6

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 1,944 | 62.49% | 14 | 9984.3 |
| BareMetal.com inc | 701 | 22.53% | 14 | 12024.5 |
| MyID.ca INC. | 158 | 5.08% | 13 | 9227.8 |
| Webnames.ca Inc. | 100 | 3.21% | 14 | 79414.7 |
| Register.ca Inc. | 70 | 2.25% | 11 | 3237.8 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 43 | 1.38% | 12 | 30240.6 |
| Grape Inc. | 29 | 0.93% | 12 | 1429.9 |
| DomainePlus.com (3612040 CANADA inc.) | 22 | 0.71% | 12 | 4218.0 |
| Namespro Solutions Inc. | 15 | 0.48% | 7 | 29527.7 |
| PlanetHoster | 14 | 0.45% | 9 | 1403.5 |
| easyDNS Technologies Inc. | 10 | 0.32% | 7 | 12320.0 |
| CanSpace Solutions Inc. | 3 | 0.1% | 3 | 160067.3 |
| FastWebServer Internet Services Inc. | 2 | 0.06% | 2 | 3029.5 |

![Last 26 Weeks Market Share](charts/last_26_weeks_market_share.png)


---

### Last 52 Weeks

- **Sessions covered:** 14  (2026-04-15 → 2026-07-15)
- **Total domains registered:** 3,111
- **Avg domains/session:** 222.2
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 9.3
- **Market concentration HHI:** 4,457.6

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 1,944 | 62.49% | 14 | 9984.3 |
| BareMetal.com inc | 701 | 22.53% | 14 | 12024.5 |
| MyID.ca INC. | 158 | 5.08% | 13 | 9227.8 |
| Webnames.ca Inc. | 100 | 3.21% | 14 | 79414.7 |
| Register.ca Inc. | 70 | 2.25% | 11 | 3237.8 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 43 | 1.38% | 12 | 30240.6 |
| Grape Inc. | 29 | 0.93% | 12 | 1429.9 |
| DomainePlus.com (3612040 CANADA inc.) | 22 | 0.71% | 12 | 4218.0 |
| Namespro Solutions Inc. | 15 | 0.48% | 7 | 29527.7 |
| PlanetHoster | 14 | 0.45% | 9 | 1403.5 |
| easyDNS Technologies Inc. | 10 | 0.32% | 7 | 12320.0 |
| CanSpace Solutions Inc. | 3 | 0.1% | 3 | 160067.3 |
| FastWebServer Internet Services Inc. | 2 | 0.06% | 2 | 3029.5 |

![Last 52 Weeks Market Share](charts/last_52_weeks_market_share.png)


---

## All Time

- **Sessions covered:** 14  (2026-04-15 → 2026-07-15)
- **Total domains registered:** 3,111
- **Avg domains/session:** 222.2
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 9.3
- **Market concentration HHI:** 4,457.6

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 1,944 | 62.49% | 14 | 9984.3 |
| BareMetal.com inc | 701 | 22.53% | 14 | 12024.5 |
| MyID.ca INC. | 158 | 5.08% | 13 | 9227.8 |
| Webnames.ca Inc. | 100 | 3.21% | 14 | 79414.7 |
| Register.ca Inc. | 70 | 2.25% | 11 | 3237.8 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 43 | 1.38% | 12 | 30240.6 |
| Grape Inc. | 29 | 0.93% | 12 | 1429.9 |
| DomainePlus.com (3612040 CANADA inc.) | 22 | 0.71% | 12 | 4218.0 |
| Namespro Solutions Inc. | 15 | 0.48% | 7 | 29527.7 |
| PlanetHoster | 14 | 0.45% | 9 | 1403.5 |
| easyDNS Technologies Inc. | 10 | 0.32% | 7 | 12320.0 |
| CanSpace Solutions Inc. | 3 | 0.1% | 3 | 160067.3 |
| FastWebServer Internet Services Inc. | 2 | 0.06% | 2 | 3029.5 |

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

- **Sessions covered:** 14  (2026-04-15 → 2026-07-15)
- **Total domains registered:** 3,111
- **Avg domains/session:** 222.2
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 9.3
- **Market concentration HHI:** 4,457.6

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 1,944 | 62.49% | 14 | 9984.3 |
| BareMetal.com inc | 701 | 22.53% | 14 | 12024.5 |
| MyID.ca INC. | 158 | 5.08% | 13 | 9227.8 |
| Webnames.ca Inc. | 100 | 3.21% | 14 | 79414.7 |
| Register.ca Inc. | 70 | 2.25% | 11 | 3237.8 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 43 | 1.38% | 12 | 30240.6 |
| Grape Inc. | 29 | 0.93% | 12 | 1429.9 |
| DomainePlus.com (3612040 CANADA inc.) | 22 | 0.71% | 12 | 4218.0 |
| Namespro Solutions Inc. | 15 | 0.48% | 7 | 29527.7 |
| PlanetHoster | 14 | 0.45% | 9 | 1403.5 |
| easyDNS Technologies Inc. | 10 | 0.32% | 7 | 12320.0 |
| CanSpace Solutions Inc. | 3 | 0.1% | 3 | 160067.3 |
| FastWebServer Internet Services Inc. | 2 | 0.06% | 2 | 3029.5 |

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

- **Sessions covered:** 3  (2026-07-01 → 2026-07-15)
- **Total domains registered:** 708
- **Avg domains/session:** 236.0
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 10.7
- **Market concentration HHI:** 4,218.8

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 425 | 60.03% | 3 | 10113.5 |
| BareMetal.com inc | 168 | 23.73% | 3 | 14185.2 |
| MyID.ca INC. | 39 | 5.51% | 3 | 2963.7 |
| Register.ca Inc. | 20 | 2.82% | 3 | 3747.2 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 17 | 2.4% | 3 | 37344.3 |
| Webnames.ca Inc. | 17 | 2.4% | 3 | 68149.0 |
| Grape Inc. | 9 | 1.27% | 3 | 2242.8 |
| DomainePlus.com (3612040 CANADA inc.) | 4 | 0.56% | 2 | 8745.8 |
| PlanetHoster | 3 | 0.42% | 3 | 368 |
| easyDNS Technologies Inc. | 2 | 0.28% | 2 | 6388 |
| FastWebServer Internet Services Inc. | 2 | 0.28% | 2 | 3029.5 |
| CanSpace Solutions Inc. | 1 | 0.14% | 1 | 549 |
| Namespro Solutions Inc. | 1 | 0.14% | 1 | 87000 |


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
