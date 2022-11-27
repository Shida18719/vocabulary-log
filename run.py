"""
 Import required modules
 """
from PyDictionary import PyDictionary
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('vocabulary_log')

# new_words = SHEET.worksheet("new_words") 

# data = new_words.get_all_values()

# print(data)

dictionary = PyDictionary()

print(dictionary.meaning("Incomprehensible"))
