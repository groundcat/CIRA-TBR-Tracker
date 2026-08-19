# CIRA TBR Tracker

> Automated archive and analytics for CIRA **To-Be-Released (TBR)** `.CA` domain
> drop sessions. Updated every **Wednesday ≈ 19:30 UTC** via GitHub Actions.

**Last updated:** 2026-08-19 &nbsp;|&nbsp; **Total sessions tracked:** 18

---

## What is TBR?

CIRA releases expired `.CA` domains every **Wednesday at 19:00 UTC** via a
first-come, first-served process. Whichever registrar submits a registration
request first wins the domain (one connection, one request per 5 s per registrar).

Capture latency is measured from the official session open at **19:00:00.000 UTC**.

---

## Last Session

- **Date:** 2026-08-12
- **Domains released:** 331
- **Domains registered:** 331
- **Registration rate:** 100.0%
- **Unique registrars:** 9
- **Session duration:** 78,513 ms
- **Market concentration (HHI):** 4,832.0

**Capture latency across all registrars:**
- Min: 0 ms | Median: 15347 ms | Mean: 14397.1 ms | P95: 26206 ms | Max: 78513 ms

**Per-registrar latency breakdown:**

| Registrar | Domains | Min (ms) | Median (ms) | Mean (ms) | P95 (ms) | Max (ms) | StdDev (ms) |
|-----------|--------:|---------:|------------:|----------:|---------:|---------:|------------:|
| WHC Online Solutions Inc. | 214 | 43 | 13066 | 13730.3 | 23030 | 25732 | 6920.9 |
| BareMetal.com inc | 83 | 31 | 16646 | 16840.9 | 30343 | 30431 | 8528.7 |
| MyID.ca INC. | 11 | 8 | 59 | 1904.8 | 5374 | 5374 | 2591.2 |
| Webnames.ca Inc. | 8 | 13060 | 40863 | 39556.6 | 78513 | 78513 | 21493.3 |
| Register.ca Inc. | 7 | 0 | 47 | 1477.7 | 5083 | 5083 | 2462.3 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 4 | 1740 | 12206 | 11824.2 | 21145 | 21145 | 8288.8 |
| CanSpace Solutions Inc. | 2 | 31 | 3299 | 3299 | 6567 | 6567 | 4621.6 |
| Grape Inc. | 1 | 97 | 97 | 97 | 97 | 97 | 0 |
| Namespro Solutions Inc. | 1 | 27624 | 27624 | 27624 | 27624 | 27624 | 0 |

**Timing distribution (captures by second offset from 19:00:00 UTC):**

| Offset (s) | Domains Captured |
|-----------:|-----------------:|
| +0 | 27 |
| +1 | 10 |
| +2 | 1 |
| +4 | 1 |
| +5 | 27 |
| +6 | 22 |
| +7 | 9 |
| +9 | 1 |
| +10 | 18 |
| +11 | 31 |
| +12 | 11 |
| +13 | 2 |
| +15 | 22 |
| +16 | 32 |
| +17 | 11 |
| +18 | 3 |
| +20 | 15 |
| +21 | 35 |
| +22 | 11 |
| +23 | 3 |
| +25 | 21 |
| +26 | 7 |
| +27 | 1 |
| +30 | 5 |
| +38 | 1 |
| +43 | 1 |
| +48 | 1 |
| +53 | 1 |
| +78 | 1 |

![Last Session Market Share](charts/last_session_market_share.png)


![Last Session Latency Distribution](charts/last_session_latency_histogram.png)


![Last Session Latency by Registrar](charts/last_session_latency_by_registrar.png)


![Last Session Timing Distribution](charts/last_session_timing_distribution.png)


---

## Rolling Windows

### Last 4 Sessions

- **Sessions covered:** 4  (2026-07-22 → 2026-08-12)
- **Total domains registered:** 1,131
- **Avg domains/session:** 282.8
- **Unique registrars (ever active):** 11
- **Avg registrars/session:** 8.5
- **Market concentration HHI:** 4,465.5

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 700 | 61.89% | 4 | 12046.8 |
| BareMetal.com inc | 274 | 24.23% | 4 | 15536.9 |
| MyID.ca INC. | 63 | 5.57% | 4 | 3085.7 |
| Register.ca Inc. | 29 | 2.56% | 4 | 2283.3 |
| Webnames.ca Inc. | 29 | 2.56% | 4 | 82127.1 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 21 | 1.86% | 4 | 53461.8 |
| Namespro Solutions Inc. | 5 | 0.44% | 4 | 23710.2 |
| Grape Inc. | 4 | 0.35% | 2 | 6010.5 |
| PlanetHoster | 3 | 0.27% | 2 | 1196.5 |
| CanSpace Solutions Inc. | 2 | 0.18% | 1 | 3299 |
| easyDNS Technologies Inc. | 1 | 0.09% | 1 | 1187 |

![Last 4 Sessions Market Share](charts/last_4_sessions_market_share.png)


---

### Last ~6 Months (26 Weeks)

