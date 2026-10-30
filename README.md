# Event Capacity Intelligence

A data-driven event capacity planning dashboard that helps event organizers estimate attendance, identify venue capacity risks, and make better registration decisions.

## Dashboard Preview

The project includes a PDF dashboard demonstrating the event capacity analysis, registration planning, risk classification, and attendance scenarios.

**[View the Event Capacity Intelligence Dashboard PDF](Event-Capacity-Intelligence-Dashboard.pdf)**

---

## 1. Business Problem

Event organizers sometimes accept more registrations than their venue can safely accommodate.

However, not every registered attendee will attend the event. This creates a planning challenge:

- Too many registrations can lead to overcrowding.
- Too few registrations can result in unused venue capacity.
- Organizers need a practical way to estimate attendance before an event takes place.

**Event Capacity Intelligence** addresses this challenge by combining event data, expected show-up rates, and safety buffers to provide registration recommendations.

---

## 2. Project Objectives

- Monitor event registrations and attendance.
- Compare actual attendance with venue capacity.
- Calculate a recommended registration limit.
- Identify events with high capacity utilization.
- Compare low, expected, and high attendance scenarios.
- Provide clear, rule-based business insights.

---

## 3. Dashboard Features

### Event Overview

The dashboard provides:

- Total number of events
- High-risk events
- Events exceeding venue capacity
- Average show-up rate

### Capacity Calculator

Users can enter:

- Venue capacity
- Number of registrations
- Expected show-up rate
- Safety buffer

The calculator returns:

- Recommended registration cap
- Safe planning target
- Estimated attendance
- Difference from the safe planning target
- Capacity risk classification

### Attendance Scenario Comparison

The dashboard compares three illustrative scenarios:

- **Low attendance:** show-up rate reduced by 5 percentage points
- **Expected attendance:** selected show-up rate
- **High attendance:** show-up rate increased by 5 percentage points

### Data Visualizations

The dashboard includes:

- Capacity utilization by event
- Actual attendance versus venue capacity
- Business insights generated from event data

---

## 4. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend logic and calculations |
| Flask | REST API and application server |
| MySQL | Event data storage |
| HTML | Dashboard structure |
| CSS | Dashboard styling |
| JavaScript | Interactive functionality |
| Chart.js | Data visualizations |

---

## 5. Project Structure

```text
event-capacity-intelligence/
│
├── app.py
├── capacity.py
├── index.html
│
├── events.csv
├── analyze_events.py
├── analyze_mysql_events.py
├── read_events_from_mysql.py
│
├── test_capacity.py
├── test_mysql.py
│
├── requirements.txt
├── .gitignore
├── README.md
│
├── capacity_utilization.png
└── Event-Capacity-Intelligence-Dashboard.pdf
```

### Key files

- `app.py` — Flask application and API endpoints
- `capacity.py` — Capacity planning and risk calculation logic
- `index.html` — Interactive dashboard interface
- `events.csv` — Synthetic event data
- `test_capacity.py` — Calculation test suite
- `requirements.txt` — Python dependencies
- `Event-Capacity-Intelligence-Dashboard.pdf` — Dashboard/report artifact

---

## 6. How the System Works

1. Event records are stored in MySQL.
2. Flask retrieves event data through the `/api/events` endpoint.
3. The dashboard displays event metrics and charts.
4. Users enter planning assumptions in the capacity calculator.
5. JavaScript sends the inputs to Flask through `/api/calculate`.
6. The backend calculates expected attendance, safe planning target, recommended registration cap, and difference.
7. The dashboard displays the results and classifies the capacity risk.

### System Flow

```text
MySQL Event Data
       ↓
