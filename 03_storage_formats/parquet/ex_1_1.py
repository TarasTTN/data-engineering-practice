import pandas as pd

df = pd.DataFrame({
    "order_id": [1001, 1002, 1003, 1004],
    "user_id": [501, 502, 503, 501],
    "status": ["paid", "cancelled", "paid", "pending"],
    "amount": [1200, 500, 700, 300]
})

df.to_parquet('orders.parquet', index = False)

df_read = pd.read_parquet('orders.parquet')

ischodnoe = len(df)
itog = len(df_read)

print(f"\nСтрок до записи: {ischodnoe}")
print(f"Строк после чтения: {itog}")
print("Количество строк совпадает:", ischodnoe == itog)