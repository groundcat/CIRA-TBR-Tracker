# CIRA TBR Tracker

> Automated archive and analytics for CIRA **To-Be-Released (TBR)** `.CA` domain
> drop sessions. Updated every **Wednesday ≈ 19:30 UTC** via GitHub Actions.

**Last updated:** 2026-05-13 &nbsp;|&nbsp; **Total sessions tracked:** 5

---

## What is TBR?

CIRA releases expired `.CA` domains every **Wednesday at 19:00 UTC** via a
first-come, first-served process. Whichever registrar submits a registration
request first wins the domain (one connection, one request per 5 s per registrar).

Capture latency is measured from the official session open at **19:00:00.000 UTC**.

---

## Last Session

- **Date:** 2026-05-13
- **Domains released:** 240
- **Domains registered:** 240
- **Registration rate:** 100.0%
- **Unique registrars:** 9
- **Session duration:** 123,162 ms
- **Market concentration (HHI):** 4,647.4

**Capture latency across all registrars:**
- Min: 2 ms | Median: 11542 ms | Mean: 12205.5 ms | P95: 21920 ms | Max: 123164 ms

**Per-registrar latency breakdown:**

| Registrar | Domains | Min (ms) | Median (ms) | Mean (ms) | P95 (ms) | Max (ms) | StdDev (ms) |
|-----------|--------:|---------:|------------:|----------:|---------:|---------:|------------:|
| WHC Online Solutions Inc. | 150 | 46 | 11158 | 10482.5 | 17825 | 18620 | 5209.8 |
| BareMetal.com inc | 64 | 14 | 15571 | 14160.2 | 22555 | 25241 | 6763.0 |
| Register.ca Inc. | 11 | 2 | 29 | 1752.6 | 6946 | 6946 | 2910.0 |
| Webnames.ca Inc. | 5 | 22692 | 67967 | 73967.2 | 123164 | 123164 | 41622.4 |
| MyID.ca INC. | 4 | 12 | 19 | 1605.2 | 6370 | 6370 | 3176.5 |
| Grape Inc. | 2 | 31 | 32 | 32 | 33 | 33 | 1.4 |
| easyDNS Technologies Inc. | 2 | 12866 | 22970 | 22970.5 | 33075 | 33075 | 14289.9 |
| DomainePlus.com (3612040 CANADA inc.) | 1 | 1794 | 1794 | 1794 | 1794 | 1794 | 0 |
| CanSpace Solutions Inc. | 1 | 7370 | 7370 | 7370 | 7370 | 7370 | 0 |

**Timing distribution (captures by second offset from 19:00:00 UTC):**

| Offset (s) | Domains Captured |
|-----------:|-----------------:|
| +0 | 28 |
| +1 | 8 |
| +4 | 3 |
| +5 | 17 |
| +6 | 14 |
| +7 | 15 |
| +8 | 8 |
| +9 | 4 |
| +10 | 15 |
| +11 | 15 |
| +12 | 17 |
| +13 | 13 |
| +14 | 5 |
| +15 | 16 |
| +16 | 15 |
| +17 | 15 |
| +18 | 6 |
| +20 | 6 |
| +21 | 9 |
| +22 | 3 |
| +23 | 2 |
| +25 | 1 |
| +33 | 1 |
| +47 | 1 |
| +67 | 1 |
| +108 | 1 |
| +123 | 1 |

![Last Session Market Share](charts/last_session_market_share.png)


![Last Session Latency Distribution](charts/last_session_latency_histogram.png)


![Last Session Latency by Registrar](charts/last_session_latency_by_registrar.png)


![Last Session Timing Distribution](charts/last_session_timing_distribution.png)


---

## Rolling Windows

### Last 4 Sessions

