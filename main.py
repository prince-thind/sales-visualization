import pandas as pd

# Load dataset
df = pd.read_csv('./data/data.csv', encoding='ISO-8859-1')

# Data Cleaning
df.dropna(subset=['CustomerID'], inplace=True)
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], format='%m/%d/%y %H:%M')

# Save the cleaned data for further analysis
df.to_csv('./output/cleaned_sales_data.csv', index=False)

print("Data loaded, cleaned, and saved to './output/cleaned_sales_data.csv'.")

# Load cleaned dataset
df = pd.read_csv('./output/cleaned_sales_data.csv')

# Calculate total sales per row
df['Total_Sales'] = df['Quantity'] * df['UnitPrice']

# Aggregate data by month for sales trends
df['Month'] = df['InvoiceDate'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Total_Sales'].sum().reset_index()

# Save the aggregated data
monthly_sales.to_csv('./output/monthly_sales_data.csv', index=False)

print("Monthly sales trends calculated and saved to './output/monthly_sales_data.csv'.")
