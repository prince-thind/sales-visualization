import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load and clean data
def load_and_clean_data(filepath, output_cleaned_data):
    df = pd.read_csv(filepath, encoding='ISO-8859-1')
    df.dropna(subset=['CustomerID'], inplace=True)
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], format='%m/%d/%y %H:%M', errors='coerce')
    df.dropna(subset=['InvoiceDate'], inplace=True)
    df.to_csv(output_cleaned_data, index=False)
    return df

# calculate total sales
def calculate_total_sales(df):
    df['Total_Sales'] = df['Quantity'] * df['UnitPrice']
    return df

# aggregate data by month for sales trends
def aggregate_monthly_sales(df, output_monthly_data):
    df['Month'] = df['InvoiceDate'].dt.to_period('M')
    monthly_sales = df.groupby('Month')['Total_Sales'].sum().reset_index()
    monthly_sales.to_csv(output_monthly_data, index=False)
    return monthly_sales

# ensure correct data types in monthly sales data
def ensure_data_types(monthly_sales):
    monthly_sales['Month'] = monthly_sales['Month'].astype(str)
    monthly_sales['Total_Sales'] = pd.to_numeric(monthly_sales['Total_Sales'], errors='coerce')
    monthly_sales.dropna(subset=['Total_Sales'], inplace=True)
    return monthly_sales

# visualize monthly sales trends
def visualize_sales_trends(monthly_sales, output_plot):
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='Month', y='Total_Sales', data=monthly_sales)
    plt.title('Sales Trends Over Time')
    plt.xticks(rotation=45)
    plt.savefig(output_plot)

# Main run the entire workflow
def main():
    # File paths
    input_file = './data/data.csv'
    output_cleaned_data = './output/cleaned_sales_data.csv'
    output_monthly_data = './output/monthly_sales_data.csv'
    output_plot = './output/sales_trends.png'

    # 1: Load and clean data
    df = load_and_clean_data(input_file, output_cleaned_data)

    # 2: Calculate total sales
    df = calculate_total_sales(df)

    # 3: Aggregate monthly sales
    monthly_sales = aggregate_monthly_sales(df, output_monthly_data)

    # 4: Ensure correct data types
    monthly_sales = ensure_data_types(monthly_sales)

    # 5: Visualize sales trends
    visualize_sales_trends(monthly_sales, output_plot)

    print("Data processing and visualization complete.")

# Execute the main function
if __name__ == '__main__':
    main()

