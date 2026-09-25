import pandas as pd

# Direct file path
file_path = r"C:\Data_Analyst\HealthCare Analytics\Python\archive\hospital_readmission_risk_10000.csv"

print(f"Loading from: {file_path}")
df = pd.read_csv(file_path)

print("\n=== DATASET OVERVIEW ===")
print(f"Total Rows: {df.shape[0]}")
print(f"Total Columns: {df.shape[1]}\n")

print("=== COLUMN NAMES & DATA TYPES ===")
print(df.dtypes)

print("\n=== FIRST 3 ROWS ===")
print(df.head(3).T)

print("\n=== MISSING VALUES COUNT ===")
print(df.isnull().sum())
