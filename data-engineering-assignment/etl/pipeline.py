from etl.transform.transform_pipeline import run_transform_pipeline
from etl.load.load_pipeline import run_load_pipeline
from etl.extract.csv_extractor import extract_from_csv


def run_pipeline_from_rows(raw_rows):
    transform_result = run_transform_pipeline(
        raw_rows,
        mapping_path="etl/mappings/titanic_mapping.json"
    )

    transformed_data = transform_result["data"]
    load_summary = run_load_pipeline(transformed_data)

    return {
        "transform_metrics": transform_result["metrics"],
        "load_summary": load_summary
    }


def run_etl_pipeline():
    """
    Used for batch ETL runs (Task 4)
    """
    print("🚀 ETL Pipeline Started")

    # ✅ USE TITANIC CSV (single source of truth)
    raw_rows = extract_from_csv("titanic.csv")
    print(f"📤 Extracted {len(raw_rows)} raw rows")

    result = run_pipeline_from_rows(raw_rows)

    print("🧹 Transform Metrics:", result["transform_metrics"])
    print("📥 Load Summary:", result["load_summary"])
    print("✅ ETL Pipeline Completed Successfully")

    return result


if __name__ == "__main__":
    run_etl_pipeline()
