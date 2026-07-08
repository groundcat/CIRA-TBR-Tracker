# CIRA TBR Tracker

> Automated archive and analytics for CIRA **To-Be-Released (TBR)** `.CA` domain
> drop sessions. Updated every **Wednesday ≈ 19:30 UTC** via GitHub Actions.

**Last updated:** 2026-07-08 &nbsp;|&nbsp; **Total sessions tracked:** 13

---

## What is TBR?

CIRA releases expired `.CA` domains every **Wednesday at 19:00 UTC** via a
first-come, first-served process. Whichever registrar submits a registration
request first wins the domain (one connection, one request per 5 s per registrar).

Capture latency is measured from the official session open at **19:00:00.000 UTC**.

---

## Last Session

- **Date:** 2026-07-08
- **Domains released:** 182
- **Domains registered:** 182
- **Registration rate:** 100.0%
- **Unique registrars:** 10
- **Session duration:** 99,022 ms
- **Market concentration (HHI):** 3,659.8

**Capture latency across all registrars:**
- Min: 0 ms | Median: 7056 ms | Mean: 9547.9 ms | P95: 20111 ms | Max: 99022 ms

**Per-registrar latency breakdown:**

| Registrar | Domains | Min (ms) | Median (ms) | Mean (ms) | P95 (ms) | Max (ms) | StdDev (ms) |
|-----------|--------:|---------:|------------:|----------:|---------:|---------:|------------:|
| WHC Online Solutions Inc. | 101 | 0 | 6521 | 7183.3 | 11725 | 12360 | 3722.7 |
| BareMetal.com inc | 39 | 0 | 11464 | 11960.5 | 20111 | 20123 | 5255.2 |
| MyID.ca INC. | 16 | 3 | 43 | 2193.4 | 5047 | 5047 | 2543.3 |
| Webnames.ca Inc. | 8 | 1416 | 21016 | 23291.5 | 53733 | 53733 | 16942.7 |
| Register.ca Inc. | 6 | 3 | 5070 | 5071.3 | 10315 | 10315 | 4534.7 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 6 | 1267 | 51527 | 46710.7 | 99022 | 99022 | 35232.0 |
| Grape Inc. | 2 | 3 | 2499 | 2499.5 | 4996 | 4996 | 3530.6 |
| DomainePlus.com (3612040 CANADA inc.) | 2 | 1267 | 4169 | 4169 | 7071 | 7071 | 4104.0 |
| FastWebServer Internet Services Inc. | 1 | 9 | 9 | 9 | 9 | 9 | 0 |
| PlanetHoster | 1 | 290 | 290 | 290 | 290 | 290 | 0 |

**Timing distribution (captures by second offset from 19:00:00 UTC):**

| Offset (s) | Domains Captured |
|-----------:|-----------------:|
| +0 | 30 |
| +1 | 5 |
| +4 | 5 |
| +5 | 24 |
| +6 | 26 |
| +7 | 7 |
| +8 | 2 |
| +9 | 1 |
| +10 | 22 |
| +11 | 29 |
| +12 | 3 |
| +13 | 2 |
| +14 | 1 |
| +15 | 4 |
| +16 | 8 |
| +18 | 2 |
| +20 | 3 |
| +23 | 1 |
| +28 | 1 |
| +38 | 1 |
| +46 | 1 |
| +53 | 1 |
| +56 | 1 |
| +62 | 1 |
| +99 | 1 |

![Last Session Market Share](charts/last_session_market_share.png)


![Last Session Latency Distribution](charts/last_session_latency_histogram.png)


![Last Session Latency by Registrar](charts/last_session_latency_by_registrar.png)


![Last Session Timing Distribution](charts/last_session_timing_distribution.png)


---

## Rolling Windows

### Last 4 Sessions

