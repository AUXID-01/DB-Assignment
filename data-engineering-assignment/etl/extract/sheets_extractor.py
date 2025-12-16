"""
Google Sheets Extractor

Purpose:
- Extract raw tabular data from Google Sheets
- Return data as List[Dict[str, Any]]
- Perform NO cleaning, validation, or transformation

This module is part of the Extract phase of the ETL pipeline.
"""

from typing import List, Dict, Any

from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

from etl.config.sheet_config import load_sheet_config
from etl.utils.logger import get_logger

logger = get_logger(__name__)

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]


def extract_google_sheet() -> List[Dict[str, Any]]:
    """
    Extract raw rows from a Google Sheet.

    Returns:
        List of rows as dictionaries using header row as keys.

    Raises:
        Exception if extraction fails.
    """

    config = load_sheet_config()

    logger.info("Starting Google Sheets extraction")
    logger.info(f"Sheet ID: {config.sheet_id}")
    logger.info(f"Range: {config.range_name}")

    creds = Credentials.from_service_account_file(
        config.service_account_file,
        scopes=SCOPES,
    )

    service = build("sheets", "v4", credentials=creds, cache_discovery=False)
    sheet = service.spreadsheets()

    result = sheet.values().get(
        spreadsheetId=config.sheet_id,
        range=config.range_name,
    ).execute()

    values = result.get("values", [])

    if not values:
        logger.warning("No data found in Google Sheet")
        return []

    headers = values[0]
    data_rows = values[1:]

    records: List[Dict[str, Any]] = []

    for row in data_rows:
        record = {}
        for idx, header in enumerate(headers):
            record[header] = row[idx] if idx < len(row) else None
        records.append(record)

    logger.info(f"Extracted {len(records)} rows from Google Sheet")

    return records