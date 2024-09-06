import pandas as pd

def ensure_data_types(monthly_sales):
    monthly_sales['Month'] = monthly_sales['Month'].astype(str)
    monthly_sales['Total_Sales'] = pd.to_numeric(monthly_sales['Total_Sales'], errors='coerce')
    monthly_sales.dropna(subset=['Total_Sales'], inplace=True)
    return monthly_sales

