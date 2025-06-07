# 📁 Auto Folder Creator from Excel

This Python script reads names from an Excel file and automatically creates a folder for each name. It also installs all required Python packages automatically — so you can run it in one go without manual setup.

---

## 🚀 Features

- 📄 Reads names from an Excel file (`names.xlsx`)
- 🗂️ Creates a folder for each unique name in the `Name` column
- 🧠 Skips empty or duplicate names
- 🔧 Automatically installs required Python packages (`pandas`, `openpyxl`)

---

## 📦 Requirements

- Python 3.x
- No pre-installed packages needed — the script installs everything it needs

---

## 📝 File Structure

```
project-folder/
│
├── names.xlsx             # Your Excel file with a "Name" column
├── auto_folder_creator.py # The Python script
└── (Generated folders)     # One folder per name from Excel
```

---

## 📥 How to Use

1. Make sure `names.xlsx` is in the same folder as the script.
2. Ensure the Excel file has a column named exactly `Name`.
3. Run the script:

```bash
python auto_folder_creator.py
```

The script will:
- Install `pandas` and `openpyxl` (if missing)
- Read names from the Excel file
- Create folders with those names in the same directory

---

## ⚠️ Notes

- The script checks if folders already exist to avoid overwriting.
- Folder names are stripped of extra spaces.
- Excel file must be `.xlsx` format (not `.xls` or `.csv`).

---

## 📌 Example

**Input Excel (`names.xlsx`)**
```
| Name         |
|--------------|
| Prathmesh    |
| Ayush        |
| Aasha        |
```

**Output Folders**
```
Prathmesh/
Ayush/
Aasha/
```

---