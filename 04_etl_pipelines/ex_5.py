import psycopg2

DB_CONFIG = {
    "dbname": "zhiva_db",  # имя базы (как в DBeaver)
    "user": "zhiva_admin",  # имя пользователя
    "password": "zhiva_admin",  # пароль от postgres
    "host": "localhost",  # хост
    "port": 5433,  # порт подключения (на скрине DBeaver указан localhost:5433)
}

conn = psycopg2.connect(**DB_CONFIG)
cursor = conn.cursor()

create_tables_sql = """
CREATE TABLE IF NOT EXISTS source_users (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS target_users (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);
"""

cursor.execute(create_tables_sql)

# 4. Тестовые строки для добавления в source_users
test_data = [
    (1, "Alice", "alice@mail.com"),
    (2, "Bob", "bob@mail.com"),
    (3, "Charlie", "charlie@mail.com"),
]
# 5. Вставляем строки через параметризованный запрос (%s)
insert_sql = """
INSERT INTO source_users (id, name, email)
VALUES (%s, %s, %s)
ON CONFLICT (id) DO NOTHING;
"""

for user in test_data:
    cursor.execute(insert_sql, user)

# 6. Фиксируем изменения в базе данных
conn.commit()

# 7. Закрываем курсор и соединение
cursor.close()
conn.close()

print(
    "Таблицы созданы, тестовые строки успешно добавлены в source_users!"
)