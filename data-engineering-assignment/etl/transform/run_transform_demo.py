from etl.transform.transform_pipeline import run_students_transform


raw_rows = [
    {
        "Name": "Alice",
        "Email": "alice@example.com",
        "Year": "2",
        "Dept": "CS"
    }
]

result = run_students_transform(raw_rows)

print(result["data"])
print(result["metrics"])






# from etl.transform.cleaners import clean_rows
# from etl.transform.validators import validate_rows
# from etl.transform.deduplicator import deduplicate_rows
# from etl.transform.mapper import map_rows, load_mapping
# from etl.transform.normalizer import normalize_students

# raw_rows = [
#     {
#         "Name": "Alice",
#         "Email": "alice@example.com",
#         "Year": "2",
#         "Dept": "CS"
#     }
# ]


# # Run transform step by step
# cleaned = clean_rows(raw_rows)
# valid, invalid = validate_rows(cleaned)
# unique, duplicates = deduplicate_rows(valid, ["Email"])

# mapping = load_mapping("etl/mappings/students_mapping.json")
# mapped = map_rows(unique, mapping)
# normalized = normalize_students(mapped)

# print("\n=== FINAL TRANSFORM OUTPUT ===")
# for k, v in normalized.items():
#     print(f"\n{k.upper()}:")
#     for row in v:
#         print(row)

# print("\n=== ROW COUNTS ===")
# print("Raw:", len(raw_rows))
# print("Cleaned:", len(cleaned))
# print("Valid:", len(valid))
# print("Invalid:", len(invalid))
# print("Deduped:", len(unique))

# ALLOWED_STUDENT_KEYS = {"name", "email", "phone", "year", "department_name"}

# for row in normalized["students"]:
#     assert set(row.keys()) <= ALLOWED_STUDENT_KEYS


# first = normalize_students(map_rows(unique, mapping))
# second = normalize_students(map_rows(unique, mapping))

# assert first == second



