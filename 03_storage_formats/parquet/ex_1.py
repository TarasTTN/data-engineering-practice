import pandas as pd

df = pd.DataFrame({
    "order_id": [1001, 1002, 1003, 1004],
    "user_id": [501, 502, 503, 501],
    "status": ["paid", "cancelled", "paid", "pending"],
    "amount": [1200, 500, 700, 300]
})
df.to_parquet('orders.parquet', index=False)

df_read = pd.read_parquet('orders.parquet')

print("Прочитанный DataFrame:")
print(df_read)

orig_rows = len(df)
read_rows = len(df_read)

print(f"\nСтрок до записи: {orig_rows}")
print(f"Строк после чтения: {read_rows}")
print("Количество строк совпадает:", orig_rows == read_rows)