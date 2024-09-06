def aggregate_monthly_sales(df, output_monthly_data):
    df['Month'] = df['InvoiceDate'].dt.to_period('M')
    monthly_sales = df.groupby('Month')['Total_Sales'].sum().reset_index()
    monthly_sales.to_csv(output_monthly_data, index=False)
    return monthly_sales

