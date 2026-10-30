# Event Capacity Intelligence

A data analytics dashboard that helps event organizers make better registration and venue-capacity decisions using attendance estimates, capacity calculations, and risk analysis.

## 1. Business Problem

Events can receive more registrations than their venues can accommodate. However, not every registered participant attends the event.

Without proper planning, organizers may underestimate attendance, exceed venue capacity, or leave too many seats unused.

This project uses sample event data to estimate attendance and help organizers set more informed registration limits.

## 2. Project Objectives

- Estimate expected event attendance.
- Calculate recommended registration limits.
- Identify events with potential capacity risks.
- Compare low, expected, and high attendance scenarios.
- Present useful business insights through a dashboard.

## 3. Dashboard Features

- **KPI Cards:** Display venue capacity, registrations, and expected attendance.
- **Event Overview:** Show total events, high-risk events, over-capacity events, and average show-up rate.
- **Capacity Calculator:** Calculate attendance estimates and recommended registration limits.
- **Scenario Analysis:** Compare low, expected, and high attendance scenarios.
- **Charts:** Visualize capacity utilization and estimated attendance.
- **Business Insights:** Highlight potential capacity issues using calculated results.

## 4. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend calculations and data processing |
| Flask | Web application and API |
| MySQL | Database |
| HTML | Dashboard structure |
| CSS | Dashboard styling |
| JavaScript | Interactive dashboard |
| Chart.js | Data visualizations |
| Pandas | Data analysis |

## 5. Project Structure

```text
Event-Capacity-Intelligence/
│
├── app.py
├── capacity.py
├── analyze_events.py
├── analyze_mysql_events.py
├── read_events_from_mysql.py
├── test_capacity.py
├── test_mysql.py
├── events.csv
├── index.html
├── requirements.txt
├── README.md
├── Event-Capacity-Intelligence-Dashboard.pdf
├── capacity_utilization.png
└── .gitignore
```

The `.env` file stores local database credentials and should not be uploaded to GitHub.

## 6. How the System Works

1. Event information is stored in a MySQL database.
2. Python and Flask handle the application logic.
3. The capacity calculator estimates expected attendance.
4. The system calculates a recommended registration cap.
5. The dashboard displays the results, charts, and business insights.

## 7. Core Calculation Logic

**Expected Attendance**

Calculated using the number of registrations and the expected show-up rate.

**Safe Planning Target**

The venue capacity after applying a safety buffer.

**Recommended Registration Cap**

Calculated by dividing the safe planning target by the expected show-up rate.

These calculations help organizers estimate how many registrations a venue can reasonably accommodate.

## 8. Risk Classification

| Risk Level | Meaning |
|---|---|
| Within Target | Expected attendance is within the safe planning target. |
| Warning | Expected attendance is above the safe target but does not exceed venue capacity. |
| High Risk | Expected attendance exceeds venue capacity. |

These categories are planning indicators, not guarantees of actual attendance or physical safety.

## 9. Testing and Validation

The capacity calculation logic was tested using different scenarios.

**Test results:**

- 12 automated tests passed.
- Tested normal registration levels.
- Tested warning-level capacity scenarios.
- Tested high-risk capacity scenarios.
- Tested zero registrations.
- Tested invalid show-up rates.
- Tested the Flask calculation API.

## 10. Sample Data

The project uses synthetic sample event data.

The dataset includes:

- Event name
- Venue capacity
- Number of registrations
- Actual attendees
- Event type

The sample dataset contains six events across different event categories.

## 11. Running the Project Locally

### Prerequisites

Install the following:

- Python
- MySQL Server
- A web browser

### Step 1: Install Dependencies

Open a terminal in the project folder and run:

```bash
pip install -r requirements.txt
```

### Step 2: Create the Database

Open MySQL and run:

```sql
CREATE DATABASE event_capacity;
USE event_capacity;
```

### Step 3: Create the Events Table

Run the following SQL:

```sql
CREATE TABLE events (
    event_id INT AUTO_INCREMENT PRIMARY KEY,
    event_name VARCHAR(100) NOT NULL,
    venue_capacity INT NOT NULL,
    registrations INT NOT NULL,
    actual_attendees INT NOT NULL,
    event_type VARCHAR(50)
);
```

### Step 4: Import the Sample Data

Import the provided `events.csv` file into the `events` table using MySQL Workbench's Table Data Import Wizard.

Make sure the CSV columns match the table columns, excluding the auto-generated `event_id` column.

### Step 5: Configure Database Credentials

Create a `.env` file in the project folder:

```env
DB_HOST=localhost
DB_USERNAME=event_app
DB_PASSWORD=your_database_password
```

Use your actual local database password.

**Do not commit the `.env` file to GitHub.**

### Step 6: Start the Application

Run:

```bash
python app.py
```

### Step 7: Open the Dashboard

Open your browser and visit:

http://127.0.0.1:5000/dashboard

## 12. API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/api/events` | Retrieve event data |
| POST | `/api/calculate` | Calculate capacity recommendations |

## 13. Future Improvements

- Add more historical event data.
- Improve attendance forecasting using machine learning.
- Add interactive event comparisons.
- Deploy the dashboard online.
- Introduce additional analytics for event planning.

## 14. Project Purpose

This project demonstrates how data analytics can support practical business decisions.

It combines data processing, database management, backend development, calculations, and visualization to address a real-world event-planning problem.

**GitHub Repository:**

https://github.com/jinu5360/event-capacity-intelligence

## 15. Business Insight Example

For example, consider an event with:

- Venue capacity: 2,000
- Registrations: 2,500
- Expected show-up rate: 90%
- Safety buffer: 5%

The estimated attendance is 2,250, while the safe planning target is 1,900.

This indicates a high capacity risk. The organizer should consider limiting registrations to the recommended cap of 2,111.

This example demonstrates how the dashboard can turn event data into practical registration decisions.