def calculate_total_sales(df):
    df['Total_Sales'] = df['Quantity'] * df['UnitPrice']
    return df

