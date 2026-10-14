# CIRA TBR Tracker

> Automated archive and analytics for CIRA **To-Be-Released (TBR)** `.CA` domain
> drop sessions. Updated every **Wednesday ≈ 19:30 UTC** via GitHub Actions.

**Last updated:** 2026-10-14 &nbsp;|&nbsp; **Total sessions tracked:** 26

---

## What is TBR?

CIRA releases expired `.CA` domains every **Wednesday at 19:00 UTC** via a
first-come, first-served process. Whichever registrar submits a registration
request first wins the domain (one connection, one request per 5 s per registrar).

Capture latency is measured from the official session open at **19:00:00.000 UTC**.

---

## Last Session

- **Date:** 2026-10-14
- **Domains released:** 454
- **Domains registered:** 454
- **Registration rate:** 100.0%
- **Unique registrars:** 8
- **Session duration:** 221,309 ms
- **Market concentration (HHI):** 5,779.8

**Capture latency across all registrars:**
- Min: 2 ms | Median: 18603 ms | Mean: 20495.3 ms | P95: 35837 ms | Max: 221311 ms

**Per-registrar latency breakdown:**

| Registrar | Domains | Min (ms) | Median (ms) | Mean (ms) | P95 (ms) | Max (ms) | StdDev (ms) |
|-----------|--------:|---------:|------------:|----------:|---------:|---------:|------------:|
| WHC Online Solutions Inc. | 330 | 46 | 19586 | 19244.9 | 35032 | 36984 | 10574.3 |
| BareMetal.com inc | 100 | 7 | 11040 | 12650.5 | 25741 | 26019 | 8659.9 |
| Webnames.ca Inc. | 14 | 2842 | 108390 | 101644 | 221311 | 221311 | 71995.2 |
| Grape Inc. | 3 | 14 | 57 | 1740 | 5149 | 5149 | 2952.4 |
| Register.ca Inc. | 3 | 137 | 5151 | 3501.7 | 5217 | 5217 | 2914.1 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 2 | 121956 | 124874 | 124874 | 127792 | 127792 | 4126.7 |
| FastWebServer Internet Services Inc. | 1 | 2 | 2 | 2 | 2 | 2 | 0 |
| PlanetHoster | 1 | 500 | 500 | 500 | 500 | 500 | 0 |

**Timing distribution (captures by second offset from 19:00:00 UTC):**

| Offset (s) | Domains Captured |
|-----------:|-----------------:|
| +0 | 35 |
| +1 | 15 |
| +2 | 2 |
| +5 | 26 |
| +6 | 32 |
| +7 | 12 |
| +8 | 1 |
| +10 | 17 |
| +11 | 23 |
| +12 | 3 |
| +13 | 16 |
| +14 | 3 |
| +15 | 15 |
| +16 | 17 |
| +17 | 8 |
| +18 | 16 |
| +19 | 2 |
| +20 | 22 |
| +21 | 20 |
| +22 | 11 |
| +23 | 16 |
| +24 | 3 |
| +25 | 17 |
| +26 | 13 |
| +27 | 12 |
| +28 | 15 |
| +29 | 2 |
| +30 | 9 |
| +31 | 13 |
| +32 | 12 |
| +33 | 15 |
| +34 | 2 |
| +35 | 8 |
| +36 | 9 |
| +45 | 1 |
| +85 | 1 |
| +95 | 1 |
| +120 | 1 |
| +121 | 1 |
| +125 | 1 |
| +127 | 1 |
| +141 | 1 |
| +146 | 1 |
| +156 | 1 |
| +216 | 1 |
| +221 | 1 |

![Last Session Market Share](charts/last_session_market_share.png)


![Last Session Latency Distribution](charts/last_session_latency_histogram.png)


![Last Session Latency by Registrar](charts/last_session_latency_by_registrar.png)


![Last Session Timing Distribution](charts/last_session_timing_distribution.png)


---

