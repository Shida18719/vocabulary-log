"""
 Import required module/library
 """
import sys
import time
from os import system
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
vocabulary_sheet = SHEET.worksheet("vocabulary")


# Create an instance from  module
dictionary = PyDictionary()
spell = SpellChecker()

# Global variable
word = ""
meaning = ""


def short_sleep():
    """
    Creating a short sleep timer to delay printing
    """
    time.sleep(1.5)


def long_sleep():
    """
    Creating a Long sleep timer to delay printing
    """
    time.sleep(3)


def clear():
    """
    Clears the terminal
    """
    system('clear')


# def title_page():
#     """
#     Display page title using tprint art
#     """
#     tprint("VOCABULARY  LOG")   


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
            log_meaning(meaning)
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
                log_meaning(meaning)
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

    if word is not corrected_word:
        print("corrected_word: ", corrected_word)

    if word == "":
        sys.exit()
    else:
        meaning = (dictionary.meaning(corrected_word, disable_errors=True))
        if meaning is None:
            print("Word not found in dictionary")
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
    by the user
    """
    print("\nUpdating vocabulary log...\n")
    vocabulary_worksheet = SHEET.worksheet("vocabulary")
    vocabulary_worksheet.append_row([word])
    print("Updating Done. Word Logged! \n")


def log_meaning(meaning):
    """
    Update spread sheet, add new row with the new word searched
    by the user from the dictionary
    """
    meaning = ""
    print(meaning)
    vocabulary_worksheet = SHEET.worksheet("vocabulary")
    meaning_row = vocabulary_worksheet
    meaning_row.append_row([meaning])
    print("Updating Done. Word Logged! \n")


def display_log():
    """
    Get and prints saved vocabulary from the spreadsheet back the to user,
    """
    clear()
    print("fetching your saved vocabulay...\n")
    short_sleep()
    fecth_log = vocabulary_sheet.get_all_values()
    print(fecth_log)
    print("\nLooking good..... Keep it up\n")
    input('\nPress "Enter" to return to display menu')
    display_menu()


def exit_progm():
    """
    Function #4 to allow user exit program, with a validation of input
    """
    while True:
        clear()
        print("\nSo you are calling it a quit?\n")
        exit_choice = input('\n"y" = Stay. "n" = Leave:\n')
        if exit_choice.lower() == "n" or exit_choice.lower() == "no":
            clear()
            print("\nExiting...\n")
            short_sleep()
            tprint("Thank you")
            long_sleep()
            sys.exit()
        elif exit_choice.lower() == "y" or exit_choice.lower() == "yes":
            display_menu()
        else:
            clear()
            print("\nNice decision...")
            long_sleep()


def welcome_page():
    """
    Welcome page
    """
    # title_page()
    clear()
    long_sleep()
    print("\n *** Welcome to Vocabulary Log ***")
    short_sleep()
    print("\nVocabulary Log is an interactive mini version of English "
          "dictionary, where you can log new vocabulary words.")
    short_sleep()
    input('\nPress "Enter" to continue\n')
    display_menu()


def display_menu():
    """
    Main display menu, on user's choice,
    Triggers the chosen function
    """
    while True:
        print("""
        V O C A B U L A R Y  L O G
        ==========================
        1. Search and display meaning of words
        2. Save new word to worksheet
        3. Display worksheet log
        4. Exit Program
            """)
        menu_choice = int(input("Choose number between (1-4) to continue:\n"))
        if menu_choice == 1:
            search_word()
        elif menu_choice == 2:
            save_log()
        elif menu_choice == 3:
            display_log()
        elif menu_choice == 4:
            exit_progm()
        else:
            print("Invalid number! Enter a number between 1-4: \n")
            long_sleep()


welcome_page()
