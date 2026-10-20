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

cursor.execute('SELECT * FROM source_users;')
rows = cursor.fetchall()
rows_len = len(rows)

insert_target_sql = """
INSERT INTO target_users (id, name, email)
VALUES (%s, %s, %s)
ON CONFLICT (id) DO NOTHING;
"""

rows_written = 0

for row in rows:
    cursor.execute(insert_target_sql, row)
    rows_written += 1

conn.commit()

# 6. Выводим результат в терминал
print(f"Сколько строк прочитано: {rows_len}")
print(f"Сколько строк записано: {rows_written}")

# 7. Закрываем курсор и соединение
cursor.close()
conn.close()


import psycopg2
from psycopg2.extras import RealDictCursor

conn = psycopg2.connect(...)

# with conn -> сам сделает commit() при успешной записи или rollback() при ошибке
with conn:
    # cursor_factory=RealDictCursor -> возвращает словари вместо кортежей
    with conn.cursor(cursor_factory=RealDictCursor) as cur:

        # Запись: коммит произойдёт сам при выходе из блока with conn
        cur.execute(
            "INSERT INTO target_users (id, name, email) VALUES (%s, %s, %s);",
            (5, "Eva", "eva@mail.com"),
        )

        # Чтение: вернёт удобный список словарей
        cur.execute("SELECT id, name, email FROM target_users;")
        users = cur.fetchall()

        for user in users:
            print(f"ID {user['id']}: {user['name']} ({user['email']})")

# Закрываем сам сетевой провод
conn.close()