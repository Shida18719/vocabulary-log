# Vocabulary Log


Welcome to Vocabulary log! Vocabulary Log is a Python Command Line User Interface, which takes user input in words, define the meaning of the word in English base on coincidence of either a "Noun", "Verb", "Adjective"and "Adverb" then display the meaning to user. User can then Log their new Vocabulary Word in the Google sheet.


[View the live site here](https://shida18719.github.io/)



![VOCABULARY](./READMEimages/imiresponsive-image.png) 


***

1. [Overview]()
2. [Features]()
   + [Existing Features]()  
   + [Future Features]() 
3. [User Experience]()
   + [Site Goals]()  
   + [User Stories]() 
   + [Design Structure]() 
   + [Wireframes]() 
4. [Technologies]()
   + [Python Modules/Libraries]() 
5. [Testing]() 
   + [Code validation]()
   + [Test case]()
6. [Bugs]()
   + [Manual Testing]()
   + [Fixed bugs]()
   + [Unknown bugs]()
7. [Deployment]() 
8. [Citation of Sources]() 
   + [Content]()
   + [Media]()
9. [Acknowledgements]() 

***


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

+ [NPStation](https://www.youtube.com/watch?v=Acojo0G9kD0). Used for general knowldege.


## Code Reference

+ Code used for the spell checker #Line 112 - (Spelling Checker program using "pyspellchecker") was adapted from [Geeks for Geeks ](https://www.geeksforgeeks.org/spelling-checker-in-python/?ref=gcse)

+ Code used to disable dictionary word meaning error message. #Line 121, adapted from [Stack Overflow](https://stackoverflow.com/questions/67990505/how-to-get-rid-of-python-dictionary-error-messages)

+ Code adapted to get the value of the word list column. #Line 153 -[Stack Overflow](https://stackoverflow.com/questions/45134764/getting-all-column-values-from-google-sheet-using-gspread-and-python)

+ Clear terminal module. #Line 53, used sparingly in the program where is needed. [geeksforgeeks](https://www.geeksforgeeks.org/clear-screen-python/#:~:text=You%20can%20simply%20%E2%80%9Ccls%E2%80%9D%20to%20clear%20the%20screen%20in%20windows)


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

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!