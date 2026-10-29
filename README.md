# Event Capacity Intelligence

A data-driven event capacity planning dashboard that helps event organizers estimate attendance, identify venue capacity risks, and make better registration decisions.

## 1. Business Problem

Event organizers sometimes accept more registrations than their venue can safely accommodate.

However, not every registered attendee will attend the event. This creates a planning challenge:

- Too many registrations can lead to overcrowding.
- Too few registrations can result in unused venue capacity.
- Organizers need a practical way to estimate attendance before an event takes place.

**Event Capacity Intelligence** addresses this challenge by combining historical event data, expected show-up rates, and safety buffers to provide registration recommendations.

## 2. Project Objectives

- Monitor event registrations and attendance.
- Compare actual attendance with venue capacity.
- Calculate a recommended registration limit.
- Identify events with high capacity utilization.
- Compare low, expected, and high attendance scenarios.
- Provide clear, rule-based business insights.

## 3. Dashboard Features

### Event Overview
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

- Low attendance: show-up rate reduced by 5 percentage points.
- Expected attendance: selected show-up rate.
- High attendance: show-up rate increased by 5 percentage points.

### Data Visualizations
- Capacity utilization by event
- Actual attendance versus venue capacity
- Business insights generated from event data

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

## 5. How the System Works

1. Event records are stored in MySQL.
2. Flask retrieves event data through the `/api/events` endpoint.
3. The dashboard displays event metrics and charts.
4. Users enter planning assumptions in the capacity calculator.
5. JavaScript sends the inputs to Flask through `/api/calculate`.
6. The backend calculates the expected attendance, safe target, recommended registration cap, and difference.
7. The dashboard displays the results and classifies the capacity risk.

## 6. Core Calculation Logic

The project uses the following planning calculations:

**Expected Attendance**

Registrations × Expected Show-up Rate

**Safe Planning Target**

Venue Capacity × (1 − Safety Buffer)

**Recommended Registration Cap**

Safe Planning Target ÷ Expected Show-up Rate

The recommended registration cap is rounded down to a whole person.

These calculations are planning estimates, not guarantees of actual attendance or physical safety.

## 7. Risk Classification

| Condition | Classification |
|---|---|
| Expected attendance is within the safe target | Within Target |
| Expected attendance exceeds the safe target but remains within venue capacity | Warning |
| Expected attendance exceeds venue capacity | High Risk |

## 8. Testing and Validation

The project includes calculation tests and manual dashboard testing.

Five manual scenarios were successfully checked:

| Test | Scenario | Result |
|---|---|---|
| 1 | Normal attendance | Passed |
| 2 | Above safe target, below capacity | Passed |
| 3 | Above venue capacity | Passed |
| 4 | Zero registrations | Passed |
| 5 | Invalid show-up rate | Passed |

The separate calculation test suite also passed 12 test cases.

## 9. Sample Data

The project uses synthetic event records for demonstration and testing.

No real attendee personal information is required for the sample dashboard.

## 10. Running the Project Locally

### Prerequisites
- Python
- MySQL Server
- A web browser

### Install Python dependencies

```bash
pip install flask flask-cors mysql-connector-python python-dotenv
```

### Configure database credentials

Create a `.env` file in the project folder:

```env
DB_HOST=localhost
DB_USERNAME=event_app
DB_PASSWORD=your_database_password
```

Use your actual local database password. Do not commit this file to GitHub.

### Start the application

```bash
python app.py
```

Open the dashboard:

```text
http://127.0.0.1:5000/dashboard
```

## 11. Future Improvements

- Event creation and editing
- Attendee registration management
- Automatic registration caps
- Ticket and check-in tracking
- Live capacity monitoring
- More advanced attendance forecasting
- Improved reporting and export functionality

## 12. Project Purpose

This project demonstrates how database management, backend development, data analysis, and interactive visualizations can be combined to address a practical event operations problem.

**Project:** Event Capacity Intelligence
**Developer:** Jinesh Jain
**GitHub:** https://github.com/jinu5360/event-capacity-intelligence
