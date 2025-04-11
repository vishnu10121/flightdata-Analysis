# Flight Cancellation Analysis - Objective 4

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load cleaned dataset
flight_data = pd.read_csv("cleaned_flight_data.csv")

# Add a dummy 'cancelled' column (simulate 10% cancelled flights)
np.random.seed(42)
flight_data['cancelled'] = np.random.choice([0, 1], size=len(flight_data), p=[0.9, 0.1])

# 1. Bar Chart - Cancellations by Airline
cancel_by_airline = flight_data[flight_data['cancelled'] == 1]['carrier'].value_counts()

plt.figure(figsize=(8, 6))
plt.bar(cancel_by_airline.index, cancel_by_airline.values, color='tomato')
plt.title("Cancelled Flights by Airline")
plt.xlabel("Airline Code")
plt.ylabel("Number of Cancellations")
plt.tight_layout()
plt.show()

# 2. Pie Chart - Cancellations by Airport
cancel_by_airport = flight_data[flight_data['cancelled'] == 1]['origin'].value_counts()

plt.figure(figsize=(7, 7))
plt.pie(cancel_by_airport.values, labels=cancel_by_airport.index, autopct='%1.1f%%', startangle=140)
plt.title("Cancellation Share by Airport")
plt.tight_layout()
plt.show()