## Rolling Windows

### Last 4 Sessions

- **Sessions covered:** 4  (2026-09-23 → 2026-10-14)
- **Total domains registered:** 1,428
- **Avg domains/session:** 357.0
- **Unique registrars (ever active):** 11
- **Avg registrars/session:** 7.8
- **Market concentration HHI:** 4,534.9

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 896 | 62.75% | 4 | 14835.2 |
| BareMetal.com inc | 332 | 23.25% | 4 | 16447.3 |
| Webnames.ca Inc. | 90 | 6.3% | 4 | 166959.8 |
| MyID.ca INC. | 46 | 3.22% | 3 | 3851.9 |
| Register.ca Inc. | 32 | 2.24% | 4 | 3663.8 |
| Grape Inc. | 15 | 1.05% | 4 | 3484.7 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 11 | 0.77% | 3 | 65031.5 |
| Namespro Solutions Inc. | 2 | 0.14% | 1 | 15298.5 |
| PlanetHoster | 2 | 0.14% | 2 | 447 |
| CanSpace Solutions Inc. | 1 | 0.07% | 1 | 448 |
| FastWebServer Internet Services Inc. | 1 | 0.07% | 1 | 2 |

![Last 4 Sessions Market Share](charts/last_4_sessions_market_share.png)


---

### Last ~6 Months (26 Weeks)

- **Sessions covered:** 25  (2026-04-22 → 2026-10-14)
- **Total domains registered:** 6,551
- **Avg domains/session:** 262.0
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 8.7
- **Market concentration HHI:** 4,372.9

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 4,018 | 61.33% | 25 | 11342.8 |
| BareMetal.com inc | 1,553 | 23.71% | 25 | 14623.2 |
| Webnames.ca Inc. | 302 | 4.61% | 25 | 100789.1 |
| MyID.ca INC. | 285 | 4.35% | 23 | 6206.7 |
| Register.ca Inc. | 164 | 2.5% | 22 | 2665.1 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 89 | 1.36% | 21 | 44833.3 |
| Grape Inc. | 54 | 0.82% | 19 | 2305.6 |
| DomainePlus.com (3612040 CANADA inc.) | 26 | 0.4% | 15 | 3695.8 |
| Namespro Solutions Inc. | 21 | 0.32% | 12 | 25393.1 |
| PlanetHoster | 18 | 0.27% | 13 | 893.6 |
| easyDNS Technologies Inc. | 9 | 0.14% | 7 | 10801.9 |
| CanSpace Solutions Inc. | 8 | 0.12% | 7 | 70527.7 |
| FastWebServer Internet Services Inc. | 4 | 0.06% | 4 | 2788 |

![Last 26 Weeks Market Share](charts/last_26_weeks_market_share.png)


---

### Last 52 Weeks

- **Sessions covered:** 26  (2026-04-15 → 2026-10-14)
- **Total domains registered:** 6,806
- **Avg domains/session:** 261.8
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 8.8
- **Market concentration HHI:** 4,381.2

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 4,182 | 61.45% | 26 | 11366.5 |
| BareMetal.com inc | 1,605 | 23.58% | 26 | 14573.3 |
| Webnames.ca Inc. | 318 | 4.67% | 26 | 102968.8 |
| MyID.ca INC. | 292 | 4.29% | 24 | 6164.0 |
| Register.ca Inc. | 165 | 2.42% | 23 | 2985.4 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 93 | 1.37% | 22 | 43451.4 |
| Grape Inc. | 57 | 0.84% | 20 | 2364.6 |
| DomainePlus.com (3612040 CANADA inc.) | 28 | 0.41% | 16 | 3511.3 |
| Namespro Solutions Inc. | 23 | 0.34% | 13 | 24380.5 |
| PlanetHoster | 20 | 0.29% | 14 | 1166.9 |
| easyDNS Technologies Inc. | 11 | 0.16% | 8 | 10928.4 |
| CanSpace Solutions Inc. | 8 | 0.12% | 7 | 70527.7 |
| FastWebServer Internet Services Inc. | 4 | 0.06% | 4 | 2788 |

