# CIRA TBR Tracker

> Automated archive and analytics for CIRA **To-Be-Released (TBR)** `.CA` domain
> drop sessions. Updated every **Wednesday ≈ 19:30 UTC** via GitHub Actions.

**Last updated:** 2026-07-22 &nbsp;|&nbsp; **Total sessions tracked:** 15

---

## What is TBR?

CIRA releases expired `.CA` domains every **Wednesday at 19:00 UTC** via a
first-come, first-served process. Whichever registrar submits a registration
request first wins the domain (one connection, one request per 5 s per registrar).

Capture latency is measured from the official session open at **19:00:00.000 UTC**.

---

## Last Session

- **Date:** 2026-07-22
- **Domains released:** 256
- **Domains registered:** 256
- **Registration rate:** 100.0%
- **Unique registrars:** 9
- **Session duration:** 233,708 ms
- **Market concentration (HHI):** 4,382.3

**Capture latency across all registrars:**
- Min: 0 ms | Median: 10625 ms | Mean: 13480.4 ms | P95: 20498 ms | Max: 233708 ms

**Per-registrar latency breakdown:**

| Registrar | Domains | Min (ms) | Median (ms) | Mean (ms) | P95 (ms) | Max (ms) | StdDev (ms) |
|-----------|--------:|---------:|------------:|----------:|---------:|---------:|------------:|
| WHC Online Solutions Inc. | 159 | 37 | 10876 | 9944.5 | 16701 | 16996 | 5133.4 |
| BareMetal.com inc | 52 | 0 | 15236 | 13383.1 | 21018 | 21107 | 6669.6 |
| MyID.ca INC. | 25 | 0 | 5081 | 5583.9 | 10873 | 14872 | 4120.2 |
| Register.ca Inc. | 7 | 2 | 4959 | 3564.9 | 5015 | 5015 | 2420.0 |
| Webnames.ca Inc. | 7 | 6515 | 163004 | 111881.3 | 233708 | 233708 | 96429.1 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 3 | 7364 | 85703 | 72359.7 | 124012 | 124012 | 59457.7 |
| easyDNS Technologies Inc. | 1 | 1187 | 1187 | 1187 | 1187 | 1187 | 0 |
| PlanetHoster | 1 | 1248 | 1248 | 1248 | 1248 | 1248 | 0 |
| Namespro Solutions Inc. | 1 | 6646 | 6646 | 6646 | 6646 | 6646 | 0 |

**Timing distribution (captures by second offset from 19:00:00 UTC):**

| Offset (s) | Domains Captured |
|-----------:|-----------------:|
| +0 | 25 |
| +1 | 6 |
| +4 | 6 |
| +5 | 46 |
| +6 | 21 |
| +7 | 1 |
| +9 | 2 |
| +10 | 34 |
| +11 | 26 |
| +14 | 2 |
| +15 | 33 |
| +16 | 32 |
| +17 | 1 |
| +20 | 11 |
| +21 | 4 |
| +85 | 1 |
| +124 | 1 |
| +163 | 1 |
| +168 | 1 |
| +183 | 1 |
| +233 | 1 |

![Last Session Market Share](charts/last_session_market_share.png)


![Last Session Latency Distribution](charts/last_session_latency_histogram.png)


![Last Session Latency by Registrar](charts/last_session_latency_by_registrar.png)


![Last Session Timing Distribution](charts/last_session_timing_distribution.png)


---

## Rolling Windows

### Last 4 Sessions

