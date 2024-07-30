import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set the style for better visualization
sns.set(style="whitegrid")

# Load the sales data from the CSV file
file_path = '../Data file/sales.csv'
data = pd.read_csv(file_path)

# Basic Summary Statistics
total_sales = data['sales'].sum()
average_sales = data['sales'].mean()
max_sales = data.loc[data['sales'].idxmax()]
min_sales = data.loc[data['sales'].idxmin()]

print("🚀 Basic Summary Statistics 🚀")
print(f"🎯 Total Sales Over the Year: £{total_sales:,.2f}")
print(f"📊 Average Monthly Sales: £{average_sales:,.2f}")
print(f"📈 Month with Highest Sales: {max_sales['month'].capitalize()} with £{max_sales['sales']:.2f}")
print(f"📉 Month with Lowest Sales: {min_sales['month'].capitalize()} with £{min_sales['sales']:.2f}")

# 1. Monthly Sales Growth Rate
data['sales_growth_rate'] = data['sales'].pct_change() * 100
growth_rate = data[['month', 'sales_growth_rate']].dropna()
print("\n📈 Monthly Sales Growth Rate:")
print(growth_rate.to_string(index=False))

# 2. Seasonal Trends Analysis
seasonal_trends = data.groupby('month')['sales'].mean().sort_index()
print("\n🌟 Average Monthly Sales (Seasonal Trends):")
print(seasonal_trends.to_string())

# 3. Sales Distribution Analysis
sales_distribution = data['sales'].describe()
print("\n📊 Sales Distribution Statistics:")
print(f"Mean Sales: £{sales_distribution['mean']:,.2f}")
print(f"Median Sales: £{sales_distribution['50%']:,.2f}")
print(f"Standard Deviation: £{sales_distribution['std']:,.2f}")
print(f"Minimum Sales: £{sales_distribution['min']:,.2f}")
print(f"Maximum Sales: £{sales_distribution['max']:,.2f}")

# 4. Simulated Year-on-Year Comparison
previous_year_sales = np.random.uniform(low=data['sales'].min(), high=data['sales'].max(), size=len(data))
data['previous_year_sales'] = previous_year_sales
data['year_on_year_change'] = ((data['sales'] - data['previous_year_sales']) / data['previous_year_sales']) * 100
year_on_year_comparison = data[['month', 'previous_year_sales', 'sales', 'year_on_year_change']]
print("\n🔄 Simulated Year-on-Year Comparison:")
print(year_on_year_comparison.to_string(index=False))

# 5. Expenditure Analysis
if 'expenditure' in data.columns:
    correlation = data[['sales', 'expenditure']].corr().iloc[0, 1]
    print("\n💡 Expenditure and Sales Correlation:")
    print(f"The correlation coefficient between sales and expenditure is {correlation:.2f}")
else:
    print("\n💡 Expenditure Analysis: Expenditure column not found in data.")

# Visualization Section

# 1. Monthly Sales and Growth Rate
fig, ax1 = plt.subplots(figsize=(14, 7))
color_sales = '#1f77b4'
ax1.set_xlabel('Month')
ax1.set_ylabel('Sales (£)', color=color_sales)
ax1.plot(data['month'], data['sales'], marker='o', linestyle='-', color=color_sales, label='Monthly Sales', linewidth=2)
ax1.tick_params(axis='y', labelcolor=color_sales)

# Set tick positions and labels
ax1.set_xticks(data['month'])
ax1.set_xticklabels(data['month'], rotation=45, ha='right')

ax2 = ax1.twinx()
color_change = '#d62728'
ax2.set_ylabel('Growth Rate (%)', color=color_change)
ax2.plot(data['month'][1:], growth_rate['sales_growth_rate'], marker='s', linestyle='--', color=color_change, label='Sales Growth Rate (%)', linewidth=2)
ax2.tick_params(axis='y', labelcolor=color_change)

fig.suptitle('Monthly Sales and Growth Rate Analysis', fontsize=18, weight='bold')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
ax1.grid(False)  # Remove grid lines from ax1
ax2.grid(False)  # Remove grid lines from ax2
plt.tight_layout()
plt.show()

# 2. Seasonal Trends Visualization
plt.figure(figsize=(10, 6))
sns.barplot(x=seasonal_trends.index, y=seasonal_trends.values, color='teal')
plt.title('Average Monthly Sales (Seasonal Trends)', fontsize=16)
plt.xlabel('Month')
plt.ylabel('Average Sales (£)')
plt.xticks(rotation=45)
plt.grid(False)  # Remove grid lines
plt.tight_layout()
plt.show()

# 3. Sales Distribution Visualization
plt.figure(figsize=(10, 6))
sns.histplot(data['sales'], bins=10, kde=True, color='skyblue')
plt.title('Sales Distribution', fontsize=16)
plt.xlabel('Sales (£)')
plt.ylabel('Frequency')
plt.grid(False)  # Remove grid lines
plt.tight_layout()
plt.show()

# 4. Simulated Year-on-Year Comparison Visualization
plt.figure(figsize=(14, 7))
plt.plot(data['month'], data['sales'], marker='o', linestyle='-', label='Current Year Sales', color='#1f77b4')
plt.plot(data['month'], data['previous_year_sales'], marker='o', linestyle='--', label='Previous Year Sales', color='#ff7f0e')
plt.title('Year-on-Year Sales Comparison', fontsize=16)
plt.xlabel('Month')
plt.ylabel('Sales (£)')
plt.legend()
plt.grid(False)  # Remove grid lines
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 5. Expenditure Analysis Visualization (Correlation Heatmap)
plt.figure(figsize=(10, 6))
correlation_matrix = data[['sales', 'expenditure']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, vmin=-1, vmax=1)
plt.title('Correlation Heatmap between Sales and Expenditure', fontsize=16)
plt.grid(False)  # Remove grid lines
plt.tight_layout()
plt.show()