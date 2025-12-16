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
cur.execute("""
SELECT tablename
FROM pg_tables
WHERE schemaname = 'public';
""")

tables = cur.fetchall()
print("📦 Tables in database:")
for t in tables:
    print("-", t[0])

cur.close()
conn.close()
