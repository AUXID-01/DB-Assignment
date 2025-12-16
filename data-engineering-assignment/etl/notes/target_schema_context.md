Target Database Schema Context
Version: v1.0 (Frozen)
Source: Titanic Dataset
Purpose: Provide authoritative schema reference for ETL mapping.

TABLE: passenger_classes
- id (PK)
- class_number (INT, UNIQUE)
- description (VARCHAR)

TABLE: embarkation_ports
- id (PK)
- code (CHAR, UNIQUE)
- name (VARCHAR)

TABLE: passengers
- id (PK)
- passenger_ref (INT, UNIQUE)
- name (TEXT)
- sex (VARCHAR)
- age (NUMERIC)
- survived (BOOLEAN)
- sib_sp (INT)
- parch (INT)
- ticket (VARCHAR)
- fare (NUMERIC)
- cabin (VARCHAR)
- class_id (FK → passenger_classes.id)
- embarkation_id (FK → embarkation_ports.id)
- created_at (TIMESTAMP)
