# CIRA TBR Tracker

> Automated archive and analytics for CIRA **To-Be-Released (TBR)** `.CA` domain
> drop sessions. Updated every **Wednesday ≈ 19:30 UTC** via GitHub Actions.

**Last updated:** 2026-09-23 &nbsp;|&nbsp; **Total sessions tracked:** 23

---

## What is TBR?

CIRA releases expired `.CA` domains every **Wednesday at 19:00 UTC** via a
first-come, first-served process. Whichever registrar submits a registration
request first wins the domain (one connection, one request per 5 s per registrar).

Capture latency is measured from the official session open at **19:00:00.000 UTC**.

---

## Last Session

- **Date:** 2026-09-23
- **Domains released:** 319
- **Domains registered:** 319
- **Registration rate:** 100.0%
- **Unique registrars:** 8
- **Session duration:** 386,514 ms
- **Market concentration (HHI):** 4,153.8

**Capture latency across all registrars:**
- Min: 9 ms | Median: 14994 ms | Mean: 30578.0 ms | P95: 215868 ms | Max: 386523 ms

**Per-registrar latency breakdown:**

| Registrar | Domains | Min (ms) | Median (ms) | Mean (ms) | P95 (ms) | Max (ms) | StdDev (ms) |
|-----------|--------:|---------:|------------:|----------:|---------:|---------:|------------:|
| WHC Online Solutions Inc. | 191 | 361 | 14175 | 14143.0 | 23150 | 24470 | 6303.0 |
| BareMetal.com inc | 70 | 22 | 18642 | 17421.9 | 32207 | 32537 | 11167.9 |
| Webnames.ca Inc. | 23 | 8900 | 266088 | 242437.8 | 381504 | 386523 | 121467.9 |
| MyID.ca INC. | 15 | 20 | 4894 | 2950.5 | 5181 | 5181 | 2450.7 |
| Register.ca Inc. | 10 | 9 | 4999 | 3640.4 | 6061 | 6061 | 2518.7 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 5 | 406 | 35365 | 31671.4 | 57130 | 57130 | 24141.8 |
| Grape Inc. | 4 | 357 | 5801 | 4503.2 | 6053 | 6053 | 2767.3 |
| CanSpace Solutions Inc. | 1 | 448 | 448 | 448 | 448 | 448 | 0 |

**Timing distribution (captures by second offset from 19:00:00 UTC):**

| Offset (s) | Domains Captured |
|-----------:|-----------------:|
| +0 | 25 |
| +1 | 7 |
| +3 | 1 |
| +4 | 10 |
| +5 | 21 |
| +6 | 13 |
| +7 | 18 |
| +8 | 10 |
| +9 | 2 |
| +10 | 13 |
| +11 | 9 |
| +12 | 17 |
| +13 | 1 |
| +14 | 13 |
| +15 | 15 |
| +16 | 5 |
| +17 | 21 |
| +18 | 3 |
| +19 | 14 |
| +20 | 12 |
| +21 | 9 |
| +22 | 7 |
| +23 | 16 |
| +24 | 6 |
| +25 | 2 |
| +26 | 2 |
| +27 | 6 |
| +28 | 3 |
| +29 | 3 |
| +30 | 3 |
| +31 | 3 |
| +32 | 4 |
| +34 | 1 |
| +35 | 1 |
| +50 | 1 |
| +51 | 1 |
| +55 | 1 |
| +57 | 1 |
| +105 | 1 |
| +145 | 1 |
| +210 | 1 |
| +215 | 1 |
| +220 | 1 |
| +240 | 1 |
| +256 | 1 |
| +266 | 1 |
| +281 | 1 |
| +291 | 1 |
| +301 | 1 |
| +321 | 1 |
| +346 | 1 |
| +351 | 1 |
| +356 | 1 |
| +371 | 1 |
| +376 | 1 |
| +381 | 1 |
| +386 | 1 |

![Last Session Market Share](charts/last_session_market_share.png)


![Last Session Latency Distribution](charts/last_session_latency_histogram.png)


![Last Session Latency by Registrar](charts/last_session_latency_by_registrar.png)


