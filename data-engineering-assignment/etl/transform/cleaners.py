from typing import Dict, List, Any


def clean_row(row: Dict[str, Any]) -> Dict[str, Any]:
    """
    Standardizes raw row values.
    Does NOT validate or reject rows.
    """
    cleaned = {}

    for key, value in row.items():
        if isinstance(value, str):
            cleaned[key] = value.strip()
        else:
            cleaned[key] = value

    # Normalize known fields (safe defaults)
    if "Email" in cleaned and cleaned["Email"]:
        cleaned["Email"] = cleaned["Email"].lower()
    if "Year" in cleaned and cleaned["Year"] is not None:
        cleaned["Year"] = str(cleaned["Year"]).strip()



    return cleaned


def clean_rows(rows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return [clean_row(row) for row in rows]
