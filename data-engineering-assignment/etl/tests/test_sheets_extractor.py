"""
Smoke test for Google Sheets extractor.
"""

from etl.extract.sheets_extractor import extract_google_sheet


def test_extract_google_sheet():
    rows = extract_google_sheet()

    assert isinstance(rows, list)

    if rows:
        assert isinstance(rows[0], dict)

    print(f"✅ Sheets extractor test PASSED — extracted {len(rows)} rows")


if __name__ == "__main__":
    test_extract_google_sheet()