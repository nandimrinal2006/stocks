import os
import shutil
import sys
from tkinter import Tk, filedialog

def upload_and_save_to_folder(destination_folder):
    # Initialize tkinter and hide the main window
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    
    # Ensure your specific target folder actually exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"Created destination directory: {destination_folder}")

    print("Opening file dialogue... Please select any file.")
    
    # Open file picker allowing *any* file type
    input_path = filedialog.askopenfilename(
        title="Select Any File to Upload",
        filetypes=[("All Files", "*.*")]  # This unlocks every file type
    )
    
    # Handle user canceling
    if not input_path:
        print("❌ Operation cancelled: No file selected.")
        return None

    # Extract the original file name (e.g., "data.xlsx")
    file_name = os.path.basename(input_path)
    
    # Construct the final save path (e.g., "my_storage/data.xlsx")
    destination_path = os.path.join(destination_folder, file_name)
    
    try:
        # Copy the file byte-for-byte to the new folder
        shutil.copy2(input_path, destination_path)
        print(f"\n🎉 Success! File uploaded and saved.")
        print(f" From: {input_path}")
        print(f" To:   {destination_path}")
        return destination_path
        
    except Exception as e:
        print(f"❌ Error copying file: {e}", file=sys.stderr)
        return None

# --- HOW TO RUN IT ---
# Change "my_processed_files" to whatever folder name you want
TARGET_FOLDER = "my_processed_files" 
upload_and_save_to_folder(TARGET_FOLDER)