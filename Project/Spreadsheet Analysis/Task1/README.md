# Task 1: Load and Display Sales Data

This step involves reading sales data from a CSV file and displaying the entire dataset. This README provides an explanation of the key components of the script, including function definitions and the main execution block.

The following code accomplishes this task using Python in Pycharm.

## Code Explanation

```python
import pandas as pd
import os

# Step 1: Read the data from the sales.csv file
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print("Data successfully loaded!")
        return data
    except FileNotFoundError:
        print("The file was not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Step 2: Display the data in a clear manner
def display_data(data):
    if data is not None:
        print("\nHere's the complete sales data:\n")
        print(data.to_string(index=False))
    else:
        print("No data to display.")

# Main execution
if __name__ == "__main__":
    # Set the file path relative to the script location
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, '..', 'Data file', 'sales.csv')  # Ensure the file is in the "Data file" folder

    sales_data = load_data(file_path)
    display_data(sales_data)
```

## Explanation

### `def`: Defining Functions

In Python, `def` is used to define a function. A function is a reusable block of code that performs a specific task. Functions help organize code, make it reusable, and improve readability.

#### Functions in This Script

1. **`load_data(file_path)`**:
   - **Purpose**: Reads data from the given CSV file.
   - **Parameters**: `file_path` - the path to the CSV file.
   - **Functionality**:
     - Attempts to read the CSV file using `pandas.read_csv()`.
     - If the file is successfully read, it prints a success message and returns the data.
     - If the file is not found, it catches the `FileNotFoundError` and prints an error message.
     - Handles any other exceptions that may occur and prints an error message.

2. **`display_data(data)`**:
   - **Purpose**: Displays the entire dataset in a clear format.
   - **Parameters**: `data` - the DataFrame containing the sales data.
   - **Functionality**:
     - Checks if `data` is not `None`.
     - If `data` is valid, it prints the entire DataFrame using `data.to_string(index=False)`.
     - If `data` is `None`, it prints a message indicating that there's no data to display.


### Main Execution Block

### Understanding the Main Execution Block

The main execution block is used to ensure that certain parts of the code only run when the script is executed directly, not when it's imported as a module into another script. This is achieved using the `if __name__ == "__main__":` statement.

#### Simplified Explanation

1. **Purpose**: Ensures that specific code runs only when the script is run directly. This is useful for running tests or executing parts of the script that should not run when the script is imported elsewhere.

2. **How It Works**:
   - Every Python script has a special built-in variable called `__name__`.
   - When you run a script directly, Python sets this variable to `"__main__"`.
   - If the script is imported into another script, the `__name__` variable is set to the name of the script/module, not `"__main__"`.

3. **When to Use It**: Use this block to control what parts of your script should execute when running directly, and what should be available for import without executing unintended code.

#### Example in This Script

```python
if __name__ == "__main__":
    # Set the file path relative to the script location
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, '..', 'Data file', 'sales.csv')  # Ensure the file is in the "Data file" folder

    sales_data = load_data(file_path)  # Load the data from the CSV file
    display_data(sales_data)           # Display the entire dataset
```

- **`if __name__ == "__main__":`**: Checks if the script is being run directly.
  - If true, it executes the code inside this block.
  - If false, it does not execute the code inside this block, making it safe for import.

- **`current_dir = os.path.dirname(os.path.abspath(__file__))`**: Gets the directory where the script is located.

- **`file_path = os.path.join(current_dir, '..', 'Data file', 'sales.csv')`**: Constructs the path to the CSV file by navigating to the "Data file" folder.

- **`sales_data = load_data(file_path)`**: Calls the `load_data` function to read data from the CSV file.

- **`display_data(sales_data)`**: Calls the `display_data` function to print the dataset.

### Why It’s Important

Using the main execution block keeps your code organized and prevents unintended code execution when the script is imported as a module. It helps manage code execution and reuse effectively.
