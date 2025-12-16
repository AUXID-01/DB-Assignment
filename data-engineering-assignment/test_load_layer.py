from etl.load.db_connection import get_db_connection
from etl.load.loaders import upsert_rows, resolve_department_ids

# Fake data similar to transform output
data = {
    "departments": [
        {"name": "CS"},
        {"name": "EE"}
    ],
    "students": [
        {
            "name": "Alice",
            "email": "alice@example.com",
            "phone": None,
            "year": 2,
            "department_name": "CS"
        }
    ]
}

with get_db_connection() as conn:
    dept_count = upsert_rows(conn, "departments", data["departments"])

    students = resolve_department_ids(conn, data["students"])
    student_count = upsert_rows(conn, "students", students)

print("Departments upserted:", dept_count)
print("Students upserted:", student_count)
