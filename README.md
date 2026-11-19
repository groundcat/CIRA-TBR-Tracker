# CIRA TBR Tracker

> Automated archive and analytics for CIRA **To-Be-Released (TBR)** `.CA` domain
> drop sessions. Updated every **Wednesday ≈ 19:30 UTC** via GitHub Actions.

**Last updated:** 2026-11-19 &nbsp;|&nbsp; **Total sessions tracked:** 31

---

## What is TBR?

CIRA releases expired `.CA` domains every **Wednesday at 19:00 UTC** via a
first-come, first-served process. Whichever registrar submits a registration
request first wins the domain (one connection, one request per 5 s per registrar).

Capture latency is measured from the official session open at **19:00:00.000 UTC**.

---

## Last Session

- **Date:** 2026-11-18
- **Domains released:** 287
- **Domains registered:** 287
- **Registration rate:** 100.0%
- **Unique registrars:** 10
- **Session duration:** 341,916 ms
- **Market concentration (HHI):** 2,998.0

**Capture latency across all registrars:**
- Min: 3 ms | Median: 11337 ms | Mean: 32300.8 ms | P95: 193842 ms | Max: 341919 ms

**Per-registrar latency breakdown:**

| Registrar | Domains | Min (ms) | Median (ms) | Mean (ms) | P95 (ms) | Max (ms) | StdDev (ms) |
|-----------|--------:|---------:|------------:|----------:|---------:|---------:|------------:|
| BareMetal.com inc | 111 | 43 | 14961 | 13238.7 | 25570 | 25997 | 8308.5 |
| WHC Online Solutions Inc. | 105 | 324 | 8143 | 8911.1 | 13668 | 15854 | 3850.5 |
| Webnames.ca Inc. | 32 | 20769 | 181056 | 191150.6 | 336717 | 341919 | 95089.9 |
| Register.ca Inc. | 10 | 3 | 3208 | 2766.5 | 5481 | 5481 | 2617.4 |
| MyID.ca INC. | 10 | 15 | 4906 | 4035.8 | 9996 | 9996 | 3872.8 |
| Grape Inc. | 8 | 48 | 86 | 2130.8 | 6586 | 6586 | 2883.9 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 7 | 37136 | 85287 | 91753.7 | 148269 | 148269 | 41077.0 |
| easyDNS Technologies Inc. | 2 | 7367 | 10307 | 10307.5 | 13248 | 13248 | 4158.5 |
| FastWebServer Internet Services Inc. | 1 | 72 | 72 | 72 | 72 | 72 | 0 |
| DomainePlus.com (3612040 CANADA inc.) | 1 | 311 | 311 | 311 | 311 | 311 | 0 |

**Timing distribution (captures by second offset from 19:00:00 UTC):**

| Offset (s) | Domains Captured |
|-----------:|-----------------:|
| +0 | 31 |
| +1 | 9 |
| +2 | 1 |
| +4 | 6 |
| +5 | 29 |
| +6 | 27 |
| +7 | 12 |
| +8 | 2 |
| +9 | 3 |
| +10 | 21 |
| +11 | 27 |
| +12 | 12 |
| +13 | 6 |
| +14 | 2 |
| +15 | 20 |
| +16 | 3 |
| +19 | 2 |
| +20 | 16 |
| +21 | 3 |
| +24 | 2 |
| +25 | 15 |
| +37 | 1 |
| +51 | 1 |
| +63 | 1 |
| +69 | 1 |
| +71 | 1 |
| +76 | 1 |
| +85 | 1 |
| +86 | 1 |
| +91 | 1 |
| +96 | 2 |
| +107 | 1 |
| +117 | 1 |
| +122 | 1 |
| +132 | 1 |
| +138 | 1 |
| +142 | 1 |
| +148 | 2 |
| +163 | 1 |
| +173 | 1 |
| +178 | 1 |
| +183 | 1 |
| +193 | 1 |
| +203 | 1 |
| +224 | 1 |
| +234 | 1 |
| +239 | 1 |
| +244 | 1 |
| +249 | 1 |
| +290 | 1 |
| +300 | 1 |
| +316 | 1 |
| +321 | 1 |
| +326 | 1 |
| +331 | 1 |
| +336 | 1 |
| +341 | 1 |

![Last Session Market Share](charts/last_session_market_share.png)


![Last Session Latency Distribution](charts/last_session_latency_histogram.png)


![Last Session Latency by Registrar](charts/last_session_latency_by_registrar.png)


![Last Session Timing Distribution](charts/last_session_timing_distribution.png)


---

## Rolling Windows

### Last 4 Sessions

