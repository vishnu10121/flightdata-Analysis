# Estimated Flight Cost Analysis - Objective 6


import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
flight_data = pd.read_csv("cleaned_flight_data.csv")


# Estimating Cost:
# Since the dataset does not contain real ticket prices,
# we are estimating the cost of each flight based on distance ..
# Assumption: Each kilometer of flight costs ₹5.
# Formula: estimated_cost = distance × ₹5.

flight_data["estimated_cost"] = flight_data["distance"] * 5

# 1. Bar Chart - Average Estimated Cost per Airline
# This shows which airlines are more/less expensive on average

avg_cost_by_airline = flight_data.groupby("carrier")["estimated_cost"].mean()

plt.figure(figsize=(10, 6))
plt.bar(avg_cost_by_airline.index, avg_cost_by_airline.values, color="skyblue")
plt.title("Average Estimated Cost per Airline")
plt.xlabel("Airline")
plt.ylabel("Estimated Cost (₹)")
plt.tight_layout()
plt.show()


# 2. Pie Chart - Cost Share of Top 5 Airlines
# Shows which airlines earn the most (in estimated cost).

total_cost_by_airline = flight_data.groupby("carrier")["estimated_cost"].sum()
top5_airlines_cost = total_cost_by_airline.sort_values(ascending=False).head(5)

plt.figure(figsize=(7, 7))
plt.pie(top5_airlines_cost.values, labels=top5_airlines_cost.index, autopct='%1.1f%%', startangle=140)
plt.title("Estimated Cost Share - Top 5 Airlines")
plt.tight_layout()
plt.show()


# 3. Line Chart - Average Cost for Top 10 Destinations
# Shows average cost trend across most popular destinations.

top_dest = flight_data["dest"].value_counts().head(10).index
avg_cost_by_dest = flight_data[flight_data["dest"].isin(top_dest)].groupby("dest")["estimated_cost"].mean()

plt.figure(figsize=(10, 6))
plt.plot(avg_cost_by_dest.index, avg_cost_by_dest.values, marker='o', linestyle='-', color="green")
plt.title("Average Estimated Cost for Top 10 Destinations")
plt.xlabel("Destination")
plt.ylabel("Estimated Cost (₹)")
plt.grid(True)
plt.tight_layout()
plt.show()
