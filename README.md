# CIRA TBR Tracker

> Automated archive and analytics for CIRA **To-Be-Released (TBR)** `.CA` domain
> drop sessions. Updated every **Wednesday ≈ 19:30 UTC** via GitHub Actions.

**Last updated:** 2026-05-06 &nbsp;|&nbsp; **Total sessions tracked:** 4

---

## What is TBR?

CIRA releases expired `.CA` domains every **Wednesday at 19:00 UTC** via a
first-come, first-served process. Whichever registrar submits a registration
request first wins the domain (one connection, one request per 5 s per registrar).

Capture latency is measured from the official session open at **19:00:00.000 UTC**.

---

## Last Session

- **Date:** 2026-05-06
- **Domains released:** 238
- **Domains registered:** 238
- **Registration rate:** 100.0%
- **Unique registrars:** 8
- **Session duration:** 184,056 ms
- **Market concentration (HHI):** 5,021.3

**Capture latency across all registrars:**
- Min: 63 ms | Median: 10728 ms | Mean: 15706.6 ms | P95: 55170 ms | Max: 184119 ms

**Per-registrar latency breakdown:**

| Registrar | Domains | Min (ms) | Median (ms) | Mean (ms) | P95 (ms) | Max (ms) | StdDev (ms) |
|-----------|--------:|---------:|------------:|----------:|---------:|---------:|------------:|
| WHC Online Solutions Inc. | 156 | 90 | 10364 | 8953.9 | 16434 | 16696 | 5187.0 |
| BareMetal.com inc | 63 | 91 | 15249 | 13934.9 | 20750 | 25134 | 6318.4 |
| Webnames.ca Inc. | 11 | 73682 | 113823 | 120217.1 | 184119 | 184119 | 36408.6 |
| Grape Inc. | 2 | 63 | 75 | 75 | 87 | 87 | 17.0 |
| Namespro Solutions Inc. | 2 | 24683 | 27678 | 27678.5 | 30674 | 30674 | 4236.3 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 2 | 28949 | 42059 | 42059.5 | 55170 | 55170 | 18541.0 |
| PlanetHoster | 1 | 439 | 439 | 439 | 439 | 439 | 0 |
| DomainePlus.com (3612040 CANADA inc.) | 1 | 1006 | 1006 | 1006 | 1006 | 1006 | 0 |

**Timing distribution (captures by second offset from 19:00:00 UTC):**

| Offset (s) | Domains Captured |
|-----------:|-----------------:|
| +0 | 27 |
| +1 | 4 |
| +5 | 36 |
| +6 | 21 |
| +8 | 1 |
| +10 | 34 |
| +11 | 26 |
| +12 | 1 |
| +13 | 1 |
| +15 | 36 |
| +16 | 15 |
| +20 | 19 |
| +24 | 1 |
| +25 | 2 |
| +28 | 1 |
| +30 | 1 |
| +55 | 1 |
| +73 | 1 |
| +78 | 1 |
| +83 | 1 |
| +98 | 1 |
| +108 | 1 |
| +113 | 1 |
| +123 | 1 |
| +143 | 1 |
| +148 | 1 |
| +164 | 1 |
| +184 | 1 |

![Last Session Market Share](charts/last_session_market_share.png)


![Last Session Latency Distribution](charts/last_session_latency_histogram.png)


![Last Session Latency by Registrar](charts/last_session_latency_by_registrar.png)


![Last Session Timing Distribution](charts/last_session_timing_distribution.png)


---

## Rolling Windows

### Last 4 Sessions

- **Sessions covered:** 4  (2026-04-15 → 2026-05-06)
- **Total domains registered:** 984
- **Avg domains/session:** 246.0
- **Unique registrars (ever active):** 12
- **Avg registrars/session:** 9.5
- **Market concentration HHI:** 5,060.9

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 668 | 67.89% | 4 | 11006.7 |
| BareMetal.com inc | 203 | 20.63% | 4 | 12587.9 |
| Webnames.ca Inc. | 35 | 3.56% | 4 | 98325.1 |
| MyID.ca INC. | 31 | 3.15% | 3 | 5312.3 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 10 | 1.02% | 4 | 28115.2 |
| Grape Inc. | 9 | 0.91% | 4 | 1335.3 |
| DomainePlus.com (3612040 CANADA inc.) | 9 | 0.91% | 4 | 4445.5 |
| Namespro Solutions Inc. | 7 | 0.71% | 3 | 23383.4 |
| PlanetHoster | 5 | 0.51% | 3 | 1795.2 |
| easyDNS Technologies Inc. | 3 | 0.3% | 2 | 9532.5 |
| Register.ca Inc. | 3 | 0.3% | 2 | 5020.8 |
| CanSpace Solutions Inc. | 1 | 0.1% | 1 | 472283 |

![Last 4 Sessions Market Share](charts/last_4_sessions_market_share.png)


---

### Last ~6 Months (26 Weeks)

- **Sessions covered:** 4  (2026-04-15 → 2026-05-06)
- **Total domains registered:** 984
- **Avg domains/session:** 246.0
- **Unique registrars (ever active):** 12
- **Avg registrars/session:** 9.5
- **Market concentration HHI:** 5,060.9

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 668 | 67.89% | 4 | 11006.7 |
| BareMetal.com inc | 203 | 20.63% | 4 | 12587.9 |
| Webnames.ca Inc. | 35 | 3.56% | 4 | 98325.1 |
| MyID.ca INC. | 31 | 3.15% | 3 | 5312.3 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 10 | 1.02% | 4 | 28115.2 |
| Grape Inc. | 9 | 0.91% | 4 | 1335.3 |
| DomainePlus.com (3612040 CANADA inc.) | 9 | 0.91% | 4 | 4445.5 |
| Namespro Solutions Inc. | 7 | 0.71% | 3 | 23383.4 |
| PlanetHoster | 5 | 0.51% | 3 | 1795.2 |
| easyDNS Technologies Inc. | 3 | 0.3% | 2 | 9532.5 |
| Register.ca Inc. | 3 | 0.3% | 2 | 5020.8 |
| CanSpace Solutions Inc. | 1 | 0.1% | 1 | 472283 |

