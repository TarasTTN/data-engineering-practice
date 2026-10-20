import pandas as pd 

df = pd.DataFrame({
    "order_id": [1001, 1002, 1003, 1004, 1005, 1006],
    "city": ["Moscow", "Kazan", "Moscow", "SPb", "Kazan", "Moscow"],
    "status": ["paid", "paid", "cancelled", "paid", "pending", "paid"],
    "amount": [1200, 800, 400, 950, 300, 1500],
})

df.to_parquet('orders_by_city.parquet', index=False)

df_2 = pd.read_parquet('orders_by_city.parquet')

total_orders = (
    df_2.groupby('city')['order_id'].count().rename("total_orders")
)

paid_order = (
    df_2.groupby('city')
)
print(total_orders)