"""
 Import required module/library
 """
import sys
from PyDictionary import PyDictionary
from spellchecker import SpellChecker
# from art import tprint
import gspread
from google.oauth2.service_account import Credentials


# API
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
# vocabulary_sheet = SHEET.worksheet("vocabulary")


# Create an instance from  module
dictionary = PyDictionary()
spell = SpellChecker()

# Global variable
word = ""


def save_log():
    """
    Ask the user if they would like to save the new vocabulary,
    Confirm input. If yes, the worksheet_log(word) function is triggered
    to log word to spreadsheet.
    If not, validate user input for their log choice, 
    either save and return to display_menu or exit the program
    """
    key = ""
    while True: 
        key = input(("\nWould you like to save your new vocabulary?"
                     " (y/n)\n"))
        if key.lower() == "y" or key.lower() == "yes":
            worksheet_log(word)
            input('\nPress "Enter" to return to display menu\n')
            display_menu()
        elif key.lower() == "n " or key.lower() == "no":
            print("\nAre you sure? You don't want to save the new vocabulary?")
            user_choice = input('\n"y" = Quit and no word saved.'
                                ' "n" = Save and return to Main Menu.\n')
            if user_choice.lower() == "y" or user_choice.lower() == "yes":
                sys.exit()
            elif user_choice.lower() == "n" or user_choice.lower() == "no":
                print("\nSaving vocabulary...")
                worksheet_log(word)
                input('\nPress "Enter" to return to display menu')
            else:
                print("Log completed")         


def search_word():
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


def worksheet_log(word):
    """
    Update spread sheet, add new row with the new word searched
    by the user from the dictionary
    """
    print("\nUpdating vocabulary log...\n")
    vocabulary_worksheet = SHEET.worksheet("vocabulary")
    vocabulary_worksheet.append_row([word])
    print("Updating Done. Word Logged! \n")


# def title_page():
#     """
#     Display page title using tprint art
#     """
#     tprint("VOCABULARY  LOG")


# def open_page():
#     """
#     Welcome page
#     """
#     title_page()
#     print("\n *** Welcome to Vocabulary Log ***")


def display_menu():
    """
    Main display menu
    """
    while True:

        # open_page()
        print("""
        V O C A B U L A R Y  L O G
        ==========================
        1. Search and display meaning of words
        2. Save new word to worksheet
        3. Display worksheet log
        4. Exit Program
            """)
        menu_choice = int(input("Select number of your choice to continue:\n"))
        if menu_choice == 1:
            search_word()
        elif menu_choice == 2:
            save_log()
        # elif menu_choice == 3:
        #     display_log()
        # elif menu_choice == 4:
            break
        else:
            print("Invalid number! Enter a number between 1-4: \n")

    # except:
    #     print("Invalid entry")


display_menu()
