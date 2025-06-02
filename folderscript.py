import subprocess
import sys
import os

# Step 1: Automatically install required packages
try:
    import pandas as pd
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas", "openpyxl"])
    import pandas as pd

# Step 2: Check if Excel file exists
excel_file = "names.xlsx"
if not os.path.exists(excel_file):
    print(f"❌ Excel file '{excel_file}' not found. Please place it in the same folder.")
    sys.exit(1)

# Step 3: Read names and create folders
try:
    df = pd.read_excel(excel_file)
    names = df['Name'].dropna().unique()

    for name in names:
        folder_name = str(name).strip()
        if folder_name:
            try:
                os.makedirs(folder_name)
                print(f"✅ Created folder: {folder_name}")
            except FileExistsError:
                print(f"⚠️ Folder already exists: {folder_name}")
except Exception as e:
    print("❌ Error reading Excel file or creating folders:", e)