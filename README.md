# CIRA TBR Tracker

> Automated archive and analytics for CIRA **To-Be-Released (TBR)** `.CA` domain
> drop sessions. Updated every **Wednesday ≈ 19:30 UTC** via GitHub Actions.

**Last updated:** 2026-07-01 &nbsp;|&nbsp; **Total sessions tracked:** 12

---

## What is TBR?

CIRA releases expired `.CA` domains every **Wednesday at 19:00 UTC** via a
first-come, first-served process. Whichever registrar submits a registration
request first wins the domain (one connection, one request per 5 s per registrar).

Capture latency is measured from the official session open at **19:00:00.000 UTC**.

---

## Last Session

- **Date:** 2026-07-01
- **Domains released:** 243
- **Domains registered:** 243
- **Registration rate:** 100.0%
- **Unique registrars:** 13
- **Session duration:** 165,973 ms
- **Market concentration (HHI):** 4,527.7

**Capture latency across all registrars:**
- Min: 1 ms | Median: 12611 ms | Mean: 13249.4 ms | P95: 23132 ms | Max: 165974 ms

**Per-registrar latency breakdown:**

| Registrar | Domains | Min (ms) | Median (ms) | Mean (ms) | P95 (ms) | Max (ms) | StdDev (ms) |
|-----------|--------:|---------:|------------:|----------:|---------:|---------:|------------:|
| WHC Online Solutions Inc. | 153 | 1 | 11710 | 11920.8 | 20077 | 20656 | 5677.5 |
| BareMetal.com inc | 56 | 1 | 15220 | 14664.1 | 23600 | 23670 | 6943.6 |
| MyID.ca INC. | 9 | 13 | 4917 | 3710.9 | 7884 | 7884 | 3256.2 |
| Register.ca Inc. | 8 | 7 | 2549 | 2727.6 | 5680 | 5680 | 2855.3 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 5 | 1353 | 16897 | 18153.6 | 33597 | 33597 | 12894.6 |
| Grape Inc. | 3 | 2 | 6 | 1681 | 5035 | 5035 | 2904.6 |
| DomainePlus.com (3612040 CANADA inc.) | 2 | 1465 | 13322 | 13322.5 | 25180 | 25180 | 16769.0 |
| Webnames.ca Inc. | 2 | 135886 | 150930 | 150930 | 165974 | 165974 | 21275.4 |
| PlanetHoster | 1 | 325 | 325 | 325 | 325 | 325 | 0 |
| CanSpace Solutions Inc. | 1 | 549 | 549 | 549 | 549 | 549 | 0 |
| easyDNS Technologies Inc. | 1 | 1064 | 1064 | 1064 | 1064 | 1064 | 0 |
| FastWebServer Internet Services Inc. | 1 | 6050 | 6050 | 6050 | 6050 | 6050 | 0 |
| Namespro Solutions Inc. | 1 | 87000 | 87000 | 87000 | 87000 | 87000 | 0 |

**Timing distribution (captures by second offset from 19:00:00 UTC):**

| Offset (s) | Domains Captured |
|-----------:|-----------------:|
| +0 | 24 |
| +1 | 9 |
| +2 | 1 |
| +4 | 6 |
| +5 | 16 |
| +6 | 13 |
| +7 | 2 |
| +8 | 8 |
| +9 | 12 |
| +10 | 14 |
| +11 | 15 |
| +12 | 2 |
| +13 | 13 |
| +14 | 14 |
| +15 | 20 |
| +16 | 15 |
| +17 | 1 |
| +18 | 14 |
| +19 | 11 |
| +20 | 19 |
| +22 | 1 |
| +23 | 7 |
| +25 | 1 |
| +27 | 1 |
| +33 | 1 |
| +87 | 1 |
| +135 | 1 |
| +165 | 1 |

![Last Session Market Share](charts/last_session_market_share.png)


![Last Session Latency Distribution](charts/last_session_latency_histogram.png)


![Last Session Latency by Registrar](charts/last_session_latency_by_registrar.png)


![Last Session Timing Distribution](charts/last_session_timing_distribution.png)


---

## Rolling Windows

