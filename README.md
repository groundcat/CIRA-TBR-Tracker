# CIRA TBR Tracker

> Automated archive and analytics for CIRA **To-Be-Released (TBR)** `.CA` domain
> drop sessions. Updated every **Wednesday ≈ 19:30 UTC** via GitHub Actions.

**Last updated:** 2026-05-20 &nbsp;|&nbsp; **Total sessions tracked:** 6

---

## What is TBR?

CIRA releases expired `.CA` domains every **Wednesday at 19:00 UTC** via a
first-come, first-served process. Whichever registrar submits a registration
request first wins the domain (one connection, one request per 5 s per registrar).

Capture latency is measured from the official session open at **19:00:00.000 UTC**.

---

## Last Session

- **Date:** 2026-05-20
- **Domains released:** 217
- **Domains registered:** 217
- **Registration rate:** 100.0%
- **Unique registrars:** 8
- **Session duration:** 232,435 ms
- **Market concentration (HHI):** 3,904.4

**Capture latency across all registrars:**
- Min: 69 ms | Median: 10868 ms | Mean: 23457.7 ms | P95: 152152 ms | Max: 232504 ms

**Per-registrar latency breakdown:**

| Registrar | Domains | Min (ms) | Median (ms) | Mean (ms) | P95 (ms) | Max (ms) | StdDev (ms) |
|-----------|--------:|---------:|------------:|----------:|---------:|---------:|------------:|
| WHC Online Solutions Inc. | 125 | 69 | 10793 | 9633.4 | 16245 | 16306 | 5114.4 |
| BareMetal.com inc | 44 | 70 | 11396 | 11406.9 | 20041 | 20071 | 5572.7 |
| Webnames.ca Inc. | 22 | 16518 | 149646 | 140043.1 | 227407 | 232504 | 69074.9 |
| MyID.ca INC. | 18 | 4904 | 5151 | 7216.7 | 10018 | 10018 | 2544.5 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 3 | 121 | 32014 | 53930.7 | 129657 | 129657 | 67491.8 |
| DomainePlus.com (3612040 CANADA inc.) | 2 | 108 | 111 | 111.5 | 115 | 115 | 4.9 |
| PlanetHoster | 2 | 4966 | 4998 | 4998.5 | 5031 | 5031 | 46.0 |
| easyDNS Technologies Inc. | 1 | 1381 | 1381 | 1381 | 1381 | 1381 | 0 |

**Timing distribution (captures by second offset from 19:00:00 UTC):**

| Offset (s) | Domains Captured |
|-----------:|-----------------:|
| +0 | 21 |
| +1 | 3 |
| +4 | 15 |
| +5 | 21 |
| +6 | 11 |
| +7 | 2 |
| +9 | 11 |
| +10 | 27 |
| +11 | 24 |
| +12 | 6 |
| +15 | 29 |
| +16 | 19 |
| +17 | 1 |
| +20 | 4 |
| +21 | 1 |
| +31 | 1 |
| +32 | 1 |
| +36 | 1 |
| +51 | 1 |
| +106 | 1 |
| +127 | 1 |
| +129 | 1 |
| +132 | 1 |
| +137 | 1 |
| +142 | 1 |
| +147 | 1 |
| +152 | 1 |
| +157 | 1 |
| +162 | 1 |
| +182 | 1 |
| +192 | 1 |
| +197 | 1 |
| +202 | 1 |
| +207 | 1 |
| +217 | 1 |
| +227 | 1 |
| +232 | 1 |

![Last Session Market Share](charts/last_session_market_share.png)


![Last Session Latency Distribution](charts/last_session_latency_histogram.png)


![Last Session Latency by Registrar](charts/last_session_latency_by_registrar.png)


![Last Session Timing Distribution](charts/last_session_timing_distribution.png)


---

## Rolling Windows

### Last 4 Sessions

