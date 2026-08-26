# CIRA TBR Tracker

> Automated archive and analytics for CIRA **To-Be-Released (TBR)** `.CA` domain
> drop sessions. Updated every **Wednesday ≈ 19:30 UTC** via GitHub Actions.

**Last updated:** 2026-08-26 &nbsp;|&nbsp; **Total sessions tracked:** 19

---

## What is TBR?

CIRA releases expired `.CA` domains every **Wednesday at 19:00 UTC** via a
first-come, first-served process. Whichever registrar submits a registration
request first wins the domain (one connection, one request per 5 s per registrar).

Capture latency is measured from the official session open at **19:00:00.000 UTC**.

---

## Last Session

- **Date:** 2026-08-26
- **Domains released:** 242
- **Domains registered:** 242
- **Registration rate:** 100.0%
- **Unique registrars:** 9
- **Session duration:** 147,470 ms
- **Market concentration (HHI):** 3,763.3

**Capture latency across all registrars:**
- Min: 8 ms | Median: 11499 ms | Mean: 21389.5 ms | P95: 77058 ms | Max: 147478 ms

**Per-registrar latency breakdown:**

| Registrar | Domains | Min (ms) | Median (ms) | Mean (ms) | P95 (ms) | Max (ms) | StdDev (ms) |
|-----------|--------:|---------:|------------:|----------:|---------:|---------:|------------:|
| WHC Online Solutions Inc. | 128 | 44 | 10290 | 9484.7 | 16161 | 16599 | 4713.8 |
| BareMetal.com inc | 72 | 12 | 26881 | 32995.3 | 77058 | 82294 | 26392.2 |
| Webnames.ca Inc. | 17 | 1708 | 82214 | 76569.2 | 147478 | 147478 | 51908.3 |
| MyID.ca INC. | 11 | 43 | 121 | 1084.5 | 5035 | 5035 | 1622.2 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 6 | 335 | 51139 | 45068.5 | 75692 | 75692 | 26114.7 |
| Register.ca Inc. | 5 | 8 | 85 | 80 | 117 | 117 | 42.9 |
| DomainePlus.com (3612040 CANADA inc.) | 1 | 75 | 75 | 75 | 75 | 75 | 0 |
| PlanetHoster | 1 | 418 | 418 | 418 | 418 | 418 | 0 |
| CanSpace Solutions Inc. | 1 | 1647 | 1647 | 1647 | 1647 | 1647 | 0 |

**Timing distribution (captures by second offset from 19:00:00 UTC):**

| Offset (s) | Domains Captured |
|-----------:|-----------------:|
| +0 | 34 |
| +1 | 8 |
| +2 | 1 |
| +5 | 27 |
| +6 | 17 |
| +7 | 5 |
| +9 | 1 |
| +10 | 26 |
| +11 | 18 |
| +12 | 8 |
| +13 | 2 |
| +14 | 1 |
| +15 | 20 |
| +16 | 8 |
| +21 | 4 |
| +23 | 2 |
| +26 | 11 |
| +27 | 2 |
| +31 | 2 |
| +32 | 1 |
| +42 | 1 |
| +43 | 4 |
| +45 | 1 |
| +48 | 3 |
| +50 | 1 |
| +52 | 1 |
| +54 | 1 |
| +55 | 2 |
| +57 | 1 |
| +59 | 1 |
| +60 | 5 |
| +65 | 2 |
| +71 | 2 |
| +72 | 1 |
| +75 | 1 |
| +76 | 4 |
| +77 | 3 |
| +82 | 2 |
| +97 | 1 |
| +107 | 1 |
| +117 | 1 |
| +122 | 1 |
| +127 | 1 |
| +137 | 1 |
| +142 | 1 |
| +147 | 1 |

![Last Session Market Share](charts/last_session_market_share.png)


![Last Session Latency Distribution](charts/last_session_latency_histogram.png)


![Last Session Latency by Registrar](charts/last_session_latency_by_registrar.png)


![Last Session Timing Distribution](charts/last_session_timing_distribution.png)


---

## Rolling Windows

### Last 4 Sessions

- **Sessions covered:** 4  (2026-07-29 → 2026-08-26)
- **Total domains registered:** 1,117
- **Avg domains/session:** 279.2
- **Unique registrars (ever active):** 11
- **Avg registrars/session:** 8.5
- **Market concentration HHI:** 4,321.9

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 669 | 59.89% | 4 | 11931.8 |
| BareMetal.com inc | 294 | 26.32% | 4 | 20440.0 |
| MyID.ca INC. | 49 | 4.39% | 4 | 1960.9 |
| Webnames.ca Inc. | 39 | 3.49% | 4 | 73299.1 |
| Register.ca Inc. | 27 | 2.42% | 4 | 1412.1 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 24 | 2.15% | 4 | 46639.0 |
| Namespro Solutions Inc. | 4 | 0.36% | 3 | 29398.3 |
| Grape Inc. | 4 | 0.36% | 2 | 6010.5 |
| PlanetHoster | 3 | 0.27% | 2 | 781.5 |
| CanSpace Solutions Inc. | 3 | 0.27% | 2 | 2473 |
| DomainePlus.com (3612040 CANADA inc.) | 1 | 0.09% | 1 | 75 |

![Last 4 Sessions Market Share](charts/last_4_sessions_market_share.png)


---

### Last ~6 Months (26 Weeks)

