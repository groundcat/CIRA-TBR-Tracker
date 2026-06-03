# CIRA TBR Tracker

> Automated archive and analytics for CIRA **To-Be-Released (TBR)** `.CA` domain
> drop sessions. Updated every **Wednesday ≈ 19:30 UTC** via GitHub Actions.

**Last updated:** 2026-06-03 &nbsp;|&nbsp; **Total sessions tracked:** 8

---

## What is TBR?

CIRA releases expired `.CA` domains every **Wednesday at 19:00 UTC** via a
first-come, first-served process. Whichever registrar submits a registration
request first wins the domain (one connection, one request per 5 s per registrar).

Capture latency is measured from the official session open at **19:00:00.000 UTC**.

---

## Last Session

- **Date:** 2026-06-03
- **Domains released:** 166
- **Domains registered:** 166
- **Registration rate:** 100.0%
- **Unique registrars:** 10
- **Session duration:** 68,557 ms
- **Market concentration (HHI):** 3,837.5

**Capture latency across all registrars:**
- Min: 1 ms | Median: 6460 ms | Mean: 8843.9 ms | P95: 18275 ms | Max: 68558 ms

**Per-registrar latency breakdown:**

| Registrar | Domains | Min (ms) | Median (ms) | Mean (ms) | P95 (ms) | Max (ms) | StdDev (ms) |
|-----------|--------:|---------:|------------:|----------:|---------:|---------:|------------:|
| WHC Online Solutions Inc. | 95 | 1 | 6456 | 7326.7 | 11663 | 12445 | 3793.2 |
| BareMetal.com inc | 36 | 21 | 10336 | 9275.1 | 15340 | 15357 | 4863.8 |
| MyID.ca INC. | 12 | 53 | 961 | 2454 | 6120 | 6120 | 2691.2 |
| Register.ca Inc. | 8 | 16 | 5015 | 3343.8 | 5267 | 5267 | 2465.8 |
| Webnames.ca Inc. | 4 | 8178 | 28358 | 33363.2 | 68558 | 68558 | 26623.4 |
| Namespro Solutions Inc. | 4 | 24610 | 33608 | 33609 | 42609 | 42609 | 7745.2 |
| PlanetHoster | 2 | 1101 | 1102 | 1102 | 1103 | 1103 | 1.4 |
| easyDNS Technologies Inc. | 2 | 6459 | 30047 | 30047.5 | 53636 | 53636 | 33359.2 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 2 | 18189 | 25854 | 25854.5 | 33520 | 33520 | 10840.7 |
| Grape Inc. | 1 | 44 | 44 | 44 | 44 | 44 | 0 |

**Timing distribution (captures by second offset from 19:00:00 UTC):**

| Offset (s) | Domains Captured |
|-----------:|-----------------:|
| +0 | 26 |
| +1 | 6 |
| +5 | 31 |
| +6 | 24 |
| +7 | 4 |
| +8 | 1 |
| +9 | 2 |
| +10 | 23 |
| +11 | 29 |
| +12 | 2 |
| +14 | 1 |
| +15 | 7 |
| +18 | 2 |
| +24 | 1 |
| +30 | 1 |
| +33 | 1 |
| +36 | 1 |
| +38 | 1 |
| +42 | 1 |
| +53 | 1 |
| +68 | 1 |

![Last Session Market Share](charts/last_session_market_share.png)


![Last Session Latency Distribution](charts/last_session_latency_histogram.png)


![Last Session Latency by Registrar](charts/last_session_latency_by_registrar.png)


![Last Session Timing Distribution](charts/last_session_timing_distribution.png)


---

## Rolling Windows

### Last 4 Sessions

- **Sessions covered:** 4  (2026-05-13 → 2026-06-03)
- **Total domains registered:** 791
- **Avg domains/session:** 197.8
- **Unique registrars (ever active):** 12
- **Avg registrars/session:** 8.8
- **Market concentration HHI:** 4,123.4

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 469 | 59.29% | 4 | 9102.2 |
| BareMetal.com inc | 183 | 23.14% | 4 | 10497.0 |
| MyID.ca INC. | 51 | 6.45% | 4 | 12262.1 |
| Webnames.ca Inc. | 33 | 4.17% | 4 | 75439.9 |
| Register.ca Inc. | 27 | 3.41% | 3 | 1781.0 |
| easyDNS Technologies Inc. | 5 | 0.63% | 3 | 18133.0 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 5 | 0.63% | 2 | 39892.6 |
| Namespro Solutions Inc. | 5 | 0.63% | 2 | 20165.5 |
| Grape Inc. | 4 | 0.51% | 3 | 39.3 |
| DomainePlus.com (3612040 CANADA inc.) | 4 | 0.51% | 3 | 645.8 |
| PlanetHoster | 4 | 0.51% | 2 | 3050.2 |
| CanSpace Solutions Inc. | 1 | 0.13% | 1 | 7370 |

![Last 4 Sessions Market Share](charts/last_4_sessions_market_share.png)


---

### Last ~6 Months (26 Weeks)

- **Sessions covered:** 8  (2026-04-15 → 2026-06-03)
- **Total domains registered:** 1,775
- **Avg domains/session:** 221.9
- **Unique registrars (ever active):** 12
- **Avg registrars/session:** 9.1
- **Market concentration HHI:** 4,618.3

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 1,137 | 64.06% | 8 | 10054.5 |
| BareMetal.com inc | 386 | 21.75% | 8 | 11542.4 |
| MyID.ca INC. | 82 | 4.62% | 7 | 9283.6 |
| Webnames.ca Inc. | 68 | 3.83% | 8 | 86882.5 |
| Register.ca Inc. | 30 | 1.69% | 5 | 3076.9 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 15 | 0.85% | 6 | 32041.0 |
| Grape Inc. | 13 | 0.73% | 7 | 779.9 |
| DomainePlus.com (3612040 CANADA inc.) | 13 | 0.73% | 7 | 2817.1 |
| Namespro Solutions Inc. | 12 | 0.68% | 5 | 22096.2 |
| PlanetHoster | 9 | 0.51% | 5 | 2297.2 |
| easyDNS Technologies Inc. | 8 | 0.45% | 5 | 14692.8 |
| CanSpace Solutions Inc. | 2 | 0.11% | 2 | 239826.5 |

