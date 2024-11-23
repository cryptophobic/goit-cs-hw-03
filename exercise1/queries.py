from faker import Faker
from exercise1.DBConnect import DBConnect

db = DBConnect()

def retrieve_all_the_tasks_by_user_id(user_id):
    return db.select_query(
        'SELECT * FROM tasks WHERE user_id=%(user_id)s',
        {'user_id': user_id})

def select_task_by_status(status_name):
    return db.select_query(
        "SELECT t.* FROM tasks t INNER JOIN status s ON t.status_id=s.id WHERE s.name=%(status_name)s",
        {'status_name': status_name})

def update_status_task(task_id, status_name):
    try:
        cursor = db.conn.cursor()
        cursor.execute(
            "UPDATE tasks SET status_id = (SELECT id FROM status WHERE name=%(status_name)s) WHERE id=%(task_id)s",
            {'status_name': status_name, 'task_id': task_id}
        )
        db.conn.commit()
    except Exception as e:
        print(f"Сталася помилка: {e}")
        db.conn.rollback()

def retrieve_list_of_the_users_without_tasks():
    return db.select_query("SELECT * FROM users WHERE id NOT IN (SELECT DISTINCT user_id FROM tasks);")

def add_new_task_to_user(title, description, status_name, user_id):
    try:
        cursor = db.conn.cursor()
        cursor.execute(
            """INSERT INTO tasks (title, description, status_id, user_id) 
                VALUES (
                %(title)s, 
                %(description)s, 
                (SELECT id FROM status WHERE name = %(status_name)s), 
                %(user_id)s)
            """,
            {'title': title, 'description': description, 'status_name': status_name, 'user_id': user_id});
        db.conn.commit()

    except Exception as e:
        print(f"Сталася помилка: {e}")
        db.conn.rollback()

def retrieve_all_the_tasks_in_not_completed_status():
    return db.select_query(
        'SELECT t.* FROM tasks t INNER JOIN status s ON t.status_id=s.id WHERE s.name != %(status_name)s',
        {'status_name': 'completed'})

def remove_task(task_id):
    try:
        cursor = db.conn.cursor()
        cursor.execute('DELETE FROM tasks WHERE id = %(task_id)s', {'task_id': task_id})
        db.conn.commit()
    except Exception as e:
        print(f"Сталася помилка: {e}")
        db.conn.rollback()

def find_users_by_email(email):
    return db.select_query('SELECT * FROM users WHERE email=%(email)s', {'email': email})

def update_user_name(user_id, user_name):
    try:
        cursor = db.conn.cursor()
        cursor.execute(
            'UPDATE users SET fullname = %(user_name)s WHERE id = %(user_id)s',
            {'user_id': user_id, 'user_name': user_name})
        db.conn.commit()
    except Exception as e:
        print(f"Сталася помилка: {e}")
        db.conn.rollback()

def retrieve_number_of_tasks_grouped_by_status_name():
    return db.select_query('''
    SELECT s.name AS status, COUNT(t.id) AS task_count
        FROM status s
    LEFT JOIN tasks t ON s.id = t.status_id
    GROUP BY s.name''')

def retrieve_tasks_of_users_specified_by_email_address_domain(domain):
    return db.select_query(
        '''
        SELECT t.* 
        FROM tasks t
        INNER JOIN users u ON t.user_id = u.id
        WHERE u.email LIKE %(domain)s''',
        {'domain': f"%@{domain}"})

def retrieve_list_of_tasks_without_description():
    return db.select_query("SELECT * FROM tasks WHERE description IS NULL OR description = ''")

def select_users_and_tasks_in_in_progress_status():
    return db.select_query(
        '''SELECT u.fullname, t.title, t.description 
        FROM users u
        INNER JOIN tasks t ON u.id = t.user_id
        INNER JOIN status s ON t.status_id = s.id
        WHERE s.name = %(status_name)s''',
    {'status_name': 'in progress'})

def retrieve_users_and_number_of_their_tasks():
    return db.select_query(
        '''
        SELECT u.fullname, COUNT(t.id) AS task_count 
        FROM users u
        LEFT JOIN tasks t ON u.id = t.user_id
        GROUP BY u.id;''')


def execute_queries():
    print (retrieve_all_the_tasks_by_user_id(2))
    print (select_task_by_status('in progress'))
    print (update_status_task(1, 'in progress'))
    print (retrieve_list_of_the_users_without_tasks())
    fake = Faker()
    title = fake.sentence(nb_words=6)
    description = fake.text()
    print (add_new_task_to_user(title, description, 'in progress', 1))
    print (retrieve_all_the_tasks_in_not_completed_status())
    print (remove_task(32))
    print (find_users_by_email('kathyortega@example.net'))
    print (update_user_name(1, 'Fedir Ivanovych'))
    print (retrieve_number_of_tasks_grouped_by_status_name())
    print (retrieve_tasks_of_users_specified_by_email_address_domain('example.net'))
    print (retrieve_list_of_tasks_without_description())
    print (select_users_and_tasks_in_in_progress_status())
    print (retrieve_users_and_number_of_their_tasks())
