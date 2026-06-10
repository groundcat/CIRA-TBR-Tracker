# CIRA TBR Tracker

> Automated archive and analytics for CIRA **To-Be-Released (TBR)** `.CA` domain
> drop sessions. Updated every **Wednesday ≈ 19:30 UTC** via GitHub Actions.

**Last updated:** 2026-06-10 &nbsp;|&nbsp; **Total sessions tracked:** 9

---

## What is TBR?

CIRA releases expired `.CA` domains every **Wednesday at 19:00 UTC** via a
first-come, first-served process. Whichever registrar submits a registration
request first wins the domain (one connection, one request per 5 s per registrar).

Capture latency is measured from the official session open at **19:00:00.000 UTC**.

---

## Last Session

- **Date:** 2026-06-10
- **Domains released:** 194
- **Domains registered:** 194
- **Registration rate:** 100.0%
- **Unique registrars:** 9
- **Session duration:** 599,899 ms
- **Market concentration (HHI):** 3,737.8

**Capture latency across all registrars:**
- Min: 1 ms | Median: 10383 ms | Mean: 14217.3 ms | P95: 20998 ms | Max: 599900 ms

**Per-registrar latency breakdown:**

| Registrar | Domains | Min (ms) | Median (ms) | Mean (ms) | P95 (ms) | Max (ms) | StdDev (ms) |
|-----------|--------:|---------:|------------:|----------:|---------:|---------:|------------:|
| WHC Online Solutions Inc. | 106 | 28 | 10383 | 9495.3 | 16422 | 16697 | 4938.7 |
| BareMetal.com inc | 50 | 43 | 13370 | 12214.0 | 20863 | 21100 | 6470.4 |
| MyID.ca INC. | 15 | 1 | 4908 | 42406.3 | 599900 | 599900 | 154246.8 |
| Register.ca Inc. | 7 | 14 | 5013 | 3610.1 | 5082 | 5082 | 2454.1 |
| Webnames.ca Inc. | 5 | 43569 | 73757 | 77759.6 | 118936 | 118936 | 27379.1 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 4 | 7070 | 21215 | 19884.2 | 30036 | 30036 | 9823.7 |
| Grape Inc. | 3 | 44 | 5013 | 3694.3 | 6026 | 6026 | 3201.6 |
| PlanetHoster | 2 | 41 | 41 | 41.5 | 42 | 42 | 0.7 |
| DomainePlus.com (3612040 CANADA inc.) | 2 | 45 | 45 | 45.5 | 46 | 46 | 0.7 |

**Timing distribution (captures by second offset from 19:00:00 UTC):**

| Offset (s) | Domains Captured |
|-----------:|-----------------:|
| +0 | 26 |
| +1 | 7 |
| +4 | 3 |
| +5 | 30 |
| +6 | 16 |
| +7 | 3 |
| +8 | 2 |
| +10 | 18 |
| +11 | 21 |
| +12 | 8 |
| +13 | 2 |
| +15 | 18 |
| +16 | 22 |
| +18 | 1 |
| +20 | 8 |
| +21 | 1 |
| +24 | 1 |
| +30 | 1 |
| +43 | 1 |
| +68 | 1 |
| +73 | 1 |
| +83 | 1 |
| +118 | 1 |
| +599 | 1 |

![Last Session Market Share](charts/last_session_market_share.png)


![Last Session Latency Distribution](charts/last_session_latency_histogram.png)


![Last Session Latency by Registrar](charts/last_session_latency_by_registrar.png)


![Last Session Timing Distribution](charts/last_session_timing_distribution.png)


---

## Rolling Windows

### Last 4 Sessions

- **Sessions covered:** 4  (2026-05-20 → 2026-06-10)
- **Total domains registered:** 745
- **Avg domains/session:** 186.2
- **Unique registrars (ever active):** 11
- **Avg registrars/session:** 8.8
- **Market concentration HHI:** 3,871.1

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 425 | 57.05% | 4 | 8855.4 |
| BareMetal.com inc | 169 | 22.68% | 4 | 10010.5 |
| MyID.ca INC. | 62 | 8.32% | 4 | 22462.4 |
| Webnames.ca Inc. | 33 | 4.43% | 4 | 76388.0 |
| Register.ca Inc. | 23 | 3.09% | 3 | 2400.1 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 9 | 1.21% | 3 | 33223.1 |
| PlanetHoster | 6 | 0.81% | 3 | 2047.3 |
| DomainePlus.com (3612040 CANADA inc.) | 5 | 0.67% | 3 | 63.0 |
| Grape Inc. | 5 | 0.67% | 3 | 1260.1 |
| Namespro Solutions Inc. | 5 | 0.67% | 2 | 20165.5 |
| easyDNS Technologies Inc. | 3 | 0.4% | 2 | 15714.2 |

![Last 4 Sessions Market Share](charts/last_4_sessions_market_share.png)


---

### Last ~6 Months (26 Weeks)

- **Sessions covered:** 9  (2026-04-15 → 2026-06-10)
- **Total domains registered:** 1,969
- **Avg domains/session:** 218.8
- **Unique registrars (ever active):** 12
- **Avg registrars/session:** 9.1
- **Market concentration HHI:** 4,520.2

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 1,243 | 63.13% | 9 | 9992.3 |
| BareMetal.com inc | 436 | 22.14% | 9 | 11617.0 |
| MyID.ca INC. | 97 | 4.93% | 8 | 13423.9 |
| Webnames.ca Inc. | 73 | 3.71% | 9 | 85868.8 |
| Register.ca Inc. | 37 | 1.88% | 6 | 3165.8 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 19 | 0.96% | 7 | 30304.3 |
| Grape Inc. | 16 | 0.81% | 8 | 1144.2 |
| DomainePlus.com (3612040 CANADA inc.) | 15 | 0.76% | 8 | 2470.6 |
| Namespro Solutions Inc. | 12 | 0.61% | 5 | 22096.2 |
| PlanetHoster | 11 | 0.56% | 6 | 1921.2 |
| easyDNS Technologies Inc. | 8 | 0.41% | 5 | 14692.8 |
| CanSpace Solutions Inc. | 2 | 0.1% | 2 | 239826.5 |

