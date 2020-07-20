# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask import session


import requests
import random
API_endpoint = "https://jservice.io/api/clues"
API_query = "value=1000"
API_url = API_endpoint +"?"+ API_query
r = requests.get(API_url)
data = r.json()
print(API_url)

import requests #To access our API

# -- Initialization section --
app = Flask(__name__)

## secret key for session (In production, you would set this key via an environment variable)
app.secret_key = b'HO\xf8\xff+\n\x1e\\~/;}'

# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    session["name"] = "Prachi"
    return render_template('index.html')
@app.route("/random")
def jeopardy_random():
    ## Use jservice API/random to get 1 jeopardy clue
    return render_template("random_clue.html")

def display_clue(clue):
    clue_category = clue["category"]["title"]
    clue_value = clue["value"]
    clue_question = clue["question"]
    print(f"Category: {clue_category}")
    print(f"Value: {clue_value}")
    print(f"Question: {clue_question}")
def input_answer(clue):
    global score
    clue_question = clue["question"]
    answer_user = (input("What is "))
    if answer_user.lower() == clue["answer"].lower():
        print("Congrats!")
        score =+clue["value"]
    else:
        print("Sorry! That didn't work.")
        score =-clue["value"]
score=0
print("Welcome to the game!")
while True:
    clue_one = random.choice(data)
    display_clue(clue_one)
    input_answer(clue_one)
    print(score)
    if input("Play again? y/n") == "n":
        break 



@app.route('/answerJeopardy', methods = ['GET', 'POST'])
def answerJeopardy():
    if request.method == 'GET':
        return ""
    else:   
        def display_clue(clue):
            clue_category = clue["category"]["title"]
            clue_value = clue["value"]
            clue_question = clue["question"]
            print(f"Category: {clue_category}")
            print(f"Value: {clue_value}")
            print(f"Question: {clue_question}")
def input_answer(clue):
    global score
    clue_question = clue["question"]
    answer_user = (input("What is "))
    if answer_user.lower() == clue["answer"].lower():
        print("Congrats!")
        score =+clue["value"]
    else:
        print("Sorry! That didn't work.")
        score =-clue["value"]
score=0
print("Welcome to the game!")
while True:
    clue_one = random.choice(data)
    display_clue(clue_one)
    input_answer(clue_one)
    print(score)
    if input("Play again? y/n") == "n":
        break 
    
   






