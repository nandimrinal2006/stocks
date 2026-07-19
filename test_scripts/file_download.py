import os
import shutil
import sys
from tkinter import Tk, filedialog

def download_file_to_user_choice(source_file_path):
    # 1. Safety check: Make sure the file we want to give them actually exists
    if not os.path.exists(source_file_path):
        print(f"❌ Error: The file at '{source_file_path}' does not exist.", file=sys.stderr)
        return False

    # Initialize tkinter and hide the main window
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)

    # Extract the original file name and extension (e.g., "report.xlsx")
    file_name = os.path.basename(source_file_path)
    _, file_extension = os.path.splitext(file_name)

    print(f"Opening 'Save As' dialogue for: {file_name}")
    
    # 2. Open the "Save As" dialogue box
    output_path = filedialog.asksaveasfilename(
        title="Download / Save File As",
        initialfile=file_name,  # Pre-fills the original file name for the user
        defaultextension=file_extension,
        filetypes=[("Original File Type", f"*{file_extension}"), ("All Files", "*.*")]
    )
    
    # Handle user canceling the dialogue box
    if not output_path:
        print("❌ Operation cancelled: No download location selected.")
        return False

    try:
        # 3. Copy the file byte-for-byte to the user's chosen location
        shutil.copy2(source_file_path, output_path)
        print(f"\n🎉 Success! File downloaded successfully.")
        print(f" Saved to: {output_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error saving file: {e}", file=sys.stderr)
        return False

# --- HOW TO RUN IT ---
# Pass the path of the file you want the user to be able to "download"
FILE_TO_DOWNLOAD = "my_processed_files/upwork_calc.xlsx" 
download_file_to_user_choice(FILE_TO_DOWNLOAD)