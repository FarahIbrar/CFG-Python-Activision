import pandas as pd
import os

# Define the path to the CSV file
data_file_path = '../Data file/sales.csv'

# Load the CSV file into a DataFrame
df = pd.read_csv(data_file_path)

# Extract the sales data and month names
monthly_sales = df['sales'].tolist()
months = df['month'].tolist()

# Combine months and sales into a list of tuples
monthly_sales_info = list(zip(months, monthly_sales))

# Output: Display sales figures as a simple list
print("Sales figures for each month:")
print(monthly_sales)

# Output: Display months and sales in pounds (£)
print("\nSales figures with months (in pounds):")
for month, sales in monthly_sales_info:
    print(f"{month.capitalize()}: £{sales:,.2f}")

