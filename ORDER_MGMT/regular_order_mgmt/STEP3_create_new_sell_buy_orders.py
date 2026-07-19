import numpy as np
import pandas as pd

# 1. Load the Excel file 
print("Generate New Buy/Sell orders as per the executed Sell/Buy orders list provided, with your specified profit value. Both input and output as xlsx file : ") 
input_file = input("Enter the input file name: ")

# Prompt the user for the second input and assign it to 'text_two'
output_file = input("Enter the output/processed file name: ")

profit = int(input("Profit needed for each new order ( including tax etc. everithing) : "))


file_path = "order_files/"+input_file #input file 
df = pd.read_excel(file_path)

#add 2 new columns 
df["New Order Price"]="" 
df["New Order Type (Sell/Buy)"]="" 

# 2. Apply the conditional logic using numpy.where
# For 'Sell/Buy':
# If Buy/Sell is 'B' -> (650 / Quantity) + price
# If Buy/Sell is 'S' -> price - (650 / Quantity)
df["New Order Price"] = np.where(
    df["Order Type (Buy/Sell)"] == "B",
    (profit / df["Quantity"]) + df["Price"],
    np.where(
        df["Order Type (Buy/Sell)"] == "S",
        df["Price"] - (profit / df["Quantity"]),
        df["New Order Price"],  # Keeps existing value if it's neither B nor S
    ),
)

# For 'S/B':
# If Buy/Sell is 'B' -> 'S'
# If Buy/Sell is 'S' -> 'B'
df["New Order Type (Sell/Buy)"] = np.where(
    df["Order Type (Buy/Sell)"] == "B",
    "S",
    np.where(
        df["Order Type (Buy/Sell)"] == "S",
        "B",
        df["New Order Type (Sell/Buy)"],  # Keeps existing value if it's neither B nor S
    ),
)

# 3. Save the calculated data to a new Excel file
output_file_path = "order_files/"+output_file #output file 
df.to_excel(output_file_path, index=False)

print(f"Calculations complete! File saved as {output_file_path}")