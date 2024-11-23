import os

from dotenv import load_dotenv, find_dotenv
import psycopg

class DBConnect:

    def __init__(self):
        load_dotenv(find_dotenv(), override=True)

        db_name = os.getenv("RDS_DB_NAME")
        db_user = os.getenv("RDS_USERNAME")
        db_password = os.getenv("RDS_PASSWORD")
        db_host = os.getenv("RDS_HOST")
        db_port = os.getenv("RDS_PORT")

        self.conn = psycopg.connect(f"dbname={db_name} user={db_user} password={db_password} host={db_host} port={db_port}")

    def __del__(self):
        self.conn.close()

    def select_query(self, query, params = None):
        cur = self.conn.cursor()
        cur.execute(query, params)
        rows = cur.fetchall()
        self.conn.commit()
        return rows