- **Sessions covered:** 4  (2026-04-22 → 2026-05-13)
- **Total domains registered:** 969
- **Avg domains/session:** 242.2
- **Unique registrars (ever active):** 12
- **Avg registrars/session:** 9
- **Market concentration HHI:** 5,065.9

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 654 | 67.49% | 4 | 10637.2 |
| BareMetal.com inc | 215 | 22.19% | 4 | 12796.2 |
| MyID.ca INC. | 28 | 2.89% | 3 | 4120.8 |
| Webnames.ca Inc. | 24 | 2.48% | 4 | 77451.8 |
| Register.ca Inc. | 13 | 1.34% | 2 | 881.5 |
| Grape Inc. | 8 | 0.83% | 4 | 471.8 |
| DomainePlus.com (3612040 CANADA inc.) | 8 | 0.83% | 4 | 4708 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 6 | 0.62% | 3 | 32676.5 |
| Namespro Solutions Inc. | 5 | 0.52% | 2 | 28960.6 |
| PlanetHoster | 3 | 0.31% | 2 | 332.8 |
| easyDNS Technologies Inc. | 3 | 0.31% | 2 | 15110.8 |
| CanSpace Solutions Inc. | 2 | 0.21% | 2 | 239826.5 |

![Last 4 Sessions Market Share](charts/last_4_sessions_market_share.png)


---

### Last ~6 Months (26 Weeks)

- **Sessions covered:** 5  (2026-04-15 → 2026-05-13)
- **Total domains registered:** 1,224
- **Avg domains/session:** 244.8
- **Unique registrars (ever active):** 12
- **Avg registrars/session:** 9.4
- **Market concentration HHI:** 4,964.9

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 818 | 66.83% | 5 | 10901.9 |
| BareMetal.com inc | 267 | 21.81% | 5 | 12902.3 |
| Webnames.ca Inc. | 40 | 3.27% | 5 | 93453.5 |
| MyID.ca INC. | 35 | 2.86% | 4 | 4385.5 |
| Register.ca Inc. | 14 | 1.14% | 3 | 3931.4 |
| Grape Inc. | 11 | 0.9% | 5 | 1074.7 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 10 | 0.82% | 4 | 28115.2 |
| DomainePlus.com (3612040 CANADA inc.) | 10 | 0.82% | 5 | 3915.2 |
| Namespro Solutions Inc. | 7 | 0.57% | 3 | 23383.4 |
| PlanetHoster | 5 | 0.41% | 3 | 1795.2 |
| easyDNS Technologies Inc. | 5 | 0.41% | 3 | 14011.8 |
| CanSpace Solutions Inc. | 2 | 0.16% | 2 | 239826.5 |

![Last 26 Weeks Market Share](charts/last_26_weeks_market_share.png)


---

### Last 52 Weeks

- **Sessions covered:** 5  (2026-04-15 → 2026-05-13)
- **Total domains registered:** 1,224
- **Avg domains/session:** 244.8
- **Unique registrars (ever active):** 12
- **Avg registrars/session:** 9.4
- **Market concentration HHI:** 4,964.9

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 818 | 66.83% | 5 | 10901.9 |
| BareMetal.com inc | 267 | 21.81% | 5 | 12902.3 |
| Webnames.ca Inc. | 40 | 3.27% | 5 | 93453.5 |
| MyID.ca INC. | 35 | 2.86% | 4 | 4385.5 |
| Register.ca Inc. | 14 | 1.14% | 3 | 3931.4 |
| Grape Inc. | 11 | 0.9% | 5 | 1074.7 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 10 | 0.82% | 4 | 28115.2 |
| DomainePlus.com (3612040 CANADA inc.) | 10 | 0.82% | 5 | 3915.2 |
| Namespro Solutions Inc. | 7 | 0.57% | 3 | 23383.4 |
| PlanetHoster | 5 | 0.41% | 3 | 1795.2 |
| easyDNS Technologies Inc. | 5 | 0.41% | 3 | 14011.8 |
| CanSpace Solutions Inc. | 2 | 0.16% | 2 | 239826.5 |

