# CIRA TBR Tracker

> Automated archive and analytics for CIRA **To-Be-Released (TBR)** `.CA` domain
> drop sessions. Updated every **Wednesday ≈ 19:30 UTC** via GitHub Actions.

**Last updated:** 2026-11-12 &nbsp;|&nbsp; **Total sessions tracked:** 30

---

## What is TBR?

CIRA releases expired `.CA` domains every **Wednesday at 19:00 UTC** via a
first-come, first-served process. Whichever registrar submits a registration
request first wins the domain (one connection, one request per 5 s per registrar).

Capture latency is measured from the official session open at **19:00:00.000 UTC**.

---

## Last Session

- **Date:** 2026-11-11
- **Domains released:** 338
- **Domains registered:** 338
- **Registration rate:** 100.0%
- **Unique registrars:** 10
- **Session duration:** 236,340 ms
- **Market concentration (HHI):** 4,369.3

**Capture latency across all registrars:**
- Min: 21 ms | Median: 11869 ms | Mean: 16455.9 ms | P95: 25334 ms | Max: 236361 ms

**Per-registrar latency breakdown:**

| Registrar | Domains | Min (ms) | Median (ms) | Mean (ms) | P95 (ms) | Max (ms) | StdDev (ms) |
|-----------|--------:|---------:|------------:|----------:|---------:|---------:|------------:|
| WHC Online Solutions Inc. | 200 | 329 | 12226 | 12755.0 | 22427 | 23156 | 6677.1 |
| BareMetal.com inc | 98 | 58 | 15207 | 13638.2 | 25413 | 26196 | 7542.0 |
| Register.ca Inc. | 12 | 26 | 155 | 2341.1 | 9961 | 9961 | 3323.7 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 9 | 7033 | 167530 | 162510.2 | 236361 | 236361 | 76578.6 |
| Grape Inc. | 7 | 21 | 74 | 2927.6 | 9977 | 9977 | 3940.3 |
| Webnames.ca Inc. | 5 | 5190 | 32086 | 26574 | 42177 | 42177 | 15395.7 |
| MyID.ca INC. | 4 | 49 | 5346 | 4296.5 | 6444 | 6444 | 2879.5 |
| FastWebServer Internet Services Inc. | 1 | 26 | 26 | 26 | 26 | 26 | 0 |
| DomainePlus.com (3612040 CANADA inc.) | 1 | 437 | 437 | 437 | 437 | 437 | 0 |
| easyDNS Technologies Inc. | 1 | 12843 | 12843 | 12843 | 12843 | 12843 | 0 |

**Timing distribution (captures by second offset from 19:00:00 UTC):**

| Offset (s) | Domains Captured |
|-----------:|-----------------:|
| +0 | 32 |
| +1 | 11 |
| +4 | 1 |
| +5 | 31 |
| +6 | 30 |
| +7 | 12 |
| +9 | 2 |
| +10 | 21 |
| +11 | 30 |
| +12 | 17 |
| +15 | 20 |
| +16 | 23 |
| +17 | 23 |
| +18 | 2 |
| +20 | 19 |
| +21 | 22 |
| +22 | 19 |
| +23 | 2 |
| +25 | 9 |
| +26 | 1 |
| +32 | 1 |
| +37 | 1 |
| +42 | 1 |
| +94 | 1 |
| +136 | 1 |
| +146 | 1 |
| +167 | 1 |
| +219 | 1 |
| +224 | 1 |
| +230 | 1 |
| +236 | 1 |

![Last Session Market Share](charts/last_session_market_share.png)


![Last Session Latency Distribution](charts/last_session_latency_histogram.png)


![Last Session Latency by Registrar](charts/last_session_latency_by_registrar.png)


![Last Session Timing Distribution](charts/last_session_timing_distribution.png)


---

## Rolling Windows

### Last 4 Sessions

