from pathlib import Path

import pandas as pd  # pip install pandas openpyxl
from docxtpl import DocxTemplate  # pip install docxtpl
import sys, os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

base_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
word_template_path = base_dir / "Prideone_IC SOW_Hallmark_Automation_template.docx"
excel_path = base_dir / "data.xlsx"
output_dir = base_dir / "OUTPUT SOW Documents"
application_path = os.path.dirname(sys.executable)


# Create output folder for the word documents
output_dir.mkdir(exist_ok=True)

# Convert Excel sheet to pandas dataframe
df = pd.read_excel(excel_path, sheet_name="SOW")

# Keep only date part YYYY-MM-DD (not the time)
df["Start"] = pd.to_datetime(df["Start"]).dt.strftime('%m/%d/%Y')
df["End"] = pd.to_datetime(df["End"]).dt.strftime('%m/%d/%Y')


# Iterate over each row in df and render word document
for record in df.to_dict(orient="records"):
    doc = DocxTemplate(word_template_path)
    doc.render(record)
    output_path = output_dir / f"{record['Name']}-contract.docx"
    doc.save(output_path)
