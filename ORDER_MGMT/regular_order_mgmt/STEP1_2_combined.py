import pandas as pd 

#Step 1: get_raw_match by a column value ( order status in this case) 
def extract_executed_rows(input_file, output_file, search_text):
    # 1. Load the Excel file
    # If your data is on a specific sheet, add sheet_name="SheetName" inside read_excel()
    df = pd.read_excel(input_file)
    
    # 2. Search the ENTIRE dataframe for the value "Executed"
    # .astype(str) ensures we can search numbers/dates safely without throwing errors
    mask = df.astype(str).apply(lambda row: row.str.contains(r'^'+search_text+'$', case=False, na=False)).any(axis=1)
    
    # 3. Filter the dataframe using the mask
    filtered_df = df[mask]
    
    # 4. Drop completely duplicate rows
    # keep='first' ensures the first occurrence of the row is retained
    clean_df = filtered_df.drop_duplicates()
    
    # 5. Save the result to a new Excel file
    # index=False prevents pandas from adding an extra column for row numbers
    clean_df.to_excel(output_file, index=False)
    
    print(f"Success! Found {len(clean_df)} unique rows containing '"+search_text+"'. Saved to {output_file}")

# --- Configuration ---
print("Get all rows of an Excel file with a text in any cell, into another new excel file: ") 
input_file = input("Enter the input file name: ")

# Prompt the user for the second input and assign it to 'text_two'
#output_file = input("Enter the output/processed file name: ")
output_file = "Raw_Searched_"+input_file 

search_text = input("Enter the text to search:") 

INPUT_FILE_PATH = "order_files/"+input_file    # Replace with your actual file path
OUTPUT_FILE_PATH = "order_files/"+output_file

# Run the script
extract_executed_rows(INPUT_FILE_PATH, OUTPUT_FILE_PATH, search_text) 





#step2 : XLSX_2_XLSX_Column_Mapping 
def col_letter_to_index(col_letter):
    """Converts Excel column letters (A, B, C, ..., AA, etc.) to a 0-based index."""
    col_letter = col_letter.upper().strip()
    exp = 0
    col_index = 0
    for char in reversed(col_letter):
        col_index += (ord(char) - 64) * (26 ** exp)
        exp += 1
    return col_index - 1  # Pandas uses 0-based indexing

def process_excel(input_file, output_file, mapping_str):
    try:
        # 1. Parse the mapping string (e.g., "C=>Date, E=>Stock")
        # Creates a dictionary: { 2: "Date", 4: "Stock", ... }
        mappings = {}
        pairs = mapping_str.split(",")
        for pair in pairs:
            if "=>" in pair:
                letter, new_name = pair.split("=>")
                col_idx = col_letter_to_index(letter.strip())
                mappings[col_idx] = new_name.strip()
        
        # Sort indices to read them in chronological order
        target_indices = sorted(mappings.keys())
        
        # 2. Read only the specified columns from the source Excel file
        # header=None is temporarily used to safely grab by index, or we read normally
        print(f"Reading {input_file}...")
        df = pd.read_excel(input_file, usecols=target_indices)
        
        # 3. If your Excel sheet has headers, pandas might use them as column names. 
        # To accurately map our indices, we map the current dataframe column order.
        # We read the Excel file's raw column names at those position indexes:
        raw_df_all_cols = pd.read_excel(input_file, nrows=0)
        col_name_mapping = {raw_df_all_cols.columns[idx]: mappings[idx] for idx in target_indices}
        
        # Filter the DataFrame to our target columns and rename them
        final_df = df[[raw_df_all_cols.columns[idx] for idx in target_indices]].copy()
        final_df.rename(columns=col_name_mapping, inplace=True)
        
        # 4. Save to the new Excel file
        final_df.to_excel(output_file, index=False)
        print(f"Successfully created {output_file} with the mapped columns!")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found. Please check the path.")
    except Exception as e:
        print(f"An error occurred: {e}")

# --- Execution ---
user_mapping = "C=>Date, E=>Stock, G=>Order Type (Buy/Sell), H=>Quantity, K=>Price, P=>Status" 
 
print("Converts Excel column letters (A, B, C, ..., AA, etc.) to a set of provided column names. Input will be in this format: "+user_mapping) 
 
if __name__ == "__main__":
    # Get file paths from user
    #in_file = "order_files/"+input("Enter path to the source .xlsx file: ").strip()
    #out_file = "order_files/"+input("Enter path/name for the new output .xlsx file: ").strip() 
    in_file = OUTPUT_FILE_PATH #output file full path from step 1 
    out_file = "order_files/"+"Mapped_"+output_file 
    
    # Get user mapping input
    #if(input("Do you want any other column mapping rather the default one ("+user_mapping+"):y/n: ")=="y"): 
        #user_mapping = input("Enter column mapping (e.g., "+user_mapping+"): ").strip()
        
    # Run the process
    process_excel(in_file, out_file, user_mapping)