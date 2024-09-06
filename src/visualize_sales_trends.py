import matplotlib.pyplot as plt
import seaborn as sns

def visualize_sales_trends(monthly_sales, output_plot):
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='Month', y='Total_Sales', data=monthly_sales)
    plt.title('Sales Trends Over Time')
    plt.xticks(rotation=45)
    plt.savefig(output_plot)

