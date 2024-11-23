from exercise1.DBConnect import DBConnect

queries = [
    '''
    CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        fullname VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL UNIQUE
    );''',
    '''
    CREATE TABLE status (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL UNIQUE
    );
    ''',
    '''
    INSERT INTO status (name) VALUES 
        ('new'),
        ('in progress'),
        ('completed');
    ''',
    '''
    CREATE TABLE tasks (
        id SERIAL PRIMARY KEY,
        title VARCHAR(100) NOT NULL,
        description TEXT NOT NULL,
        status_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        CONSTRAINT fk_status FOREIGN KEY (status_id) REFERENCES status (id) ON DELETE CASCADE,
        CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
    );'''
]

def create_tables():
    db = DBConnect()
    cursor = db.conn.cursor()
    try:
        for query in queries:
            cursor.execute(query)
        db.conn.commit()
    except Exception as e:
        print(f"Сталася помилка: {e}")
        db.conn.rollback()
    finally:
        cursor.close()