![Last 52 Weeks Market Share](charts/last_52_weeks_market_share.png)


---

## All Time

- **Sessions covered:** 5  (2026-04-15 → 2026-05-13)
- **Total domains registered:** 1,224
- **Avg domains/session:** 244.8
- **Unique registrars (ever active):** 12
- **Avg registrars/session:** 9.4
- **Market concentration HHI:** 4,964.9

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 818 | 66.83% | 5 | 10901.9 |
| BareMetal.com inc | 267 | 21.81% | 5 | 12902.3 |
| Webnames.ca Inc. | 40 | 3.27% | 5 | 93453.5 |
| MyID.ca INC. | 35 | 2.86% | 4 | 4385.5 |
| Register.ca Inc. | 14 | 1.14% | 3 | 3931.4 |
| Grape Inc. | 11 | 0.9% | 5 | 1074.7 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 10 | 0.82% | 4 | 28115.2 |
| DomainePlus.com (3612040 CANADA inc.) | 10 | 0.82% | 5 | 3915.2 |
| Namespro Solutions Inc. | 7 | 0.57% | 3 | 23383.4 |
| PlanetHoster | 5 | 0.41% | 3 | 1795.2 |
| easyDNS Technologies Inc. | 5 | 0.41% | 3 | 14011.8 |
| CanSpace Solutions Inc. | 2 | 0.16% | 2 | 239826.5 |

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

- **Sessions covered:** 5  (2026-04-15 → 2026-05-13)
- **Total domains registered:** 1,224
- **Avg domains/session:** 244.8
- **Unique registrars (ever active):** 12
- **Avg registrars/session:** 9.4
- **Market concentration HHI:** 4,964.9

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 818 | 66.83% | 5 | 10901.9 |
| BareMetal.com inc | 267 | 21.81% | 5 | 12902.3 |
| Webnames.ca Inc. | 40 | 3.27% | 5 | 93453.5 |
| MyID.ca INC. | 35 | 2.86% | 4 | 4385.5 |
| Register.ca Inc. | 14 | 1.14% | 3 | 3931.4 |
| Grape Inc. | 11 | 0.9% | 5 | 1074.7 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 10 | 0.82% | 4 | 28115.2 |
| DomainePlus.com (3612040 CANADA inc.) | 10 | 0.82% | 5 | 3915.2 |
| Namespro Solutions Inc. | 7 | 0.57% | 3 | 23383.4 |
| PlanetHoster | 5 | 0.41% | 3 | 1795.2 |
| easyDNS Technologies Inc. | 5 | 0.41% | 3 | 14011.8 |
| CanSpace Solutions Inc. | 2 | 0.16% | 2 | 239826.5 |

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

- **Sessions covered:** 2  (2026-05-06 → 2026-05-13)
- **Total domains registered:** 478
- **Avg domains/session:** 239.0
- **Unique registrars (ever active):** 12
- **Avg registrars/session:** 8.5
- **Market concentration HHI:** 4,823.2

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 306 | 64.02% | 2 | 9718.2 |
| BareMetal.com inc | 127 | 26.57% | 2 | 14047.5 |
| Webnames.ca Inc. | 16 | 3.35% | 2 | 97092.1 |
| Register.ca Inc. | 11 | 2.3% | 1 | 1752.6 |
| Grape Inc. | 4 | 0.84% | 2 | 53.5 |
| MyID.ca INC. | 4 | 0.84% | 1 | 1605.2 |
| Namespro Solutions Inc. | 2 | 0.42% | 1 | 27678.5 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 2 | 0.42% | 1 | 42059.5 |
| DomainePlus.com (3612040 CANADA inc.) | 2 | 0.42% | 2 | 1400 |
| easyDNS Technologies Inc. | 2 | 0.42% | 1 | 22970.5 |
| PlanetHoster | 1 | 0.21% | 1 | 439 |
| CanSpace Solutions Inc. | 1 | 0.21% | 1 | 7370 |


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
