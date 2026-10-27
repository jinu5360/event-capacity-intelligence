# Event Capacity Intelligence

A data analytics project that helps event organizers assess attendance patterns, monitor venue capacity, and explore hypothetical registration scenarios through an interactive dashboard.

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

<!-- Add a dashboard screenshot here after uploading it to the repository. -->

*Screenshot coming soon.*

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

1. Install Python and MySQL.
2. Clone this repository and open its folder.
3. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create the `event_capacity` database and configure the `events` table.
5. Configure your local `.env` file with the required database settings, including `DB_PASSWORD`.
6. Start the Flask application:

   ```bash
   python app.py
   ```

7. Open `http://127.0.0.1:5000/` to view the dashboard.
8. Open `http://127.0.0.1:5000/api/events` to inspect the event data returned by the API.

Make sure your MySQL service is running and your database credentials and schema match the application's configuration.

## Data Disclaimer

The dataset is illustrative and intended for portfolio demonstration. The metrics and insights should not be interpreted as predictions about actual events.

## Roadmap

- [x] Connect event analytics to a database
- [x] Build a Flask API and interactive dashboard
- [x] Visualize capacity and attendance metrics
- [ ] Add a dashboard screenshot and improve project documentation
- [ ] Complete public deployment and verify the live application
- [ ] Expand automated testing and error handling

## Author

**Jinesh Jain**

[GitHub Repository](https://github.com/jinu5360/event-capacity-intelligence)