- **Sessions covered:** 4  (2026-10-21 → 2026-11-11)
- **Total domains registered:** 1,201
- **Avg domains/session:** 300.2
- **Unique registrars (ever active):** 11
- **Avg registrars/session:** 9.5
- **Market concentration HHI:** 3,541.9

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 585 | 48.71% | 4 | 11036.4 |
| BareMetal.com inc | 399 | 33.22% | 4 | 14113.1 |
| MyID.ca INC. | 56 | 4.66% | 4 | 61804.7 |
| Webnames.ca Inc. | 53 | 4.41% | 4 | 77591.6 |
| Register.ca Inc. | 50 | 4.16% | 4 | 3242.6 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 25 | 2.08% | 4 | 81376.6 |
| Grape Inc. | 19 | 1.58% | 4 | 3953.1 |
| DomainePlus.com (3612040 CANADA inc.) | 6 | 0.5% | 4 | 2518.6 |
| FastWebServer Internet Services Inc. | 4 | 0.33% | 3 | 2524.5 |
| CanSpace Solutions Inc. | 2 | 0.17% | 1 | 11312.5 |
| easyDNS Technologies Inc. | 2 | 0.17% | 2 | 7101 |

![Last 4 Sessions Market Share](charts/last_4_sessions_market_share.png)


---

### Last ~6 Months (26 Weeks)

- **Sessions covered:** 25  (2026-05-20 → 2026-11-11)
- **Total domains registered:** 6,783
- **Avg domains/session:** 271.3
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 8.8
- **Market concentration HHI:** 4,103.0

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 3,949 | 58.22% | 25 | 11406.6 |
| BareMetal.com inc | 1,737 | 25.61% | 25 | 14833.9 |
| Webnames.ca Inc. | 331 | 4.88% | 25 | 100811.5 |
| MyID.ca INC. | 313 | 4.61% | 24 | 15733.8 |
| Register.ca Inc. | 201 | 2.96% | 24 | 2910.0 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 108 | 1.59% | 22 | 53135.3 |
| Grape Inc. | 65 | 0.96% | 19 | 3038.4 |
| DomainePlus.com (3612040 CANADA inc.) | 24 | 0.35% | 15 | 3112.0 |
| Namespro Solutions Inc. | 16 | 0.24% | 10 | 24679.6 |
| PlanetHoster | 15 | 0.22% | 11 | 995.5 |
| easyDNS Technologies Inc. | 8 | 0.12% | 7 | 8513.4 |
| CanSpace Solutions Inc. | 8 | 0.12% | 6 | 4225.6 |
| FastWebServer Internet Services Inc. | 8 | 0.12% | 7 | 2675.1 |

![Last 26 Weeks Market Share](charts/last_26_weeks_market_share.png)


---

### Last 52 Weeks

- **Sessions covered:** 30  (2026-04-15 → 2026-11-11)
- **Total domains registered:** 8,007
- **Avg domains/session:** 266.9
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 8.9
- **Market concentration HHI:** 4,222.5

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 4,767 | 59.54% | 30 | 11322.5 |
| BareMetal.com inc | 2,004 | 25.03% | 30 | 14512.0 |
| Webnames.ca Inc. | 371 | 4.63% | 30 | 99585.1 |
| MyID.ca INC. | 348 | 4.35% | 28 | 14112.6 |
| Register.ca Inc. | 215 | 2.69% | 27 | 3023.5 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 118 | 1.47% | 26 | 49286.1 |
| Grape Inc. | 76 | 0.95% | 24 | 2629.3 |
| DomainePlus.com (3612040 CANADA inc.) | 34 | 0.42% | 20 | 3312.8 |
| Namespro Solutions Inc. | 23 | 0.29% | 13 | 24380.5 |
| PlanetHoster | 20 | 0.25% | 14 | 1166.9 |
| easyDNS Technologies Inc. | 13 | 0.16% | 10 | 10162.9 |
| CanSpace Solutions Inc. | 10 | 0.12% | 8 | 63125.8 |
| FastWebServer Internet Services Inc. | 8 | 0.1% | 7 | 2675.1 |