- **Sessions covered:** 4  (2026-07-01 → 2026-07-22)
- **Total domains registered:** 964
- **Avg domains/session:** 241.0
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 10.2
- **Market concentration HHI:** 4,254.5

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 584 | 60.58% | 4 | 10071.2 |
| BareMetal.com inc | 220 | 22.82% | 4 | 13984.6 |
| MyID.ca INC. | 64 | 6.64% | 4 | 3618.8 |
| Register.ca Inc. | 27 | 2.8% | 4 | 3701.7 |
| Webnames.ca Inc. | 24 | 2.49% | 4 | 79082.1 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 20 | 2.07% | 4 | 46098.1 |
| Grape Inc. | 9 | 0.93% | 3 | 2242.8 |
| DomainePlus.com (3612040 CANADA inc.) | 4 | 0.41% | 2 | 8745.8 |
| PlanetHoster | 4 | 0.41% | 4 | 588 |
| easyDNS Technologies Inc. | 3 | 0.31% | 3 | 4654.3 |
| FastWebServer Internet Services Inc. | 2 | 0.21% | 2 | 3029.5 |
| Namespro Solutions Inc. | 2 | 0.21% | 2 | 46823 |
| CanSpace Solutions Inc. | 1 | 0.1% | 1 | 549 |

![Last 4 Sessions Market Share](charts/last_4_sessions_market_share.png)


---

### Last ~6 Months (26 Weeks)

- **Sessions covered:** 15  (2026-04-15 → 2026-07-22)
- **Total domains registered:** 3,367
- **Avg domains/session:** 224.5
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 9.3
- **Market concentration HHI:** 4,449.8

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 2,103 | 62.46% | 15 | 9981.6 |
| BareMetal.com inc | 753 | 22.36% | 15 | 12115.1 |
| MyID.ca INC. | 183 | 5.44% | 14 | 8967.5 |
| Webnames.ca Inc. | 107 | 3.18% | 15 | 81579.1 |
| Register.ca Inc. | 77 | 2.29% | 12 | 3265.0 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 46 | 1.37% | 13 | 33480.5 |
| Grape Inc. | 29 | 0.86% | 12 | 1429.9 |
| DomainePlus.com (3612040 CANADA inc.) | 22 | 0.65% | 12 | 4218.0 |
| Namespro Solutions Inc. | 16 | 0.48% | 8 | 26667.5 |
| PlanetHoster | 15 | 0.45% | 10 | 1388.0 |
| easyDNS Technologies Inc. | 11 | 0.33% | 8 | 10928.4 |
| CanSpace Solutions Inc. | 3 | 0.09% | 3 | 160067.3 |
| FastWebServer Internet Services Inc. | 2 | 0.06% | 2 | 3029.5 |

![Last 26 Weeks Market Share](charts/last_26_weeks_market_share.png)


---

### Last 52 Weeks

- **Sessions covered:** 15  (2026-04-15 → 2026-07-22)
- **Total domains registered:** 3,367
- **Avg domains/session:** 224.5
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 9.3
- **Market concentration HHI:** 4,449.8

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 2,103 | 62.46% | 15 | 9981.6 |
| BareMetal.com inc | 753 | 22.36% | 15 | 12115.1 |
| MyID.ca INC. | 183 | 5.44% | 14 | 8967.5 |
| Webnames.ca Inc. | 107 | 3.18% | 15 | 81579.1 |
| Register.ca Inc. | 77 | 2.29% | 12 | 3265.0 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 46 | 1.37% | 13 | 33480.5 |
| Grape Inc. | 29 | 0.86% | 12 | 1429.9 |
| DomainePlus.com (3612040 CANADA inc.) | 22 | 0.65% | 12 | 4218.0 |
| Namespro Solutions Inc. | 16 | 0.48% | 8 | 26667.5 |
| PlanetHoster | 15 | 0.45% | 10 | 1388.0 |
| easyDNS Technologies Inc. | 11 | 0.33% | 8 | 10928.4 |
| CanSpace Solutions Inc. | 3 | 0.09% | 3 | 160067.3 |
| FastWebServer Internet Services Inc. | 2 | 0.06% | 2 | 3029.5 |

![Last 52 Weeks Market Share](charts/last_52_weeks_market_share.png)


---

## All Time

