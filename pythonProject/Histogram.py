import matplotlib.pyplot as plt
import pandas as pd


# Read data from CSV files
df_country = pd.read_csv('Country.csv')
df_customer = pd.read_csv('Customer.csv')
df_market_trends = pd.read_csv('Market.csv')
df_product = pd.read_csv('Product.csv')
df_sales = pd.read_csv('Sales.csv')
# Histogram
plt.figure(figsize=(20, 6))
plt.hist(
    df_product['UnitPrice'],
    bins=15,
    color='#87CEEB',
    edgecolor='white',
    alpha=0.8  #
)
plt.xlabel('Unit Price (in USD)', fontsize=14, fontweight='bold', color='darkblue')
plt.ylabel('Frequency', fontsize=14, fontweight='bold', color='darkblue')
plt.title('Distribution of Unit Prices', fontsize=18, fontweight='bold', color='navy')
plt.grid(True, linestyle=':', color='gray', alpha=0.7)
plt.xticks(fontsize=12, color='darkblue')
plt.yticks(fontsize=12, color='darkblue')
plt.tight_layout()
plt.show()

