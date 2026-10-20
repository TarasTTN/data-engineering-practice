import pandas as pd

df = pd.read_parquet('orders.parquet')

sort = df[(df['status'] == 'paid')]

sort.to_parquet('paid_orders.parquet', index = False)

df_2 = pd.read_parquet('paid_orders.parquet')

print(f'Всего заказов {len(df)}')
print(f'Оплаченных заказов {len(df_2)}')