![Last 26 Weeks Market Share](charts/last_26_weeks_market_share.png)


---

### Last 52 Weeks

- **Sessions covered:** 4  (2026-04-15 → 2026-05-06)
- **Total domains registered:** 984
- **Avg domains/session:** 246.0
- **Unique registrars (ever active):** 12
- **Avg registrars/session:** 9.5
- **Market concentration HHI:** 5,060.9

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 668 | 67.89% | 4 | 11006.7 |
| BareMetal.com inc | 203 | 20.63% | 4 | 12587.9 |
| Webnames.ca Inc. | 35 | 3.56% | 4 | 98325.1 |
| MyID.ca INC. | 31 | 3.15% | 3 | 5312.3 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 10 | 1.02% | 4 | 28115.2 |
| Grape Inc. | 9 | 0.91% | 4 | 1335.3 |
| DomainePlus.com (3612040 CANADA inc.) | 9 | 0.91% | 4 | 4445.5 |
| Namespro Solutions Inc. | 7 | 0.71% | 3 | 23383.4 |
| PlanetHoster | 5 | 0.51% | 3 | 1795.2 |
| easyDNS Technologies Inc. | 3 | 0.3% | 2 | 9532.5 |
| Register.ca Inc. | 3 | 0.3% | 2 | 5020.8 |
| CanSpace Solutions Inc. | 1 | 0.1% | 1 | 472283 |

![Last 52 Weeks Market Share](charts/last_52_weeks_market_share.png)


---

## All Time

- **Sessions covered:** 4  (2026-04-15 → 2026-05-06)
- **Total domains registered:** 984
- **Avg domains/session:** 246.0
- **Unique registrars (ever active):** 12
- **Avg registrars/session:** 9.5
- **Market concentration HHI:** 5,060.9

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 668 | 67.89% | 4 | 11006.7 |
| BareMetal.com inc | 203 | 20.63% | 4 | 12587.9 |
| Webnames.ca Inc. | 35 | 3.56% | 4 | 98325.1 |
| MyID.ca INC. | 31 | 3.15% | 3 | 5312.3 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 10 | 1.02% | 4 | 28115.2 |
| Grape Inc. | 9 | 0.91% | 4 | 1335.3 |
| DomainePlus.com (3612040 CANADA inc.) | 9 | 0.91% | 4 | 4445.5 |
| Namespro Solutions Inc. | 7 | 0.71% | 3 | 23383.4 |
| PlanetHoster | 5 | 0.51% | 3 | 1795.2 |
| easyDNS Technologies Inc. | 3 | 0.3% | 2 | 9532.5 |
| Register.ca Inc. | 3 | 0.3% | 2 | 5020.8 |
| CanSpace Solutions Inc. | 1 | 0.1% | 1 | 472283 |

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

- **Sessions covered:** 4  (2026-04-15 → 2026-05-06)
- **Total domains registered:** 984
- **Avg domains/session:** 246.0
- **Unique registrars (ever active):** 12
- **Avg registrars/session:** 9.5
- **Market concentration HHI:** 5,060.9

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 668 | 67.89% | 4 | 11006.7 |
| BareMetal.com inc | 203 | 20.63% | 4 | 12587.9 |
| Webnames.ca Inc. | 35 | 3.56% | 4 | 98325.1 |
| MyID.ca INC. | 31 | 3.15% | 3 | 5312.3 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 10 | 1.02% | 4 | 28115.2 |
| Grape Inc. | 9 | 0.91% | 4 | 1335.3 |
| DomainePlus.com (3612040 CANADA inc.) | 9 | 0.91% | 4 | 4445.5 |
| Namespro Solutions Inc. | 7 | 0.71% | 3 | 23383.4 |
| PlanetHoster | 5 | 0.51% | 3 | 1795.2 |
| easyDNS Technologies Inc. | 3 | 0.3% | 2 | 9532.5 |
| Register.ca Inc. | 3 | 0.3% | 2 | 5020.8 |
| CanSpace Solutions Inc. | 1 | 0.1% | 1 | 472283 |

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

- **Sessions covered:** 1  (2026-05-06 → 2026-05-06)
- **Total domains registered:** 238
- **Avg domains/session:** 238.0
- **Unique registrars (ever active):** 8
- **Avg registrars/session:** 8
- **Market concentration HHI:** 5,021.3

| Registrar | Domains | Share | Sessions Active | Mean Latency (ms) |
|-----------|--------:|------:|----------------:|------------------:|
| WHC Online Solutions Inc. | 156 | 65.55% | 1 | 8953.9 |
| BareMetal.com inc | 63 | 26.47% | 1 | 13934.9 |
| Webnames.ca Inc. | 11 | 4.62% | 1 | 120217.1 |
| Grape Inc. | 2 | 0.84% | 1 | 75 |
| Namespro Solutions Inc. | 2 | 0.84% | 1 | 27678.5 |
| 8648255 CANADA LTD. O/A Dynadot LLC | 2 | 0.84% | 1 | 42059.5 |
| PlanetHoster | 1 | 0.42% | 1 | 439 |
| DomainePlus.com (3612040 CANADA inc.) | 1 | 0.42% | 1 | 1006 |


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
