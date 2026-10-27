
import mysql.connector
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

connection = None

try:
    # Connect Python to MySQL
    connection = mysql.connector.connect(
        host="localhost",
        user="event_app",
        password=os.getenv("DB_PASSWORD"),
        database="event_capacity"
    )

    # Load event records into Pandas
    events = pd.read_sql(
        """
        SELECT event_name, venue_capacity, registrations,
               actual_attendees, event_type
        FROM events
        """,
        connection
    )

    # Calculate business metrics
    events["show_up_rate"] = (
        events["actual_attendees"] / events["registrations"] * 100
    ).round(1)

    events["capacity_utilization"] = (
        events["actual_attendees"] / events["venue_capacity"] * 100
    ).round(1)

    events["capacity_exceeded"] = (
        events["actual_attendees"] > events["venue_capacity"]
    )

    # Illustrative risk thresholds, not universal standards
    events["risk_level"] = events["capacity_utilization"].apply(
        lambda rate:
            "High" if rate >= 95
            else "Moderate" if rate >= 85
            else "Low"
    )

    # Display results
    print("\n===== EVENT CAPACITY ANALYSIS =====")
    print(events.to_string(index=False))

    print("\n===== EXECUTIVE SUMMARY =====")
    print(f"Events analyzed: {len(events)}")
    print(f"High-risk events: {(events['risk_level'] == 'High').sum()}")
    print(f"Events exceeding capacity: {events['capacity_exceeded'].sum()}")
    print(f"Average show-up rate: {events['show_up_rate'].mean():.1f}%")

    highest = events.loc[events["capacity_utilization"].idxmax()]
    print(f"Highest utilization: {highest['event_name']}")
    print(f"Utilization rate: {highest['capacity_utilization']:.1f}%")

except mysql.connector.Error as error:
    print("MySQL connection/query error:", error)

finally:
    if connection is not None and connection.is_connected():
        connection.close()
