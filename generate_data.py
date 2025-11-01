# generate_data.py
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)
n_rows = 1000
products = ['TV', 'Smartphone', 'Refrigerator', 'Laptop', 'Washing Machine']
customer_ids = [f'CUST_{i:05d}' for i in range(1, 101)]

df = pd.DataFrame({
    'Customer_ID': np.random.choice(customer_ids, n_rows),
    'Age': np.random.randint(18, 70, n_rows),
    'Income': np.random.lognormal(10, 0.5, n_rows).round(0),
    'Gender': np.random.choice(['M', 'F'], n_rows, p=[0.55, 0.45]),
    'Purchase_Date': [datetime.now() - timedelta(days=np.random.randint(1, 365)) for _ in range(n_rows)],
    'Product': np.random.choice(products, n_rows),
    'Spend': np.random.uniform(50, 1500, n_rows),
    'Pref_TV': np.random.uniform(1, 10, n_rows),
    'Pref_Appliance': np.random.uniform(1, 10, n_rows),
    'Location': np.random.choice(['Urban', 'Suburban', 'Rural'], n_rows, p=[0.5, 0.3, 0.2])
})

# RFM
df['Recency'] = (df['Purchase_Date'].max() - df['Purchase_Date']).dt.days
df['Frequency'] = df.groupby('Customer_ID')['Spend'].transform('count')
df['Monetary'] = df.groupby('Customer_ID')['Spend'].transform('sum')
df['Pref_Score'] = (df['Pref_TV'] + df['Pref_Appliance']) / 2

df = df.drop(columns=['Purchase_Date'])
df.to_csv('lg_customer_data.csv', index=False)

print("Dataset created: lg_customer_data.csv")
print(f"Shape: {df.shape}")
print(df.head())
