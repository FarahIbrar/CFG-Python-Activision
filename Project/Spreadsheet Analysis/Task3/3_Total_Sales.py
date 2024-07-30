import pandas as pd

# Load the sales data from the CSV file
file_path = '../Data file/sales.csv'
data = pd.read_csv(file_path)

# Extract the 'sales' column and compute the sum
total_sales = data['sales'].sum()

# Creating a captivating output message
print("🚀 Sales Celebration Alert! 🚀")
print(f"🎯 Total Sales Over the Year: £{total_sales:,.2f}")

# Adding a personalized touch
print("\nHere's the grand total:")
print(f"🎉 You’ve achieved a phenomenal total of £{total_sales:,.2f} in sales across all months! 🎉")

# Adding some visual appeal
print("\n📊 Summary Highlights:")
print("------------------------------------------------")
print(f"💼 Total Sales: £{total_sales:,.2f}")
print("------------------------------------------------")
print("📅 Keep an eye out for more detailed analyses and exciting updates!")


