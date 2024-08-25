import pandas as pd
import sqlite3
from datetime import datetime

# Configuration
CSV_FILE_PATH = '/var/lib/jenkins/workspace/ETL_Pipeline/input_data.csv'
DATABASE_FILE = '/var/lib/jenkins/workspace/ETL_Pipeline/output_database.db'
TABLE_NAME = 'transformed_data'

# Extract
def extract(csv_file_path):
    df = pd.read_csv(csv_file_path)
    return df

# Transform
def transform(df):
    # Example transformation: filter rows and add a new column
    df = df[df['value'] > 10]
    df['transformation_date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return df

# Load
def load(df, database_file, table_name):
    conn = sqlite3.connect(database_file)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()

# Main ETL process
def main():
    df = extract(CSV_FILE_PATH)
    df_transformed = transform(df)
    load(df_transformed, DATABASE_FILE, TABLE_NAME)
    print("ETL process completed successfully.")

if __name__ == "__main__":
    main()
