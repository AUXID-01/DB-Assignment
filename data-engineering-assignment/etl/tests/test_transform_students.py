from etl.transform.cleaners import clean_rows
from etl.transform.validators import validate_rows
from etl.transform.deduplicator import deduplicate_rows
from etl.transform.mapper import map_rows
from etl.transform.normalizer import normalize_students
from etl.transform.mapper import load_mapping
import json

def test_students_transform_pipeline():
    raw_rows = [
        {
            "Name": " Alice ",
            "Email": "ALICE@EXAMPLE.COM",
            "Phone": "99999",
            "Year": "2",
            "Dept": "CS"
        },
        {
            "Name": "Bob",
            "Email": "bob@example.com",
            "Phone": "88888",
            "Year": "three",
            "Dept": "Math"
        },
        {
            "Name": "Alice Dup",
            "Email": "alice@example.com",
            "Phone": "77777",
            "Year": "2",
            "Dept": "CS"
        }
    ]

    # Clean
    cleaned = clean_rows(raw_rows)
    assert cleaned[0]["Email"] == "alice@example.com"

    # Validate
    valid, invalid = validate_rows(cleaned)
    assert len(valid) == 2
    assert len(invalid) == 1
    assert "Year must be numeric" in invalid[0]["_errors"]

    # Deduplicate
    unique, duplicates = deduplicate_rows(valid, business_keys=["Email"])
    assert len(unique) == 1
    assert len(duplicates) == 1

    # Map
    mapping = load_mapping("etl/mappings/students_mapping.json")
    mapped = map_rows(unique, mapping)
    assert "students" in mapped
    assert "email" in mapped["students"][0]

    # Normalize
    normalized = normalize_students(mapped)
    assert "departments" in normalized
    assert normalized["departments"][0]["name"] == "CS"

    print("✅ Transform pipeline test passed")

    print("\n=== NORMALIZED OUTPUT ===")
    print(json.dumps(normalized, indent=2))
