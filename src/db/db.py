from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()

def get_connection():
    return psycopg2.connect(os.getenv("DB_URL"))