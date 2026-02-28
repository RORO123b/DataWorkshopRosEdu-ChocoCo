import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data/processed/Chocolate_Sales_Processed.csv')

print('====================== HEAD ======================')
print(df.head())
print('====================== INFO ======================')
print(df.info())
print('====================== DESCRIBE ======================')
print(df.describe())
print('====================== NULL VALUES ======================')
print(df.isna().sum().sort_values())
print('====================== PERIOD ======================')
print(pd.to_datetime(df['date']).dt.to_period('M'))

print('====================== GRAPHS ======================')
df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.to_period('M')

df.boxplot(column='amount', by='month', figsize=(14, 6))
plt.title('Boxplot of Amount by Month')
plt.xlabel('Month')
plt.ylabel('Amount')
plt.suptitle('')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

product_revenue = df.groupby('product')['amount'].sum().sort_values(ascending=False)
plt.bar(product_revenue.head(10).index, product_revenue.head(10).values, color = 'green')
plt.title('Top 10 products by revenue')
plt.xlabel('Products')
plt.ylabel('Revenue')
plt.suptitle('')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.scatter(x = df['boxes_shipped'], y = df['amount'])
plt.title('Boxes shipped vs revenue')
plt.xlabel('Boxes Shipped')
plt.ylabel('Revenue')
plt.suptitle('')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
