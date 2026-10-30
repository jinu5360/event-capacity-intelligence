
from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
import mysql.connector
import os
from dotenv import load_dotenv

from capacity import calculate_capacity

load_dotenv(override=True)

app = Flask(__name__)
CORS(app)


def get_database_connection():
    password = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST", "localhost")
    db_user = os.getenv("DB_USERNAME") or os.getenv("DB_USER", "event_app")

    if not password:
        raise RuntimeError("DB_PASSWORD is missing. Check your .env file.")

    return mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=password,
        database="event_capacity"
    )


@app.route("/api/events")
def get_events():
    connection = get_database_connection()
    cursor = connection.cursor(dictionary=True)

    try:
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
        return jsonify(events)

    finally:
        cursor.close()
        connection.close()


@app.route("/api/calculate", methods=["POST"])
def calculate_event_capacity():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Please provide valid JSON input."}), 400

    required_fields = [
        "venue_capacity",
        "registrations",
        "show_up_rate",
        "safety_buffer"
    ]

    missing_fields = [
        field for field in required_fields if field not in data
    ]

    if missing_fields:
        return jsonify({
            "error": "Missing required fields.",
            "missing_fields": missing_fields
        }), 400

    try:
        result = calculate_capacity(
            venue_capacity=data["venue_capacity"],
            registrations=data["registrations"],
            show_up_rate=data["show_up_rate"],
            safety_buffer=data["safety_buffer"]
        )

        return jsonify(result)

    except (ValueError, TypeError) as error:
        return jsonify({"error": str(error)}), 400


@app.route("/")
def home():
    return "Event Capacity Intelligence API is running!"


@app.route("/dashboard")
def dashboard():
    return send_from_directory(app.root_path, "index.html")


if __name__ == "__main__":
    app.run(debug=True)