![Last 52 Weeks Market Share](charts/last_52_weeks_market_share.png)


---

## All Time

- **Sessions covered:** 26  (2026-04-15 → 2026-10-14)
- **Total domains registered:** 6,806
- **Avg domains/session:** 261.8
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 8.8
- **Market concentration HHI:** 4,381.2

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 4,182 | 61.45% | 26 | 11366.5 |
| BareMetal.com inc | 1,605 | 23.58% | 26 | 14573.3 |
| Webnames.ca Inc. | 318 | 4.67% | 26 | 102968.8 |
| MyID.ca INC. | 292 | 4.29% | 24 | 6164.0 |
| Register.ca Inc. | 165 | 2.42% | 23 | 2985.4 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 93 | 1.37% | 22 | 43451.4 |
| Grape Inc. | 57 | 0.84% | 20 | 2364.6 |
| DomainePlus.com (3612040 CANADA inc.) | 28 | 0.41% | 16 | 3511.3 |
| Namespro Solutions Inc. | 23 | 0.34% | 13 | 24380.5 |
| PlanetHoster | 20 | 0.29% | 14 | 1166.9 |
| easyDNS Technologies Inc. | 11 | 0.16% | 8 | 10928.4 |
| CanSpace Solutions Inc. | 8 | 0.12% | 7 | 70527.7 |
| FastWebServer Internet Services Inc. | 4 | 0.06% | 4 | 2788 |

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

- **Sessions covered:** 26  (2026-04-15 → 2026-10-14)
- **Total domains registered:** 6,806
- **Avg domains/session:** 261.8
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 8.8
- **Market concentration HHI:** 4,381.2

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 4,182 | 61.45% | 26 | 11366.5 |
| BareMetal.com inc | 1,605 | 23.58% | 26 | 14573.3 |
| Webnames.ca Inc. | 318 | 4.67% | 26 | 102968.8 |
| MyID.ca INC. | 292 | 4.29% | 24 | 6164.0 |
| Register.ca Inc. | 165 | 2.42% | 23 | 2985.4 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 93 | 1.37% | 22 | 43451.4 |
| Grape Inc. | 57 | 0.84% | 20 | 2364.6 |
| DomainePlus.com (3612040 CANADA inc.) | 28 | 0.41% | 16 | 3511.3 |
| Namespro Solutions Inc. | 23 | 0.34% | 13 | 24380.5 |
| PlanetHoster | 20 | 0.29% | 14 | 1166.9 |
| easyDNS Technologies Inc. | 11 | 0.16% | 8 | 10928.4 |
| CanSpace Solutions Inc. | 8 | 0.12% | 7 | 70527.7 |
| FastWebServer Internet Services Inc. | 4 | 0.06% | 4 | 2788 |

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

- **Sessions covered:** 2  (2026-10-07 → 2026-10-14)
- **Total domains registered:** 759
- **Avg domains/session:** 379.5
- **Unique registrars (ever active):** 9
- **Avg registrars/session:** 7.5
- **Market concentration HHI:** 5,006.1

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 507 | 66.8% | 2 | 15931.1 |
| BareMetal.com inc | 171 | 22.53% | 2 | 13422.4 |
| Webnames.ca Inc. | 41 | 5.4% | 2 | 106412.9 |
| MyID.ca INC. | 15 | 1.98% | 1 | 4620.9 |
| Register.ca Inc. | 9 | 1.19% | 2 | 3547.1 |
| Grape Inc. | 8 | 1.05% | 2 | 1877.8 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 6 | 0.79% | 2 | 81711.6 |
| FastWebServer Internet Services Inc. | 1 | 0.13% | 1 | 2 |
| PlanetHoster | 1 | 0.13% | 1 | 500 |


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
