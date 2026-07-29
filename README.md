# CIRA TBR Tracker

> Automated archive and analytics for CIRA **To-Be-Released (TBR)** `.CA` domain
> drop sessions. Updated every **Wednesday ≈ 19:30 UTC** via GitHub Actions.

**Last updated:** 2026-07-29 &nbsp;|&nbsp; **Total sessions tracked:** 16

---

## What is TBR?

CIRA releases expired `.CA` domains every **Wednesday at 19:00 UTC** via a
first-come, first-served process. Whichever registrar submits a registration
request first wins the domain (one connection, one request per 5 s per registrar).

Capture latency is measured from the official session open at **19:00:00.000 UTC**.

---

## Last Session

- **Date:** 2026-07-29
- **Domains released:** 279
- **Domains registered:** 279
- **Registration rate:** 100.0%
- **Unique registrars:** 8
- **Session duration:** 162,835 ms
- **Market concentration (HHI):** 4,282.5

**Capture latency across all registrars:**
- Min: 3 ms | Median: 12939 ms | Mean: 15717.0 ms | P95: 32907 ms | Max: 162838 ms

**Per-registrar latency breakdown:**

| Registrar | Domains | Min (ms) | Median (ms) | Mean (ms) | P95 (ms) | Max (ms) | StdDev (ms) |
|-----------|--------:|---------:|------------:|----------:|---------:|---------:|------------:|
| WHC Online Solutions Inc. | 164 | 12 | 11982 | 12138.9 | 20587 | 21513 | 5685.8 |
| BareMetal.com inc | 78 | 3 | 20355 | 19705.3 | 35315 | 35411 | 10226.0 |
| MyID.ca INC. | 15 | 34 | 436 | 2070.8 | 5880 | 5880 | 2444.5 |
| Webnames.ca Inc. | 9 | 4727 | 37361 | 60975.9 | 162838 | 162838 | 57551.8 |
| Register.ca Inc. | 5 | 25 | 52 | 2034 | 5040 | 5040 | 2734.1 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 4 | 20408 | 47186 | 45996 | 69203 | 69203 | 23705.8 |
| PlanetHoster | 2 | 483 | 1145 | 1145 | 1807 | 1807 | 936.2 |
| Namespro Solutions Inc. | 2 | 37932 | 40483 | 40483 | 43034 | 43034 | 3607.7 |

**Timing distribution (captures by second offset from 19:00:00 UTC):**

| Offset (s) | Domains Captured |
|-----------:|-----------------:|
| +0 | 26 |
| +1 | 4 |
| +2 | 1 |
| +4 | 2 |
| +5 | 28 |
| +6 | 15 |
| +7 | 7 |
| +8 | 1 |
| +9 | 1 |
| +10 | 22 |
| +11 | 20 |
| +12 | 13 |
| +13 | 3 |
| +14 | 2 |
| +15 | 25 |
| +16 | 15 |
| +17 | 17 |
| +18 | 4 |
| +19 | 2 |
| +20 | 19 |
| +21 | 6 |
| +22 | 2 |
| +25 | 4 |
| +26 | 2 |
| +27 | 5 |
| +30 | 12 |
| +31 | 3 |
| +32 | 5 |
| +35 | 4 |
| +37 | 2 |
| +43 | 1 |
| +47 | 1 |
| +62 | 1 |
| +69 | 1 |
| +77 | 1 |
| +147 | 1 |
| +162 | 1 |

![Last Session Market Share](charts/last_session_market_share.png)


![Last Session Latency Distribution](charts/last_session_latency_histogram.png)


![Last Session Latency by Registrar](charts/last_session_latency_by_registrar.png)


![Last Session Timing Distribution](charts/last_session_timing_distribution.png)


---

## Rolling Windows

### Last 4 Sessions

- **Sessions covered:** 4  (2026-07-08 → 2026-07-29)
- **Total domains registered:** 1,000
- **Avg domains/session:** 250.0
- **Unique registrars (ever active):** 12
- **Avg registrars/session:** 9
- **Market concentration HHI:** 4,194.7

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 595 | 59.5% | 4 | 10125.8 |
| BareMetal.com inc | 242 | 24.2% | 4 | 15245.0 |
| MyID.ca INC. | 70 | 7.0% | 4 | 3208.7 |
| Webnames.ca Inc. | 31 | 3.1% | 4 | 56593.5 |
| Register.ca Inc. | 24 | 2.4% | 4 | 3528.2 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 19 | 1.9% | 4 | 53058.7 |
| Grape Inc. | 6 | 0.6% | 2 | 2523.7 |
| PlanetHoster | 5 | 0.5% | 4 | 793 |
| Namespro Solutions Inc. | 3 | 0.3% | 2 | 23564.5 |
| DomainePlus.com (3612040 CANADA inc.) | 2 | 0.2% | 1 | 4169 |
| easyDNS Technologies Inc. | 2 | 0.2% | 2 | 6449.5 |
| FastWebServer Internet Services Inc. | 1 | 0.1% | 1 | 9 |

![Last 4 Sessions Market Share](charts/last_4_sessions_market_share.png)


---

