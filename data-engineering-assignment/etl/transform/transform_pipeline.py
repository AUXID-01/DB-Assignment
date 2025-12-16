from etl.transform.cleaners import clean_rows
from etl.transform.validators import validate_rows
from etl.transform.deduplicator import deduplicate_rows
from etl.transform.mapper import map_rows, load_mapping
from etl.transform.normalizer import normalize_students




def run_students_transform(rows):
    """
    Runs the full transform pipeline for students.
    Input: List[Dict] from Extract
    Output: Normalized, load-ready dict
    """

    # Step 1: Clean
    cleaned_rows = clean_rows(rows)

    # Step 2: Validate
    valid_rows, invalid_rows = validate_rows(cleaned_rows)

    # Step 3: Deduplicate
    unique_rows, duplicate_rows = deduplicate_rows(
        valid_rows,
        business_keys=["Email"]
    )

    # Step 4: Map
    mapping = load_mapping("etl/mappings/students_mapping.json")
    mapped = map_rows(unique_rows, mapping)

    # Step 5: Normalize
    normalized = normalize_students(mapped)

    return {
        "data": normalized,
        "metrics": {
            "raw": len(rows),
            "cleaned": len(cleaned_rows),
            "valid": len(valid_rows),
            "invalid": len(invalid_rows),
            "deduplicated": len(unique_rows),
            "duplicates": len(duplicate_rows),
        }
    }
def run_transform_pipeline(raw_rows, mapping_path: str):
    mapping = load_mapping(mapping_path)
    mapped_data = map_rows(raw_rows, mapping)

    metrics = {
        "raw": len(raw_rows),
        "deduplicated": {}
    }

    # 🔑 Deduplicate lookup tables using business keys
    if "passenger_classes" in mapped_data:
        unique, duplicates = deduplicate_rows(
            mapped_data["passenger_classes"],
            business_keys=["class_number"]
        )
        mapped_data["passenger_classes"] = unique
        metrics["deduplicated"]["passenger_classes"] = len(duplicates)

    if "embarkation_ports" in mapped_data:
        unique, duplicates = deduplicate_rows(
            mapped_data["embarkation_ports"],
            business_keys=["code"]
        )
        mapped_data["embarkation_ports"] = unique
        metrics["deduplicated"]["embarkation_ports"] = len(duplicates)

    return {
        "data": mapped_data,
        "metrics": metrics
    }
