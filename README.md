# CIRA TBR Tracker

> Automated archive and analytics for CIRA **To-Be-Released (TBR)** `.CA` domain
> drop sessions. Updated every **Wednesday ≈ 19:30 UTC** via GitHub Actions.

**Last updated:** 2026-09-09 &nbsp;|&nbsp; **Total sessions tracked:** 21

---

## What is TBR?

CIRA releases expired `.CA` domains every **Wednesday at 19:00 UTC** via a
first-come, first-served process. Whichever registrar submits a registration
request first wins the domain (one connection, one request per 5 s per registrar).

Capture latency is measured from the official session open at **19:00:00.000 UTC**.

---

## Last Session

- **Date:** 2026-09-09
- **Domains released:** 260
- **Domains registered:** 260
- **Registration rate:** 100.0%
- **Unique registrars:** 9
- **Session duration:** 213,704 ms
- **Market concentration (HHI):** 4,798.6

**Capture latency across all registrars:**
- Min: 13 ms | Median: 12117 ms | Mean: 20275.4 ms | P95: 118370 ms | Max: 213717 ms

**Per-registrar latency breakdown:**

| Registrar | Domains | Min (ms) | Median (ms) | Mean (ms) | P95 (ms) | Max (ms) | StdDev (ms) |
|-----------|--------:|---------:|------------:|----------:|---------:|---------:|------------:|
| WHC Online Solutions Inc. | 171 | 60 | 12042 | 11658.9 | 20617 | 21490 | 6022.4 |
| BareMetal.com inc | 52 | 45 | 15336 | 13490.2 | 22135 | 22154 | 7380.7 |
| Webnames.ca Inc. | 20 | 1597 | 138442 | 125320.2 | 213717 | 213717 | 63513.1 |
| Register.ca Inc. | 8 | 75 | 5048 | 4419.9 | 5083 | 5083 | 1756.0 |
| Grape Inc. | 5 | 13 | 5013 | 4029.2 | 5094 | 5094 | 2245.6 |
| MyID.ca INC. | 1 | 34 | 34 | 34 | 34 | 34 | 0 |
| DomainePlus.com (3612040 CANADA inc.) | 1 | 1312 | 1312 | 1312 | 1312 | 1312 | 0 |
| FastWebServer Internet Services Inc. | 1 | 5091 | 5091 | 5091 | 5091 | 5091 | 0 |
| CanSpace Solutions Inc. | 1 | 8098 | 8098 | 8098 | 8098 | 8098 | 0 |

**Timing distribution (captures by second offset from 19:00:00 UTC):**

| Offset (s) | Domains Captured |
|-----------:|-----------------:|
| +0 | 26 |
| +1 | 4 |
| +4 | 3 |
| +5 | 26 |
| +6 | 10 |
| +7 | 19 |
| +8 | 2 |
| +10 | 14 |
| +11 | 13 |
| +12 | 23 |
| +13 | 5 |
| +15 | 19 |
| +16 | 17 |
| +17 | 21 |
| +18 | 10 |
| +20 | 14 |
| +21 | 7 |
| +22 | 9 |
| +53 | 1 |
| +58 | 1 |
| +73 | 1 |
| +78 | 1 |
| +83 | 1 |
| +118 | 1 |
| +123 | 1 |
| +133 | 1 |
| +143 | 1 |
| +148 | 1 |
| +158 | 1 |
| +163 | 1 |
| +168 | 1 |
| +178 | 1 |
| +193 | 1 |
| +198 | 1 |
| +203 | 1 |
| +213 | 1 |

![Last Session Market Share](charts/last_session_market_share.png)


![Last Session Latency Distribution](charts/last_session_latency_histogram.png)


![Last Session Latency by Registrar](charts/last_session_latency_by_registrar.png)


![Last Session Timing Distribution](charts/last_session_timing_distribution.png)


---

## Rolling Windows

### Last 4 Sessions

