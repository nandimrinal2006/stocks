import pandas as pd
import argparse

def filter_xls_rows(input_file, output_file, order_status, column_name, target_value):
    #input_file = "order_files/" + input_file 
    try:
        # Read the .xls file
        df = pd.read_excel(input_file)

        # Filter the rows where the column matches the target value
        if order_status.lower() == "executed":  
            filtered_df = df[df[column_name] >= target_value] 
        elif order_status.lower() == "pending": 
            filtered_df = df[df[column_name] < target_value]

        # Write the filtered rows to a new .xls file 
        filtered_df.to_excel(output_file, index=False)

        print(f"Filtered data saved to '{output_file}' successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
#input_xls = "order_files/Orders_sell_all.xlsx"
output_xls = "order_files/Filtered_data.xlsx"
column_to_check = "Exec. Qty"
target_min_value = 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find column number in Excel file.")
    parser.add_argument("input_file", help="Name of the Excel (.xlsx) file")
    parser.add_argument("order_status", help="Type of orders status needed: Executed / Pending")

args = parser.parse_args()
#find_column_number(args.input_file, args.target_column_name)

if args.input_file=="":
    args.input_file="Orders_sell_all.xlsx" 
if args.order_status=="":
    args.order_status="Pending" 

args.input_file="order_files/"+args.input_file
  
filter_xls_rows(args.input_file, output_xls, args.order_status, column_to_check, target_min_value)


