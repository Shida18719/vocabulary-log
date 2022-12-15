"""
 Import required module/library
 """
import sys
import time
from os import system
from art import tprint
from PyDictionary import PyDictionary
from spellchecker import SpellChecker
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
    time.sleep(3.5)


def clear():
    """
    Clears the terminal
    """
    system('clear')


def title_page():
    """
    Display page title using tprint art
    """
    tprint("  VOCABULARY")
    tprint("       LOG")


def save_log():
    """
    Menu function #2,
    Ask the user if they would like to save the new vocabulary,
    Confirm input. If yes, the worksheet_log(word) function is triggered
    to log word into spreadsheet.
    If not, validate user input for their log choice,
    either save and return to display menu or exit the program
    Otherwise, display invalid input, error message
    """
    save = ""
    while True:
        save = input(("\nWould you like to save your new vocabulary?"
                     " (y/n)\n"))
        if save.lower() == "y" or save.lower() == "yes":
            worksheet_log()
            long_sleep()
            clear()
            input('\nPress "Enter" to return to display menu\n')
            display_menu()
        elif save.lower() == "n" or save.lower() == "no":
            print("\nAre you sure? You don't want to save the new vocabulary?")
            user_choice = input('\n"y" = Quit and no word saved.'
                                ' "n" = Save and return to display menu.\n')
            if user_choice.lower() == "y" or user_choice.lower() == "yes":
                exit_progm()
            elif user_choice.lower() == "n" or user_choice.lower() == "no":
                print("\nSaving vocabulary...")
                worksheet_log()
                input('\nPress "Enter" to return to display menu\n')
                clear()
                display_menu()
            else:
                print("Invalid input! Please check and try again.")
                print(user_choice)
        else:
            print("Invalid entry! Sorry... we have to go again.")
            short_sleep()
            input('\nPress "Enter" to continue\n')
            save_log()


def search_word():
    """
    Menu function #1,
    Take user input and display word meaning
    Search a word in dictionary and print its coincidences by types
    Check user misspelt word, returns the correct word
    Check input of empty or whitespace
    Disables PyDictionary errors message
    """
    global word
    word = input("\nEnter new word you want to look up: \n")
    corrected_word = spell.correction(word)

    if word is not corrected_word:
        print("corrected word:", corrected_word)
        if word.count(' ') > 0:
            print("\nOops.. Wrong input!\n")
    else:
        global meaning
        meaning = dictionary.meaning(corrected_word, disable_errors=True)
        types = ["Noun", "Verb", "Adjective", "Adverb"]
        if meaning is None:
            print("Word not found in dictionary. Please double check!")
        else:
            for meaning_type in types:
                try:
                    print(f"{meaning_type} {meaning[meaning_type]}")
                except KeyError:
                    continue


def worksheet_log():
    """
    Update spread sheet, add new row with the new word and meaning of word
    looked up by the user.
    tprint prints updating message
    """
    print("\nUpdating vocabulary log...\n")
    vocabulary_worksheet = SHEET.worksheet("vocabulary")
    vocabulary_worksheet.append_row([word, str(meaning)])
    long_sleep()
    tprint(" Done.")
    tprint("    Word Logged!")


def display_log_words():
    """
    Menu function #3,
    Get and prints lists of saved vocabulary words
    from spreadsheet's words column back the to user
    """
    clear()
    print("fetching your saved vocabulary...\n")
    short_sleep()
    fecth_log = [item for item in vocabulary_sheet.col_values(1) if item]
    fecth_log.pop(0)
    print(fecth_log)
    print("\nLooking good..... Keep it up!\n")
    input('\nPress "Enter" to return to display menu\n')
    display_menu()


def display_last_2_logs():
    """
    Menu function #4,
    Fetch and prints last 2 saved words including word meaning,
    from the spreadsheet back the to user
    Delay prints and clear screen at intervals
    """
    clear()
    print("fetching your last 2 saved vocabulary logs...\n")
    short_sleep()
    print("""
    Here are your Last 2 Logs
    *==*==*==*==*==*==*==*==*
    """)
    all_logs = vocabulary_sheet.get_all_values()
    last_log = all_logs[-1]
    prev_log = all_logs[-2]
    long_sleep()
    clear()
    short_sleep()
    print("""
    Here is your Last log
    *==*==*==*==*==*==*==*
    \n""")
    print(f"\n{last_log}\n")
    long_sleep()
    print("""
    ....and here is your Previous log
    *==*==*==*==*==*==*==*==*==*==*==*
    \n""")
    print(f"\n{prev_log}")
    print("\nPretty cool....Right?\n")
    input('\nPress "Enter" to return to display menu\n')


def exit_progm():
    """
    Menu function #5, allow user exit program, with a validation of input.
    If wrong input, display invalid entry, press enter to continue,
    go back to exit choice
    tprint prints messages in delay print
    """
    while True:
        clear()
        print("\nSo you are calling it a quit?\n")
        exit_choice = input('\n"y" = Stay. "n" = Leave:\n')
        if exit_choice.lower() == "n" or exit_choice.lower() == "no":
            clear()
            tprint("Exiting...")
            short_sleep()
            tprint("Thank you", "random")
            long_sleep()
            clear()
            tprint("See you")
            tprint("       again")
            long_sleep()
            clear()
            tprint("Bye", "random")
            tprint("    Bye", "random")
            long_sleep()
            clear()
            sys.exit()
        elif exit_choice.lower() == "y" or exit_choice.lower() == "yes":
            clear()
            tprint("    Nice")
            tprint("      Decision...")
            long_sleep()
            input('\nPress "Enter" to return to display menu\n')
            display_menu()
        else:
            print("Invalid entry! Please check.")
            short_sleep()
            input('\nPress "Enter" to continue\n')
            print(exit_choice)


def welcome_page():
    """
    Welcome page. Display program title and a welcome message
    Triggers display menu function to start the program
    """
    title_page()
    long_sleep()
    clear()
    long_sleep()
    print("""\n
    ***  Welcome To  Vocabulary Log  ***
    *==*==*==*==*==*==*==*==*==*==*==*==*
    """)
    short_sleep()
    print("""\nVocabulary Log is an interactive mini version of
    the English Dictionary,\n
    where you can get meaning and log new vocabulary.\n""")
    long_sleep()
    print("""\nHow to use Vocabulary Log:\n
    Select an option from display menu,\n
    preferable starting from "1" to begin with.\n
    Press the "Enter" key after your input\n
    """)
    long_sleep()
    clear()
    input('\nPress "Enter" to continue\n')
    display_menu()


def display_menu():
    """
    Main display menu, with user's choice of input,
    Triggers the chosen function
    """
    while True:
        print("""
        V O C A B U L A R Y  L O G
        ==========================
        1. Search and display meaning of words
        2. Save new word to worksheet
        3. Display list of saved words
        4. Display last 2 saved logs
        5. Exit Program
            """)
        menu_choice = input("Choose number between (1-5) to continue:\n")
        if menu_choice == "1":
            search_word()
        elif menu_choice == "2":
            save_log()
        elif menu_choice == "3":
            display_log_words()
        elif menu_choice == "4":
            display_last_2_logs()
        elif menu_choice == "5":
            exit_progm()
        else:
            print("Invalid entry! A number between 1-5 is required\n")
            long_sleep()


welcome_page()
