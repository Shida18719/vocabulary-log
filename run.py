"""
 Import required module/library
 """
import sys
# import random
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
# print(SHEET.readlines())

# Variable for spreadsheet worksheets
vocabulary = SHEET.worksheet("vocabulary")


# Create an instance from  module
dictionary = PyDictionary()
spell = SpellChecker()

# Global variable
word = ""


def check_word():
    """
    Take user input and display word meaning
    Search a word in dictionary and print its coincidences
    Check user misspelt word
    """
    global word
    word = input("\nEnter new word you want to look up: \n")
    corrected_word = spell.correction(word)
    print("corrected_word ", corrected_word)

    if word == "":
        sys.exit()
    else:
        meaning = (dictionary.meaning(corrected_word, disable_errors=True))
        if meaning is None:
            print("Word not found")
        else:
            try:
                print("Noun", meaning["Noun"])
                print("Verb", meaning["Verb"])
                print("Adjective", meaning["Adjective"])
                print("Adverb", meaning["Adverb"])
            except KeyError:
                pass


def display_menu():
    """
    Main display menu
    """
    while True:

        # open_page()
        print("""
        V O C A B U L A R Y  L O G
        ==========================
        1. Search, display and log meaning of words
        2. Search random words
        3. Update worksheet with new word
        4  Display worksheet log
        5. Exit Program
            """)
        menu_choice = int(input("Select a number of your choice to begin:\n"))
        if menu_choice == 1:
            check_word()
        elif menu_choice == 2:
            update_worksheet()
        # elif menu_choice == 3:
        #     display_log()
        # elif menu_choice == 4:
            break
        else:
            print("Invalid number! Enter a number between 1-4: \n")

    # except:
    #     print("Invalid entry")


display_menu()
