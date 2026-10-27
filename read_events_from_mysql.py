
import mysql.connector
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

connection = None
cursor = None

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="event_app",
        password=os.getenv("DB_PASSWORD"),
        database="event_capacity"
    )

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            event_id,
            event_name,
            venue_capacity,
            registrations,
            actual_attendees,
            event_type
        FROM events
    """)

    rows = cursor.fetchall()
    columns = [column[0] for column in cursor.description]

    events = pd.DataFrame(rows, columns=columns)

    print("Connected to MySQL successfully!")
    print(f"\nTotal events retrieved: {len(events)}")
    print("\nEvent data:")
    print(events.to_string(index=False))

except mysql.connector.Error as error:
    print("MySQL error:", error)

finally:
    if cursor is not None:
        cursor.close()

    if connection is not None and connection.is_connected():
        connection.close()
