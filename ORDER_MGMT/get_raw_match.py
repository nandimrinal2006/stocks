import pandas as pd 
def extract_executed_rows(input_file, output_file):
    # 1. Load the Excel file
    # If your data is on a specific sheet, add sheet_name="SheetName" inside read_excel()
    df = pd.read_excel(input_file)
    
    # 2. Search the ENTIRE dataframe for the value "Executed"
    # .astype(str) ensures we can search numbers/dates safely without throwing errors
    mask = df.astype(str).apply(lambda row: row.str.contains(r'^Executed$', case=False, na=False)).any(axis=1)
    
    # 3. Filter the dataframe using the mask
    filtered_df = df[mask]
    
    # 4. Drop completely duplicate rows
    # keep='first' ensures the first occurrence of the row is retained
    clean_df = filtered_df.drop_duplicates()
    
    # 5. Save the result to a new Excel file
    # index=False prevents pandas from adding an extra column for row numbers
    clean_df.to_excel(output_file, index=False)
    
    print(f"Success! Found {len(clean_df)} unique rows containing 'Executed'. Saved to {output_file}")

# --- Configuration ---
INPUT_FILE_PATH = "order_files/OrderBook_Equity_1.xlsx"    # Replace with your actual file path
OUTPUT_FILE_PATH = "order_files/filtered_data.xlsx"

# Run the script
extract_executed_rows(INPUT_FILE_PATH, OUTPUT_FILE_PATH)