![Last 26 Weeks Market Share](charts/last_26_weeks_market_share.png)


---

### Last 52 Weeks

- **Sessions covered:** 9  (2026-04-15 → 2026-06-10)
- **Total domains registered:** 1,969
- **Avg domains/session:** 218.8
- **Unique registrars (ever active):** 12
- **Avg registrars/session:** 9.1
- **Market concentration HHI:** 4,520.2

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 1,243 | 63.13% | 9 | 9992.3 |
| BareMetal.com inc | 436 | 22.14% | 9 | 11617.0 |
| MyID.ca INC. | 97 | 4.93% | 8 | 13423.9 |
| Webnames.ca Inc. | 73 | 3.71% | 9 | 85868.8 |
| Register.ca Inc. | 37 | 1.88% | 6 | 3165.8 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 19 | 0.96% | 7 | 30304.3 |
| Grape Inc. | 16 | 0.81% | 8 | 1144.2 |
| DomainePlus.com (3612040 CANADA inc.) | 15 | 0.76% | 8 | 2470.6 |
| Namespro Solutions Inc. | 12 | 0.61% | 5 | 22096.2 |
| PlanetHoster | 11 | 0.56% | 6 | 1921.2 |
| easyDNS Technologies Inc. | 8 | 0.41% | 5 | 14692.8 |
| CanSpace Solutions Inc. | 2 | 0.1% | 2 | 239826.5 |

![Last 52 Weeks Market Share](charts/last_52_weeks_market_share.png)


---

## All Time

- **Sessions covered:** 9  (2026-04-15 → 2026-06-10)
- **Total domains registered:** 1,969
- **Avg domains/session:** 218.8
- **Unique registrars (ever active):** 12
- **Avg registrars/session:** 9.1
- **Market concentration HHI:** 4,520.2

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 1,243 | 63.13% | 9 | 9992.3 |
| BareMetal.com inc | 436 | 22.14% | 9 | 11617.0 |
| MyID.ca INC. | 97 | 4.93% | 8 | 13423.9 |
| Webnames.ca Inc. | 73 | 3.71% | 9 | 85868.8 |
| Register.ca Inc. | 37 | 1.88% | 6 | 3165.8 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 19 | 0.96% | 7 | 30304.3 |
| Grape Inc. | 16 | 0.81% | 8 | 1144.2 |
| DomainePlus.com (3612040 CANADA inc.) | 15 | 0.76% | 8 | 2470.6 |
| Namespro Solutions Inc. | 12 | 0.61% | 5 | 22096.2 |
| PlanetHoster | 11 | 0.56% | 6 | 1921.2 |
| easyDNS Technologies Inc. | 8 | 0.41% | 5 | 14692.8 |
| CanSpace Solutions Inc. | 2 | 0.1% | 2 | 239826.5 |

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

- **Sessions covered:** 9  (2026-04-15 → 2026-06-10)
- **Total domains registered:** 1,969
- **Avg domains/session:** 218.8
- **Unique registrars (ever active):** 12
- **Avg registrars/session:** 9.1
- **Market concentration HHI:** 4,520.2

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 1,243 | 63.13% | 9 | 9992.3 |
| BareMetal.com inc | 436 | 22.14% | 9 | 11617.0 |
| MyID.ca INC. | 97 | 4.93% | 8 | 13423.9 |
| Webnames.ca Inc. | 73 | 3.71% | 9 | 85868.8 |
| Register.ca Inc. | 37 | 1.88% | 6 | 3165.8 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 19 | 0.96% | 7 | 30304.3 |
| Grape Inc. | 16 | 0.81% | 8 | 1144.2 |
| DomainePlus.com (3612040 CANADA inc.) | 15 | 0.76% | 8 | 2470.6 |
| Namespro Solutions Inc. | 12 | 0.61% | 5 | 22096.2 |
| PlanetHoster | 11 | 0.56% | 6 | 1921.2 |
| easyDNS Technologies Inc. | 8 | 0.41% | 5 | 14692.8 |
| CanSpace Solutions Inc. | 2 | 0.1% | 2 | 239826.5 |

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

- **Sessions covered:** 2  (2026-06-03 → 2026-06-10)
- **Total domains registered:** 360
- **Avg domains/session:** 180.0
- **Unique registrars (ever active):** 11
- **Avg registrars/session:** 9.5
- **Market concentration HHI:** 3,774.7

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 201 | 55.83% | 2 | 8411.0 |
| BareMetal.com inc | 86 | 23.89% | 2 | 10744.5 |
| MyID.ca INC. | 27 | 7.5% | 2 | 22430.2 |
| Register.ca Inc. | 15 | 4.17% | 2 | 3476.9 |
| Webnames.ca Inc. | 9 | 2.5% | 2 | 55561.4 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 6 | 1.67% | 2 | 22869.3 |
| Namespro Solutions Inc. | 4 | 1.11% | 1 | 33609 |
| PlanetHoster | 4 | 1.11% | 2 | 571.8 |
| Grape Inc. | 4 | 1.11% | 2 | 1869.2 |
| easyDNS Technologies Inc. | 2 | 0.56% | 1 | 30047.5 |
| DomainePlus.com (3612040 CANADA inc.) | 2 | 0.56% | 1 | 45.5 |


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
