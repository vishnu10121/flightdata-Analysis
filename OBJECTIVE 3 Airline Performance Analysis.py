# Airline Performance Analysis - Objective 3

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset ..
flight_data = pd.read_csv("cleaned_flight_data.csv")

# 1. Line Chart - Average Departure and Arrival Delays by Airline
flight_count_by_airline = flight_data["carrier"].value_counts()

plt.figure(figsize=(8, 6))
plt.bar(flight_count_by_airline.index, flight_count_by_airline.values, color="teal")
plt.title("Total Flights by Airline")
plt.xlabel("Airline Code")
plt.ylabel("Number of Flights")
plt.tight_layout()
plt.show()

# 2. Pie Chart - Flight Share by Airline
flight_share = flight_data["carrier"].value_counts()

plt.figure(figsize=(7, 7))
plt.pie(flight_share.values, labels=flight_share.index, autopct='%1.1f%%', startangle=140)
plt.title("Flight Distribution by Airline")
plt.tight_layout()
plt.show()
