# Event Capacity Intelligence

A data analytics portfolio project that helps event organizers assess attendance patterns, monitor venue capacity, and explore hypothetical registration scenarios through an interactive dashboard.

## Overview

Event Capacity Intelligence demonstrates an end-to-end analytics workflow using illustrative event data. It combines MySQL, Python, Pandas, Flask, and a browser-based dashboard to turn event registration and attendance records into practical capacity-planning insights.

## Business Problem

Registration totals do not necessarily equal actual attendance. Event organizers need to understand show-up rates, estimate potential attendance, and identify when a venue could approach its capacity limit.

This project explores how data analytics can support those decisions.

## Key Features

- Store and retrieve event records using MySQL.
- Analyze registration and attendance data with Python and Pandas.
- Calculate show-up rates and venue capacity utilization.
- Identify events that may present capacity risks.
- Explore hypothetical attendance scenarios.
- Present key metrics and visualizations in an interactive web dashboard.
- Provide a Flask API to retrieve event data.

## Technology Stack

| Area | Tools |
|---|---|
| Database | MySQL |
| Data analysis | Python, Pandas |
| Backend and API | Flask |
| Frontend | HTML, CSS, JavaScript |
| Visualizations | Matplotlib and dashboard charts |
| Version control | Git and GitHub |

## Example Findings

The current illustrative dataset contains six events.

- **Average show-up rate:** 82.3%
- **High-risk events:** 2
- **Events exceeding capacity:** 0
- **Highest observed capacity utilization:** 98.7%

These results describe only the sample dataset. They are not validated forecasts of real-world event attendance.

## Dashboard Preview

The dashboard includes KPI cards, event selection, a capacity calculator, utilization visualizations, attendance comparisons, and rule-based business insights.

[**View the Dashboard PDF**](Event-Capacity-Intelligence-Dashboard.pdf)

> Note: The PDF is a static snapshot. The interactive dashboard currently runs locally; public deployment is pending.

## Project Structure

- `app.py` — Flask application and API routes
- `index.html` — Interactive dashboard interface
- `analyze_events.py` — CSV-based analysis
- `analyze_mysql_events.py` — MySQL-based analysis
- `read_events_from_mysql.py` — MySQL data retrieval
- `events.csv` — Illustrative sample dataset
- `test_capacity.py` — Capacity calculation tests
- `test_mysql.py` — MySQL connection test
- `capacity_utilization.png` — Analysis visualization
- `requirements.txt` — Python dependencies
- `.gitignore` — Files excluded from version control

Local database credentials belong in `.env`. Never commit passwords, tokens, or other secrets to GitHub.

## Running Locally

### Prerequisites

- Python installed
- MySQL Server installed and running
- Git installed

### Setup

1. Clone this repository and open its folder in a terminal.
2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a MySQL database named `event_capacity` and configure the `events` table to match the columns used by the application.
4. Create a local `.env` file with your database settings:

   ```text
   DB_HOST=localhost
   DB_USER=event_app
   DB_PASSWORD=your_local_password
   ```

5. Make sure the MySQL user has permission to access the database and table.
6. Start the Flask application:

   ```bash
   python app.py
   ```

7. Open the interactive dashboard:

   http://127.0.0.1:5000/dashboard

8. To inspect the event data returned by the API, open:

   http://127.0.0.1:5000/api/events

Make sure your MySQL service is running and your database credentials and schema match the application's configuration.

## Testing

The project includes scripts for testing capacity calculations and checking MySQL connectivity:

- `test_capacity.py`
- `test_mysql.py`

Run these scripts in your local Python environment after configuring the required dependencies and database access.

## Data Disclaimer

The dataset is illustrative and intended for portfolio demonstration. The metrics and insights should not be interpreted as predictions about actual events.

## Roadmap

- [x] Create an illustrative event dataset.
- [x] Build Python and Pandas analysis scripts.
- [x] Connect the local application to MySQL.
- [x] Build a Flask API and interactive dashboard.
- [x] Publish the project source code to GitHub.
- [x] Add a static dashboard PDF.
- [ ] Resolve hosting deployment issues and verify the live application.
- [ ] Expand automated testing and error handling.
- [ ] Add a full-size dashboard screenshot to the README.

## Author

**Jinesh Jain**

[GitHub Repository](https://github.com/jinu5360/event-capacity-intelligence)
