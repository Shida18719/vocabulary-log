"""
 Import required module/library
 """
# import sys
from PyDictionary import PyDictionary
from spellchecker import SpellChecker
# from art import tprint
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
spell = SpellChecker(distance=1)
# Spread sheet variable
vocabulary = SHEET.worksheet("vocabulary")


def display_menu():
    """
    Main display menu
    """
    while True:
        print("""
        VOCABULARY LOG
        ==============
        1. Search, display and log meaning of words
        2. Search words by letter
        3. Search random words
        4. Update worksheet with new word
        5. Exit Program
            """)
        menu_choice = int(input("Select a number of your choice to begin:\n"))
        if menu_choice == 1:
            check_word()
            break
        print("Invalid number! Enter a number between 1-5: \n")


display_menu()
