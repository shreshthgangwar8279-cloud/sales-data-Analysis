import pandas as pd

# Try reading CSV with encoding
df = pd.read_csv("sales_data_sample.csv", encoding='latin1')


df.columns = df.columns.str.strip()

# Basic info about column and data types
print(df.info())

# Count missing values per column
print(df.isnull().sum())

print(df.columns.tolist())

# Remove leading/trailing spaces from column names
df.columns = df.columns.str.strip()
print(df.columns.tolist())

columns_to_use = ['ORDERDATE', 'COUNTRY', 'PRODUCTLINE', 'SALES', 'QUANTITYORDERED']
df = df[columns_to_use]
print(df.head())

