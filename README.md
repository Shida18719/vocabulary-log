# Vocabulary Log


Welcome to Vocabulary log! Vocabulary Log is a Python Command Line User Interface, which takes user input in words, define the meaning of the word in English base on coincidence of either a "Noun", "Verb", "Adjective"and "Adverb" then display the meaning to user. User can then choose to Log their new Vocabulary Word in the Google sheet.


[View the live site here](https://shida18719.github.io/)



![VOCABULARY](./READMEimages/imiresponsive-image.png) 


***

# Table of Contents

1. [Overview]()
2. [Features]()
   + [Existing Features]()  
   + [Future Features]() 
3. [User Experience]()
   + [Client Goals]()  
   + [User Stories]() 
   + [Design Structure]() 
   + [Wireframes]() 
4. [Technologies]()
   + [Python Modules/Libraries]() 
5. [Testing]() 
   + [Code validation]()
   + [Manual Testing]()
6. [Bugs]()
   + [Fixed bugs]()
   + [Unknown bugs]()
7. [Deployment]() 
8. [Citation of Sources]() 
   + [Content]()
   + [Media]()
9. [Acknowledgements]() 

***

# 1. Overview

This project is a concept which is aim at helping the user to learn the meaning of new word, in so doing increasing vocabulary usage and able to save their new vocabulary words.

As a mum, and someone who love helping children learn. I took the time to create tones of hand written words and meaning "flash cards" to help my son improve his vocabulary daily, but soon realised how much he let this "cards" fly everywhere after use. As such I decided to create a fun way of learning and improving vocabulary and also save, retrive and access the words for future reference.

An easier method is needed to learn faster and also to help retain the new words and their meaning in the user’s memory. Vocabulary Log aim to achieve this by providing a menu based program where the user can search for the meaning of new words, log the result in a database (Google Sheet), display the meaning of the new word on the screen base on coincidence of "figure of speech", display list of all words and display the meaning of the last two words stored in the database for practicing. There may be occasion where the user might have an idea of a word but not sure of the spelling. The program have an in-built spell checker to display probable words. This assists the user by not only saving time but also making the learning experience enjoyable. With the Vocabulary Log the user can test themselves periodically and have a record of their achievement.

Vocabulary Log is aim at anyone aiming to improve their vocabulary and it's presently for one user, but can be develop for a multi-user program moving forward.  

+ Key Information for this program:

  + Choose from menu display option
  + Enter word to look up meaning
  + Display word and meaning base on coincednce of "figure of speech" using PyDictionary
  + Provide a system for spell checking and providing probable correct word  
  + Log searched word and meaning via google sheet API
  + Display list of search words pulled from the google spreadsheet
  + Display last two words and meaning logged by the user, pulled from the google spreadsheet
  + Provide a reliable error-handling program
  + Provide user with clear instructions 

# 2. Features

## Existing Features
***



## Future Features
***

The following features can be added at a later date in order to improve user experience: 

+ Currently, vocabulary log was only program to retrieve words based on a coincedence of the following figure of speech: "Noun", "Adjective", "Verb" and "Adverb". Which excludes "Synonymn", "Antonymn" and word "translation" to other languages. These can be included to give user varying experience.

+ Refactor code to specify columns for individual figure of speech.

+ Adapt a multi-user functionality via personalised sheet


# 3. User Experience

## Client Goals

+ Create a program where the user can search for the meaning of a word.

+ Create a program where the searched word and meaning will be display on screen.

+ Create a program where the user can log the searched word and meaning.

+ Create a program to assist the user with a probable correct word spelling if the user is unsure.

+ Create a program to display on screen the lists of words logged by the user.

+ Create a program to display on screen the last two words and meaning logged by the user.


## User Stories

+ First Time Visitor Goal:
  + I want to understand how to navigate the program easily
  
  + I want to learn the meaning of new words.

  + I want the word and meaning to be displayed on screen

  + I want to be able to log the meaning of the new words I have learned.

  + I want the program to assist me with the word spelling if I am unsure.

  + I want to be able to view the lists of my save words.

  + I want to be able to display on screen the words and meaning of my last two log.

  + I want to be able to easily exit the program


+ Returning Visitor Goal:

  + I want to continue learning new words and their meaning.

  + I want to see a log of my searched words and their meaning.

  + I want to test myself to see that I retained the meaning of previous words searched.


+ Frequent Visitor Goals:

  + I want my English vocabulary to have improved.

  + I want to learn new words and meaning faster and retain them in memory for easy recall.


## Design Structure
***
This program was design with a simplistic strucrure, with clear and easy to follow instruction, that will allow user easily navigate across the program.

The `tprint ascii art` uses both the standard and the random print to create an environment for fun way of learning, engaging the user and keeping user informed.



## Wireframes

A wireframe is not required due to the nature of the program using the terminal shell to display out.



# 4. Technologies

## Language and Programs used is as follow:

+ [Python](https://www.python.org/) programming language was used for this site


## Programs Used includes:

+ Git - Was used for version control, the Gitpod terminal to commit and push to GitHub.

+ [Gitpod](https://gitpod.io/) - The online integrated development environment (IDE) for all coding work.

+ [GitHub](https://github.com/) - Was used to store the project code  in a repository.

+ [GSpread API](https://developers.google.com/sheets/api) - was used as the API for reading and writing data to the Google Sheet.

+ [Google Auth]() - was used to generate the authentication and authorization credentials for the API


## Python Modules/Libraries 

+ [PyDictionary](https://pypi.org/project/PyDictionary/) - A Dictionary Module for Python, was used to generate meaning of words.

+ [SpellChecker](https://pypi.org/project/pyspellchecker/) - A spell checking algorithm with varying functions. The correction 'correction(word)' function was  used for to returns the most probable result for the misspelt word by the user.

+ [Python Ascii Art](https://pypi.org/project/art/) - a Python library with varying functions and fonts for converting text into ASCII fancy art. Both the standard and the random font was adapted into a printing function for this program.

+ os - A python command used to clear the terminal or shell adapted for clearing the screen after the execution of the program using the `clear()` function, it is called when required.

+ [Time](https://docs.python.org/3/library/time.html) - A python module adapted for delaying the execution of the program.  

+ System Exit - A python module adapted to aborts the execution of the program using the `sys.exit()`.

***

# 5. Testing

+ ## Code Validator Testing

### Pep8
+ No errors or warnings were returned when passing through the [Pep8](https://pep8ci.herokuapp.com/#)


+ ## Manual Testing

This program was tested manually with the following:

+ It was pass through PEP8 linter with all clear - "Results:
All clear, no errors found".

+ This project was also tested on my Gitpod local terminal with the following output:
Test case can be viewed here [<< Manual Testing](test.md)


+ ## Tools

The following tools were used in the development of this project:

+ [GitPod](https://gitpod.io/)
+ [GitHub](https://github.com/)
+ [Heroku](https://www.heroku.com/)
+ [Python Tutor](https://pythontutor.com/visualize.html#mode=edit)
+ [Google Sheets](https://www.google.co.uk/sheets/about/)
+ [Google Drive](https://www.google.co.uk/intl/en-GB/drive/)

***

# 6. Bugs

## Fixed bugs

The following known bugs where caught and fixed during the development stage of this program.

+ `menu_choice = input(int("Choose number between (1-5) to continue:\n"))` run.py Line #285, initialy didn't catch the error message.

  + This was fixed by removing the interger from the input and converting the menu_choice options to string.

+ Working with PyDictionary, the below error was thrown after every word defined from the dictionary. -  
"Error: The Following Error occured: list index out of range"

   + This was fixed using the (`disable_errors=True`) method, inside the meaning variable parenthesis.
   + Code Reference adapted from [Stack Overflow](https://stackoverflow.com/questions/52563826/python-how-to-get-rid-of-pydictionary-error-messages)
   `meaning = dictionary.meaning(corrected_word, disable_errors=True)` run.py Line #133.

+ Used `break` with an if statement, gave the following error:
"SyntaxError: 'break' outside loop"

   +  This was fixed using `sys.exit()` run.py Line #95.
   +  Code Reference adapted from [Stack Overflow](https://stackoverflow.com/questions/2462566/python-break-outside-loop)


+ Error with logging word meaning in to the spreadsheet. 
`vocabulary_worksheet.append_row([word, meaning])`
   + It gave the following error: "AttributeError: 'string' list object has no attribute 'value'"

   + This was fixed by passing the meaning into a string;
   `vocabulary_worksheet.append_row([word, str(meaning)])` run.py Line #152.



## UnKnown Bugs
The only unknown bug is a single character been converted to "i" during the test carried out on the `search_word()` #Line 112

***

# 7. Deployment

## Heroku
***

This project was deloyed to [Heroku](https://www.heroku.com/). The steps taken in deploying this project are as follows:

+ Log in to Heroku or create an account if necessary

+ Navigate to your dashboard, click "New" and select "Create new app"

+ Input an appropriate name for your project and choose a region

+ Click the "Settings" tab

+ Click "Reveal Config Vars"

+ Input PORT and 8000 as one config var and click add

+ Input CREDS and the information from your Google Sheet API creds file as another config var and click add

+ Click "Add buildpack"

+ Add "nodejs" and "python", then click save.

+ Ensure python is the first build pack. YOu can drag to change the order
Select "Deploy" from the heading tabs

+ Select "GitHub - Connect to GitHub" next to the Deployment Methods

+ Click "Connect to GitHub"

+ Search for the repository 'vocabulary-log' and click to connect

+ Click either 'Enable Automatic Deploys' or 'Deploy Branch' to deploy manually. If you select Deploy Branch please note you will need to manually deploy each time you update the repository.

+ Click 'View' to visit the deployed site.


## Forking
***

Fork this repository on Github with the following steps:

+ Log it to GitHub (create account if necessary)
+ Locate the GitHub Respository
+ Find the 'Fork' menu on the top right, click on the small down arrow
+ Select '+ Create a new fork'
+ Remane repository to your choice
+ Click 'Create Fork'
+ The forked version of this repository is all yours


## Cloning
***

Clone this repository on Github with the following steps:

+ Log in to GitHub (create an account if necessary)
+ Locate the GitHub Respository
+ Find and click on the 'Code' menu in the mid-top right of the page.
+ Choose to either download or open in GitHub Desktop, OR
+ Choose the HTTPS option and copy the URL to your clipboard. 
  + To clone the repository using HTTPS, under "HTTPS", copy the url
  + To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click SSH, then copy the url
  + To clone a repository using GitHub CLI, click GitHub CLI, then copy url
  + Open Terminal and change the current directory to where you want the cloned directory.
  + Type git clone, and paste the url, press Enter to create your local clone


***

# 8. Citation of Sources

## General Reference

+ [Code Institute Lesson Content](https://learn.codeinstitute.net/dashboard)

+ [GSpread](https://docs.gspread.org/en/latest/user-guide.html) use for Google Sheet API.

+ [Python Tutor](https://pythontutor.com/visualize.html#mode=edit) used for checking syntax and logic.

+ [W3Schools] use for general python reference

+ [NPStation](https://www.youtube.com/watch?v=Acojo0G9kD0). Used for general knowldege and idea.

+ [PyDictionary](https://pypi.org/project/PyDictionary/). Utilised for PyDictionary usage 

+ [ASCII Art Library For Python](https://pypi.org/project/art/). Utilised for creating ascii art in python.

## Code Reference

+ Code used for the spell checker run.py #Line 112 - (Spelling Checker program using "pyspellchecker") was adapted from [Geeks for Geeks ](https://www.geeksforgeeks.org/spelling-checker-in-python/?ref=gcse)

+ Code used to disable dictionary word meaning error message. run.py  #Line 121, adapted from [Stack Overflow](https://stackoverflow.com/questions/67990505/how-to-get-rid-of-python-dictionary-error-messages)

+ Code adapted to get the value of the word list column. run.py #Line 153 -[Stack Overflow](https://stackoverflow.com/questions/45134764/getting-all-column-values-from-google-sheet-using-gspread-and-python)

+ Clear terminal module. run.py #Line 53, used sparingly in the program where is needed. [geeksforgeeks](https://www.geeksforgeeks.org/clear-screen-python/#:~:text=You%20can%20simply%20%E2%80%9Ccls%E2%80%9D%20to%20clear%20the%20screen%20in%20windows)


***

# 9. Acknowledgements

 I would like to acknowledge the following people who helped me along the way in completing my third milestone project:

  + My family, for their uderstanding and support both morally and mentally.

  + The slack community, for always being there.

  + Tutor - George-Alexandru Ciobanu, for the time spent in guiding and explaing the steps to figuring things out .

  + My Code Institute mentor jubril_mentor, for his guidance.

  + Course provider - Code Institute

















![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)


## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.