- **Sessions covered:** 15  (2026-04-15 → 2026-07-22)
- **Total domains registered:** 3,367
- **Avg domains/session:** 224.5
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 9.3
- **Market concentration HHI:** 4,449.8

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 2,103 | 62.46% | 15 | 9981.6 |
| BareMetal.com inc | 753 | 22.36% | 15 | 12115.1 |
| MyID.ca INC. | 183 | 5.44% | 14 | 8967.5 |
| Webnames.ca Inc. | 107 | 3.18% | 15 | 81579.1 |
| Register.ca Inc. | 77 | 2.29% | 12 | 3265.0 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 46 | 1.37% | 13 | 33480.5 |
| Grape Inc. | 29 | 0.86% | 12 | 1429.9 |
| DomainePlus.com (3612040 CANADA inc.) | 22 | 0.65% | 12 | 4218.0 |
| Namespro Solutions Inc. | 16 | 0.48% | 8 | 26667.5 |
| PlanetHoster | 15 | 0.45% | 10 | 1388.0 |
| easyDNS Technologies Inc. | 11 | 0.33% | 8 | 10928.4 |
| CanSpace Solutions Inc. | 3 | 0.09% | 3 | 160067.3 |
| FastWebServer Internet Services Inc. | 2 | 0.06% | 2 | 3029.5 |

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

- **Sessions covered:** 15  (2026-04-15 → 2026-07-22)
- **Total domains registered:** 3,367
- **Avg domains/session:** 224.5
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 9.3
- **Market concentration HHI:** 4,449.8

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 2,103 | 62.46% | 15 | 9981.6 |
| BareMetal.com inc | 753 | 22.36% | 15 | 12115.1 |
| MyID.ca INC. | 183 | 5.44% | 14 | 8967.5 |
| Webnames.ca Inc. | 107 | 3.18% | 15 | 81579.1 |
| Register.ca Inc. | 77 | 2.29% | 12 | 3265.0 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 46 | 1.37% | 13 | 33480.5 |
| Grape Inc. | 29 | 0.86% | 12 | 1429.9 |
| DomainePlus.com (3612040 CANADA inc.) | 22 | 0.65% | 12 | 4218.0 |
| Namespro Solutions Inc. | 16 | 0.48% | 8 | 26667.5 |
| PlanetHoster | 15 | 0.45% | 10 | 1388.0 |
| easyDNS Technologies Inc. | 11 | 0.33% | 8 | 10928.4 |
| CanSpace Solutions Inc. | 3 | 0.09% | 3 | 160067.3 |
| FastWebServer Internet Services Inc. | 2 | 0.06% | 2 | 3029.5 |

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

- **Sessions covered:** 4  (2026-07-01 → 2026-07-22)
- **Total domains registered:** 964
- **Avg domains/session:** 241.0
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 10.2
- **Market concentration HHI:** 4,254.5

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 584 | 60.58% | 4 | 10071.2 |
| BareMetal.com inc | 220 | 22.82% | 4 | 13984.6 |
| MyID.ca INC. | 64 | 6.64% | 4 | 3618.8 |
| Register.ca Inc. | 27 | 2.8% | 4 | 3701.7 |
| Webnames.ca Inc. | 24 | 2.49% | 4 | 79082.1 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 20 | 2.07% | 4 | 46098.1 |
| Grape Inc. | 9 | 0.93% | 3 | 2242.8 |
| DomainePlus.com (3612040 CANADA inc.) | 4 | 0.41% | 2 | 8745.8 |
| PlanetHoster | 4 | 0.41% | 4 | 588 |
| easyDNS Technologies Inc. | 3 | 0.31% | 3 | 4654.3 |
| FastWebServer Internet Services Inc. | 2 | 0.21% | 2 | 3029.5 |
| Namespro Solutions Inc. | 2 | 0.21% | 2 | 46823 |
| CanSpace Solutions Inc. | 1 | 0.1% | 1 | 549 |


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
