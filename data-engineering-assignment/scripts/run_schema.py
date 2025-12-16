import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    port=os.getenv("DB_PORT"),
    sslmode="require"
)

cur = conn.cursor()

with open("sql/schema.sql", "r") as f:
    cur.execute(f.read())

conn.commit()
cur.close()
conn.close()

print("✅ Schema executed successfully")
