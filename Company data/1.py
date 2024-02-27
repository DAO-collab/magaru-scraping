import pandas as pd

# Read the Excel file
df = pd.read_excel("SCH(0-26692).xlsx")

# Remove duplicates based on all columns
df = df.drop_duplicates()

# Save the updated DataFrame to a new Excel file
df.to_excel("a.xlsx", index=False)