### Last 4 Sessions

- **Sessions covered:** 4  (2026-06-10 → 2026-07-01)
- **Total domains registered:** 871
- **Avg domains/session:** 217.8
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 9.5
- **Market concentration HHI:** 4,363.4

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 535 | 61.42% | 4 | 10231.1 |
| BareMetal.com inc | 203 | 23.31% | 4 | 12028.0 |
| MyID.ca INC. | 46 | 5.28% | 4 | 12449.0 |
| Register.ca Inc. | 28 | 3.21% | 4 | 2929.2 |
| Webnames.ca Inc. | 17 | 1.95% | 4 | 90807.1 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 16 | 1.84% | 4 | 19190.6 |
| Grape Inc. | 10 | 1.15% | 3 | 2217.4 |
| DomainePlus.com (3612040 CANADA inc.) | 7 | 0.8% | 4 | 6682.0 |
| PlanetHoster | 3 | 0.34% | 2 | 183.2 |
| Namespro Solutions Inc. | 3 | 0.34% | 2 | 48106.2 |
| CanSpace Solutions Inc. | 1 | 0.11% | 1 | 549 |
| easyDNS Technologies Inc. | 1 | 0.11% | 1 | 1064 |
| FastWebServer Internet Services Inc. | 1 | 0.11% | 1 | 6050 |

![Last 4 Sessions Market Share](charts/last_4_sessions_market_share.png)


---

### Last ~6 Months (26 Weeks)

- **Sessions covered:** 12  (2026-04-15 → 2026-07-01)
- **Total domains registered:** 2,646
- **Avg domains/session:** 220.5
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 9.2
- **Market concentration HHI:** 4,530.4

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 1,672 | 63.19% | 12 | 10113.3 |
| BareMetal.com inc | 589 | 22.26% | 12 | 11704.3 |
| MyID.ca INC. | 128 | 4.84% | 11 | 10434.6 |
| Webnames.ca Inc. | 85 | 3.21% | 12 | 88190.7 |
| Register.ca Inc. | 58 | 2.19% | 9 | 3011.2 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 31 | 1.17% | 10 | 26900.8 |
| Grape Inc. | 23 | 0.87% | 10 | 1211.1 |
| DomainePlus.com (3612040 CANADA inc.) | 20 | 0.76% | 11 | 4222.5 |
| Namespro Solutions Inc. | 15 | 0.57% | 7 | 29527.7 |
| PlanetHoster | 12 | 0.45% | 7 | 1693.2 |
| easyDNS Technologies Inc. | 9 | 0.34% | 6 | 12421.3 |
| CanSpace Solutions Inc. | 3 | 0.11% | 3 | 160067.3 |
| FastWebServer Internet Services Inc. | 1 | 0.04% | 1 | 6050 |

![Last 26 Weeks Market Share](charts/last_26_weeks_market_share.png)


---

### Last 52 Weeks

- **Sessions covered:** 12  (2026-04-15 → 2026-07-01)
- **Total domains registered:** 2,646
- **Avg domains/session:** 220.5
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 9.2
- **Market concentration HHI:** 4,530.4

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 1,672 | 63.19% | 12 | 10113.3 |
| BareMetal.com inc | 589 | 22.26% | 12 | 11704.3 |
| MyID.ca INC. | 128 | 4.84% | 11 | 10434.6 |
| Webnames.ca Inc. | 85 | 3.21% | 12 | 88190.7 |
| Register.ca Inc. | 58 | 2.19% | 9 | 3011.2 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 31 | 1.17% | 10 | 26900.8 |
| Grape Inc. | 23 | 0.87% | 10 | 1211.1 |
| DomainePlus.com (3612040 CANADA inc.) | 20 | 0.76% | 11 | 4222.5 |
| Namespro Solutions Inc. | 15 | 0.57% | 7 | 29527.7 |
| PlanetHoster | 12 | 0.45% | 7 | 1693.2 |
| easyDNS Technologies Inc. | 9 | 0.34% | 6 | 12421.3 |
| CanSpace Solutions Inc. | 3 | 0.11% | 3 | 160067.3 |
| FastWebServer Internet Services Inc. | 1 | 0.04% | 1 | 6050 |

