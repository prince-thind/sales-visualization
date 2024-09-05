# **Sales Data Analysis and Trend Visualization**

## **Project Overview**

This project aims to analyze sales data from a retail dataset by cleaning and preparing the data, calculating total sales, and visualizing monthly sales trends. The project walks through the process of data cleaning, calculating monthly sales, and visualizing these trends over time. The final output includes cleaned data, aggregated sales data by month, and a plot showing sales trends.

---

## **Key Features**

### 1. **Data Cleaning**

- **Removing Missing Values:** The dataset is cleaned by removing rows where `CustomerID` is missing.
- **Date Handling:** The `InvoiceDate` column is converted to a datetime format to ensure that time-based calculations can be made accurately.
- The cleaned dataset is saved as `cleaned_sales_data.csv` for further analysis.

### 2. **Sales Calculation**

- **Total Sales Calculation:** The total sales per transaction are calculated by multiplying the quantity of items by their unit price. This results in a new `Total_Sales` column.
- **Monthly Aggregation:** The data is aggregated by month to calculate the total sales for each month. This aggregated data is saved as `monthly_sales_data.csv`.

### 3. **Visualization**

- **Sales Trends Visualization:** A line plot is generated to visualize sales trends over time, highlighting the fluctuations in total sales month by month.
- The plot is saved as `sales_trends.png`.

---

## **Project Workflow**

1. **Data Loading and Cleaning:**

   - Load the dataset (`data.csv`) from the `./data/` folder.
   - Clean the data by removing missing customer IDs and converting invoice dates to the correct datetime format.
   - Save the cleaned data to `./output/cleaned_sales_data.csv`.

2. **Sales Calculation:**

   - Load the cleaned data.
   - Calculate the total sales for each transaction by multiplying `Quantity` and `UnitPrice`.
   - Aggregate sales data by month, calculating the total monthly sales.
   - Save the monthly aggregated data to `./output/monthly_sales_data.csv`.

3. **Sales Trend Visualization:**
   - Load the monthly sales data.
   - Create a line plot to visualize the sales trends over time, highlighting any peaks or drops in sales.
   - Save the plot to `./output/sales_trends.png`.

---

## **Input and Output Information**

- **Input:**

  - The input data should be stored in a file named `data.csv` located in the `./data/` folder.
  - The dataset should include the following columns:
    - `CustomerID`: Unique identifier for each customer.
    - `InvoiceDate`: Date and time of each transaction.
    - `Quantity`: Number of units purchased in each transaction.
    - `UnitPrice`: Price per unit for each item.

- **Output:**
  - `cleaned_sales_data.csv`: The cleaned sales data saved in the `./output/` folder.
  - `monthly_sales_data.csv`: The aggregated monthly sales data saved in the `./output/` folder.
  - `sales_trends.png`: A line plot showing sales trends over time, saved in the `./output/` folder.

---

## **Technologies and Libraries Used**

- **Python**: The programming language used for data manipulation, analysis, and visualization.
- **Pandas**: A library used for data loading, cleaning, and aggregation.
- **Matplotlib and Seaborn**: Libraries used for data visualization, specifically for creating line plots to track trends over time.
- **CSV**: File format for input and output data storage.

---

## **Project Files and Structure**

- `data/`: Contains the input data file (`data.csv`).
- `output/`: Contains the output files, including:
  - `cleaned_sales_data.csv`: Cleaned and prepared data.
  - `monthly_sales_data.csv`: Aggregated monthly sales data.
  - `sales_trends.png`: Visual representation of monthly sales trends.

---

## **How to Run the Project**

1. **Install the required Python libraries**:

   - Install the required dependencies using the following command:
     ```bash
     pip install pandas matplotlib seaborn
     ```

2. **Run the Python script**:
   - Run the script to clean the data, calculate total sales, and generate visualizations.
   - The cleaned data, monthly sales data, and sales trends plot will be saved in the `./output/` folder.

---

## **Next Steps and Improvements**

- **Enhance Visualization**: Add additional data points like average order value or number of transactions to gain more insights into sales trends.
- **Advanced Analysis**: Perform deeper statistical analysis to understand seasonality, customer behavior, or sales forecasting.
- **Interactive Dashboards**: Implement tools like **Power BI** or **Tableau** to create dynamic dashboards for real-time monitoring of sales trends.

---
