import math


def calculate_capacity(venue_capacity, registrations, show_up_rate, safety_buffer):
    expected_attendance = registrations * (show_up_rate / 100)

    safe_target = venue_capacity * (1 - safety_buffer / 100)

    recommended_cap = math.floor(safe_target / (show_up_rate / 100))

    difference = expected_attendance - safe_target

    return {
        "expected_attendance": expected_attendance,
        "safe_target": safe_target,
        "recommended_cap": recommended_cap,
        "difference": difference
    }


# Test 1
result = calculate_capacity(2000, 2350, 84, 5)

assert result["expected_attendance"] == 1974
assert result["safe_target"] == 1900
assert result["recommended_cap"] == 2261

print("Test 1 passed")


# Test 2
result = calculate_capacity(2000, 1500, 70, 5)

assert result["expected_attendance"] == 1050
assert result["safe_target"] == 1900
assert result["recommended_cap"] == 2714

print("Test 2 passed")


# Test 3
result = calculate_capacity(2000, 2000, 100, 5)

assert result["expected_attendance"] == 2000
assert result["safe_target"] == 1900
assert result["recommended_cap"] == 1900

print("Test 3 passed")


# Test 4
result = calculate_capacity(2000, 500, 10, 5)

assert result["expected_attendance"] == 50
assert result["safe_target"] == 1900
assert result["recommended_cap"] == 19000

print("Test 4 passed")


print("\nAll capacity calculation tests passed!")