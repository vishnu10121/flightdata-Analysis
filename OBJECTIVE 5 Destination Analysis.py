# Destination Analysis - Project Objective 5


import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
flight_data = pd.read_csv("cleaned_flight_data.csv")

# 1. Bar Chart - Top 10 Busiest Destinations
top_destinations = flight_data['dest'].value_counts().head(10)

plt.figure(figsize=(9, 6))
plt.bar(top_destinations.index, top_destinations.values, color='teal')
plt.title("Top 10 Busiest Destinations")
plt.xlabel("Destination Airport")
plt.ylabel("Number of Flights")
plt.tight_layout()
plt.show()

# 2. Line Chart - Average Arrival Delay for Top 10 Destinations
avg_arrival_delay = flight_data.groupby('dest')['arr_delay'].mean().loc[top_destinations.index]

plt.figure(figsize=(10, 6))
plt.plot(avg_arrival_delay.index, avg_arrival_delay.values, marker='^', color='darkorange', linewidth=2)
plt.title("Average Arrival Delay for Top 10 Destinations")
plt.xlabel("Destination Airport")
plt.ylabel("Average Arrival Delay (minutes)")
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