![Last 26 Weeks Market Share](charts/last_26_weeks_market_share.png)


---

### Last 52 Weeks

- **Sessions covered:** 8  (2026-04-15 → 2026-06-03)
- **Total domains registered:** 1,775
- **Avg domains/session:** 221.9
- **Unique registrars (ever active):** 12
- **Avg registrars/session:** 9.1
- **Market concentration HHI:** 4,618.3

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 1,137 | 64.06% | 8 | 10054.5 |
| BareMetal.com inc | 386 | 21.75% | 8 | 11542.4 |
| MyID.ca INC. | 82 | 4.62% | 7 | 9283.6 |
| Webnames.ca Inc. | 68 | 3.83% | 8 | 86882.5 |
| Register.ca Inc. | 30 | 1.69% | 5 | 3076.9 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 15 | 0.85% | 6 | 32041.0 |
| Grape Inc. | 13 | 0.73% | 7 | 779.9 |
| DomainePlus.com (3612040 CANADA inc.) | 13 | 0.73% | 7 | 2817.1 |
| Namespro Solutions Inc. | 12 | 0.68% | 5 | 22096.2 |
| PlanetHoster | 9 | 0.51% | 5 | 2297.2 |
| easyDNS Technologies Inc. | 8 | 0.45% | 5 | 14692.8 |
| CanSpace Solutions Inc. | 2 | 0.11% | 2 | 239826.5 |

![Last 52 Weeks Market Share](charts/last_52_weeks_market_share.png)


---

## All Time

- **Sessions covered:** 8  (2026-04-15 → 2026-06-03)
- **Total domains registered:** 1,775
- **Avg domains/session:** 221.9
- **Unique registrars (ever active):** 12
- **Avg registrars/session:** 9.1
- **Market concentration HHI:** 4,618.3

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 1,137 | 64.06% | 8 | 10054.5 |
| BareMetal.com inc | 386 | 21.75% | 8 | 11542.4 |
| MyID.ca INC. | 82 | 4.62% | 7 | 9283.6 |
| Webnames.ca Inc. | 68 | 3.83% | 8 | 86882.5 |
| Register.ca Inc. | 30 | 1.69% | 5 | 3076.9 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 15 | 0.85% | 6 | 32041.0 |
| Grape Inc. | 13 | 0.73% | 7 | 779.9 |
| DomainePlus.com (3612040 CANADA inc.) | 13 | 0.73% | 7 | 2817.1 |
| Namespro Solutions Inc. | 12 | 0.68% | 5 | 22096.2 |
| PlanetHoster | 9 | 0.51% | 5 | 2297.2 |
| easyDNS Technologies Inc. | 8 | 0.45% | 5 | 14692.8 |
| CanSpace Solutions Inc. | 2 | 0.11% | 2 | 239826.5 |

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

- **Sessions covered:** 8  (2026-04-15 → 2026-06-03)
- **Total domains registered:** 1,775
- **Avg domains/session:** 221.9
- **Unique registrars (ever active):** 12
- **Avg registrars/session:** 9.1
- **Market concentration HHI:** 4,618.3

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 1,137 | 64.06% | 8 | 10054.5 |
| BareMetal.com inc | 386 | 21.75% | 8 | 11542.4 |
| MyID.ca INC. | 82 | 4.62% | 7 | 9283.6 |
| Webnames.ca Inc. | 68 | 3.83% | 8 | 86882.5 |
| Register.ca Inc. | 30 | 1.69% | 5 | 3076.9 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 15 | 0.85% | 6 | 32041.0 |
| Grape Inc. | 13 | 0.73% | 7 | 779.9 |
| DomainePlus.com (3612040 CANADA inc.) | 13 | 0.73% | 7 | 2817.1 |
| Namespro Solutions Inc. | 12 | 0.68% | 5 | 22096.2 |
| PlanetHoster | 9 | 0.51% | 5 | 2297.2 |
| easyDNS Technologies Inc. | 8 | 0.45% | 5 | 14692.8 |
| CanSpace Solutions Inc. | 2 | 0.11% | 2 | 239826.5 |

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

- **Sessions covered:** 1  (2026-06-03 → 2026-06-03)
- **Total domains registered:** 166
- **Avg domains/session:** 166.0
- **Unique registrars (ever active):** 10
- **Avg registrars/session:** 10
- **Market concentration HHI:** 3,837.5

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 95 | 57.23% | 1 | 7326.7 |
| BareMetal.com inc | 36 | 21.69% | 1 | 9275.1 |
| MyID.ca INC. | 12 | 7.23% | 1 | 2454 |
| Register.ca Inc. | 8 | 4.82% | 1 | 3343.8 |
| Webnames.ca Inc. | 4 | 2.41% | 1 | 33363.2 |
| Namespro Solutions Inc. | 4 | 2.41% | 1 | 33609 |
| PlanetHoster | 2 | 1.2% | 1 | 1102 |
| easyDNS Technologies Inc. | 2 | 1.2% | 1 | 30047.5 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 2 | 1.2% | 1 | 25854.5 |
| Grape Inc. | 1 | 0.6% | 1 | 44 |


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
