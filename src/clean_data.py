import pandas as pd

df = pd.read_csv('data/raw/Chocolate_Sales.csv')

df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# print(pd.to_datetime(df['date'], dayfirst=True, errors='coerce').isna().sum())

df['date'] = pd.to_datetime(df['date'], dayfirst=True, errors='coerce')
df['amount'] = pd.to_numeric(df['amount'].str.replace('$', '').str.replace(',',''), errors='coerce')
df['amount'] = df['amount'].dropna()
df = df.drop_duplicates()

print(df.head())
df.to_csv('data/processed/Chocolate_Sales_Processed.csv', index=False)