![Last 52 Weeks Market Share](charts/last_52_weeks_market_share.png)


---

## All Time

- **Sessions covered:** 12  (2026-04-15 → 2026-07-01)
- **Total domains registered:** 2,646
- **Avg domains/session:** 220.5
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 9.2
- **Market concentration HHI:** 4,530.4

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 1,672 | 63.19% | 12 | 10113.3 |
| BareMetal.com inc | 589 | 22.26% | 12 | 11704.3 |
| MyID.ca INC. | 128 | 4.84% | 11 | 10434.6 |
| Webnames.ca Inc. | 85 | 3.21% | 12 | 88190.7 |
| Register.ca Inc. | 58 | 2.19% | 9 | 3011.2 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 31 | 1.17% | 10 | 26900.8 |
| Grape Inc. | 23 | 0.87% | 10 | 1211.1 |
| DomainePlus.com (3612040 CANADA inc.) | 20 | 0.76% | 11 | 4222.5 |
| Namespro Solutions Inc. | 15 | 0.57% | 7 | 29527.7 |
| PlanetHoster | 12 | 0.45% | 7 | 1693.2 |
| easyDNS Technologies Inc. | 9 | 0.34% | 6 | 12421.3 |
| CanSpace Solutions Inc. | 3 | 0.11% | 3 | 160067.3 |
| FastWebServer Internet Services Inc. | 1 | 0.04% | 1 | 6050 |

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

- **Sessions covered:** 12  (2026-04-15 → 2026-07-01)
- **Total domains registered:** 2,646
- **Avg domains/session:** 220.5
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 9.2
- **Market concentration HHI:** 4,530.4

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 1,672 | 63.19% | 12 | 10113.3 |
| BareMetal.com inc | 589 | 22.26% | 12 | 11704.3 |
| MyID.ca INC. | 128 | 4.84% | 11 | 10434.6 |
| Webnames.ca Inc. | 85 | 3.21% | 12 | 88190.7 |
| Register.ca Inc. | 58 | 2.19% | 9 | 3011.2 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 31 | 1.17% | 10 | 26900.8 |
| Grape Inc. | 23 | 0.87% | 10 | 1211.1 |
| DomainePlus.com (3612040 CANADA inc.) | 20 | 0.76% | 11 | 4222.5 |
| Namespro Solutions Inc. | 15 | 0.57% | 7 | 29527.7 |
| PlanetHoster | 12 | 0.45% | 7 | 1693.2 |
| easyDNS Technologies Inc. | 9 | 0.34% | 6 | 12421.3 |
| CanSpace Solutions Inc. | 3 | 0.11% | 3 | 160067.3 |
| FastWebServer Internet Services Inc. | 1 | 0.04% | 1 | 6050 |

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

- **Sessions covered:** 1  (2026-07-01 → 2026-07-01)
- **Total domains registered:** 243
- **Avg domains/session:** 243.0
- **Unique registrars (ever active):** 13
- **Avg registrars/session:** 13
- **Market concentration HHI:** 4,527.7

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 153 | 62.96% | 1 | 11920.8 |
| BareMetal.com inc | 56 | 23.05% | 1 | 14664.1 |
| MyID.ca INC. | 9 | 3.7% | 1 | 3710.9 |
| Register.ca Inc. | 8 | 3.29% | 1 | 2727.6 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 5 | 2.06% | 1 | 18153.6 |
| Grape Inc. | 3 | 1.23% | 1 | 1681 |
| DomainePlus.com (3612040 CANADA inc.) | 2 | 0.82% | 1 | 13322.5 |
| Webnames.ca Inc. | 2 | 0.82% | 1 | 150930 |
| PlanetHoster | 1 | 0.41% | 1 | 325 |
| CanSpace Solutions Inc. | 1 | 0.41% | 1 | 549 |
| easyDNS Technologies Inc. | 1 | 0.41% | 1 | 1064 |
| FastWebServer Internet Services Inc. | 1 | 0.41% | 1 | 6050 |
| Namespro Solutions Inc. | 1 | 0.41% | 1 | 87000 |


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