![Last Session Timing Distribution](charts/last_session_timing_distribution.png)


---

## Rolling Windows

### Last 4 Sessions

- **Sessions covered:** 4  (2026-09-02 → 2026-09-23)
- **Total domains registered:** 1,213
- **Avg domains/session:** 303.2
- **Unique registrars (ever active):** 11
- **Avg registrars/session:** 8.2
- **Market concentration HHI:** 4,067.7

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 705 | 58.12% | 4 | 13220.0 |
| BareMetal.com inc | 296 | 24.4% | 4 | 16763.5 |
| Webnames.ca Inc. | 105 | 8.66% | 4 | 183725.9 |
| Register.ca Inc. | 39 | 3.22% | 4 | 3205.1 |
| MyID.ca INC. | 29 | 2.39% | 4 | 1485.2 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 17 | 1.4% | 3 | 56901.7 |
| Grape Inc. | 13 | 1.07% | 3 | 2892.1 |
| DomainePlus.com (3612040 CANADA inc.) | 5 | 0.41% | 3 | 1829.8 |
| CanSpace Solutions Inc. | 2 | 0.16% | 2 | 4273 |
| Namespro Solutions Inc. | 1 | 0.08% | 1 | 113 |
| FastWebServer Internet Services Inc. | 1 | 0.08% | 1 | 5091 |

![Last 4 Sessions Market Share](charts/last_4_sessions_market_share.png)


---

### Last ~6 Months (26 Weeks)

- **Sessions covered:** 23  (2026-04-15 → 2026-09-23)
- **Total domains registered:** 5,697
- **Avg domains/session:** 247.7
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 9.0
- **Market concentration HHI:** 4,330.5

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 3,477 | 61.03% | 23 | 10884.0 |
| BareMetal.com inc | 1,343 | 23.57% | 23 | 14371.3 |
| MyID.ca INC. | 261 | 4.58% | 22 | 6333.2 |
| Webnames.ca Inc. | 251 | 4.41% | 23 | 97903.8 |
| Register.ca Inc. | 143 | 2.51% | 20 | 2882.5 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 87 | 1.53% | 20 | 39625.4 |
| Grape Inc. | 46 | 0.81% | 17 | 2226.8 |
| DomainePlus.com (3612040 CANADA inc.) | 28 | 0.49% | 16 | 3511.3 |
| Namespro Solutions Inc. | 21 | 0.37% | 12 | 25137.3 |
| PlanetHoster | 18 | 0.32% | 12 | 1286.9 |
| easyDNS Technologies Inc. | 11 | 0.19% | 8 | 10928.4 |
| CanSpace Solutions Inc. | 8 | 0.14% | 7 | 70527.7 |
| FastWebServer Internet Services Inc. | 3 | 0.05% | 3 | 3716.7 |

![Last 26 Weeks Market Share](charts/last_26_weeks_market_share.png)


---

### Last 52 Weeks

- **Sessions covered:** 23  (2026-04-15 → 2026-09-23)
- **Total domains registered:** 5,697
- **Avg domains/session:** 247.7
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 9.0
- **Market concentration HHI:** 4,330.5

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 3,477 | 61.03% | 23 | 10884.0 |
| BareMetal.com inc | 1,343 | 23.57% | 23 | 14371.3 |
| MyID.ca INC. | 261 | 4.58% | 22 | 6333.2 |
| Webnames.ca Inc. | 251 | 4.41% | 23 | 97903.8 |
| Register.ca Inc. | 143 | 2.51% | 20 | 2882.5 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 87 | 1.53% | 20 | 39625.4 |
| Grape Inc. | 46 | 0.81% | 17 | 2226.8 |
| DomainePlus.com (3612040 CANADA inc.) | 28 | 0.49% | 16 | 3511.3 |
| Namespro Solutions Inc. | 21 | 0.37% | 12 | 25137.3 |
| PlanetHoster | 18 | 0.32% | 12 | 1286.9 |
| easyDNS Technologies Inc. | 11 | 0.19% | 8 | 10928.4 |
| CanSpace Solutions Inc. | 8 | 0.14% | 7 | 70527.7 |
| FastWebServer Internet Services Inc. | 3 | 0.05% | 3 | 3716.7 |

