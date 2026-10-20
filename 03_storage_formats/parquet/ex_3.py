import pandas as pd



df = pd.read_parquet('py_youtube/pandas/orders.parquet')

success_buys = df[df['status'] == 'paid']

success_buys.to_parquet('paid_orders.parquet', index=False)

df_new = pd.read_parquet('py_youtube/pandas/paid_orders.parquet')

print(f'Всего заказов было: {len(df)}')
print(f'Оплаченных заказов: {len(df_new)}')