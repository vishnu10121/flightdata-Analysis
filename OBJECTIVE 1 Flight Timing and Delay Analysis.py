#objective 1: Flight Time and Delay Analysis
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv("cleaned_flight_data.csv")

avg_dep_delay = data.groupby("airline")["dep_delay"].mean()

# Plot bar chart
plt.bar(avg_dep_delay.index, avg_dep_delay.values, color='orange')
plt.title("Average Departure Delay by Airline")
plt.xlabel("Airline")
plt.ylabel("Delay (in minutes)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


avg_delay_hour = data.groupby("hour")[["dep_delay", "arr_delay"]].mean()

# Plot line chart
plt.plot(avg_delay_hour.index, avg_delay_hour["dep_delay"], label="Departure Delay", color="blue", marker='o')
plt.plot(avg_delay_hour.index, avg_delay_hour["arr_delay"], label="Arrival Delay", color="green", marker='s')
plt.title("Average Delay by Hour")
plt.xlabel("Hour")
plt.ylabel("Delay (minutes)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