- **Sessions covered:** 4  (2026-10-28 → 2026-11-18)
- **Total domains registered:** 1,155
- **Avg domains/session:** 288.8
- **Unique registrars (ever active):** 10
- **Avg registrars/session:** 9.5
- **Market concentration HHI:** 3,486.3

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 544 | 47.1% | 4 | 10304.7 |
| BareMetal.com inc | 399 | 34.55% | 4 | 13234.4 |
| Webnames.ca Inc. | 75 | 6.49% | 4 | 103529.3 |
| Register.ca Inc. | 43 | 3.72% | 4 | 2880.2 |
| MyID.ca INC. | 38 | 3.29% | 4 | 28816.6 |
| Grape Inc. | 22 | 1.9% | 4 | 3167.2 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 21 | 1.82% | 4 | 85340.6 |
| DomainePlus.com (3612040 CANADA inc.) | 6 | 0.52% | 4 | 2026.9 |
| easyDNS Technologies Inc. | 4 | 0.35% | 3 | 8169.8 |
| FastWebServer Internet Services Inc. | 3 | 0.26% | 3 | 33.3 |

![Last 4 Sessions Market Share](charts/last_4_sessions_market_share.png)


---

### Last ~6 Months (26 Weeks)

- **Sessions covered:** 25  (2026-05-27 → 2026-11-18)
- **Total domains registered:** 6,853
- **Avg domains/session:** 274.1
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 8.9
- **Market concentration HHI:** 4,037.6

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 3,929 | 57.33% | 25 | 11377.7 |
| BareMetal.com inc | 1,804 | 26.32% | 25 | 14907.2 |
| Webnames.ca Inc. | 341 | 4.98% | 25 | 102855.8 |
| MyID.ca INC. | 305 | 4.45% | 24 | 15601.3 |
| Register.ca Inc. | 211 | 3.08% | 25 | 2904.3 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 112 | 1.63% | 22 | 54854.5 |
| Grape Inc. | 73 | 1.07% | 20 | 2993.1 |
| DomainePlus.com (3612040 CANADA inc.) | 23 | 0.34% | 15 | 3125.3 |
| Namespro Solutions Inc. | 16 | 0.23% | 10 | 24679.6 |
| PlanetHoster | 13 | 0.19% | 10 | 595.2 |
| easyDNS Technologies Inc. | 9 | 0.13% | 7 | 9788.6 |
| FastWebServer Internet Services Inc. | 9 | 0.13% | 8 | 2349.7 |
| CanSpace Solutions Inc. | 8 | 0.12% | 6 | 4225.6 |

![Last 26 Weeks Market Share](charts/last_26_weeks_market_share.png)


---

### Last 52 Weeks

- **Sessions covered:** 31  (2026-04-15 → 2026-11-18)
- **Total domains registered:** 8,294
- **Avg domains/session:** 267.5
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 8.9
- **Market concentration HHI:** 4,153.9

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 4,872 | 58.74% | 31 | 11244.7 |
| BareMetal.com inc | 2,115 | 25.5% | 31 | 14470.9 |
| Webnames.ca Inc. | 403 | 4.86% | 31 | 102538.9 |
| MyID.ca INC. | 358 | 4.32% | 29 | 13765.2 |
| Register.ca Inc. | 225 | 2.71% | 28 | 3014.3 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 125 | 1.51% | 27 | 50858.9 |
| Grape Inc. | 84 | 1.01% | 25 | 2609.4 |
| DomainePlus.com (3612040 CANADA inc.) | 35 | 0.42% | 21 | 3169.8 |
| Namespro Solutions Inc. | 23 | 0.28% | 13 | 24380.5 |
| PlanetHoster | 20 | 0.24% | 14 | 1166.9 |
| easyDNS Technologies Inc. | 15 | 0.18% | 11 | 10176.0 |
| CanSpace Solutions Inc. | 10 | 0.12% | 8 | 63125.8 |
| FastWebServer Internet Services Inc. | 9 | 0.11% | 8 | 2349.7 |

![Last 52 Weeks Market Share](charts/last_52_weeks_market_share.png)


---

## All Time

- **Sessions covered:** 31  (2026-04-15 → 2026-11-18)
- **Total domains registered:** 8,294
- **Avg domains/session:** 267.5
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 8.9
- **Market concentration HHI:** 4,153.9

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 4,872 | 58.74% | 31 | 11244.7 |
| BareMetal.com inc | 2,115 | 25.5% | 31 | 14470.9 |
| Webnames.ca Inc. | 403 | 4.86% | 31 | 102538.9 |
| MyID.ca INC. | 358 | 4.32% | 29 | 13765.2 |
| Register.ca Inc. | 225 | 2.71% | 28 | 3014.3 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 125 | 1.51% | 27 | 50858.9 |
| Grape Inc. | 84 | 1.01% | 25 | 2609.4 |
| DomainePlus.com (3612040 CANADA inc.) | 35 | 0.42% | 21 | 3169.8 |
| Namespro Solutions Inc. | 23 | 0.28% | 13 | 24380.5 |
| PlanetHoster | 20 | 0.24% | 14 | 1166.9 |
| easyDNS Technologies Inc. | 15 | 0.18% | 11 | 10176.0 |
| CanSpace Solutions Inc. | 10 | 0.12% | 8 | 63125.8 |
| FastWebServer Internet Services Inc. | 9 | 0.11% | 8 | 2349.7 |

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

