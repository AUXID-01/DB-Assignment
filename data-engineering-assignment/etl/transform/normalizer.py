from typing import Dict, List, Any


def normalize_students(payload: Dict[str, List[Dict[str, Any]]]) -> Dict[str, List[Dict[str, Any]]]:
    """
    Extracts departments and prepares FK-safe structures.
    """
    students = payload.get("students", [])

    departments = {}
    normalized_students = []

    for s in students:
        dept_name = s.get("department_name")
        s.pop("department_name", None)

        if dept_name:
            departments[dept_name] = {"name": dept_name}

        s["department_name"] = dept_name
        normalized_students.append(s)

    return {
        "departments": list(departments.values()),
        "students": normalized_students
    }
