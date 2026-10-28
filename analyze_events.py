import pandas as pd
import matplotlib.pyplot as plt

events = pd.read_csv("events.csv")
print(events.head())

# 2. Calculate the show-up rate as a percentage
events["show_up_rate"] = (
    events["actual_attendees"] / events["registrations"] * 100
)

# 3. Calculate physical venue capacity utilization
events["capacity_utilization"] = (
    events["actual_attendees"] / events["venue_capacity"] * 100
)

# 4. Identify whether actual attendance exceeded capacity
events["capacity_exceeded"] = (
    events["actual_attendees"] > events["venue_capacity"]
)

# 5. Display the important results
print(events[
    [
        "event_name",
        "show_up_rate",
        "capacity_utilization",
        "capacity_exceeded"
    ]
].round(2).to_string(index=False))


# 5. Classify capacity risk using utilization thresholds
events["risk_level"] = events["capacity_utilization"].apply(
    lambda utilization:
        "High" if utilization >= 95
        else "Moderate" if utilization >= 85
        else "Low"
)

# 6. Display the results
print(
    events[
        [
            "event_name",
            "capacity_utilization",
            "capacity_exceeded",
            "risk_level"
        ]
    ].round(2).to_string(index=False)
)

# Executive summary
high_risk_events = events[events["risk_level"] == "High"]

highest_utilization_event = events.loc[
    events["capacity_utilization"].idxmax()
]

print("\n===== EVENT CAPACITY INTELLIGENCE =====")

print(f"Total events analyzed: {len(events)}")

print(f"High-risk events: {len(high_risk_events)}")

print(
    "Events exceeding physical capacity: "
    f"{events['capacity_exceeded'].sum()}"
)

print(
    "Average show-up rate: "
    f"{events['show_up_rate'].mean():.1f}%"
)

print(
    "Highest utilization event: "
    f"{highest_utilization_event['event_name']}"
)

print(
    "Highest capacity utilization: "
    f"{highest_utilization_event['capacity_utilization']:.1f}%"
)

print("\n===== EVENT RISK TABLE =====")

print(
    events[
        [
            "event_name",
            "show_up_rate",
            "capacity_utilization",
            "risk_level"
        ]
    ].round(1).to_string(index=False)
)

print("\n===== HIGH-RISK EVENTS TO REVIEW =====")

if high_risk_events.empty:
    print("No events are classified as high risk.")
else:
    print(
        high_risk_events[
            ["event_name", "capacity_utilization", "risk_level"]
        ].round(1).to_string(index=False)
    )

##### visualization #######
import matplotlib.pyplot as plt

# Create a bar chart
plt.figure(figsize=(10, 6))

plt.bar(
    events["event_name"],
    events["capacity_utilization"]
)

plt.axhline(
    y=95,
    linestyle="--",
    label="High-risk threshold (95%)"
)

plt.title("Event Venue Capacity Utilization")
plt.xlabel("Event")
plt.ylabel("Capacity Utilization (%)")
plt.xticks(rotation=30, ha="right")
plt.legend()
plt.tight_layout()

# Save the chart in the project folder
plt.savefig("capacity_utilization.png", dpi=150)

print("\nChart saved as capacity_utilization.png")

plt.show()
