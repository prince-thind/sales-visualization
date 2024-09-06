from load_and_clean_data import load_and_clean_data
from calculate_total_sales import calculate_total_sales
from aggregate_monthly_sales import aggregate_monthly_sales
from ensure_data_types import ensure_data_types
from visualize_sales_trends import visualize_sales_trends

def main():
    input_file = './data/data.csv'
    output_cleaned_data = './output/cleaned_sales_data.csv'
    output_monthly_data = './output/monthly_sales_data.csv'
    output_plot = './output/sales_trends.png'

    df = load_and_clean_data(input_file, output_cleaned_data)
    df = calculate_total_sales(df)
    monthly_sales = aggregate_monthly_sales(df, output_monthly_data)
    monthly_sales = ensure_data_types(monthly_sales)
    visualize_sales_trends(monthly_sales, output_plot)
    print('Data processing and visualization complete.')

if __name__ == '__main__':
    main()