- **Sessions covered:** 19  (2026-04-15 → 2026-08-26)
- **Total domains registered:** 4,484
- **Avg domains/session:** 236.0
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 9.1
- **Market concentration HHI:** 4,413.4

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 2,772 | 61.82% | 19 | 10392.2 |
| BareMetal.com inc | 1,047 | 23.35% | 19 | 13867.7 |
| MyID.ca INC. | 232 | 5.17% | 18 | 7410.5 |
| Webnames.ca Inc. | 146 | 3.26% | 19 | 79836.0 |
| Register.ca Inc. | 104 | 2.32% | 16 | 2801.8 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 70 | 1.56% | 17 | 36576.6 |
| Grape Inc. | 33 | 0.74% | 14 | 2084.3 |
| DomainePlus.com (3612040 CANADA inc.) | 23 | 0.51% | 13 | 3899.3 |
| Namespro Solutions Inc. | 20 | 0.45% | 11 | 27412.2 |
| PlanetHoster | 18 | 0.4% | 12 | 1286.9 |
| easyDNS Technologies Inc. | 11 | 0.25% | 8 | 10928.4 |
| CanSpace Solutions Inc. | 6 | 0.13% | 5 | 97029.6 |
| FastWebServer Internet Services Inc. | 2 | 0.04% | 2 | 3029.5 |

![Last 26 Weeks Market Share](charts/last_26_weeks_market_share.png)


---

### Last 52 Weeks

- **Sessions covered:** 19  (2026-04-15 → 2026-08-26)
- **Total domains registered:** 4,484
- **Avg domains/session:** 236.0
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 9.1
- **Market concentration HHI:** 4,413.4

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 2,772 | 61.82% | 19 | 10392.2 |
| BareMetal.com inc | 1,047 | 23.35% | 19 | 13867.7 |
| MyID.ca INC. | 232 | 5.17% | 18 | 7410.5 |
| Webnames.ca Inc. | 146 | 3.26% | 19 | 79836.0 |
| Register.ca Inc. | 104 | 2.32% | 16 | 2801.8 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 70 | 1.56% | 17 | 36576.6 |
| Grape Inc. | 33 | 0.74% | 14 | 2084.3 |
| DomainePlus.com (3612040 CANADA inc.) | 23 | 0.51% | 13 | 3899.3 |
| Namespro Solutions Inc. | 20 | 0.45% | 11 | 27412.2 |
| PlanetHoster | 18 | 0.4% | 12 | 1286.9 |
| easyDNS Technologies Inc. | 11 | 0.25% | 8 | 10928.4 |
| CanSpace Solutions Inc. | 6 | 0.13% | 5 | 97029.6 |
| FastWebServer Internet Services Inc. | 2 | 0.04% | 2 | 3029.5 |

![Last 52 Weeks Market Share](charts/last_52_weeks_market_share.png)


---

## All Time

- **Sessions covered:** 19  (2026-04-15 → 2026-08-26)
- **Total domains registered:** 4,484
- **Avg domains/session:** 236.0
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 9.1
- **Market concentration HHI:** 4,413.4

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 2,772 | 61.82% | 19 | 10392.2 |
| BareMetal.com inc | 1,047 | 23.35% | 19 | 13867.7 |
| MyID.ca INC. | 232 | 5.17% | 18 | 7410.5 |
| Webnames.ca Inc. | 146 | 3.26% | 19 | 79836.0 |
| Register.ca Inc. | 104 | 2.32% | 16 | 2801.8 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 70 | 1.56% | 17 | 36576.6 |
| Grape Inc. | 33 | 0.74% | 14 | 2084.3 |
| DomainePlus.com (3612040 CANADA inc.) | 23 | 0.51% | 13 | 3899.3 |
| Namespro Solutions Inc. | 20 | 0.45% | 11 | 27412.2 |
| PlanetHoster | 18 | 0.4% | 12 | 1286.9 |
| easyDNS Technologies Inc. | 11 | 0.25% | 8 | 10928.4 |
| CanSpace Solutions Inc. | 6 | 0.13% | 5 | 97029.6 |
| FastWebServer Internet Services Inc. | 2 | 0.04% | 2 | 3029.5 |

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

- **Sessions covered:** 19  (2026-04-15 → 2026-08-26)
- **Total domains registered:** 4,484
- **Avg domains/session:** 236.0
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 9.1
- **Market concentration HHI:** 4,413.4

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 2,772 | 61.82% | 19 | 10392.2 |
| BareMetal.com inc | 1,047 | 23.35% | 19 | 13867.7 |
| MyID.ca INC. | 232 | 5.17% | 18 | 7410.5 |
| Webnames.ca Inc. | 146 | 3.26% | 19 | 79836.0 |
| Register.ca Inc. | 104 | 2.32% | 16 | 2801.8 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 70 | 1.56% | 17 | 36576.6 |
| Grape Inc. | 33 | 0.74% | 14 | 2084.3 |
| DomainePlus.com (3612040 CANADA inc.) | 23 | 0.51% | 13 | 3899.3 |
| Namespro Solutions Inc. | 20 | 0.45% | 11 | 27412.2 |
| PlanetHoster | 18 | 0.4% | 12 | 1286.9 |
| easyDNS Technologies Inc. | 11 | 0.25% | 8 | 10928.4 |
| CanSpace Solutions Inc. | 6 | 0.13% | 5 | 97029.6 |
| FastWebServer Internet Services Inc. | 2 | 0.04% | 2 | 3029.5 |

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