- **Sessions covered:** 4  (2026-04-29 → 2026-05-20)
- **Total domains registered:** 992
- **Avg domains/session:** 248.0
- **Unique registrars (ever active):** 12
- **Avg registrars/session:** 9
- **Market concentration HHI:** 4,848.9

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 653 | 65.83% | 4 | 10615.8 |
| BareMetal.com inc | 218 | 21.98% | 4 | 13128.4 |
| Webnames.ca Inc. | 44 | 4.44% | 4 | 89801.7 |
| MyID.ca INC. | 30 | 3.02% | 3 | 5075.7 |
| Register.ca Inc. | 11 | 1.11% | 1 | 1752.6 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 8 | 0.81% | 3 | 42726.4 |
| DomainePlus.com (3612040 CANADA inc.) | 7 | 0.71% | 4 | 2368.6 |
| Namespro Solutions Inc. | 5 | 0.5% | 2 | 28960.6 |
| PlanetHoster | 5 | 0.5% | 3 | 1888.0 |
| Grape Inc. | 5 | 0.5% | 3 | 66 |
| easyDNS Technologies Inc. | 4 | 0.4% | 3 | 10534.2 |
| CanSpace Solutions Inc. | 2 | 0.2% | 2 | 239826.5 |

![Last 4 Sessions Market Share](charts/last_4_sessions_market_share.png)


---

### Last ~6 Months (26 Weeks)

- **Sessions covered:** 6  (2026-04-15 → 2026-05-20)
- **Total domains registered:** 1,441
- **Avg domains/session:** 240.2
- **Unique registrars (ever active):** 12
- **Avg registrars/session:** 9.2
- **Market concentration HHI:** 4,783.8

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 943 | 65.44% | 6 | 10690.5 |
| BareMetal.com inc | 311 | 21.58% | 6 | 12653.1 |
| Webnames.ca Inc. | 62 | 4.3% | 6 | 101218.4 |
| MyID.ca INC. | 53 | 3.68% | 5 | 4951.7 |
| Register.ca Inc. | 14 | 0.97% | 3 | 3931.4 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 13 | 0.9% | 5 | 33278.3 |
| DomainePlus.com (3612040 CANADA inc.) | 12 | 0.83% | 6 | 3281.2 |
| Grape Inc. | 11 | 0.76% | 5 | 1074.7 |
| Namespro Solutions Inc. | 7 | 0.49% | 3 | 23383.4 |
| PlanetHoster | 7 | 0.49% | 4 | 2596.0 |
| easyDNS Technologies Inc. | 6 | 0.42% | 4 | 10854.1 |
| CanSpace Solutions Inc. | 2 | 0.14% | 2 | 239826.5 |

![Last 26 Weeks Market Share](charts/last_26_weeks_market_share.png)


---

### Last 52 Weeks

- **Sessions covered:** 6  (2026-04-15 → 2026-05-20)
- **Total domains registered:** 1,441
- **Avg domains/session:** 240.2
- **Unique registrars (ever active):** 12
- **Avg registrars/session:** 9.2
- **Market concentration HHI:** 4,783.8

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 943 | 65.44% | 6 | 10690.5 |
| BareMetal.com inc | 311 | 21.58% | 6 | 12653.1 |
| Webnames.ca Inc. | 62 | 4.3% | 6 | 101218.4 |
| MyID.ca INC. | 53 | 3.68% | 5 | 4951.7 |
| Register.ca Inc. | 14 | 0.97% | 3 | 3931.4 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 13 | 0.9% | 5 | 33278.3 |
| DomainePlus.com (3612040 CANADA inc.) | 12 | 0.83% | 6 | 3281.2 |
| Grape Inc. | 11 | 0.76% | 5 | 1074.7 |
| Namespro Solutions Inc. | 7 | 0.49% | 3 | 23383.4 |
| PlanetHoster | 7 | 0.49% | 4 | 2596.0 |
| easyDNS Technologies Inc. | 6 | 0.42% | 4 | 10854.1 |
| CanSpace Solutions Inc. | 2 | 0.14% | 2 | 239826.5 |

