"""
ONE-TIME METADATA HELPER SCRIPT


Purpose:
Generate a column-mapping scaffold between source data
and the frozen target database schema.


NOTE:
- This script is NOT part of the ETL runtime.
- It only assists in preparing static mapping JSON files.
- The generated output must be reviewed and finalized manually.
"""


from pathlib import Path


# ---- CONFIG ----
SCHEMA_CONTEXT_FILE = "../etl/notes/target_schema_context.md"


# ---- LOAD SCHEMA CONTEXT ----
def load_schema_context() -> str:
    schema_path = Path(__file__).parent / SCHEMA_CONTEXT_FILE
    return schema_path.read_text(encoding="utf-8")




# ---- BUILD MAPPING SCAFFOLD ----
def build_mapping_scaffold(source_columns: list[str]) -> str:
    schema_context = load_schema_context()


    return f"""
ROLE:
You are acting as a senior data engineer preparing ETL metadata.


SOURCE COLUMNS:
{chr(10).join(f"- {col}" for col in source_columns)}


TARGET POSTGRES SCHEMA (FROZEN):
{schema_context}


TASK:
1. Map each relevant source column to target table.column
2. Use table.column notation for foreign keys
3. Do NOT invent new columns
4. Return STRICT JSON ONLY
"""




# ---- MAIN (ONE-TIME USE) ----
if __name__ == "__main__":
    source_columns = [
    "PassengerId",
    "Survived",
    "Pclass",
    "Name",
    "Sex",
    "Age",
    "SibSp",
    "Parch",
    "Ticket",
    "Fare",
    "Cabin",
    "Embarked"
]



    scaffold = build_mapping_scaffold(source_columns)


    print("==== MAPPING SCAFFOLD (REVIEW & FINALIZE MANUALLY) ====\n")
    print(scaffold)
    print("\n==== END SCAFFOLD ====")


    print(
        "\nNEXT STEPS:\n"
        "1. Review the mapping scaffold above\n"
        "2. Finalize column mappings manually\n"
        "3. Save the result to etl/mappings/<entity>_mapping.json\n"
        "4. Commit the JSON file to version control\n"
        "5. Do NOT modify the schema after this point\n"
    )





