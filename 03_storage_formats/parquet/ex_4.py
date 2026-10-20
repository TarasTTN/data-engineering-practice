import pandas as pd

# 1. Создаем DataFrame
df = pd.DataFrame({
    "order_id": [1001, 1002, 1003, 1004, 1005, 1006],
    "city": ["Moscow", "Kazan", "Moscow", "SPb", "Kazan", "Moscow"],
    "status": ["paid", "paid", "cancelled", "paid", "pending", "paid"],
    "amount": [1200, 800, 400, 950, 300, 1500],
})

# 1. Сохранить в parquet (не забывай index=False)
df.to_parquet("py_youtube/pandas/orders_by_city.parquet", index=False)

# 2. Прочитать файл
df_city = pd.read_parquet("py_youtube/pandas/orders_by_city.parquet")

# 3. Агрегация:
# А) Считаем общее количество заказов по каждому городу
total_orders = (
    df_city.groupby("city")["order_id"].count().rename("total_orders")
)

# Б) Оставляем ТОЛЬКО оплаченные заказы
paid_df = df_city[df_city["status"] == "paid"]

# В) Считаем количество и сумму ТОЛЬКО для оплаченных
paid_stats = paid_df.groupby("city")["amount"].agg(
    total_paid="count", total_sum="sum"
)

# Г) Склеиваем в одну таблицу
result = pd.concat([total_orders, paid_stats], axis=1).fillna(0)

# 4. Вывести результат целиком в виде красивой таблицы:
print("=== Сводная таблица ===")
print(result)

# А если хочется вывести каждый столбец отдельно:
print("\n--- Отдельный вывод метрик ---")
print("1. Всего заказов по городам:\n", result["total_orders"])
print("\n2. Оплаченных заказов:\n", result["total_paid"])
print("\n3. Сумма оплаченных заказов:\n", result["total_sum"])