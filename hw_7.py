import sqlite3

# Подключаемся к базе данных или создаем ее, если она не существует
conn = sqlite3.connect('hw.db')

# Создаем курсор для работы с базой данных
cursor = conn.cursor()

# Создаем таблицу products
cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY,
                    product_title TEXT NOT NULL CHECK(length(product_title) <= 200),
                    price FLOAT NOT NULL DEFAULT 0.0 CHECK(price >= 0),
                    quantity INTEGER NOT NULL DEFAULT 0 CHECK(quantity >= 0)
                    )''')

# Сохраняем изменения
conn.commit()

# Закрываем соединение с базой данных
conn.close()
