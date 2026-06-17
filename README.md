# CIRA TBR Tracker

> Automated archive and analytics for CIRA **To-Be-Released (TBR)** `.CA` domain
> drop sessions. Updated every **Wednesday ≈ 19:30 UTC** via GitHub Actions.

**Last updated:** 2026-06-17 &nbsp;|&nbsp; **Total sessions tracked:** 10

---

## What is TBR?

CIRA releases expired `.CA` domains every **Wednesday at 19:00 UTC** via a
first-come, first-served process. Whichever registrar submits a registration
request first wins the domain (one connection, one request per 5 s per registrar).

Capture latency is measured from the official session open at **19:00:00.000 UTC**.

---

## Last Session

- **Date:** 2026-06-17
- **Domains released:** 225
- **Domains registered:** 225
- **Registration rate:** 100.0%
- **Unique registrars:** 9
- **Session duration:** 133,571 ms
- **Market concentration (HHI):** 4,187.2

**Capture latency across all registrars:**
- Min: 0 ms | Median: 10493 ms | Mean: 10881.9 ms | P95: 20181 ms | Max: 133571 ms

**Per-registrar latency breakdown:**

| Registrar | Domains | Min (ms) | Median (ms) | Mean (ms) | P95 (ms) | Max (ms) | StdDev (ms) |
|-----------|--------:|---------:|------------:|----------:|---------:|---------:|------------:|
| WHC Online Solutions Inc. | 134 | 30 | 11196 | 9943.0 | 16800 | 17245 | 4976.5 |
| BareMetal.com inc | 54 | 15 | 15118 | 12325.4 | 20449 | 20515 | 6510.3 |
| MyID.ca INC. | 15 | 34 | 5316 | 3514.5 | 6693 | 6693 | 2956.6 |
| Register.ca Inc. | 7 | 14 | 1047 | 2765.3 | 6780 | 6780 | 3149.0 |
| Grape Inc. | 4 | 0 | 23 | 1276.8 | 5060 | 5060 | 2522.2 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 4 | 9905 | 24329 | 24425.8 | 39139 | 39139 | 12233.2 |
| Webnames.ca Inc. | 3 | 7711 | 113486 | 84922.7 | 133571 | 133571 | 67617.2 |
| DomainePlus.com (3612040 CANADA inc.) | 2 | 341 | 1211 | 1211 | 2081 | 2081 | 1230.4 |
| Namespro Solutions Inc. | 2 | 6462 | 9212 | 9212.5 | 11963 | 11963 | 3889.8 |

**Timing distribution (captures by second offset from 19:00:00 UTC):**

| Offset (s) | Domains Captured |
|-----------:|-----------------:|
| +0 | 31 |
| +1 | 5 |
| +2 | 1 |
| +5 | 18 |
| +6 | 35 |
| +7 | 11 |
| +9 | 1 |
| +10 | 12 |
| +11 | 27 |
| +12 | 16 |
| +13 | 6 |
| +15 | 14 |
| +16 | 28 |
| +17 | 5 |
| +18 | 1 |
| +20 | 9 |
| +21 | 1 |
| +27 | 1 |
| +39 | 1 |
| +113 | 1 |
| +133 | 1 |

![Last Session Market Share](charts/last_session_market_share.png)


![Last Session Latency Distribution](charts/last_session_latency_histogram.png)


![Last Session Latency by Registrar](charts/last_session_latency_by_registrar.png)


![Last Session Timing Distribution](charts/last_session_timing_distribution.png)


---

## Rolling Windows

### Last 4 Sessions

- **Sessions covered:** 4  (2026-05-27 → 2026-06-17)
- **Total domains registered:** 753
- **Avg domains/session:** 188.2
- **Unique registrars (ever active):** 11
- **Avg registrars/session:** 9
- **Market concentration HHI:** 3,973.0

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 434 | 57.64% | 4 | 8932.8 |
| BareMetal.com inc | 179 | 23.77% | 4 | 10240.1 |
| MyID.ca INC. | 59 | 7.84% | 4 | 21536.8 |
| Register.ca Inc. | 30 | 3.98% | 4 | 2491.4 |
| Webnames.ca Inc. | 14 | 1.86% | 4 | 62607.9 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 10 | 1.33% | 3 | 23388.2 |
| Grape Inc. | 9 | 1.2% | 4 | 1264.3 |
| Namespro Solutions Inc. | 7 | 0.93% | 3 | 16514.5 |
| DomainePlus.com (3612040 CANADA inc.) | 5 | 0.66% | 3 | 429.5 |
| PlanetHoster | 4 | 0.53% | 2 | 571.8 |
| easyDNS Technologies Inc. | 2 | 0.27% | 1 | 30047.5 |

![Last 4 Sessions Market Share](charts/last_4_sessions_market_share.png)


---

### Last ~6 Months (26 Weeks)

- **Sessions covered:** 10  (2026-04-15 → 2026-06-17)
- **Total domains registered:** 2,194
- **Avg domains/session:** 219.4
- **Unique registrars (ever active):** 12
- **Avg registrars/session:** 9.1
- **Market concentration HHI:** 4,482.8

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 1,377 | 62.76% | 10 | 9987.4 |
| BareMetal.com inc | 490 | 22.33% | 10 | 11687.9 |
| MyID.ca INC. | 112 | 5.1% | 9 | 12322.9 |
| Webnames.ca Inc. | 76 | 3.46% | 10 | 85774.2 |
| Register.ca Inc. | 44 | 2.01% | 7 | 3108.5 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 23 | 1.05% | 8 | 29569.5 |
| Grape Inc. | 20 | 0.91% | 9 | 1158.9 |
| DomainePlus.com (3612040 CANADA inc.) | 17 | 0.77% | 9 | 2330.7 |
| Namespro Solutions Inc. | 14 | 0.64% | 6 | 19949.0 |
| PlanetHoster | 11 | 0.5% | 6 | 1921.2 |
| easyDNS Technologies Inc. | 8 | 0.36% | 5 | 14692.8 |
| CanSpace Solutions Inc. | 2 | 0.09% | 2 | 239826.5 |