- **Sessions covered:** 18  (2026-04-15 → 2026-08-12)
- **Total domains registered:** 4,242
- **Avg domains/session:** 235.7
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 9.1
- **Market concentration HHI:** 4,458.5

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 2,644 | 62.33% | 18 | 10442.6 |
| BareMetal.com inc | 975 | 22.98% | 18 | 12805.0 |
| MyID.ca INC. | 221 | 5.21% | 17 | 7782.6 |
| Webnames.ca Inc. | 129 | 3.04% | 18 | 80017.4 |
| Register.ca Inc. | 99 | 2.33% | 15 | 2983.2 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 64 | 1.51% | 16 | 36045.9 |
| Grape Inc. | 33 | 0.78% | 14 | 2084.3 |
| DomainePlus.com (3612040 CANADA inc.) | 22 | 0.52% | 12 | 4218.0 |
| Namespro Solutions Inc. | 20 | 0.47% | 11 | 27412.2 |
| PlanetHoster | 17 | 0.4% | 11 | 1365.9 |
| easyDNS Technologies Inc. | 11 | 0.26% | 8 | 10928.4 |
| CanSpace Solutions Inc. | 5 | 0.12% | 4 | 120875.2 |
| FastWebServer Internet Services Inc. | 2 | 0.05% | 2 | 3029.5 |

![Last 26 Weeks Market Share](charts/last_26_weeks_market_share.png)


---

### Last 52 Weeks

- **Sessions covered:** 18  (2026-04-15 → 2026-08-12)
- **Total domains registered:** 4,242
- **Avg domains/session:** 235.7
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 9.1
- **Market concentration HHI:** 4,458.5

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 2,644 | 62.33% | 18 | 10442.6 |
| BareMetal.com inc | 975 | 22.98% | 18 | 12805.0 |
| MyID.ca INC. | 221 | 5.21% | 17 | 7782.6 |
| Webnames.ca Inc. | 129 | 3.04% | 18 | 80017.4 |
| Register.ca Inc. | 99 | 2.33% | 15 | 2983.2 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 64 | 1.51% | 16 | 36045.9 |
| Grape Inc. | 33 | 0.78% | 14 | 2084.3 |
| DomainePlus.com (3612040 CANADA inc.) | 22 | 0.52% | 12 | 4218.0 |
| Namespro Solutions Inc. | 20 | 0.47% | 11 | 27412.2 |
| PlanetHoster | 17 | 0.4% | 11 | 1365.9 |
| easyDNS Technologies Inc. | 11 | 0.26% | 8 | 10928.4 |
| CanSpace Solutions Inc. | 5 | 0.12% | 4 | 120875.2 |
| FastWebServer Internet Services Inc. | 2 | 0.05% | 2 | 3029.5 |

![Last 52 Weeks Market Share](charts/last_52_weeks_market_share.png)


---

## All Time

- **Sessions covered:** 18  (2026-04-15 → 2026-08-12)
- **Total domains registered:** 4,242
- **Avg domains/session:** 235.7
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 9.1
- **Market concentration HHI:** 4,458.5

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 2,644 | 62.33% | 18 | 10442.6 |
| BareMetal.com inc | 975 | 22.98% | 18 | 12805.0 |
| MyID.ca INC. | 221 | 5.21% | 17 | 7782.6 |
| Webnames.ca Inc. | 129 | 3.04% | 18 | 80017.4 |
| Register.ca Inc. | 99 | 2.33% | 15 | 2983.2 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 64 | 1.51% | 16 | 36045.9 |
| Grape Inc. | 33 | 0.78% | 14 | 2084.3 |
| DomainePlus.com (3612040 CANADA inc.) | 22 | 0.52% | 12 | 4218.0 |
| Namespro Solutions Inc. | 20 | 0.47% | 11 | 27412.2 |
| PlanetHoster | 17 | 0.4% | 11 | 1365.9 |
| easyDNS Technologies Inc. | 11 | 0.26% | 8 | 10928.4 |
| CanSpace Solutions Inc. | 5 | 0.12% | 4 | 120875.2 |
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

- **Sessions covered:** 18  (2026-04-15 → 2026-08-12)
- **Total domains registered:** 4,242
- **Avg domains/session:** 235.7
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 9.1
- **Market concentration HHI:** 4,458.5

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 2,644 | 62.33% | 18 | 10442.6 |
| BareMetal.com inc | 975 | 22.98% | 18 | 12805.0 |
| MyID.ca INC. | 221 | 5.21% | 17 | 7782.6 |
| Webnames.ca Inc. | 129 | 3.04% | 18 | 80017.4 |
| Register.ca Inc. | 99 | 2.33% | 15 | 2983.2 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 64 | 1.51% | 16 | 36045.9 |
| Grape Inc. | 33 | 0.78% | 14 | 2084.3 |
| DomainePlus.com (3612040 CANADA inc.) | 22 | 0.52% | 12 | 4218.0 |
| Namespro Solutions Inc. | 20 | 0.47% | 11 | 27412.2 |
| PlanetHoster | 17 | 0.4% | 11 | 1365.9 |
| easyDNS Technologies Inc. | 11 | 0.26% | 8 | 10928.4 |
| CanSpace Solutions Inc. | 5 | 0.12% | 4 | 120875.2 |
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

#### 2026-08

- **Sessions covered:** 2  (2026-08-05 → 2026-08-12)
- **Total domains registered:** 596
- **Avg domains/session:** 298.0
- **Unique registrars (ever active):** 9
- **Avg registrars/session:** 8.5
- **Market concentration HHI:** 4,619.5

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 377 | 63.26% | 2 | 13051.8 |
| BareMetal.com inc | 144 | 24.16% | 2 | 14529.6 |
| MyID.ca INC. | 23 | 3.86% | 2 | 2344.1 |
| Register.ca Inc. | 17 | 2.85% | 2 | 1767.2 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 14 | 2.35% | 2 | 47745.7 |
| Webnames.ca Inc. | 13 | 2.18% | 2 | 77825.7 |
| Grape Inc. | 4 | 0.67% | 2 | 6010.5 |
| Namespro Solutions Inc. | 2 | 0.34% | 2 | 23856 |
| CanSpace Solutions Inc. | 2 | 0.34% | 1 | 3299 |


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
