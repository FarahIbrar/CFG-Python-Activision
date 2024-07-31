import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress

# Set the style for better visualization
sns.set(style="whitegrid")

# Load the sales data from the CSV file
file_path = 'sales.csv'  # Update this path if necessary
data = pd.read_csv(file_path)

# Ensure data is sorted by month
data['month_num'] = pd.to_datetime(data['month'], format='%B').dt.month
data = data.sort_values('month_num').reset_index(drop=True)

# Calculate the trend using linear regression
x = np.arange(len(data))
slope, intercept, r_value, p_value, std_err = linregress(x, data['sales'])
data['trend'] = intercept + slope * x

print("🚀 Trend Analysis 🚀")
print(f"Trend Slope: {slope:.2f}")
print(f"Intercept: {intercept:.2f}")
print(f"R-squared value: {r_value**2:.2f}")

# Visualization of Sales and Trend Line
plt.figure(figsize=(14, 7))
plt.plot(data['month'], data['sales'], marker='o', linestyle='-', label='Monthly Sales', color='#1f77b4', linewidth=2)
plt.plot(data['month'], data['trend'], linestyle='--', label='Trend Line', color='#ff7f0e', linewidth=2)
plt.title('Monthly Sales and Trend Line Analysis', fontsize=18, weight='bold')
plt.xlabel('Month')
plt.ylabel('Sales (£)')
plt.xticks(rotation=45)
plt.legend()
plt.grid(False)  # Remove grid lines
plt.tight_layout()
plt.show()