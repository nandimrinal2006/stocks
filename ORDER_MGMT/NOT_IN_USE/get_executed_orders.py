import pandas as pd

def filter_xls_rows(input_file, output_file, column_name, target_value):
    try:
        # Read the .xls file
        df = pd.read_excel(input_file)

        # Filter the rows where the column matches the target value
        filtered_df = df[df[column_name] >= target_value]

        # Write the filtered rows to a new .xls file
        filtered_df.to_excel(output_file, index=False)

        print(f"Filtered data saved to '{output_file}' successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_xls = "order_files/Orders_sell_all.xlsx"
output_xls = "order_files/Orders_sell_executed.xlsx"
column_to_check = "Exec. Qty"
target_min_value = 1

filter_xls_rows(input_xls, output_xls, column_to_check, target_min_value)
