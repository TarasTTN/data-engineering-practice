import pandas as pd

df = pd.read_parquet('py_youtube/pandas/orders.parquet', columns = ['status', 'amount'])

print(df)


success_buys = df[(df['status'] == 'paid')]
sums = success_buys['amount'].sum()

print(sums)
print(f'Строк прочитано по условиям {len(success_buys)}')