- **Sessions covered:** 31  (2026-04-15 → 2026-11-18)
- **Total domains registered:** 8,294
- **Avg domains/session:** 267.5
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 8.9
- **Market concentration HHI:** 4,153.9

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 4,872 | 58.74% | 31 | 11244.7 |
| BareMetal.com inc | 2,115 | 25.5% | 31 | 14470.9 |
| Webnames.ca Inc. | 403 | 4.86% | 31 | 102538.9 |
| MyID.ca INC. | 358 | 4.32% | 29 | 13765.2 |
| Register.ca Inc. | 225 | 2.71% | 28 | 3014.3 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 125 | 1.51% | 27 | 50858.9 |
| Grape Inc. | 84 | 1.01% | 25 | 2609.4 |
| DomainePlus.com (3612040 CANADA inc.) | 35 | 0.42% | 21 | 3169.8 |
| Namespro Solutions Inc. | 23 | 0.28% | 13 | 24380.5 |
| PlanetHoster | 20 | 0.24% | 14 | 1166.9 |
| easyDNS Technologies Inc. | 15 | 0.18% | 11 | 10176.0 |
| CanSpace Solutions Inc. | 10 | 0.12% | 8 | 63125.8 |
| FastWebServer Internet Services Inc. | 9 | 0.11% | 8 | 2349.7 |

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

- **Sessions covered:** 5  (2026-09-02 → 2026-09-30)
- **Total domains registered:** 1,563
- **Avg domains/session:** 312.6
- **Unique registrars (ever active):** 12
- **Avg registrars/session:** 8.2
- **Market concentration HHI:** 4,042.4

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 903 | 57.77% | 5 | 13243.2 |
| BareMetal.com inc | 387 | 24.76% | 5 | 17715.3 |
| Webnames.ca Inc. | 131 | 8.38% | 5 | 189495.8 |
| Register.ca Inc. | 52 | 3.33% | 5 | 3348.2 |
| MyID.ca INC. | 45 | 2.88% | 5 | 1985.1 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 17 | 1.09% | 3 | 56901.7 |
| Grape Inc. | 16 | 1.02% | 4 | 3589.0 |
| DomainePlus.com (3612040 CANADA inc.) | 5 | 0.32% | 3 | 1829.8 |
| Namespro Solutions Inc. | 3 | 0.19% | 2 | 7705.8 |
| CanSpace Solutions Inc. | 2 | 0.13% | 2 | 4273 |
| FastWebServer Internet Services Inc. | 1 | 0.06% | 1 | 5091 |
| PlanetHoster | 1 | 0.06% | 1 | 394 |

#### 2026-10

- **Sessions covered:** 4  (2026-10-07 → 2026-10-28)
- **Total domains registered:** 1,352
- **Avg domains/session:** 338.0
- **Unique registrars (ever active):** 11
- **Avg registrars/session:** 8.5
- **Market concentration HHI:** 4,093.4

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 773 | 57.17% | 4 | 13461.2 |
| BareMetal.com inc | 376 | 27.81% | 4 | 13765.9 |
| Webnames.ca Inc. | 67 | 4.96% | 4 | 93696.1 |
| MyID.ca INC. | 55 | 4.07% | 3 | 80618.1 |
| Register.ca Inc. | 35 | 2.59% | 4 | 3381.2 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 19 | 1.41% | 4 | 78761.1 |
| Grape Inc. | 17 | 1.26% | 4 | 2907.5 |
| FastWebServer Internet Services Inc. | 4 | 0.3% | 3 | 2516.5 |
| DomainePlus.com (3612040 CANADA inc.) | 3 | 0.22% | 2 | 2500.2 |
| CanSpace Solutions Inc. | 2 | 0.15% | 1 | 11312.5 |
| PlanetHoster | 1 | 0.07% | 1 | 500 |

#### 2026-11

- **Sessions covered:** 3  (2026-11-04 → 2026-11-18)
- **Total domains registered:** 895
- **Avg domains/session:** 298.3
- **Unique registrars (ever active):** 10
- **Avg registrars/session:** 9.7
- **Market concentration HHI:** 3,480.7

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 424 | 47.37% | 3 | 10357.9 |
| BareMetal.com inc | 305 | 34.08% | 3 | 13824.2 |
| Webnames.ca Inc. | 59 | 6.59% | 3 | 113186.0 |
| Register.ca Inc. | 34 | 3.8% | 3 | 3102.1 |
| MyID.ca INC. | 26 | 2.91% | 3 | 4673.7 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 19 | 2.12% | 3 | 88546.3 |
| Grape Inc. | 18 | 2.01% | 3 | 3356.2 |
| DomainePlus.com (3612040 CANADA inc.) | 4 | 0.45% | 3 | 1795 |
| easyDNS Technologies Inc. | 4 | 0.45% | 3 | 8169.8 |
| FastWebServer Internet Services Inc. | 2 | 0.22% | 2 | 49 |


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
