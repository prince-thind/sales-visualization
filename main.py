import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('./data/data.csv', encoding='ISO-8859-1')

# Data Cleaning
df.dropna(subset=['CustomerID'], inplace=True)
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], format='%m/%d/%y %H:%M')

# Save the cleaned data for further analysis
df.to_csv('./output/cleaned_sales_data.csv', index=False)

print("Data loaded, cleaned, and saved to './output/cleaned_sales_data.csv'.")
import pandas as pd

# Load cleaned dataset
df = pd.read_csv('./output/cleaned_sales_data.csv')

# Ensure 'InvoiceDate' is in datetime format
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], format='%m/%d/%y %H:%M', errors='coerce')

# Drop rows where 'InvoiceDate' conversion failed (NaT)
df.dropna(subset=['InvoiceDate'], inplace=True)

# Calculate total sales per row
df['Total_Sales'] = df['Quantity'] * df['UnitPrice']

# Aggregate data by month for sales trends
df['Month'] = df['InvoiceDate'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Total_Sales'].sum().reset_index()

# Save the aggregated data
monthly_sales.to_csv('./output/monthly_sales_data.csv', index=False)

print("Monthly sales trends calculated and saved to './output/monthly_sales_data.csv'.")


# Load monthly sales data
monthly_sales = pd.read_csv('./output/monthly_sales_data.csv')

# Ensure correct data types
monthly_sales['Month'] = monthly_sales['Month'].astype(str)
monthly_sales['Total_Sales'] = pd.to_numeric(monthly_sales['Total_Sales'], errors='coerce')
monthly_sales.dropna(subset=['Total_Sales'], inplace=True)

# Visualize monthly sales trends
plt.figure(figsize=(10, 6))
sns.lineplot(x='Month', y='Total_Sales', data=monthly_sales)
plt.title('Sales Trends Over Time')
plt.xticks(rotation=45)

# Save the plot to a file
plt.savefig('./output/sales_trends.png')

print("Plot saved as './output/sales_trends.png'.")
