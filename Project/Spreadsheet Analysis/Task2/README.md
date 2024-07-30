# Task 2: Aggregating Monthly Sales

This script performs data analysis on a CSV file containing sales data. It reads the data, aggregates sales figures, and displays them in two formats: a simple list and a formatted list with month names and sales figures in pounds (£).

## Script Breakdown

```Python
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
```

### 1. Importing Libraries

```python
import pandas as pd
import os
```

- **`pandas`**: Used for data manipulation and analysis. In this script, it reads and processes the CSV file.
- **`os`**: Used to check file paths and handle file-related operations.

### 2. Defining the File Path

```python
data_file_path = '../Data file/sales.csv'
```

- **`data_file_path`**: Specifies the relative path to the CSV file containing the sales data. This path is used to load the file into a DataFrame.

### 3. Loading the CSV File

```python
df = pd.read_csv(data_file_path)
```

- **`pd.read_csv()`**: Reads the CSV file into a Pandas DataFrame (`df`). This DataFrame now holds the sales data and allows for easy manipulation and extraction.

### 4. Extracting Sales Data and Month Names

```python
monthly_sales = df['sales'].tolist()
months = df['month'].tolist()
```

- **`df['sales'].tolist()`**: Converts the 'sales' column of the DataFrame into a list of sales figures.
- **`df['month'].tolist()`**: Converts the 'month' column of the DataFrame into a list of month names.

### 5. Combining Months and Sales Data

```python
monthly_sales_info = list(zip(months, monthly_sales))
```

- **`zip(months, monthly_sales)`**: Creates an iterator of tuples where each tuple contains a month and its corresponding sales figure.
- **`list(zip(...))`**: Converts the iterator into a list of tuples for easier processing and output.

### 6. Displaying Sales Figures as a Simple List

```python
print("Sales figures for each month:")
print(monthly_sales)
```

- **`print(monthly_sales)`**: Displays the list of sales figures in a straightforward list format. This provides a quick view of all sales data without additional context.

### 7. Displaying Sales Figures with Month Names (Formatted in Pounds)

```python
print("\nSales figures with months (in pounds):")
for month, sales in monthly_sales_info:
    print(f"{month.capitalize()}: £{sales:,.2f}")
```

- **`print("\nSales figures with months (in pounds):")`**: Prints a header for the formatted output.
- **`for month, sales in monthly_sales_info:`**: Iterates over each tuple in `monthly_sales_info`.
- **`print(f"{month.capitalize()}: £{sales:,.2f}")`**: Formats and prints each month with its sales figure in pounds (£), including commas as thousand separators and two decimal places. The `capitalize()` method ensures that month names are capitalized.

## Summary

- **Simple List Output**: Provides a raw list of sales figures for quick reference.
- **Formatted Output**: Offers a more readable view with month names and sales figures in pounds, making it easier to interpret the data.

This script is useful for basic data analysis and presentation of sales data, helping to understand sales trends and figures in a structured manner.
