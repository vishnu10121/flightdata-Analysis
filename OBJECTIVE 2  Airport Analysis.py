# Airport Analysis - Objective 2

import pandas as pd
import matplotlib.pyplot as plt

# Load the data
flight_data = pd.read_csv("cleaned_flight_data.csv")

# Count total flights per origin airport
flight_count = flight_data["origin"].value_counts()

# Bar Chart - Total Flights from Each Airport
plt.bar(flight_count.index, flight_count.values, color="orange")
plt.title("Total Flights from Each Airport")
plt.xlabel("Origin Airport")
plt.ylabel("Number of Flights")
plt.tight_layout()
plt.show()
