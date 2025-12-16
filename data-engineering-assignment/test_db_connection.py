import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

try:
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )
    print("✅ Connected to PostgreSQL/NeonDB")

    cur = conn.cursor()
    cur.execute("SELECT version();")
    print("PostgreSQL Version:", cur.fetchone())

    cur.close()
    conn.close()

except Exception as e:
    print("❌ Connection failed")
    print(e)
