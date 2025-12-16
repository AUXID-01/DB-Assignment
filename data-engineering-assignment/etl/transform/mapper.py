from typing import Dict, Any, List
import json


def load_mapping(mapping_path: str) -> Dict[str, Any]:
    with open(mapping_path, "r") as f:
        return json.load(f)


def map_rows(rows: List[Dict[str, Any]], mapping: Dict[str, Any]) -> Dict[str, List[Dict[str, Any]]]:
    """
    Maps raw rows to target tables based on table.column notation.

    Returns:
        {
            "passengers": [...],
            "passenger_classes": [...],
            "embarkation_ports": [...]
        }
    """
    column_map = mapping["columns"]

    table_buffers: Dict[str, List[Dict[str, Any]]] = {}

    for row in rows:
        row_buffers: Dict[str, Dict[str, Any]] = {}

        for source_col, target in column_map.items():
            table, column = target.split(".")

            if table not in row_buffers:
                row_buffers[table] = {}

            value = row.get(source_col)

        # Normalize empty strings to None
            if value == "":
                value = None

            row_buffers[table][column] = value


        for table, data in row_buffers.items():
            table_buffers.setdefault(table, []).append(data)

    return table_buffers
