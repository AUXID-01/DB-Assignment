from etl.load.load_pipeline import run_load_pipeline

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

summary = run_load_pipeline(data)
print(summary)
