from typing import List, Dict, Any
import psycopg2
from psycopg2 import sql
from psycopg2.extras import execute_values
from etl.load.upsert_strategies import UPSERT_STRATEGIES


def resolve_department_ids(
    conn,
    students: List[Dict[str, Any]]
) -> List[Dict[str, Any]]:
    with conn.cursor() as cur:
        cur.execute("SELECT id, name FROM departments")
        dept_map = {name: id for id, name in cur.fetchall()}

    resolved = []
    for s in students:
        dept_name = s.pop("department_name", None)
        s["department_id"] = dept_map.get(dept_name)
        resolved.append(s)

    return resolved




def upsert_rows(conn, table: str, rows: list[dict]) -> int:
    if not rows:
        return 0

    # Use custom upsert strategy if present
    if table in UPSERT_STRATEGIES:
        return UPSERT_STRATEGIES[table](conn, rows)

    columns = list(rows[0].keys())

# 🔑 Drop rows where all values are None (invalid lookup rows)
    clean_rows = [
        row for row in rows
        if all(row[col] is not None for col in columns)
    ]

    if not clean_rows:
        return 0

    values = [tuple(row[col] for col in columns) for row in clean_rows]

    column_list = ", ".join(columns)

    query = f"""
        INSERT INTO {table} ({column_list})
        VALUES %s
        ON CONFLICT DO NOTHING
    """

    with conn.cursor() as cur:
        execute_values(cur, query, values)

    return len(clean_rows)

