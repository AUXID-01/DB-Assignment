import gspread
from google.oauth2.service_account import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.readonly"
]


creds = Credentials.from_service_account_file(
    "credentials/service_account.json",
    scopes=SCOPES
)

client = gspread.authorize(creds)

sheet = client.open("titanic").sheet1
data = sheet.get_all_records()

print("✅ Google Sheets Connected")
print("Sample Row:", data[0] if data else "No data")
