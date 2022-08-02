from __future__ import print_function
import os.path
from django.conf import settings
from google.oauth2 import service_account
from googleapiclient.discovery import build

JSON_PATH = 'mainapp/json'


def get_google_add(range):
    SCOPES = [settings.GOOGLE_SHEET_LINK]
    SERVICE_ACCOUNT_FILE = os.path.join(JSON_PATH, 'credentials.json')
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    SAMPLE_SPREADSHEET_ID = settings.SAMPLE_SPREADSHEET_ID
    SAMPLE_RANGE_NAME = range
    service = build('sheets', 'v4', credentials=credentials).spreadsheets().values()
    result = service.get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                         range=SAMPLE_RANGE_NAME).execute()

    data_from_sheet = result.get('values', [])
    return data_from_sheet
