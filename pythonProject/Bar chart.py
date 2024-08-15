import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV files
df_country = pd.read_csv('Country.csv')
df_customer = pd.read_csv('Customer.csv')
df_market_trends = pd.read_csv('Market.csv')
df_product = pd.read_csv('Product.csv')
df_sales = pd.read_csv('Sales.csv')

top_30_countries = df_country.head(50)
plt.figure(figsize=(25, 9))

# Create column charts with new customizations
plt.bar(
    top_30_countries['CountryName'],
    top_30_countries['GDP'],
    color='#1f77b4',
    edgecolor='black',
    linewidth=1.2
)
plt.xlabel('Country', fontsize=16, fontweight='bold', color='darkblue')
plt.ylabel('GDP (in billion USD)', fontsize=16, fontweight='bold', color='darkblue')
plt.title('Top 30 Countries by GDP', fontsize=20, fontweight='bold', color='navy')
plt.xticks(rotation=45, ha='right', fontsize=14, color='darkblue')
plt.yticks(fontsize=14, color='darkblue')
plt.grid(True, linestyle='--', color='gray', alpha=0.6, axis='y')
plt.tight_layout()
plt.show()


