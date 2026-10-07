# CIRA TBR Tracker

> Automated archive and analytics for CIRA **To-Be-Released (TBR)** `.CA` domain
> drop sessions. Updated every **Wednesday ≈ 19:30 UTC** via GitHub Actions.

**Last updated:** 2026-10-07 &nbsp;|&nbsp; **Total sessions tracked:** 25

---

## What is TBR?

CIRA releases expired `.CA` domains every **Wednesday at 19:00 UTC** via a
first-come, first-served process. Whichever registrar submits a registration
request first wins the domain (one connection, one request per 5 s per registrar).

Capture latency is measured from the official session open at **19:00:00.000 UTC**.

---

## Last Session

- **Date:** 2026-10-07
- **Domains released:** 305
- **Domains registered:** 305
- **Registration rate:** 100.0%
- **Unique registrars:** 7
- **Session duration:** 228,506 ms
- **Market concentration (HHI):** 4,020.3

**Capture latency across all registrars:**
- Min: 9 ms | Median: 12816 ms | Mean: 21305.2 ms | P95: 102912 ms | Max: 228515 ms

**Per-registrar latency breakdown:**

| Registrar | Domains | Min (ms) | Median (ms) | Mean (ms) | P95 (ms) | Max (ms) | StdDev (ms) |
|-----------|--------:|---------:|------------:|----------:|---------:|---------:|------------:|
| WHC Online Solutions Inc. | 177 | 18 | 12061 | 12617.2 | 21931 | 22094 | 6676.8 |
| BareMetal.com inc | 71 | 9 | 15948 | 14194.3 | 25918 | 26061 | 9003.3 |
| Webnames.ca Inc. | 27 | 414 | 112937 | 111181.7 | 218475 | 228515 | 68127.2 |
| MyID.ca INC. | 15 | 56 | 4922 | 4620.9 | 5258 | 5258 | 1265.8 |
| Register.ca Inc. | 6 | 22 | 747 | 3592.5 | 14969 | 14969 | 5900.5 |
| Grape Inc. | 5 | 34 | 60 | 2015.6 | 4966 | 4966 | 2690.6 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 4 | 397 | 27120 | 38549.2 | 99560 | 99560 | 45476.0 |

**Timing distribution (captures by second offset from 19:00:00 UTC):**

| Offset (s) | Domains Captured |
|-----------:|-----------------:|
| +0 | 33 |
| +1 | 9 |
| +4 | 17 |
| +5 | 19 |
| +6 | 21 |
| +7 | 4 |
| +10 | 13 |
| +11 | 30 |
| +12 | 8 |
| +14 | 2 |
| +15 | 16 |
| +16 | 31 |
| +17 | 9 |
| +18 | 4 |
| +20 | 19 |
| +21 | 27 |
| +22 | 2 |
| +24 | 2 |
| +25 | 12 |
| +26 | 2 |
| +27 | 1 |
| +32 | 1 |
| +46 | 1 |
| +47 | 1 |
| +62 | 1 |
| +77 | 1 |
| +92 | 1 |
| +97 | 1 |
| +99 | 1 |
| +102 | 1 |
| +107 | 1 |
| +112 | 1 |
| +127 | 1 |
| +133 | 1 |
| +138 | 1 |
| +143 | 1 |
| +148 | 1 |
| +153 | 1 |
| +158 | 1 |
| +168 | 1 |
| +183 | 1 |
| +193 | 1 |
| +208 | 1 |
| +218 | 1 |
| +228 | 1 |

![Last Session Market Share](charts/last_session_market_share.png)


![Last Session Latency Distribution](charts/last_session_latency_histogram.png)


![Last Session Latency by Registrar](charts/last_session_latency_by_registrar.png)


![Last Session Timing Distribution](charts/last_session_timing_distribution.png)


---

## Rolling Windows

### Last 4 Sessions

- **Sessions covered:** 4  (2026-09-16 → 2026-10-07)
- **Total domains registered:** 1,302
- **Avg domains/session:** 325.5
- **Unique registrars (ever active):** 11
- **Avg registrars/session:** 7.8
- **Market concentration HHI:** 3,948.4

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 742 | 56.99% | 4 | 13617.7 |
| BareMetal.com inc | 319 | 24.5% | 4 | 17137.0 |
| Webnames.ca Inc. | 111 | 8.53% | 4 | 195885.5 |
| MyID.ca INC. | 50 | 3.84% | 4 | 2977.7 |
| Register.ca Inc. | 40 | 3.07% | 4 | 2820.1 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 17 | 1.31% | 3 | 49236.5 |
| Grape Inc. | 16 | 1.23% | 4 | 3085.7 |
| DomainePlus.com (3612040 CANADA inc.) | 3 | 0.23% | 1 | 4067.3 |
| Namespro Solutions Inc. | 2 | 0.15% | 1 | 15298.5 |
| CanSpace Solutions Inc. | 1 | 0.08% | 1 | 448 |
| PlanetHoster | 1 | 0.08% | 1 | 394 |

![Last 4 Sessions Market Share](charts/last_4_sessions_market_share.png)


---

### Last ~6 Months (26 Weeks)

