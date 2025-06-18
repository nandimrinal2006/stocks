import pandas as pd

def filter_xlsx(input_file, output_file):
    # Read the Excel file
    df = pd.read_excel(input_file, header=0, engine='openpyxl')

    # Show detected column names
    print("Detected Columns:", df.columns.tolist())

    # Clean column names
    df.columns = df.columns.str.strip().str.replace('\xa0', ' ')

    # Confirm 'Exec. Qty' exists
    if 'Exec. Qty' not in df.columns:
        raise ValueError(f"'Exec. Qty' column not found. Actual columns: {df.columns.tolist()}")

    # Convert 'Exec. Qty' to numeric (in case of text data)
    df['Exec. Qty'] = pd.to_numeric(df['Exec. Qty'], errors='coerce')

    # Filter rows where 'Exec. Qty' > 0
    filtered_df = df[df['Exec. Qty'] > 0]

    # Save the filtered data to a new Excel file
    filtered_df.to_excel(output_file, index=False)
    print(f"Filtered data saved to {output_file}")

# Example usage:
input_file = 'order_files/Orders_sell_all.xlsx'  # Input file name
output_file = 'order_files/Orders_ sellsellsellselltest_executed_18june2025.xlsx'             # Output file name
filter_xlsx(input_file, output_file)
