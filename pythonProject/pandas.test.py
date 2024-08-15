import pandas as pd

# Read data from CSV files
df_country = pd.read_csv('Country.csv')
df_customer = pd.read_csv('Customer.csv')
df_market_trends = pd.read_csv('Market.csv')
df_product = pd.read_csv('Product.csv')
df_sales = pd.read_csv('Sales.csv')

# 1. Handling missing values

# Example: Replace missing values with mean (or other value) for column 'Sales' in df_sales
# df_sales['Sales'].fillna(df_sales['Sales'].mean(), inplace=True)

# Example: Remove rows with missing values in df_customer
# df_customer.dropna(inplace=True)

# Example: Fill missing values with mean for column 'Price' in df_product
# df_product['Price'].fillna(df_product['Price'].mean(), inplace=True)

# 2. Delete duplicate records

# Delete duplicate records based on all columns in df_customer
# df_customer.drop_duplicates(inplace=True)

# Delete duplicate records based on 'ProductID' column in df_product
# df_product.drop_duplicates(subset='ProductID', inplace=True)

# 3. Data type handling

# Convert the data type for column 'Date' in df_market_trends to datetime
# df_market_trends['Date'] = pd.to_datetime(df_market_trends['Date'])

# Convert column 'CountryCode' in df_country to string data type
# df_country['CountryCode'] = df_country['CountryCode'].astype(str)

# 4. Remove extra spaces and normalize data

# Remove extra whitespace at the beginning and end of strings in df_customer
# df_customer['CustomerName'] = df_customer['CustomerName'].str.strip()

# Convert all values in the 'CountryName' column of df_country to uppercase
# df_country['CountryName'] = df_country['CountryName'].str.upper()

# 5. Handling invalid values

# Example: Remove rows with negative values in the 'Sales' column of df_sales
# df_sales = df_sales[df_sales['Sales'] >= 0]

# Example: Delete rows with invalid values in column 'ProductCategory' of df_product
# df_product = df_product[df_product['ProductCategory'].notna()]

# Display the first  rows of each dataframe
print("Country Data:\n", df_country.head())
print("\nCustomer Data:\n", df_customer.head())
print("\nMarket Data:\n", df_market_trends.head())
print("\nProduct Data:\n", df_product.head())
print("\nSales Data:\n", df_sales.head())


