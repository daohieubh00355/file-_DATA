import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV files
df_country = pd.read_csv('Country.csv')
df_customer = pd.read_csv('Customer.csv')
df_market_trends = pd.read_csv('Market.csv')
df_product = pd.read_csv('Product.csv')
df_sales = pd.read_csv('Sales.csv')

#  Scatter Plot: Revenue vs. Quantity Sold
plt.figure(figsize=(15, 4))
# Adjust scatter plot
plt.scatter(df_sales['Quantity'], df_sales['Tax'], color='darkorange', edgecolor='black', alpha=0.7, s=100)
# Adjust axis labels and titles
plt.xlabel('Sales quantity', fontsize=14, fontweight='bold')
plt.ylabel('Tax', fontsize=14, fontweight='bold')
plt.title('Tax vs. Sales Quantity', fontsize=16, fontweight='bold')
# Add grid with line style
plt.grid(True, linestyle='--', alpha=0.7)
# Adjust ticks
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.show()

