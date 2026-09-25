import os
import pandas as pd
import numpy as np

# 1. Load Data
input_path = r"C:\Data_Analyst\HealthCare Analytics\Python\archive\hospital_readmission_risk_10000.csv"
output_dir = r"C:\Data_Analyst\HealthCare Analytics\Python\processed"
os.makedirs(output_dir, exist_ok=True)

df = pd.read_csv(input_path)
print(f"Loaded {len(df)} records.")

# 2. Impute Missing Values
df["chronic_conditions"] = df["chronic_conditions"].fillna("None")
df["alcohol_use"] = df["alcohol_use"].fillna("Not Reported")

# 3. Clinical & Operational Feature Engineering

# Binary High Risk Flag for simple aggregations
df["is_high_risk"] = (df["readmission_risk"] == "High").astype(int)

# Age Cohort
age_bins = [0, 35, 50, 65, 120]
age_labels = ["18-35", "36-50", "51-65", "65+"]
df["age_group"] = pd.cut(df["age"], bins=age_bins, labels=age_labels, right=True)

# Length of Stay (LoS) Tiers
los_bins = [-1, 3, 7, 14, 100]
los_labels = [
    "01. Short (1-3d)",
    "02. Medium (4-7d)",
    "03. Extended (8-14d)",
    "04. Long-term (>14d)",
]
df["los_tier"] = pd.cut(
    df["length_of_stay"], bins=los_bins, labels=los_labels, right=True
)

# Clinical Comorbidity Burden Index (Rule-based composite risk score 0 - 5)
df["clinical_risk_score"] = (
    (df["age"] >= 65).astype(int)
    + (df["last_glucose"] > 140.0).astype(int)
    + (df["last_creatinine"] > 1.2).astype(int)
    + (df["num_previous_admissions"] >= 3).astype(int)
    + (df["last_hemoglobin"] < 12.0).astype(int)
)

# Glycemic Control Category
conditions = [
    (df["last_glucose"] < 100),
    (df["last_glucose"] >= 100) & (df["last_glucose"] <= 140),
    (df["last_glucose"] > 140),
]
choices = ["Normal (<100)", "Pre-Diabetic (100-140)", "Hyperglycemic (>140)"]
df["glycemic_status"] = np.select(conditions, choices, default="Normal (<100)")

# 4. Save Processed Master File
processed_path = os.path.join(output_dir, "patient_encounters_cleaned.csv")
df.to_csv(processed_path, index=False)

print("\n=== ETL COMPLETE ===")
print(f"Cleaned dataset saved to: {processed_path}")
print(f"Total Rows: {df.shape[0]}, Total Columns: {df.shape[1]}")
print(df[["is_high_risk", "age_group", "los_tier", "clinical_risk_score", "glycemic_status"]].head(5))