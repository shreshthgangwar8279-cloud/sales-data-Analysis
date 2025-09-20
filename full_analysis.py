import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------
# 1️⃣ Load the CSV file
# -----------------------
df = pd.read_csv("sales_data_sample.csv", encoding='latin1')

# Remove leading/trailing spaces from column names
df.columns = df.columns.str.strip()

# -----------------------
# 2️⃣ Select key columns
# -----------------------
columns_to_use = ['ORDERDATE', 'COUNTRY', 'PRODUCTLINE', 'SALES', 'QUANTITYORDERED']
df = df[columns_to_use]

# -----------------------
# 3️⃣ Rename columns for simplicity
# -----------------------
df = df.rename(columns={
    'ORDERDATE': 'OrderDate',
    'COUNTRY': 'Region',
    'PRODUCTLINE': 'Product',
    'SALES': 'Sales',
    'QUANTITYORDERED': 'Quantity'
})

# -----------------------
# 4️⃣ Data Cleaning
# -----------------------
# Convert OrderDate to datetime
df['OrderDate'] = pd.to_datetime(df['OrderDate'], errors='coerce')

# Convert numeric columns
df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')

# Drop rows with missing values in these columns
df = df.dropna(subset=['OrderDate', 'Region', 'Product', 'Sales', 'Quantity'])

# -----------------------
# 5️⃣ Basic Exploration
# -----------------------
print("Dataset shape:", df.shape)
print(df.head())
print("\nTotal sales by Product:")
print(df.groupby('Product')['Sales'].sum().sort_values(ascending=False))
print("\nTotal sales by Region:")
print(df.groupby('Region')['Sales'].sum().sort_values(ascending=False))
print("\nTop 5 orders by Sales:")
print(df.sort_values(by='Sales', ascending=False).head(5))

# -----------------------
# 6️⃣ Visualization
# -----------------------
plt.figure(figsize=(10,6))
sns.barplot(x=df.groupby('Product')['Sales'].sum().index,
            y=df.groupby('Product')['Sales'].sum().values)
plt.title("Total Sales by Product")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10,6))
sns.barplot(x=df.groupby('Region')['Sales'].sum().index,
            y=df.groupby('Region')['Sales'].sum().values)
plt.title("Total Sales by Region")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()

# Optional: Monthly Sales Trend
df['Month'] = df['OrderDate'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Sales'].sum()

plt.figure(figsize=(12,6))
monthly_sales.plot(marker='o')
plt.title("Monthly Sales Trend")
plt.ylabel("Sales")
plt.xlabel("Month")
plt.xticks(rotation=45)
plt.show()
