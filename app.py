from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)
CORS(app)



def get_database_connection():
    password = os.getenv("DB_PASSWORD")

    if not password:
        raise RuntimeError(
            "DB_PASSWORD is missing. Check your .env file."
        )

    return mysql.connector.connect(
        host="localhost",
        user="event_app",
        password=password,
        database="event_capacity"
    )



@app.route("/api/events")
def get_events():

    connection = get_database_connection()
    cursor = connection.cursor(dictionary=True)

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

    events = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(events)


@app.route("/")
def home():
    return "Event Capacity Intelligence API is running!"

@app.route("/dashboard")
def dashboard():
    return send_from_directory(app.root_path, "index.html")


if __name__ == "__main__":
    app.run(debug=True)
    