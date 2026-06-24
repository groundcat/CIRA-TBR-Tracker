# CIRA TBR Tracker

> Automated archive and analytics for CIRA **To-Be-Released (TBR)** `.CA` domain
> drop sessions. Updated every **Wednesday ≈ 19:30 UTC** via GitHub Actions.

**Last updated:** 2026-06-24 &nbsp;|&nbsp; **Total sessions tracked:** 11

---

## What is TBR?

CIRA releases expired `.CA` domains every **Wednesday at 19:00 UTC** via a
first-come, first-served process. Whichever registrar submits a registration
request first wins the domain (one connection, one request per 5 s per registrar).

Capture latency is measured from the official session open at **19:00:00.000 UTC**.

---

## Last Session

- **Date:** 2026-06-24
- **Domains released:** 209
- **Domains registered:** 209
- **Registration rate:** 100.0%
- **Unique registrars:** 7
- **Session duration:** 85,592 ms
- **Market concentration (HHI):** 5,072.0

**Capture latency across all registrars:**
- Min: 7 ms | Median: 10381 ms | Mean: 10337.5 ms | P95: 17758 ms | Max: 85599 ms

**Per-registrar latency breakdown:**

| Registrar | Domains | Min (ms) | Median (ms) | Mean (ms) | P95 (ms) | Max (ms) | StdDev (ms) |
|-----------|--------:|---------:|------------:|----------:|---------:|---------:|------------:|
| WHC Online Solutions Inc. | 142 | 41 | 10695 | 9565.3 | 16936 | 18111 | 4954.5 |
| BareMetal.com inc | 43 | 8 | 10381 | 8908.5 | 15432 | 15488 | 5035.4 |
| MyID.ca INC. | 7 | 29 | 41 | 164.3 | 555 | 555 | 208.2 |
| Webnames.ca Inc. | 7 | 20062 | 45270 | 49616.3 | 85599 | 85599 | 24092.4 |
| Register.ca Inc. | 6 | 7 | 186 | 2613.8 | 10129 | 10129 | 4202.6 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 3 | 755 | 12718 | 14298.7 | 29423 | 29423 | 14399.2 |
| DomainePlus.com (3612040 CANADA inc.) | 1 | 12149 | 12149 | 12149 | 12149 | 12149 | 0 |

**Timing distribution (captures by second offset from 19:00:00 UTC):**

| Offset (s) | Domains Captured |
|-----------:|-----------------:|
| +0 | 28 |
| +1 | 7 |
| +2 | 3 |
| +4 | 1 |
| +5 | 21 |
| +6 | 24 |
| +7 | 11 |
| +8 | 1 |
| +10 | 23 |
| +11 | 23 |
| +12 | 18 |
| +13 | 1 |
| +14 | 4 |
| +15 | 16 |
| +16 | 14 |
| +17 | 4 |
| +18 | 2 |
| +20 | 1 |
| +29 | 1 |
| +30 | 1 |
| +35 | 1 |
| +45 | 1 |
| +55 | 1 |
| +75 | 1 |
| +85 | 1 |

![Last Session Market Share](charts/last_session_market_share.png)


![Last Session Latency Distribution](charts/last_session_latency_histogram.png)


![Last Session Latency by Registrar](charts/last_session_latency_by_registrar.png)


![Last Session Timing Distribution](charts/last_session_timing_distribution.png)


---

## Rolling Windows

### Last 4 Sessions

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

![Last 4 Sessions Market Share](charts/last_4_sessions_market_share.png)


---

### Last ~6 Months (26 Weeks)

- **Sessions covered:** 11  (2026-04-15 → 2026-06-24)
- **Total domains registered:** 2,403
- **Avg domains/session:** 218.5
- **Unique registrars (ever active):** 12
- **Avg registrars/session:** 8.9
- **Market concentration HHI:** 4,531.3

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 1,519 | 63.21% | 11 | 9949.0 |
| BareMetal.com inc | 533 | 22.18% | 11 | 11435.2 |
| MyID.ca INC. | 119 | 4.95% | 10 | 11107.0 |
| Webnames.ca Inc. | 83 | 3.45% | 11 | 82487.1 |
| Register.ca Inc. | 50 | 2.08% | 8 | 3046.7 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 26 | 1.08% | 9 | 27872.7 |
| Grape Inc. | 20 | 0.83% | 9 | 1158.9 |
| DomainePlus.com (3612040 CANADA inc.) | 18 | 0.75% | 10 | 3312.5 |
| Namespro Solutions Inc. | 14 | 0.58% | 6 | 19949.0 |
| PlanetHoster | 11 | 0.46% | 6 | 1921.2 |
| easyDNS Technologies Inc. | 8 | 0.33% | 5 | 14692.8 |
| CanSpace Solutions Inc. | 2 | 0.08% | 2 | 239826.5 |

