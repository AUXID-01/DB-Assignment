from typing import Dict, List, Any
from etl.load.db_connection import get_db_connection
from etl.load.loaders import upsert_rows


def run_load_pipeline(data: Dict[str, List[Dict[str, Any]]]) -> Dict[str, Any]:
    """
    Generic Load Pipeline.

    Expected input format:
    {
        "table_name": [ {column: value}, ... ]
    }
    """
    summary: Dict[str, Any] = {}

    with get_db_connection() as conn:
        for table_name, rows in data.items():
            if not rows:
                continue

            received = len(rows)
            affected = upsert_rows(conn, table_name, rows)

            summary[table_name] = {
                "received": received,
                "affected": affected
            }

    return summary
