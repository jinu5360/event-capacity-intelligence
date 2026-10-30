# Event Capacity Intelligence

A data analytics dashboard that helps event organizers make better registration and venue-capacity decisions using attendance estimates, capacity calculations, and risk analysis.

All sample event records are synthetic.

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
- Tested a fresh installation using a separate GitHub download.

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
- MySQL Workbench (recommended)
- A web browser

### Step 1: Download the Project

Clone the repository:

```bash
git clone https://github.com/jinu5360/event-capacity-intelligence.git
```

Open the downloaded project folder in VS Code.

### Step 2: Install Dependencies

Open a terminal in the project folder and run:

```bash
pip install -r requirements.txt
```

### Step 3: Create the Database

Open MySQL Workbench or the MySQL command-line client and run:

```sql
CREATE DATABASE event_capacity;
USE event_capacity;
```

### Step 4: Create the Events Table

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

### Step 5: Import the Sample Data

Import the provided `events.csv` file into the `events` table using MySQL Workbench's Table Data Import Wizard.

Make sure the CSV columns match the table columns. Do not import `event_id` if MySQL is generating it automatically.

### Step 6: Create a MySQL Application User

For security, the application uses a separate MySQL user instead of the MySQL root account.

Run the following SQL:

```sql
CREATE USER 'event_app'@'localhost'
IDENTIFIED BY 'choose_your_password';

GRANT SELECT, INSERT, UPDATE, DELETE
ON event_capacity.*
TO 'event_app'@'localhost';
```

Replace `choose_your_password` with a password of your choice.

If the `event_app` user already exists, update its password using:

```sql
ALTER USER 'event_app'@'localhost'
IDENTIFIED BY 'choose_your_password';
```

Then run the `GRANT` statement above.

### Step 7: Configure Environment Variables

Create a file named `.env` in the project folder, at the same level as `app.py`.

Add:

```env
DB_HOST=localhost
DB_USERNAME=event_app
DB_PASSWORD=choose_your_password
```

Use the same password you assigned to the `event_app` MySQL user.

The application loads these settings using `python-dotenv`.

The application uses `load_dotenv(override=True)` so values from the project's `.env` file take precedence over existing environment variables.

**Important:** Never upload your `.env` file or database passwords to GitHub.

### Step 8: Start the Application

Run:

```bash
python app.py
```

Keep the terminal open while using the application.

### Step 9: Open the Dashboard

Open your browser and visit:

http://127.0.0.1:5000/dashboard

The dashboard should retrieve the six sample events from MySQL.

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

## 15. Business Insight Example

Consider an event with:

- Venue capacity: 2,000
- Registrations: 2,500
- Expected show-up rate: 90%
- Safety buffer: 5%

The estimated attendance is 2,250, while the safe planning target is 1,900.

This indicates a high capacity risk. The organizer should consider limiting registrations to the recommended cap of 2,111.

This example demonstrates how the dashboard can turn event data into practical registration decisions.

---
---

**GitHub Repository:**  
[Event Capacity Intelligence](https://github.com/jinu5360/event-capacity-intelligence)

## Dashboard Preview

[View Dashboard PDF](Event-Capacity-Intelligence-Dashboard.pdf)