![Last 26 Weeks Market Share](charts/last_26_weeks_market_share.png)


---

### Last 52 Weeks

- **Sessions covered:** 10  (2026-04-15 → 2026-06-17)
- **Total domains registered:** 2,194
- **Avg domains/session:** 219.4
- **Unique registrars (ever active):** 12
- **Avg registrars/session:** 9.1
- **Market concentration HHI:** 4,482.8

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 1,377 | 62.76% | 10 | 9987.4 |
| BareMetal.com inc | 490 | 22.33% | 10 | 11687.9 |
| MyID.ca INC. | 112 | 5.1% | 9 | 12322.9 |
| Webnames.ca Inc. | 76 | 3.46% | 10 | 85774.2 |
| Register.ca Inc. | 44 | 2.01% | 7 | 3108.5 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 23 | 1.05% | 8 | 29569.5 |
| Grape Inc. | 20 | 0.91% | 9 | 1158.9 |
| DomainePlus.com (3612040 CANADA inc.) | 17 | 0.77% | 9 | 2330.7 |
| Namespro Solutions Inc. | 14 | 0.64% | 6 | 19949.0 |
| PlanetHoster | 11 | 0.5% | 6 | 1921.2 |
| easyDNS Technologies Inc. | 8 | 0.36% | 5 | 14692.8 |
| CanSpace Solutions Inc. | 2 | 0.09% | 2 | 239826.5 |

![Last 52 Weeks Market Share](charts/last_52_weeks_market_share.png)


---

## All Time

- **Sessions covered:** 10  (2026-04-15 → 2026-06-17)
- **Total domains registered:** 2,194
- **Avg domains/session:** 219.4
- **Unique registrars (ever active):** 12
- **Avg registrars/session:** 9.1
- **Market concentration HHI:** 4,482.8

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 1,377 | 62.76% | 10 | 9987.4 |
| BareMetal.com inc | 490 | 22.33% | 10 | 11687.9 |
| MyID.ca INC. | 112 | 5.1% | 9 | 12322.9 |
| Webnames.ca Inc. | 76 | 3.46% | 10 | 85774.2 |
| Register.ca Inc. | 44 | 2.01% | 7 | 3108.5 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 23 | 1.05% | 8 | 29569.5 |
| Grape Inc. | 20 | 0.91% | 9 | 1158.9 |
| DomainePlus.com (3612040 CANADA inc.) | 17 | 0.77% | 9 | 2330.7 |
| Namespro Solutions Inc. | 14 | 0.64% | 6 | 19949.0 |
| PlanetHoster | 11 | 0.5% | 6 | 1921.2 |
| easyDNS Technologies Inc. | 8 | 0.36% | 5 | 14692.8 |
| CanSpace Solutions Inc. | 2 | 0.09% | 2 | 239826.5 |

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

- **Sessions covered:** 10  (2026-04-15 → 2026-06-17)
- **Total domains registered:** 2,194
- **Avg domains/session:** 219.4
- **Unique registrars (ever active):** 12
- **Avg registrars/session:** 9.1
- **Market concentration HHI:** 4,482.8

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 1,377 | 62.76% | 10 | 9987.4 |
| BareMetal.com inc | 490 | 22.33% | 10 | 11687.9 |
| MyID.ca INC. | 112 | 5.1% | 9 | 12322.9 |
| Webnames.ca Inc. | 76 | 3.46% | 10 | 85774.2 |
| Register.ca Inc. | 44 | 2.01% | 7 | 3108.5 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 23 | 1.05% | 8 | 29569.5 |
| Grape Inc. | 20 | 0.91% | 9 | 1158.9 |
| DomainePlus.com (3612040 CANADA inc.) | 17 | 0.77% | 9 | 2330.7 |
| Namespro Solutions Inc. | 14 | 0.64% | 6 | 19949.0 |
| PlanetHoster | 11 | 0.5% | 6 | 1921.2 |
| easyDNS Technologies Inc. | 8 | 0.36% | 5 | 14692.8 |
| CanSpace Solutions Inc. | 2 | 0.09% | 2 | 239826.5 |

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

- **Sessions covered:** 3  (2026-06-03 → 2026-06-17)
- **Total domains registered:** 585
- **Avg domains/session:** 195.0
- **Unique registrars (ever active):** 11
- **Avg registrars/session:** 9.3
- **Market concentration HHI:** 3,928.1

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 335 | 57.26% | 3 | 8921.7 |
| BareMetal.com inc | 140 | 23.93% | 3 | 11271.5 |
| MyID.ca INC. | 42 | 7.18% | 3 | 16124.9 |
| Register.ca Inc. | 22 | 3.76% | 3 | 3239.7 |
| Webnames.ca Inc. | 12 | 2.05% | 3 | 65348.5 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 10 | 1.71% | 3 | 23388.2 |
| Grape Inc. | 8 | 1.37% | 3 | 1671.7 |
| Namespro Solutions Inc. | 6 | 1.03% | 2 | 21410.8 |
| PlanetHoster | 4 | 0.68% | 2 | 571.8 |
| DomainePlus.com (3612040 CANADA inc.) | 4 | 0.68% | 2 | 628.2 |
| easyDNS Technologies Inc. | 2 | 0.34% | 1 | 30047.5 |


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