![Last 26 Weeks Market Share](charts/last_26_weeks_market_share.png)


---

### Last 52 Weeks

- **Sessions covered:** 11  (2026-04-15 → 2026-06-24)
- **Total domains registered:** 2,403
- **Avg domains/session:** 218.5
- **Unique registrars (ever active):** 12
- **Avg registrars/session:** 8.9
- **Market concentration HHI:** 4,531.3

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 1,519 | 63.21% | 11 | 9949.0 |
| BareMetal.com inc | 533 | 22.18% | 11 | 11435.2 |
| MyID.ca INC. | 119 | 4.95% | 10 | 11107.0 |
| Webnames.ca Inc. | 83 | 3.45% | 11 | 82487.1 |
| Register.ca Inc. | 50 | 2.08% | 8 | 3046.7 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 26 | 1.08% | 9 | 27872.7 |
| Grape Inc. | 20 | 0.83% | 9 | 1158.9 |
| DomainePlus.com (3612040 CANADA inc.) | 18 | 0.75% | 10 | 3312.5 |
| Namespro Solutions Inc. | 14 | 0.58% | 6 | 19949.0 |
| PlanetHoster | 11 | 0.46% | 6 | 1921.2 |
| easyDNS Technologies Inc. | 8 | 0.33% | 5 | 14692.8 |
| CanSpace Solutions Inc. | 2 | 0.08% | 2 | 239826.5 |

![Last 52 Weeks Market Share](charts/last_52_weeks_market_share.png)


---

## All Time

- **Sessions covered:** 11  (2026-04-15 → 2026-06-24)
- **Total domains registered:** 2,403
- **Avg domains/session:** 218.5
- **Unique registrars (ever active):** 12
- **Avg registrars/session:** 8.9
- **Market concentration HHI:** 4,531.3

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 1,519 | 63.21% | 11 | 9949.0 |
| BareMetal.com inc | 533 | 22.18% | 11 | 11435.2 |
| MyID.ca INC. | 119 | 4.95% | 10 | 11107.0 |
| Webnames.ca Inc. | 83 | 3.45% | 11 | 82487.1 |
| Register.ca Inc. | 50 | 2.08% | 8 | 3046.7 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 26 | 1.08% | 9 | 27872.7 |
| Grape Inc. | 20 | 0.83% | 9 | 1158.9 |
| DomainePlus.com (3612040 CANADA inc.) | 18 | 0.75% | 10 | 3312.5 |
| Namespro Solutions Inc. | 14 | 0.58% | 6 | 19949.0 |
| PlanetHoster | 11 | 0.46% | 6 | 1921.2 |
| easyDNS Technologies Inc. | 8 | 0.33% | 5 | 14692.8 |
| CanSpace Solutions Inc. | 2 | 0.08% | 2 | 239826.5 |

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

- **Sessions covered:** 11  (2026-04-15 → 2026-06-24)
- **Total domains registered:** 2,403
- **Avg domains/session:** 218.5
- **Unique registrars (ever active):** 12
- **Avg registrars/session:** 8.9
- **Market concentration HHI:** 4,531.3

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 1,519 | 63.21% | 11 | 9949.0 |
| BareMetal.com inc | 533 | 22.18% | 11 | 11435.2 |
| MyID.ca INC. | 119 | 4.95% | 10 | 11107.0 |
| Webnames.ca Inc. | 83 | 3.45% | 11 | 82487.1 |
| Register.ca Inc. | 50 | 2.08% | 8 | 3046.7 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 26 | 1.08% | 9 | 27872.7 |
| Grape Inc. | 20 | 0.83% | 9 | 1158.9 |
| DomainePlus.com (3612040 CANADA inc.) | 18 | 0.75% | 10 | 3312.5 |
| Namespro Solutions Inc. | 14 | 0.58% | 6 | 19949.0 |
| PlanetHoster | 11 | 0.46% | 6 | 1921.2 |
| easyDNS Technologies Inc. | 8 | 0.33% | 5 | 14692.8 |
| CanSpace Solutions Inc. | 2 | 0.08% | 2 | 239826.5 |

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
