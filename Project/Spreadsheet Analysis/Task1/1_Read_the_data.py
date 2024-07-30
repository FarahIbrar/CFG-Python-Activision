import pandas as pd
import os

# Step 1: Read the data from the sales.csv file
def load_data(file_path): # `def` is used to define a function. A function is a block of reusable code that performs a specific task.
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
        print("\nHere's the complete sales data preview:\n")
        print(data.to_string(index=False)) # Converts the entire DataFrame to a string format and prints it without the row indices.
    else:
        print("No data to display.")

# Main execution
if __name__ == "__main__":
    # Set the file path relative to the script location
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, '..', 'Data file', 'sales.csv')  # Ensure the file is in the "Data file" folder

    sales_data = load_data(file_path)
    display_data(sales_data)

