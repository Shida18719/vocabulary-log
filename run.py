"""
 Import required module/library
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


# Create an instance of dictionary from dictionary module
dictionary = PyDictionary()

while True:
    # Responds to user input case sensitivity
    new_word = input("Enter new word you want to look up here: \n").casefold()

    if new_word == "":
        break
     
    print(dictionary.meaning(new_word))