### Last ~6 Months (26 Weeks)

- **Sessions covered:** 16  (2026-04-15 → 2026-07-29)
- **Total domains registered:** 3,646
- **Avg domains/session:** 227.9
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 9.2
- **Market concentration HHI:** 4,433.8

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 2,267 | 62.18% | 16 | 10116.4 |
| BareMetal.com inc | 831 | 22.79% | 16 | 12589.5 |
| MyID.ca INC. | 198 | 5.43% | 15 | 8507.7 |
| Webnames.ca Inc. | 116 | 3.18% | 16 | 80291.4 |
| Register.ca Inc. | 82 | 2.25% | 13 | 3170.3 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 50 | 1.37% | 14 | 34374.5 |
| Grape Inc. | 29 | 0.8% | 12 | 1429.9 |
| DomainePlus.com (3612040 CANADA inc.) | 22 | 0.6% | 12 | 4218.0 |
| Namespro Solutions Inc. | 18 | 0.49% | 9 | 28202.5 |
| PlanetHoster | 17 | 0.47% | 11 | 1365.9 |
| easyDNS Technologies Inc. | 11 | 0.3% | 8 | 10928.4 |
| CanSpace Solutions Inc. | 3 | 0.08% | 3 | 160067.3 |
| FastWebServer Internet Services Inc. | 2 | 0.05% | 2 | 3029.5 |

![Last 26 Weeks Market Share](charts/last_26_weeks_market_share.png)


---

### Last 52 Weeks

- **Sessions covered:** 16  (2026-04-15 → 2026-07-29)
- **Total domains registered:** 3,646
- **Avg domains/session:** 227.9
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 9.2
- **Market concentration HHI:** 4,433.8

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 2,267 | 62.18% | 16 | 10116.4 |
| BareMetal.com inc | 831 | 22.79% | 16 | 12589.5 |
| MyID.ca INC. | 198 | 5.43% | 15 | 8507.7 |
| Webnames.ca Inc. | 116 | 3.18% | 16 | 80291.4 |
| Register.ca Inc. | 82 | 2.25% | 13 | 3170.3 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 50 | 1.37% | 14 | 34374.5 |
| Grape Inc. | 29 | 0.8% | 12 | 1429.9 |
| DomainePlus.com (3612040 CANADA inc.) | 22 | 0.6% | 12 | 4218.0 |
| Namespro Solutions Inc. | 18 | 0.49% | 9 | 28202.5 |
| PlanetHoster | 17 | 0.47% | 11 | 1365.9 |
| easyDNS Technologies Inc. | 11 | 0.3% | 8 | 10928.4 |
| CanSpace Solutions Inc. | 3 | 0.08% | 3 | 160067.3 |
| FastWebServer Internet Services Inc. | 2 | 0.05% | 2 | 3029.5 |

![Last 52 Weeks Market Share](charts/last_52_weeks_market_share.png)


---

## All Time

- **Sessions covered:** 16  (2026-04-15 → 2026-07-29)
- **Total domains registered:** 3,646
- **Avg domains/session:** 227.9
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 9.2
- **Market concentration HHI:** 4,433.8

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 2,267 | 62.18% | 16 | 10116.4 |
| BareMetal.com inc | 831 | 22.79% | 16 | 12589.5 |
| MyID.ca INC. | 198 | 5.43% | 15 | 8507.7 |
| Webnames.ca Inc. | 116 | 3.18% | 16 | 80291.4 |
| Register.ca Inc. | 82 | 2.25% | 13 | 3170.3 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 50 | 1.37% | 14 | 34374.5 |
| Grape Inc. | 29 | 0.8% | 12 | 1429.9 |
| DomainePlus.com (3612040 CANADA inc.) | 22 | 0.6% | 12 | 4218.0 |
| Namespro Solutions Inc. | 18 | 0.49% | 9 | 28202.5 |
| PlanetHoster | 17 | 0.47% | 11 | 1365.9 |
| easyDNS Technologies Inc. | 11 | 0.3% | 8 | 10928.4 |
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

- **Sessions covered:** 16  (2026-04-15 → 2026-07-29)
- **Total domains registered:** 3,646
- **Avg domains/session:** 227.9
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 9.2
- **Market concentration HHI:** 4,433.8

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 2,267 | 62.18% | 16 | 10116.4 |
| BareMetal.com inc | 831 | 22.79% | 16 | 12589.5 |
| MyID.ca INC. | 198 | 5.43% | 15 | 8507.7 |
| Webnames.ca Inc. | 116 | 3.18% | 16 | 80291.4 |
| Register.ca Inc. | 82 | 2.25% | 13 | 3170.3 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 50 | 1.37% | 14 | 34374.5 |
| Grape Inc. | 29 | 0.8% | 12 | 1429.9 |
| DomainePlus.com (3612040 CANADA inc.) | 22 | 0.6% | 12 | 4218.0 |
| Namespro Solutions Inc. | 18 | 0.49% | 9 | 28202.5 |
| PlanetHoster | 17 | 0.47% | 11 | 1365.9 |
| easyDNS Technologies Inc. | 11 | 0.3% | 8 | 10928.4 |
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