- **Sessions covered:** 25  (2026-04-15 → 2026-10-07)
- **Total domains registered:** 6,352
- **Avg domains/session:** 254.1
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 8.8
- **Market concentration HHI:** 4,292.3

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 3,852 | 60.64% | 25 | 11051.4 |
| BareMetal.com inc | 1,505 | 23.69% | 25 | 14650.3 |
| Webnames.ca Inc. | 304 | 4.79% | 25 | 103021.8 |
| MyID.ca INC. | 292 | 4.6% | 24 | 6164.0 |
| Register.ca Inc. | 162 | 2.55% | 22 | 2961.9 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 91 | 1.43% | 21 | 39574.1 |
| Grape Inc. | 54 | 0.85% | 19 | 2397.4 |
| DomainePlus.com (3612040 CANADA inc.) | 28 | 0.44% | 16 | 3511.3 |
| Namespro Solutions Inc. | 23 | 0.36% | 13 | 24380.5 |
| PlanetHoster | 19 | 0.3% | 13 | 1218.2 |
| easyDNS Technologies Inc. | 11 | 0.17% | 8 | 10928.4 |
| CanSpace Solutions Inc. | 8 | 0.13% | 7 | 70527.7 |
| FastWebServer Internet Services Inc. | 3 | 0.05% | 3 | 3716.7 |

![Last 26 Weeks Market Share](charts/last_26_weeks_market_share.png)


---

### Last 52 Weeks

- **Sessions covered:** 25  (2026-04-15 → 2026-10-07)
- **Total domains registered:** 6,352
- **Avg domains/session:** 254.1
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 8.8
- **Market concentration HHI:** 4,292.3

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 3,852 | 60.64% | 25 | 11051.4 |
| BareMetal.com inc | 1,505 | 23.69% | 25 | 14650.3 |
| Webnames.ca Inc. | 304 | 4.79% | 25 | 103021.8 |
| MyID.ca INC. | 292 | 4.6% | 24 | 6164.0 |
| Register.ca Inc. | 162 | 2.55% | 22 | 2961.9 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 91 | 1.43% | 21 | 39574.1 |
| Grape Inc. | 54 | 0.85% | 19 | 2397.4 |
| DomainePlus.com (3612040 CANADA inc.) | 28 | 0.44% | 16 | 3511.3 |
| Namespro Solutions Inc. | 23 | 0.36% | 13 | 24380.5 |
| PlanetHoster | 19 | 0.3% | 13 | 1218.2 |
| easyDNS Technologies Inc. | 11 | 0.17% | 8 | 10928.4 |
| CanSpace Solutions Inc. | 8 | 0.13% | 7 | 70527.7 |
| FastWebServer Internet Services Inc. | 3 | 0.05% | 3 | 3716.7 |

![Last 52 Weeks Market Share](charts/last_52_weeks_market_share.png)


---

## All Time

- **Sessions covered:** 25  (2026-04-15 → 2026-10-07)
- **Total domains registered:** 6,352
- **Avg domains/session:** 254.1
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 8.8
- **Market concentration HHI:** 4,292.3

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 3,852 | 60.64% | 25 | 11051.4 |
| BareMetal.com inc | 1,505 | 23.69% | 25 | 14650.3 |
| Webnames.ca Inc. | 304 | 4.79% | 25 | 103021.8 |
| MyID.ca INC. | 292 | 4.6% | 24 | 6164.0 |
| Register.ca Inc. | 162 | 2.55% | 22 | 2961.9 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 91 | 1.43% | 21 | 39574.1 |
| Grape Inc. | 54 | 0.85% | 19 | 2397.4 |
| DomainePlus.com (3612040 CANADA inc.) | 28 | 0.44% | 16 | 3511.3 |
| Namespro Solutions Inc. | 23 | 0.36% | 13 | 24380.5 |
| PlanetHoster | 19 | 0.3% | 13 | 1218.2 |
| easyDNS Technologies Inc. | 11 | 0.17% | 8 | 10928.4 |
| CanSpace Solutions Inc. | 8 | 0.13% | 7 | 70527.7 |
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

- **Sessions covered:** 25  (2026-04-15 → 2026-10-07)
- **Total domains registered:** 6,352
- **Avg domains/session:** 254.1
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 8.8
- **Market concentration HHI:** 4,292.3

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 3,852 | 60.64% | 25 | 11051.4 |
| BareMetal.com inc | 1,505 | 23.69% | 25 | 14650.3 |
| Webnames.ca Inc. | 304 | 4.79% | 25 | 103021.8 |
| MyID.ca INC. | 292 | 4.6% | 24 | 6164.0 |
| Register.ca Inc. | 162 | 2.55% | 22 | 2961.9 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 91 | 1.43% | 21 | 39574.1 |
| Grape Inc. | 54 | 0.85% | 19 | 2397.4 |
| DomainePlus.com (3612040 CANADA inc.) | 28 | 0.44% | 16 | 3511.3 |
| Namespro Solutions Inc. | 23 | 0.36% | 13 | 24380.5 |
| PlanetHoster | 19 | 0.3% | 13 | 1218.2 |
| easyDNS Technologies Inc. | 11 | 0.17% | 8 | 10928.4 |
| CanSpace Solutions Inc. | 8 | 0.13% | 7 | 70527.7 |
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

- **Sessions covered:** 1  (2026-10-07 → 2026-10-07)
- **Total domains registered:** 305
- **Avg domains/session:** 305.0
- **Unique registrars (ever active):** 7
- **Avg registrars/session:** 7
- **Market concentration HHI:** 4,020.3

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 177 | 58.03% | 1 | 12617.2 |
| BareMetal.com inc | 71 | 23.28% | 1 | 14194.3 |
| Webnames.ca Inc. | 27 | 8.85% | 1 | 111181.7 |
| MyID.ca INC. | 15 | 4.92% | 1 | 4620.9 |
| Register.ca Inc. | 6 | 1.97% | 1 | 3592.5 |
| Grape Inc. | 5 | 1.64% | 1 | 2015.6 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 4 | 1.31% | 1 | 38549.2 |


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