![Last 52 Weeks Market Share](charts/last_52_weeks_market_share.png)


---

## All Time

- **Sessions covered:** 6  (2026-04-15 → 2026-05-20)
- **Total domains registered:** 1,441
- **Avg domains/session:** 240.2
- **Unique registrars (ever active):** 12
- **Avg registrars/session:** 9.2
- **Market concentration HHI:** 4,783.8

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 943 | 65.44% | 6 | 10690.5 |
| BareMetal.com inc | 311 | 21.58% | 6 | 12653.1 |
| Webnames.ca Inc. | 62 | 4.3% | 6 | 101218.4 |
| MyID.ca INC. | 53 | 3.68% | 5 | 4951.7 |
| Register.ca Inc. | 14 | 0.97% | 3 | 3931.4 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 13 | 0.9% | 5 | 33278.3 |
| DomainePlus.com (3612040 CANADA inc.) | 12 | 0.83% | 6 | 3281.2 |
| Grape Inc. | 11 | 0.76% | 5 | 1074.7 |
| Namespro Solutions Inc. | 7 | 0.49% | 3 | 23383.4 |
| PlanetHoster | 7 | 0.49% | 4 | 2596.0 |
| easyDNS Technologies Inc. | 6 | 0.42% | 4 | 10854.1 |
| CanSpace Solutions Inc. | 2 | 0.14% | 2 | 239826.5 |

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

- **Sessions covered:** 6  (2026-04-15 → 2026-05-20)
- **Total domains registered:** 1,441
- **Avg domains/session:** 240.2
- **Unique registrars (ever active):** 12
- **Avg registrars/session:** 9.2
- **Market concentration HHI:** 4,783.8

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 943 | 65.44% | 6 | 10690.5 |
| BareMetal.com inc | 311 | 21.58% | 6 | 12653.1 |
| Webnames.ca Inc. | 62 | 4.3% | 6 | 101218.4 |
| MyID.ca INC. | 53 | 3.68% | 5 | 4951.7 |
| Register.ca Inc. | 14 | 0.97% | 3 | 3931.4 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 13 | 0.9% | 5 | 33278.3 |
| DomainePlus.com (3612040 CANADA inc.) | 12 | 0.83% | 6 | 3281.2 |
| Grape Inc. | 11 | 0.76% | 5 | 1074.7 |
| Namespro Solutions Inc. | 7 | 0.49% | 3 | 23383.4 |
| PlanetHoster | 7 | 0.49% | 4 | 2596.0 |
| easyDNS Technologies Inc. | 6 | 0.42% | 4 | 10854.1 |
| CanSpace Solutions Inc. | 2 | 0.14% | 2 | 239826.5 |

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

- **Sessions covered:** 3  (2026-05-06 → 2026-05-20)
- **Total domains registered:** 695
- **Avg domains/session:** 231.7
- **Unique registrars (ever active):** 12
- **Avg registrars/session:** 8.3
- **Market concentration HHI:** 4,494.5

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 431 | 62.01% | 3 | 9689.9 |
| BareMetal.com inc | 171 | 24.6% | 3 | 13167.3 |
| Webnames.ca Inc. | 38 | 5.47% | 3 | 111409.1 |
| MyID.ca INC. | 22 | 3.17% | 2 | 4410.9 |
| Register.ca Inc. | 11 | 1.58% | 1 | 1752.6 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 5 | 0.72% | 2 | 47995.1 |
| Grape Inc. | 4 | 0.58% | 2 | 53.5 |
| DomainePlus.com (3612040 CANADA inc.) | 4 | 0.58% | 3 | 970.5 |
| PlanetHoster | 3 | 0.43% | 2 | 2718.8 |
| easyDNS Technologies Inc. | 3 | 0.43% | 2 | 12175.8 |
| Namespro Solutions Inc. | 2 | 0.29% | 1 | 27678.5 |
| CanSpace Solutions Inc. | 1 | 0.14% | 1 | 7370 |


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