- **Sessions covered:** 4  (2026-06-17 → 2026-07-08)
- **Total domains registered:** 859
- **Avg domains/session:** 214.8
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 9.8
- **Market concentration HHI:** 4,358.0

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 530 | 61.7% | 4 | 9653.1 |
| BareMetal.com inc | 192 | 22.35% | 4 | 11964.6 |
| MyID.ca INC. | 47 | 5.47% | 4 | 2395.8 |
| Register.ca Inc. | 27 | 3.14% | 4 | 3294.5 |
| Webnames.ca Inc. | 20 | 2.33% | 4 | 77190.1 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 18 | 2.1% | 4 | 25897.2 |
| Grape Inc. | 9 | 1.05% | 3 | 1819.1 |
| DomainePlus.com (3612040 CANADA inc.) | 7 | 0.81% | 4 | 7712.9 |
| Namespro Solutions Inc. | 3 | 0.35% | 2 | 48106.2 |
| PlanetHoster | 2 | 0.23% | 2 | 307.5 |
| FastWebServer Internet Services Inc. | 2 | 0.23% | 2 | 3029.5 |
| CanSpace Solutions Inc. | 1 | 0.12% | 1 | 549 |
| easyDNS Technologies Inc. | 1 | 0.12% | 1 | 1064 |

![Last 4 Sessions Market Share](charts/last_4_sessions_market_share.png)


---

### Last ~6 Months (26 Weeks)

- **Sessions covered:** 13  (2026-04-15 → 2026-07-08)
- **Total domains registered:** 2,828
- **Avg domains/session:** 217.5
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 9.3
- **Market concentration HHI:** 4,468.9

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 1,773 | 62.69% | 13 | 9887.9 |
| BareMetal.com inc | 628 | 22.21% | 13 | 11724.0 |
| MyID.ca INC. | 144 | 5.09% | 12 | 9747.9 |
| Webnames.ca Inc. | 93 | 3.29% | 13 | 83198.5 |
| Register.ca Inc. | 64 | 2.26% | 10 | 3217.2 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 37 | 1.31% | 11 | 28701.7 |
| Grape Inc. | 25 | 0.88% | 11 | 1328.3 |
| DomainePlus.com (3612040 CANADA inc.) | 22 | 0.78% | 12 | 4218.0 |
| Namespro Solutions Inc. | 15 | 0.53% | 7 | 29527.7 |
| PlanetHoster | 13 | 0.46% | 8 | 1517.8 |
| easyDNS Technologies Inc. | 9 | 0.32% | 6 | 12421.3 |
| CanSpace Solutions Inc. | 3 | 0.11% | 3 | 160067.3 |
| FastWebServer Internet Services Inc. | 2 | 0.07% | 2 | 3029.5 |

![Last 26 Weeks Market Share](charts/last_26_weeks_market_share.png)


---

### Last 52 Weeks

- **Sessions covered:** 13  (2026-04-15 → 2026-07-08)
- **Total domains registered:** 2,828
- **Avg domains/session:** 217.5
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 9.3
- **Market concentration HHI:** 4,468.9

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 1,773 | 62.69% | 13 | 9887.9 |
| BareMetal.com inc | 628 | 22.21% | 13 | 11724.0 |
| MyID.ca INC. | 144 | 5.09% | 12 | 9747.9 |
| Webnames.ca Inc. | 93 | 3.29% | 13 | 83198.5 |
| Register.ca Inc. | 64 | 2.26% | 10 | 3217.2 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 37 | 1.31% | 11 | 28701.7 |
| Grape Inc. | 25 | 0.88% | 11 | 1328.3 |
| DomainePlus.com (3612040 CANADA inc.) | 22 | 0.78% | 12 | 4218.0 |
| Namespro Solutions Inc. | 15 | 0.53% | 7 | 29527.7 |
| PlanetHoster | 13 | 0.46% | 8 | 1517.8 |
| easyDNS Technologies Inc. | 9 | 0.32% | 6 | 12421.3 |
| CanSpace Solutions Inc. | 3 | 0.11% | 3 | 160067.3 |
| FastWebServer Internet Services Inc. | 2 | 0.07% | 2 | 3029.5 |

![Last 52 Weeks Market Share](charts/last_52_weeks_market_share.png)


