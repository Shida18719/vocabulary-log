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