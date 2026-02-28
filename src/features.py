import pandas as pd
from sklearn.preprocessing import OneHotEncoder

df = pd.read_csv('data/processed/Chocolate_Sales_Processed.csv')

df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.month


df['date'] = pd.to_datetime(df['date'])
df['day'] = df['date'].dt.dayofweek

target = df['amount']

encoder = OneHotEncoder(sparse_output=False)

features = ['sales_person','country','product','date','amount','boxes_shipped']
categorical_columns = ['sales_person','country','product']
one_hot_encoded = encoder.fit_transform(df[categorical_columns])

one_hot_df = pd.DataFrame(one_hot_encoded, 
                          columns=encoder.get_feature_names_out(categorical_columns))

df_sklearn_encoded = pd.concat([df.drop(categorical_columns, axis=1), one_hot_df], axis=1)

df_sklearn_encoded.to_csv('data/processed/Chocolate_Sales_Processed.csv', index=False)