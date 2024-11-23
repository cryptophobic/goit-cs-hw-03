import os
from pymongo import MongoClient

from dotenv import load_dotenv, find_dotenv

class DBConnect:

    def __init__(self):
        load_dotenv(find_dotenv(), override=True)
        try:
            db_host = os.getenv("MONGO_HOST")
            db_port = os.getenv("MONGO_PORT")

            # Змініть connection string на свій
            self.client = MongoClient(f"mongodb://{db_host}:{db_port}/")
            self.db = self.client['cats_db']
            self.collection = self.db['cats_collection']

        except Exception as e:
            print(f"Не вдалося підключитися до MongoDB: {e}")
            exit()

    def __del__(self):
        self.client.close()