- **Sessions covered:** 4  (2026-08-12 → 2026-09-09)
- **Total domains registered:** 1,139
- **Avg domains/session:** 284.8
- **Unique registrars (ever active):** 12
- **Avg registrars/session:** 8.8
- **Market concentration HHI:** 4,287.0

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 680 | 59.7% | 4 | 11894.4 |
| BareMetal.com inc | 294 | 25.81% | 4 | 21014.7 |
| Webnames.ca Inc. | 72 | 6.32% | 4 | 97811.2 |
| MyID.ca INC. | 32 | 2.81% | 4 | 1406.2 |
| Register.ca Inc. | 30 | 2.63% | 4 | 2652.8 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 14 | 1.23% | 3 | 39479.2 |
| Grape Inc. | 6 | 0.53% | 2 | 2063.1 |
| CanSpace Solutions Inc. | 4 | 0.35% | 3 | 4348 |
| DomainePlus.com (3612040 CANADA inc.) | 3 | 0.26% | 3 | 499 |
| Namespro Solutions Inc. | 2 | 0.18% | 2 | 13868.5 |
| PlanetHoster | 1 | 0.09% | 1 | 418 |
| FastWebServer Internet Services Inc. | 1 | 0.09% | 1 | 5091 |

![Last 4 Sessions Market Share](charts/last_4_sessions_market_share.png)


---

### Last ~6 Months (26 Weeks)

- **Sessions covered:** 21  (2026-04-15 → 2026-09-09)
- **Total domains registered:** 5,050
- **Avg domains/session:** 240.5
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 9.0
- **Market concentration HHI:** 4,390.6

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 3,110 | 61.58% | 21 | 10562.6 |
| BareMetal.com inc | 1,186 | 23.49% | 21 | 14176.6 |
| MyID.ca INC. | 242 | 4.79% | 20 | 6801.2 |
| Webnames.ca Inc. | 193 | 3.82% | 21 | 85333.4 |
| Register.ca Inc. | 122 | 2.42% | 18 | 2993.4 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 74 | 1.47% | 18 | 37963.8 |
| Grape Inc. | 38 | 0.75% | 15 | 2213.9 |
| DomainePlus.com (3612040 CANADA inc.) | 25 | 0.5% | 15 | 3474.2 |
| Namespro Solutions Inc. | 21 | 0.42% | 12 | 25137.3 |
| PlanetHoster | 18 | 0.36% | 12 | 1286.9 |
| easyDNS Technologies Inc. | 11 | 0.22% | 8 | 10928.4 |
| CanSpace Solutions Inc. | 7 | 0.14% | 6 | 82207.7 |
| FastWebServer Internet Services Inc. | 3 | 0.06% | 3 | 3716.7 |

![Last 26 Weeks Market Share](charts/last_26_weeks_market_share.png)


---

### Last 52 Weeks

- **Sessions covered:** 21  (2026-04-15 → 2026-09-09)
- **Total domains registered:** 5,050
- **Avg domains/session:** 240.5
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 9.0
- **Market concentration HHI:** 4,390.6

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 3,110 | 61.58% | 21 | 10562.6 |
| BareMetal.com inc | 1,186 | 23.49% | 21 | 14176.6 |
| MyID.ca INC. | 242 | 4.79% | 20 | 6801.2 |
| Webnames.ca Inc. | 193 | 3.82% | 21 | 85333.4 |
| Register.ca Inc. | 122 | 2.42% | 18 | 2993.4 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 74 | 1.47% | 18 | 37963.8 |
| Grape Inc. | 38 | 0.75% | 15 | 2213.9 |
| DomainePlus.com (3612040 CANADA inc.) | 25 | 0.5% | 15 | 3474.2 |
| Namespro Solutions Inc. | 21 | 0.42% | 12 | 25137.3 |
| PlanetHoster | 18 | 0.36% | 12 | 1286.9 |
| easyDNS Technologies Inc. | 11 | 0.22% | 8 | 10928.4 |
| CanSpace Solutions Inc. | 7 | 0.14% | 6 | 82207.7 |
| FastWebServer Internet Services Inc. | 3 | 0.06% | 3 | 3716.7 |

![Last 52 Weeks Market Share](charts/last_52_weeks_market_share.png)


---

## All Time

