"""
Database configuration and connection utilities.

Purpose:
- Centralize PostgreSQL / NeonDB connection logic
- Provide reusable, safe connections for ETL load layer
- Avoid credential duplication across files

Used by:
- extract/
- load/
- pipeline.py
"""

import os
import psycopg2
from psycopg2.extensions import connection
from dotenv import load_dotenv


# Load environment variables from .env
load_dotenv()


class DatabaseConfig:
    """Holds database configuration loaded from environment variables."""

    HOST: str = os.getenv("DB_HOST")
    PORT: int = int(os.getenv("DB_PORT", 5432))
    NAME: str = os.getenv("DB_NAME")
    USER: str = os.getenv("DB_USER")
    PASSWORD: str = os.getenv("DB_PASSWORD")
    SSLMODE: str = os.getenv("DB_SSLMODE", "require")

    @classmethod
    def validate(cls) -> None:
        """Validate that all required DB variables are set."""
        missing = [
            var for var in ["HOST", "NAME", "USER", "PASSWORD"]
            if not getattr(cls, var)
        ]

        if missing:
            raise EnvironmentError(
                f"Missing required database environment variables: {missing}"
            )


def get_db_connection(autocommit: bool = False) -> connection:
    """
    Create and return a PostgreSQL / NeonDB connection.

    Args:
        autocommit (bool): Whether to enable autocommit mode

    Returns:
        psycopg2.extensions.connection
    """
    DatabaseConfig.validate()

    conn = psycopg2.connect(
        host=DatabaseConfig.HOST,
        port=DatabaseConfig.PORT,
        database=DatabaseConfig.NAME,
        user=DatabaseConfig.USER,
        password=DatabaseConfig.PASSWORD,
        sslmode=DatabaseConfig.SSLMODE,
    )

    conn.autocommit = autocommit
    return conn