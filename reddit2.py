#Importing all libaries required
import praw
import csv
import random
import urllib.request
import time

#Main Function
def memes():
    #Importing the main api
    reddit = praw.Reddit(client_id = "", client_secret = "", username = "", password = "", user_agent = "")
    #Defining out list of memes.
    subredditList = ['DeepFriedMemes', 'dankmemes','shittyadviceanimals', 'me_irl', 'BlackPeopleTwitter', 'memes', 'adviceanimals','terriblefacebookmemes']

    #keep promting the user until he chooses a number between 1-7.
    while True:
        name = 1
        while True:
            try:
                memeChoice = int(input("Please enter a number between 1-7 for memes or any other number for a list of subreddits: "))
                if memeChoice < 8 and memeChoice > 0:
                    break  
                else:
                    print(subredditList)
            except: 
                print('Error Try Again')
        #Setting the users choice to allign with the array        
        memeChoice -= 1
        #Setting a variable subredditChoice because it looks much cleaner and easier to read
        subredditChoice = subredditList[memeChoice]
        #Prompt the user for the number of memes to download from the selected page
        postLimit = int(input("Please enter the number of memes to download from hot: "))
        #Defining variables used in the for loop
        subreddit = reddit.subreddit(subredditChoice)
        hot_python = subreddit.hot(limit = postLimit)
        
        #for each post in the subreddit selected sorted by hot
        #until the post limit is reached
        for submission in hot_python:
            #check that it isnt stickied
            if not submission.stickied:
                url = submission.url
                if "%imgur%" and "%giphy%" and "%.png%" not in url:
                    print("Downloading....")
                    print("Successfully downloaded ", name, " images from ", subredditChoice)
                    full_name = str(name) + "_" + subredditChoice + ".jpg"
                    print(full_name)
                    urllib.request.urlretrieve(url, full_name)
                    name += int(1)
                    print(name)

        con = input("Press Y to download more memes, N to Quit: ")
        if con == 'N' or con == 'n':
            break


memes()