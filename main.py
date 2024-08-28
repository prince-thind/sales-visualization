import pandas as pd

# Load dataset
df = pd.read_csv('./data/data.csv', encoding='ISO-8859-1')

# Data Cleaning
df.dropna(subset=['CustomerID'], inplace=True)
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], format='%m/%d/%y %H:%M')

# Save the cleaned data for further analysis
df.to_csv('./output/cleaned_sales_data.csv', index=False)

print("Data loaded, cleaned, and saved to './output/cleaned_sales_data.csv'.")
