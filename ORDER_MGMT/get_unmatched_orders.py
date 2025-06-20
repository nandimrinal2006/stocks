import pandas as pd
import os 
import argparse
   
#Purpose :  Get unmatced orders between any 2 order files
import pandas as pd

def compare_excels_on_columns(file1, file2, columns, output_file):
    # Read both Excel files
    df1 = pd.read_excel(file1, engine='openpyxl')
    df2 = pd.read_excel(file2, engine='openpyxl')

    # Check if the columns exist in both files
    for col in columns:
        if col not in df1.columns or col not in df2.columns:
            raise ValueError(f"Column '{col}' not found in both files")

    # Find rows in df1 that do NOT exist in df2 based on the selected columns
    merged = df1.merge(df2[columns].drop_duplicates(), on=columns, how='left', indicator=True)
    not_in_file2 = merged[merged['_merge'] == 'left_only'].drop(columns=['_merge'])

    # Save unmatched rows to a new Excel file
    not_in_file2.to_excel(output_file, index=False)
    print(f"Unmatched rows saved to {output_file}")

 

# Specify the 3 column names to compare (exact names as in Excel)
columns_to_compare = ['Symbol/Contract', 'Ord. Qty', 'Order Price']  



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find column number in Excel file.")
    parser.add_argument("input_file_1", help="Name of the 1st Excel (.xlsx) file")
    parser.add_argument("input_file_2", help="Name of the 2nd Excel (.xlsx) file")

args = parser.parse_args()
#find_column_number(args.input_file, args.target_column_name)

# Example usage:
#file1 = 'file1.xlsx'            # First Excel file
#file2 = 'file2.xlsx'            # Second Excel file
output = 'order_files/rows_not_in_file2.xlsx'    # Output Excel file

file1="order_files/"+args.input_file_1
file2="order_files/"+args.input_file_2
  
compare_excels_on_columns(file1, file2, columns_to_compare, output)


##################################################################
#### Convert xls file into csv : NOT IN USE : JUST FOR BACKUP ####
##################################################################
def excel_to_csv(input_file, output_file=None):
    # Detect file extension
    file_extension = os.path.splitext(input_file)[1]

    if file_extension not in ['.xls', '.xlsx']:
        raise ValueError("Input file must be .xls or .xlsx")

    # Read Excel file (all sheets)
    excel_file = pd.ExcelFile(input_file)

    # For each sheet, convert to CSV
    for sheet_name in excel_file.sheet_names:
        df = excel_file.parse(sheet_name)
        # Generate output CSV filename if not provided
        if output_file is None:
            csv_file = f"{os.path.splitext(input_file)[0]}_{sheet_name}.csv"
        else:
            csv_file = output_file
        df.to_csv(csv_file, index=False)
        print(f"Sheet '{sheet_name}' converted to {csv_file}")

# Example usage:
input_path = "order_files/Orders_sell_all.xlsx"   # Change this to your file path
#excel_to_csv(input_path)   