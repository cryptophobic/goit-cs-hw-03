from exercise1.queries import execute_queries
from exercise1.seed import seed_database
from exercise1.tables import create_tables

def init():
    create_tables()
    seed_database()

if __name__ == '__main__':
    execute_queries()