![Last 52 Weeks Market Share](charts/last_52_weeks_market_share.png)


---

## All Time

- **Sessions covered:** 30  (2026-04-15 → 2026-11-11)
- **Total domains registered:** 8,007
- **Avg domains/session:** 266.9
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 8.9
- **Market concentration HHI:** 4,222.5

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 4,767 | 59.54% | 30 | 11322.5 |
| BareMetal.com inc | 2,004 | 25.03% | 30 | 14512.0 |
| Webnames.ca Inc. | 371 | 4.63% | 30 | 99585.1 |
| MyID.ca INC. | 348 | 4.35% | 28 | 14112.6 |
| Register.ca Inc. | 215 | 2.69% | 27 | 3023.5 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 118 | 1.47% | 26 | 49286.1 |
| Grape Inc. | 76 | 0.95% | 24 | 2629.3 |
| DomainePlus.com (3612040 CANADA inc.) | 34 | 0.42% | 20 | 3312.8 |
| Namespro Solutions Inc. | 23 | 0.29% | 13 | 24380.5 |
| PlanetHoster | 20 | 0.25% | 14 | 1166.9 |
| easyDNS Technologies Inc. | 13 | 0.16% | 10 | 10162.9 |
| CanSpace Solutions Inc. | 10 | 0.12% | 8 | 63125.8 |
| FastWebServer Internet Services Inc. | 8 | 0.1% | 7 | 2675.1 |

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

- **Sessions covered:** 30  (2026-04-15 → 2026-11-11)
- **Total domains registered:** 8,007
- **Avg domains/session:** 266.9
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 8.9
- **Market concentration HHI:** 4,222.5

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 4,767 | 59.54% | 30 | 11322.5 |
| BareMetal.com inc | 2,004 | 25.03% | 30 | 14512.0 |
| Webnames.ca Inc. | 371 | 4.63% | 30 | 99585.1 |
| MyID.ca INC. | 348 | 4.35% | 28 | 14112.6 |
| Register.ca Inc. | 215 | 2.69% | 27 | 3023.5 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 118 | 1.47% | 26 | 49286.1 |
| Grape Inc. | 76 | 0.95% | 24 | 2629.3 |
| DomainePlus.com (3612040 CANADA inc.) | 34 | 0.42% | 20 | 3312.8 |
| Namespro Solutions Inc. | 23 | 0.29% | 13 | 24380.5 |
| PlanetHoster | 20 | 0.25% | 14 | 1166.9 |
| easyDNS Technologies Inc. | 13 | 0.16% | 10 | 10162.9 |
| CanSpace Solutions Inc. | 10 | 0.12% | 8 | 63125.8 |
| FastWebServer Internet Services Inc. | 8 | 0.1% | 7 | 2675.1 |

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

- **Sessions covered:** 2  (2026-11-04 → 2026-11-11)
- **Total domains registered:** 608
- **Avg domains/session:** 304.0
- **Unique registrars (ever active):** 10
- **Avg registrars/session:** 9.5
- **Market concentration HHI:** 3,820.5

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 319 | 52.47% | 2 | 11081.2 |
| BareMetal.com inc | 194 | 31.91% | 2 | 14117.0 |
| Webnames.ca Inc. | 27 | 4.44% | 2 | 74203.8 |
| Register.ca Inc. | 24 | 3.95% | 2 | 3269.9 |
| MyID.ca INC. | 16 | 2.63% | 2 | 4992.6 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 12 | 1.97% | 2 | 86942.6 |
| Grape Inc. | 10 | 1.64% | 2 | 3968.9 |
| DomainePlus.com (3612040 CANADA inc.) | 3 | 0.49% | 2 | 2537 |
| easyDNS Technologies Inc. | 2 | 0.33% | 2 | 7101 |
| FastWebServer Internet Services Inc. | 1 | 0.16% | 1 | 26 |


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
