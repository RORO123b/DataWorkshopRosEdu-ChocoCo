import pandas as pd

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