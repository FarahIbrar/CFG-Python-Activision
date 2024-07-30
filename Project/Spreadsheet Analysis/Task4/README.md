# Task 4: Advanced Sales Analysis

This analysis delves into monthly sales data to uncover insights related to sales performance, growth trends, seasonal patterns, and expenditure correlations. Using Python libraries such as Pandas, NumPy, Matplotlib, and Seaborn, we performed a comprehensive examination of the dataset, producing various statistical summaries and visualizations.

## Dataset

The dataset contains the following columns:
- **`month`**: The month of the year.
- **`sales`**: The sales amount for that month.
- **`expenditure`** (optional): The expenditure associated with the sales.

The dataset was loaded from a [CSV file](https://github.com/FarahIbrar/CFG-Python-Activision/blob/main/Project/Data%20File/sales.csv) and analyzed using Python.

## Key Findings

### Basic Summary Statistics

- **Total Sales Over the Year**: £45,542.00
- **Average Monthly Sales**: £3,795.17
- **Month with Highest Sales**: July (£7,479.00)
- **Month with Lowest Sales**: February (£1,521.00)

**Explanation**: These statistics provide a high-level view of annual sales performance. July is the peak month, potentially due to seasonal demand or promotional activities. February, with the lowest sales, may be affected by post-holiday season dips or other factors.

### Monthly Sales Growth Rate

The monthly growth rate in sales compared to the previous month is summarized as follows:

| Month | Growth Rate (%) |
|-------|-----------------|
| Feb   | -75.57          |
| Mar   | 21.10           |
| Apr   | 11.35           |
| May   | -15.75          |
| Jun   | 23.73           |
| Jul   | 249.81          |
| Aug   | -40.71          |
| Sep   | -18.47          |
| Oct   | 51.37           |
| Nov   | 32.02           |
| Dec   | -74.92          |

**Explanation**: The growth rate shows significant variability, with July having an exceptional growth rate of 249.81%, indicating a substantial increase in sales. In contrast, February and December experienced notable declines, which could be due to seasonal variations or specific market conditions.

### Seasonal Trends Analysis

The average sales for each month are:

| Month | Average Sales (£) |
|-------|--------------------|
| Apr   | 2,051.00           |
| Aug   | 4,434.00           |
| Dec   | 1,812.00           |
| Feb   | 1,521.00           |
| Jan   | 6,226.00           |
| Jul   | 7,479.00           |
| Jun   | 2,138.00           |
| Mar   | 1,842.00           |
| May   | 1,728.00           |
| Nov   | 7,224.00           |
| Oct   | 5,472.00           |
| Sep   | 3,615.00           |

**Explanation**: This table shows monthly sales averages. High sales in January, July, and November may reflect seasonal trends or successful marketing campaigns. Lower sales in February and December could be due to reduced consumer spending after major holidays.

### Sales Distribution Analysis

- **Mean Sales**: £3,795.17
- **Median Sales**: £2,876.50
- **Standard Deviation**: £2,285.73
- **Minimum Sales**: £1,521.00
- **Maximum Sales**: £7,479.00

**Explanation**: The mean and median sales provide insight into the central tendency, while the standard deviation indicates the degree of variability. The large standard deviation suggests significant fluctuations in monthly sales.

### Simulated Year-on-Year Comparison

Here’s a simulated year-on-year comparison of sales:

| Month | Previous Year Sales | Current Year Sales | Year-on-Year Change (%) |
|-------|----------------------|--------------------|--------------------------|
| Jan   | £4,268.03            | £6,226.00          | 45.88                    |
| Feb   | £5,325.03            | £1,521.00          | -71.44                   |
| Mar   | £6,921.53            | £1,842.00          | -73.39                   |
| Apr   | £3,108.82            | £2,051.00          | -34.03                   |
| May   | £6,099.86            | £1,728.00          | -71.67                   |
| Jun   | £6,593.36            | £2,138.00          | -67.57                   |
| Jul   | £2,533.70            | £7,479.00          | 195.18                   |
| Aug   | £3,235.83            | £4,434.00          | 37.03                    |
| Sep   | £2,918.60            | £3,615.00          | 23.86                    |
| Oct   | £3,859.29            | £5,472.00          | 41.79                    |
| Nov   | £6,507.86            | £7,224.00          | 11.00                    |
| Dec   | £6,073.73            | £1,812.00          | -70.17                   |

**Explanation**: The simulated year-on-year change shows the percentage change in sales compared to a simulated previous year's sales. Notably, July's sales saw a significant increase, while February and December experienced large declines, which might be worth investigating further.

### Expenditure Analysis

The correlation coefficient between sales and expenditure is -0.35.

**Explanation**: The negative correlation suggests that higher expenditure is associated with lower sales, or vice versa. This could indicate inefficiencies in how expenditure impacts sales or other factors affecting performance.

## Visualizations

### 1. Monthly Sales and Growth Rate

```python
import matplotlib.pyplot as plt

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
```

**Explanation**: This dual-axis plot shows monthly sales and the corresponding growth rates. The blue line represents sales, while the red dashed line shows the growth rate. This visualization highlights how sales performance and growth rates vary over the months, with July standing out due to its exceptional growth rate.

### 2. Seasonal Trends Visualization

```python
import seaborn as sns

plt.figure(figsize=(10, 6))
sns.barplot(x=seasonal_trends.index, y=seasonal_trends.values, color='teal')
plt.title('Average Monthly Sales (Seasonal Trends)', fontsize=16)
plt.xlabel('Month')
plt.ylabel('Average Sales (£)')
plt.xticks(rotation=45)
plt.grid(False)  # Remove grid lines
plt.tight_layout()
plt.show()
```

**Explanation**: This bar chart shows average sales for each month, providing a clear view of seasonal trends. The highest bars indicate peak sales periods (e.g., January, July), while lower bars reveal months with reduced sales. This visualization helps in understanding monthly sales performance and seasonal fluctuations.

### 3. Sales Distribution Visualization

```python
plt.figure(figsize=(10, 6))
sns.histplot(data['sales'], bins=10, kde=True, color='skyblue')
plt.title('Sales Distribution', fontsize=16)
plt.xlabel('Sales (£)')
plt.ylabel('Frequency')
plt.grid(False)  # Remove grid lines
plt.tight_layout()
plt.show()
```

**Explanation**: The histogram with a KDE (Kernel Density Estimate) overlay displays the distribution of sales figures. The KDE smooths the histogram, providing a continuous estimate of the sales distribution. This helps in understanding the frequency and spread of sales amounts. The use of KDE is beneficial for visualizing the underlying distribution and can be improved by adjusting the bandwidth parameter to better capture data patterns.

### 4. Simulated Year-on-Year Comparison Visualization

```python
plt.figure(figsize=(14, 7))
plt.plot(data['month'], data['sales'], marker='o', linestyle='-', label='Current Year Sales', color='#1f77b4')
plt.plot(data['month'], data['previous_year_sales'], marker='o', linestyle='--', label='Previous Year Sales', color='#ff7f0e')
plt.title('Year-on-Year Sales Comparison', fontsize=16)
plt.xlabel('Month')
plt.ylabel('Sales (£)')
plt.legend()
plt.grid(False)

  # Remove grid lines
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

**Explanation**: This line plot compares sales for the current year with simulated previous year sales. The solid line represents current year sales, while the dashed line represents the simulated previous year. This visualization helps in understanding trends and changes in sales over time, highlighting months with significant differences.

### 5. Expenditure Analysis Visualization

```python
plt.figure(figsize=(10, 6))
correlation_matrix = data[['sales', 'expenditure']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, vmin=-1, vmax=1)
plt.title('Correlation Heatmap between Sales and Expenditure', fontsize=16)
plt.grid(False)  # Remove grid lines
plt.tight_layout()
plt.show()
```

**Explanation**: The heatmap visualizes the correlation between sales and expenditure. The color intensity reflects the strength and direction of the correlation, with blue indicating negative correlation and red indicating positive correlation. The negative correlation suggests an inverse relationship between sales and expenditure, which could be due to various factors such as inefficiencies in spending.

## Recommendations and Improvements

1. **Additional Data**: Including more granular data (e.g., regional or product-specific sales) could provide deeper insights.
2. **Seasonal Adjustments**: Analyzing and adjusting for seasonal factors can improve sales forecasting and planning.
3. **Expenditure Insights**: Investigating expenditure patterns in more detail could reveal underlying causes of the negative correlation with sales.
4. **Advanced Modeling**: Implementing time series models or machine learning techniques could enhance the analysis, particularly for trend forecasting and anomaly detection.

This detailed analysis and visualization provide a comprehensive view of the sales data, uncovering trends and relationships that can inform strategic decisions.
