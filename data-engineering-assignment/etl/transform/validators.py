from typing import Dict, List, Tuple, Any
import re

EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def validate_row(row: Dict[str, Any]) -> List[str]:
    """
    Returns list of validation errors.
    Empty list = valid row.
    """
    errors = []

    if not row.get("Email"):
        errors.append("Missing email")
    elif not EMAIL_REGEX.match(row["Email"]):
        errors.append("Invalid email format")

    if not row.get("Name"):
        errors.append("Missing name")

    if row.get("Year"):
        try:
            year = int(row["Year"])
            if year < 1 or year > 5:
                errors.append("Year must be between 1 and 5")
        except ValueError:
            errors.append("Year must be numeric")
    else:
        errors.append("Missing year")


    return errors


def validate_rows(
    rows: List[Dict[str, Any]]
) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    """
    Splits rows into valid and invalid.
    """
    valid_rows = []
    invalid_rows = []

    for row in rows:
        errors = validate_row(row)
        if errors:
            row["_errors"] = errors
            invalid_rows.append(row)
        else:
            valid_rows.append(row)

    return valid_rows, invalid_rows
