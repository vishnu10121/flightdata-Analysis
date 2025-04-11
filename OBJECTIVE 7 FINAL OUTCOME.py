#conclusion
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("cleaned_flight_data.csv")

# Add estimated cost column (₹5 per kilometer)
df["estimated_cost"] = df["distance"] * 5  # Just multiply distance by ₹5

# Select only basic numeric columns to check correlation
basic_columns = ['dep_delay', 'arr_delay', 'air_time', 'distance', 'estimated_cost']
corr = df[basic_columns].corr()  # Only these columns

# Plot the heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".1f")

# Add a title
plt.title("Basic Correlation Heatmap (Delays, Time, Distance, Cost)", fontsize=13)

# Show the plot
plt.tight_layout()
plt.show()
