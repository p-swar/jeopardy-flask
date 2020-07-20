
import requests
import random

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