---

## All Time

- **Sessions covered:** 13  (2026-04-15 → 2026-07-08)
- **Total domains registered:** 2,828
- **Avg domains/session:** 217.5
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 9.3
- **Market concentration HHI:** 4,468.9

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 1,773 | 62.69% | 13 | 9887.9 |
| BareMetal.com inc | 628 | 22.21% | 13 | 11724.0 |
| MyID.ca INC. | 144 | 5.09% | 12 | 9747.9 |
| Webnames.ca Inc. | 93 | 3.29% | 13 | 83198.5 |
| Register.ca Inc. | 64 | 2.26% | 10 | 3217.2 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 37 | 1.31% | 11 | 28701.7 |
| Grape Inc. | 25 | 0.88% | 11 | 1328.3 |
| DomainePlus.com (3612040 CANADA inc.) | 22 | 0.78% | 12 | 4218.0 |
| Namespro Solutions Inc. | 15 | 0.53% | 7 | 29527.7 |
| PlanetHoster | 13 | 0.46% | 8 | 1517.8 |
| easyDNS Technologies Inc. | 9 | 0.32% | 6 | 12421.3 |
| CanSpace Solutions Inc. | 3 | 0.11% | 3 | 160067.3 |
| FastWebServer Internet Services Inc. | 2 | 0.07% | 2 | 3029.5 |

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

- **Sessions covered:** 13  (2026-04-15 → 2026-07-08)
- **Total domains registered:** 2,828
- **Avg domains/session:** 217.5
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 9.3
- **Market concentration HHI:** 4,468.9

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 1,773 | 62.69% | 13 | 9887.9 |
| BareMetal.com inc | 628 | 22.21% | 13 | 11724.0 |
| MyID.ca INC. | 144 | 5.09% | 12 | 9747.9 |
| Webnames.ca Inc. | 93 | 3.29% | 13 | 83198.5 |
| Register.ca Inc. | 64 | 2.26% | 10 | 3217.2 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 37 | 1.31% | 11 | 28701.7 |
| Grape Inc. | 25 | 0.88% | 11 | 1328.3 |
| DomainePlus.com (3612040 CANADA inc.) | 22 | 0.78% | 12 | 4218.0 |
| Namespro Solutions Inc. | 15 | 0.53% | 7 | 29527.7 |
| PlanetHoster | 13 | 0.46% | 8 | 1517.8 |
| easyDNS Technologies Inc. | 9 | 0.32% | 6 | 12421.3 |
| CanSpace Solutions Inc. | 3 | 0.11% | 3 | 160067.3 |
| FastWebServer Internet Services Inc. | 2 | 0.07% | 2 | 3029.5 |

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

- **Sessions covered:** 2  (2026-07-01 → 2026-07-08)
- **Total domains registered:** 425
- **Avg domains/session:** 212.5
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 11.5
- **Market concentration HHI:** 4,131.3

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 254 | 59.76% | 2 | 9552.0 |
| BareMetal.com inc | 95 | 22.35% | 2 | 13312.3 |
| MyID.ca INC. | 25 | 5.88% | 2 | 2952.2 |
| Register.ca Inc. | 14 | 3.29% | 2 | 3899.4 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 11 | 2.59% | 2 | 32432.1 |
| Webnames.ca Inc. | 10 | 2.35% | 2 | 87110.8 |
| Grape Inc. | 5 | 1.18% | 2 | 2090.2 |
| DomainePlus.com (3612040 CANADA inc.) | 4 | 0.94% | 2 | 8745.8 |
| PlanetHoster | 2 | 0.47% | 2 | 307.5 |
| FastWebServer Internet Services Inc. | 2 | 0.47% | 2 | 3029.5 |
| CanSpace Solutions Inc. | 1 | 0.24% | 1 | 549 |
| easyDNS Technologies Inc. | 1 | 0.24% | 1 | 1064 |
| Namespro Solutions Inc. | 1 | 0.24% | 1 | 87000 |


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
