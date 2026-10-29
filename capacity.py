
import math


def calculate_capacity(venue_capacity, registrations, show_up_rate, safety_buffer):
    """Calculate expected attendance and a safer registration limit."""

    if venue_capacity <= 0:
        raise ValueError("Venue capacity must be positive.")

    if registrations < 0:
        raise ValueError("Registrations cannot be negative.")

    if show_up_rate <= 0 or show_up_rate > 100:
        raise ValueError(
            "Show-up rate must be above 0% and at most 100%."
        )

    if safety_buffer < 0 or safety_buffer >= 100:
        raise ValueError(
            "Safety buffer must be at least 0% and below 100%."
        )

    show_up_decimal = show_up_rate / 100

    expected_attendance = registrations * show_up_decimal
    safe_target = venue_capacity * (1 - safety_buffer / 100)

    recommended_cap = math.floor(
        safe_target / show_up_decimal
    )

    difference = expected_attendance - safe_target

    return {
        "expected_attendance": expected_attendance,
        "safe_target": safe_target,
        "recommended_cap": recommended_cap,
        "difference": difference
    }
