
import math

from capacity import calculate_capacity


def check_close(actual, expected):
    assert math.isclose(actual, expected, rel_tol=1e-9), (
        f"Expected {expected}, but received {actual}"
    )


def check_invalid_inputs(values):
    try:
        calculate_capacity(*values)
    except ValueError:
        return

    raise AssertionError(
        f"Expected invalid input to be rejected: {values}"
    )


# TEST 1: Normal event
result = calculate_capacity(2000, 2350, 84, 5)

check_close(result["expected_attendance"], 1974)
check_close(result["safe_target"], 1900)
assert result["recommended_cap"] == 2261

print("Test 1 passed: Normal event")


# TEST 2: Low attendance
result = calculate_capacity(2000, 1500, 70, 5)

check_close(result["expected_attendance"], 1050)
check_close(result["safe_target"], 1900)
assert result["recommended_cap"] == 2714

print("Test 2 passed: Low attendance")


# TEST 3: 100% show-up rate
result = calculate_capacity(2000, 2000, 100, 5)

check_close(result["expected_attendance"], 2000)
check_close(result["safe_target"], 1900)
assert result["recommended_cap"] == 1900

print("Test 3 passed: 100% show-up rate")


# TEST 4: Low show-up rate
result = calculate_capacity(2000, 500, 10, 5)

check_close(result["expected_attendance"], 50)
assert result["recommended_cap"] == 19000

print("Test 4 passed: Low show-up rate")


# TEST 5: Zero registrations
result = calculate_capacity(2000, 0, 84, 5)

check_close(result["expected_attendance"], 0)
check_close(result["safe_target"], 1900)
assert result["recommended_cap"] == 2261

print("Test 5 passed: Zero registrations")


# TEST 6: High-risk event
result = calculate_capacity(2000, 2500, 90, 5)

check_close(result["expected_attendance"], 2250)
check_close(result["safe_target"], 1900)
check_close(result["difference"], 350)
assert result["recommended_cap"] == 2111

print("Test 6 passed: High-risk event")


# TEST 7: Zero show-up rate
check_invalid_inputs((2000, 2500, 0, 5))
print("Test 7 passed: Zero show-up rate rejected")


# TEST 8: Show-up rate above 100%
check_invalid_inputs((2000, 2500, 101, 5))
print("Test 8 passed: Show-up rate above 100% rejected")


# TEST 9: 100% safety buffer
check_invalid_inputs((2000, 2500, 84, 100))
print("Test 9 passed: 100% safety buffer rejected")


# TEST 10: Negative registrations
check_invalid_inputs((2000, -10, 84, 5))
print("Test 10 passed: Negative registrations rejected")


# TEST 11: Zero venue capacity
check_invalid_inputs((0, 2500, 84, 5))
print("Test 11 passed: Zero venue capacity rejected")


# TEST 12: Negative safety buffer
check_invalid_inputs((2000, 2500, 84, -5))
print("Test 12 passed: Negative safety buffer rejected")


print("\nAll 12 capacity calculation tests passed!")
