from typing import Dict, List, Any, Tuple


def deduplicate_rows(
    rows: List[Dict[str, Any]],
    business_keys: List[str]
) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    """
    Deduplicates rows using business keys.
    Keeps first occurrence.
    """
    seen = set()
    unique_rows = []
    duplicate_rows = []

    for row in rows:
        key = tuple(str(row.get(k)).lower() for k in business_keys)

        if key in seen:
            duplicate_rows.append(row)
        else:
            seen.add(key)
            unique_rows.append(row)

    return unique_rows, duplicate_rows
