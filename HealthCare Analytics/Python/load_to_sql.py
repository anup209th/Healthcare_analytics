import urllib.parse
import pandas as pd
from sqlalchemy import create_engine

# 1. Credentials matching pgAdmin
DB_USER = "postgres"
DB_PASS = urllib.parse.quote_plus("123@nth876")
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "Healthcare_analytics"  # Exact name from pgAdmin

# 2. Load the processed CSV
csv_path = r"C:\Data_Analyst\HealthCare Analytics\Python\processed\patient_encounters_cleaned.csv"
df = pd.read_csv(csv_path)
print(f"Read {len(df)} rows from CSV.")

# 3. Create SQLAlchemy engine
engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# 4. Stream dataframe directly into PostgreSQL
print("Importing into PostgreSQL table 'patient_encounters'...")
df.to_sql("patient_encounters", engine, if_exists="replace", index=False)
print("Data import complete!")