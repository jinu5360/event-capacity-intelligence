# Event Capacity Intelligence

## Overview

Event Capacity Intelligence is a data analytics project that helps event organizers assess venue capacity utilization, understand registration and attendance patterns, and identify events that may require additional planning.

The project uses illustrative event data to demonstrate a practical analytics workflow, from database storage to a dashboard.

## Business Problem

Event organizers need to estimate attendance and understand whether a venue may approach its capacity limit. Registration totals alone may not accurately reflect the number of attendees who arrive.

This project analyzes registrations, actual attendance, venue capacity, and show-up rates to support capacity planning.

## Key Features

- Retrieve event data from MySQL.
- Analyze registration and attendance patterns using Python and Pandas.
- Calculate show-up rates and venue capacity utilization.
- Identify high-risk events and events exceeding capacity.
- Display event metrics in a web dashboard.
- Explore hypothetical attendance and capacity scenarios.

## Technology Stack

- **Database:** MySQL
- **Analytics:** Python, Pandas
- **Backend:** Flask
- **Frontend:** HTML, CSS, JavaScript
- **Version control:** Git

## Example Findings

The current illustrative dataset contains six events.

- Average show-up rate: 82.3%
- High-risk events: 2
- Events exceeding capacity: 0
- Highest observed capacity utilization: 98.7%

These results describe the sample dataset only; they are not real-world event forecasts.

## Project Structure

- `app.py` — Flask API
- `index.html` — Dashboard interface
- `analyze_events.py` — CSV-based analysis
- `analyze_mysql_events.py` — MySQL-based analysis
- `read_events_from_mysql.py` — MySQL data retrieval
- `events.csv` — Illustrative sample data
- `test_capacity.py` — Capacity calculation tests
- `test_mysql.py` — MySQL connection test
- `capacity_utilization.png` — Analysis visualization
- `.env` — Local database configuration; do not publish this file

## Running Locally

1. Install Python and MySQL.
2. Install the required Python packages used by the project.
3. Create the `event_capacity` database and configure the `events` table.
4. Set your database password in a local `.env` file using `DB_PASSWORD`.
5. Run the Flask application with `python app.py`.
6. Open `http://127.0.0.1:5000/` to check the API and `http://127.0.0.1:5000/api/events` to view event data.

## Data Disclaimer

The dataset is illustrative and intended for portfolio demonstration. Findings should not be treated as predictions about actual events.

## Future Improvements

- Improve database connection handling and error reporting.
- Add automated tests for API endpoints.
- Document dependencies and provide a reproducible setup process.
- Deploy the dashboard for public demonstration.