- **Sessions covered:** 21  (2026-04-15 → 2026-09-09)
- **Total domains registered:** 5,050
- **Avg domains/session:** 240.5
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 9.0
- **Market concentration HHI:** 4,390.6

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 3,110 | 61.58% | 21 | 10562.6 |
| BareMetal.com inc | 1,186 | 23.49% | 21 | 14176.6 |
| MyID.ca INC. | 242 | 4.79% | 20 | 6801.2 |
| Webnames.ca Inc. | 193 | 3.82% | 21 | 85333.4 |
| Register.ca Inc. | 122 | 2.42% | 18 | 2993.4 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 74 | 1.47% | 18 | 37963.8 |
| Grape Inc. | 38 | 0.75% | 15 | 2213.9 |
| DomainePlus.com (3612040 CANADA inc.) | 25 | 0.5% | 15 | 3474.2 |
| Namespro Solutions Inc. | 21 | 0.42% | 12 | 25137.3 |
| PlanetHoster | 18 | 0.36% | 12 | 1286.9 |
| easyDNS Technologies Inc. | 11 | 0.22% | 8 | 10928.4 |
| CanSpace Solutions Inc. | 7 | 0.14% | 6 | 82207.7 |
| FastWebServer Internet Services Inc. | 3 | 0.06% | 3 | 3716.7 |

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

- **Sessions covered:** 21  (2026-04-15 → 2026-09-09)
- **Total domains registered:** 5,050
- **Avg domains/session:** 240.5
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 9.0
- **Market concentration HHI:** 4,390.6

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 3,110 | 61.58% | 21 | 10562.6 |
| BareMetal.com inc | 1,186 | 23.49% | 21 | 14176.6 |
| MyID.ca INC. | 242 | 4.79% | 20 | 6801.2 |
| Webnames.ca Inc. | 193 | 3.82% | 21 | 85333.4 |
| Register.ca Inc. | 122 | 2.42% | 18 | 2993.4 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 74 | 1.47% | 18 | 37963.8 |
| Grape Inc. | 38 | 0.75% | 15 | 2213.9 |
| DomainePlus.com (3612040 CANADA inc.) | 25 | 0.5% | 15 | 3474.2 |
| Namespro Solutions Inc. | 21 | 0.42% | 12 | 25137.3 |
| PlanetHoster | 18 | 0.36% | 12 | 1286.9 |
| easyDNS Technologies Inc. | 11 | 0.22% | 8 | 10928.4 |
| CanSpace Solutions Inc. | 7 | 0.14% | 6 | 82207.7 |
| FastWebServer Internet Services Inc. | 3 | 0.06% | 3 | 3716.7 |

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

- **Sessions covered:** 3  (2026-08-05 → 2026-08-26)
- **Total domains registered:** 838
- **Avg domains/session:** 279.3
- **Unique registrars (ever active):** 11
- **Avg registrars/session:** 8.7
- **Market concentration HHI:** 4,338.3

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 505 | 60.26% | 3 | 11862.8 |
| BareMetal.com inc | 216 | 25.78% | 3 | 20684.8 |
| MyID.ca INC. | 34 | 4.06% | 3 | 1924.2 |
| Webnames.ca Inc. | 30 | 3.58% | 3 | 77406.9 |
| Register.ca Inc. | 22 | 2.63% | 3 | 1204.8 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 20 | 2.39% | 3 | 46853.3 |
| Grape Inc. | 4 | 0.48% | 2 | 6010.5 |
| CanSpace Solutions Inc. | 3 | 0.36% | 2 | 2473 |
| Namespro Solutions Inc. | 2 | 0.24% | 2 | 23856 |
| DomainePlus.com (3612040 CANADA inc.) | 1 | 0.12% | 1 | 75 |
| PlanetHoster | 1 | 0.12% | 1 | 418 |

#### 2026-09

- **Sessions covered:** 2  (2026-09-02 → 2026-09-09)
- **Total domains registered:** 566
- **Avg domains/session:** 283.0
- **Unique registrars (ever active):** 11
- **Avg registrars/session:** 8.5
- **Market concentration HHI:** 4,253.3

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 338 | 59.72% | 2 | 12181.2 |
| BareMetal.com inc | 139 | 24.56% | 2 | 17111.2 |
| Webnames.ca Inc. | 47 | 8.3% | 2 | 137559.5 |
| Register.ca Inc. | 18 | 3.18% | 2 | 4526.6 |
| MyID.ca INC. | 10 | 1.77% | 2 | 1317.8 |
| Grape Inc. | 5 | 0.88% | 1 | 4029.2 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 4 | 0.71% | 1 | 61544.8 |
| DomainePlus.com (3612040 CANADA inc.) | 2 | 0.35% | 2 | 711 |
| Namespro Solutions Inc. | 1 | 0.18% | 1 | 113 |
| FastWebServer Internet Services Inc. | 1 | 0.18% | 1 | 5091 |
| CanSpace Solutions Inc. | 1 | 0.18% | 1 | 8098 |


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
