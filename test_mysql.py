import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="event_app",
        password=os.getenv("DB_PASSWORD"),
        database="event_capacity"
    )

    print("Connected to MySQL successfully!")

    connection.close()

except mysql.connector.Error as error:
    print("MySQL connection failed:", error)