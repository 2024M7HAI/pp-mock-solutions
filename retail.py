import pandas as pd

# --- Task 1: Load the dataset
file_path = 'data/retail_store_transactions.csv'
data = pd.read_csv(file_path)

# --- Task 1: *Algorithmically* inspect the dataset
# Note: This is not *the one correct* solution; You should just be able to inspect the data-frame in your code
print(data.info())
print()
print(data.head())

# --- Task 2: Clean the data
# Step 1: Remove negative unit prices
data_cleaned = data[data['unit_price'] >= 0]
# Step 2: Remove rows with missing timestamp or quantity
data_cleaned = data_cleaned.dropna(subset=['timestamp', 'quantity'])
# Step 3: Remove duplicates
data_cleaned = data_cleaned.drop_duplicates()

# --- Task 3: Add new columns
# Step 1: Convert the 'timestamp' column to a datetime object
data_cleaned['timestamp'] = pd.to_datetime(data_cleaned['timestamp'])
# Step 2: Add a new column 'day_of_the_week' containing the name of the weekday
data_cleaned['day_of_the_week'] = data_cleaned['timestamp'].dt.day_name()
# Step 3: Add a new column 'profit' which is the product of 'unit_price' and 'quantity'
data_cleaned['profit'] = data_cleaned['unit_price'] * data_cleaned['quantity']

# --- Task 4: Group data and find best day and best selling product
# Step 1: Group the data by 'day_of_the_week' and sum the 'profit' for each group, then sort in descending order
# Note: This is the very brief way of writing it; You can also take more sequential steps
profit_by_day = data_cleaned.groupby('day_of_the_week')['profit'].sum().sort_values(ascending=False)
# Step 2: Find the day of the week with the maximum total profit
# E.g.,: https://www.w3schools.com/python/pandas/ref_df_idxmax.asp
best_day = profit_by_day.idxmax()
# Get the maximum day profit value (not strictly asked for, but here just for completion's sake)
best_day_profit = profit_by_day.max()

# Step 3: Group the data by 'product_id' and sum the 'profit' for each product, then sort in descending order, cf Step 1
profit_by_product = data_cleaned.groupby('product_id')['profit'].sum().sort_values(ascending=False)
# Step 4: Find the product with the highest total profit, cf Step 2
best_selling_product = profit_by_product.idxmax()
# Get the maximum product profit value (not strictly asked for, but here just for completion's sake)
best_selling_product_profit = profit_by_product.max()

# --- Task 5: Save the cleaned and processed DataFrame into a new CSV file
output_file_path = 'data/cleaned_retail_store_transactions.csv'
data_cleaned.to_csv(output_file_path, index=False)

