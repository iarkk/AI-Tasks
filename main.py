import pandas as pd
import matplotlib.pyplot as plt

# Assuming the dataset is in the same directory as your Python script or Jupyter notebook or VS Code or Pycharm
file_path = 'sales_data.csv'
sales_data = pd.read_csv(file_path)
# Display the first few rows of the dataset to get an overview
print(sales_data.head())
print(sales_data.tail())

# Check for missing values
print(sales_data.isnull().sum())
# Summary statistics
print(sales_data.describe())
# Unique values in the 'Product' column
print(sales_data['Product'].unique())

# Convert 'Date' column to datetime format
sales_data['Date'] = pd.to_datetime(sales_data['Date'])
# Extract month and year from the 'Date' column
sales_data['Month'] = sales_data['Date'].dt.month
sales_data['Year'] = sales_data['Date'].dt.year
# Create a new column for total sales (Quantity * Revenue)
sales_data['TotalSales'] = sales_data['Order_Quantity'] * sales_data['Revenue']

# Total sales per month
monthly_sales = sales_data.groupby(['Year', 'Month'])['TotalSales'].sum()
# Plotting total sales per month
plt.figure(figsize=(10, 6))
monthly_sales.plot(kind='bar', color='skyblue')
plt.title('Total Sales per Month')
plt.xlabel('Year-Month')
plt.ylabel('Total Sales ($)')
plt.show()

