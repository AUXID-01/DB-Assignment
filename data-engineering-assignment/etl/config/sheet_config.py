"""
Google Sheets configuration for ETL pipeline.

Purpose:
- Centralize all Google Sheets–related configuration
- Validate required environment variables
- Provide a clean config object for extractors

This module contains NO extraction logic.
"""

import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


class SheetConfigError(Exception):
    """Raised when Google Sheets configuration is invalid."""


@dataclass(frozen=True)
class SheetConfig:
    sheet_id: str
    range_name: str
    service_account_file: str
    application_name: str = "ETL Pipeline"


def load_sheet_config() -> SheetConfig:
    """
    Load and validate Google Sheets configuration from environment variables.

    Required ENV variables:
    - GOOGLE_SHEET_ID
    - GOOGLE_SHEET_RANGE
    - GOOGLE_SERVICE_ACCOUNT_FILE
    """

    sheet_id = os.getenv("GOOGLE_SHEET_ID")
    range_name = os.getenv("GOOGLE_SHEET_RANGE")
    service_account_file = os.getenv("GOOGLE_SERVICE_ACCOUNT_FILE")

    missing = []
    if not sheet_id:
        missing.append("GOOGLE_SHEET_ID")
    if not range_name:
        missing.append("GOOGLE_SHEET_RANGE")
    if not service_account_file:
        missing.append("GOOGLE_SERVICE_ACCOUNT_FILE")

    if missing:
        raise SheetConfigError(
            f"Missing required environment variables: {', '.join(missing)}"
        )

    if not os.path.exists(service_account_file):
        raise SheetConfigError(
            f"Service account file not found: {service_account_file}"
        )

    return SheetConfig(
        sheet_id=sheet_id,
        range_name=range_name,
        service_account_file=service_account_file,
    )