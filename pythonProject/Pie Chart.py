import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV files
df_country = pd.read_csv('Country.csv')
df_customer = pd.read_csv('Customer.csv')
df_market_trends = pd.read_csv('Market.csv')
df_product = pd.read_csv('Product.csv')
df_sales = pd.read_csv('Sales.csv')

# Pie Chart
market_trends = df_market_trends['MarketType'].value_counts()
plt.figure(figsize=(10, 8))
# Adjust pie chart
plt.pie(
    market_trends,
    labels=market_trends.index,
    autopct='%5.7f%%',
    colors=['#4CAF50', '#FF5722', '#03A9F4', '#FFC107'],
    startangle=140,
    wedgeprops={'edgecolor': 'black', 'linewidth': 1.5},
    textprops={'fontsize': 12, 'color': 'black'}
)
plt.title('Market Type Distribution', fontsize=16, fontweight='bold')
plt.show()

