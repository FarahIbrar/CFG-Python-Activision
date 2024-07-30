import pandas as pd
import numpy as np

# Load the sales data from the CSV file
file_path = '../Data file/sales.csv'
data = pd.read_csv(file_path)

# Ensure data is sorted by month
data['month_num'] = pd.to_datetime(data['month'], format='%b').dt.month
data = data.sort_values('month_num').reset_index(drop=True)

# Calculate the trend using linear regression
from scipy.stats import linregress

x = np.arange(len(data))
slope, intercept, r_value, p_value, std_err = linregress(x, data['sales'])

print("🚀 Trend Analysis 🚀")
print(f"Trend Slope: {slope:.2f}")
print(f"Intercept: {intercept:.2f}")
print(f"R-squared value: {r_value**2:.2f}")