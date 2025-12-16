UPSERT_STRATEGIES = {
    "departments": {
        "conflict_columns": ["name"],
        "update_columns": []
    },
    "students": {
        "conflict_columns": ["email"],
        "update_columns": ["name", "phone", "year", "department_id"]
    }
}
