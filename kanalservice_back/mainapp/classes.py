from __future__ import print_function
import psycopg2
import os.path
import pickle
import requests
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

JSON_PATH = 'mainapp/json'


class GoogleSheet:
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
    SAMPLE_SPREADSHEET_ID = '1YJNeMjZHmX1rPmeLk2A2JY5Axq_OLeRw8zMHRp5DaNI'
    service = None

    def __init__(self):
        creds = None
        if os.path.exists(os.path.join(JSON_PATH, 'token.pickle')):
            with open(os.path.join(JSON_PATH, 'token.pickle'), 'rb') as token:
                creds = pickle.load(token)

        if not creds or not creds.token:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    os.path.join(JSON_PATH, 'credentials.json'), self.SCOPES
                )
                creds = flow.run_local_server(port=0)
            with open(os.path.join(JSON_PATH, 'token.pickle'), 'wb') as token:
                pickle.dump(creds, token)
        self.service = build('sheets', 'v4', credentials=creds)

    def get_data(self, range):
        try:
            sheet = self.service.spreadsheets()
            result = sheet.values().get(spreadsheetId=self.SAMPLE_SPREADSHEET_ID,
                                        range=range).execute()
            values = result.get('values', [])

            if not values:
                print('No data found.')
                return
            else:
                return values


        except HttpError as err:
            print(err)
