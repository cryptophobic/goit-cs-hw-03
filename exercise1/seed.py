from faker import Faker
import random

from exercise1.DBConnect import DBConnect

# Функція для заповнення бази даних
def seed_database():
    fake = Faker()

    db = DBConnect()
    cursor = db.conn.cursor()

    try:
        # Заповнення таблиці users
        users = []
        for _ in range(10):  # Створити 10 користувачів
            fullname = fake.name()
            email = fake.unique.email()
            users.append((fullname, email))

        cursor.executemany("INSERT INTO users (fullname, email) VALUES (%s, %s)", users)
        print(f"{len(users)} користувачів додано до таблиці users.")

        # Заповнення таблиці tasks
        cursor.execute("SELECT id FROM users")
        user_ids = [row[0] for row in cursor.fetchall()]

        cursor.execute("SELECT id FROM status")
        status_ids = [row[0] for row in cursor.fetchall()]

        tasks = []
        for _ in range(30):  # Створити 30 завдань
            title = fake.sentence(nb_words=6)
            description = fake.text()
            status_id = random.choice(status_ids)
            user_id = random.choice(user_ids)
            tasks.append((title, description, status_id, user_id))

        cursor.executemany("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)", tasks)
        print(f"{len(tasks)} завдань додано до таблиці tasks.")

        # Підтвердження змін
        db.conn.commit()
        print("Дані успішно збережено в базу даних.")

    except Exception as e:
        print(f"Сталася помилка: {e}")
        db.conn.rollback()

    finally:
        cursor.close()