![Last 52 Weeks Market Share](charts/last_52_weeks_market_share.png)


---

## All Time

- **Sessions covered:** 23  (2026-04-15 → 2026-09-23)
- **Total domains registered:** 5,697
- **Avg domains/session:** 247.7
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 9.0
- **Market concentration HHI:** 4,330.5

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 3,477 | 61.03% | 23 | 10884.0 |
| BareMetal.com inc | 1,343 | 23.57% | 23 | 14371.3 |
| MyID.ca INC. | 261 | 4.58% | 22 | 6333.2 |
| Webnames.ca Inc. | 251 | 4.41% | 23 | 97903.8 |
| Register.ca Inc. | 143 | 2.51% | 20 | 2882.5 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 87 | 1.53% | 20 | 39625.4 |
| Grape Inc. | 46 | 0.81% | 17 | 2226.8 |
| DomainePlus.com (3612040 CANADA inc.) | 28 | 0.49% | 16 | 3511.3 |
| Namespro Solutions Inc. | 21 | 0.37% | 12 | 25137.3 |
| PlanetHoster | 18 | 0.32% | 12 | 1286.9 |
| easyDNS Technologies Inc. | 11 | 0.19% | 8 | 10928.4 |
| CanSpace Solutions Inc. | 8 | 0.14% | 7 | 70527.7 |
| FastWebServer Internet Services Inc. | 3 | 0.05% | 3 | 3716.7 |

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

- **Sessions covered:** 23  (2026-04-15 → 2026-09-23)
- **Total domains registered:** 5,697
- **Avg domains/session:** 247.7
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 9.0
- **Market concentration HHI:** 4,330.5

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 3,477 | 61.03% | 23 | 10884.0 |
| BareMetal.com inc | 1,343 | 23.57% | 23 | 14371.3 |
| MyID.ca INC. | 261 | 4.58% | 22 | 6333.2 |
| Webnames.ca Inc. | 251 | 4.41% | 23 | 97903.8 |
| Register.ca Inc. | 143 | 2.51% | 20 | 2882.5 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 87 | 1.53% | 20 | 39625.4 |
| Grape Inc. | 46 | 0.81% | 17 | 2226.8 |
| DomainePlus.com (3612040 CANADA inc.) | 28 | 0.49% | 16 | 3511.3 |
| Namespro Solutions Inc. | 21 | 0.37% | 12 | 25137.3 |
| PlanetHoster | 18 | 0.32% | 12 | 1286.9 |
| easyDNS Technologies Inc. | 11 | 0.19% | 8 | 10928.4 |
| CanSpace Solutions Inc. | 8 | 0.14% | 7 | 70527.7 |
| FastWebServer Internet Services Inc. | 3 | 0.05% | 3 | 3716.7 |

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

- **Sessions covered:** 4  (2026-09-02 → 2026-09-23)
- **Total domains registered:** 1,213
- **Avg domains/session:** 303.2
- **Unique registrars (ever active):** 11
- **Avg registrars/session:** 8.2
- **Market concentration HHI:** 4,067.7

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 705 | 58.12% | 4 | 13220.0 |
| BareMetal.com inc | 296 | 24.4% | 4 | 16763.5 |
| Webnames.ca Inc. | 105 | 8.66% | 4 | 183725.9 |
| Register.ca Inc. | 39 | 3.22% | 4 | 3205.1 |
| MyID.ca INC. | 29 | 2.39% | 4 | 1485.2 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 17 | 1.4% | 3 | 56901.7 |
| Grape Inc. | 13 | 1.07% | 3 | 2892.1 |
| DomainePlus.com (3612040 CANADA inc.) | 5 | 0.41% | 3 | 1829.8 |
| CanSpace Solutions Inc. | 2 | 0.16% | 2 | 4273 |
| Namespro Solutions Inc. | 1 | 0.08% | 1 | 113 |
| FastWebServer Internet Services Inc. | 1 | 0.08% | 1 | 5091 |


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
