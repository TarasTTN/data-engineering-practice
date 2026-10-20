import pandas as pd

df = pd.read_parquet('orders.parquet', columns = ['status', 'amount'])

kolvo = len(df)

success_buys = df[(df['status'] == 'paid')]
sums = success_buys['amount'].sum()

print(df)
print(success_buys)
print(sums)
