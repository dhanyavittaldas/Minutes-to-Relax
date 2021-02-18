#!/usr/sbin/python
from question import question
import sys
import time
import random



# help flag
if ("--h") in sys.argv:
    print("Lets play are you ready : enter either yes or no.\n difficulty : Choose easy, medium or Hard.\n exit : ctrl+Z.\n Questions: 5 on each set of difficulty.\n score: total score earned.\n")
    exit()

    
#  easy questions
questions_prompt_easy = [
    "- I am always on my way, but never arrive today. What am I?\n\n",
    "- What side of the cat has the most fur?\n\n",
    "- What has a tongue but does not eat or speak?\n\n",
    "- You buy me to eat, but never eat me. What am I?\n\n",
    "- What has a neck but no head?\n\n"



]  

# answer for the easy questions
questions_easy = [
        question(questions_prompt_easy[0], "tommorow"),
        question(questions_prompt_easy[1], "outside"),
        question(questions_prompt_easy[2], "shoe"),
        question(questions_prompt_easy[3], "silverware"),
        question(questions_prompt_easy[4], "bottle"),

]


        # medium  questions
questions_prompt_medium = [
    "- What do you call a three humped camel?\n\n\n",
    "- What can fly without wings?\n\n\n",
    "- What comes down but never goes up?\n\n\n",
    "- On which day of the year does fewer people die?\n\n\n",
    "- I am not alive but I can die what am I?\n\n\n"

    

]  
 
      # answer for the medium questions
questions_medium = [
    question(questions_prompt_medium[0], "pregnant"),
    question(questions_prompt_medium[1], "time"),
    question(questions_prompt_medium[2], "rain"),
    question(questions_prompt_medium[3], "february 29th"),
    question(questions_prompt_medium[4], "battery"),

]  
# hard questions
questions_prompt_hard = [
    "- What moves without seeing and cries without eyes?\n\n",
    "- What has one eye but cant see ?\n\n",
    "- What gets wet while drying?\n\n\n",
    "- What does a rock want to be when it grows up?\n\n",
    "- I have branches but no fruit, trunk or leaves. What am I?\n\n"
]  
 
      # answer for the hard questions
questions_hard = [
    question(questions_prompt_hard[0], "clouds"),
    question(questions_prompt_hard[1], "needle"),
    question(questions_prompt_hard[2], "towel"),
    question(questions_prompt_hard[3], "rockstar"),
    question(questions_prompt_hard[4], "bank"),
]  

# quotes to display for correct answers
quotes_correct = [

    "- With every success of yours, you take yourself to a whole new level.\n\n",
    "- You’re the most brilliant person I have ever known.\n\n",
    "- You have accomplished the things that most men can only dream of.\n\n\n",
    "- No one needs a second look at you to realize what a great achiever you are.\n\n",
    "- You’re doing just perfect on your way of becoming a legend.\n\n"

]

# quotes to display for incorrect answers

quotes_incorrect =[

    "- Storms doesn’t last forever, so cheer up and never give up!\n\n",
    "- You are pretty awesome, never forget that.\n\n",
    "- Life is great when you smile more often.\n\n\n",
    "- The worrisome face of yours doesn’t suit you at all. Make way for a charming smiling face. \n\n",
    "- You are the music to my monotonous life so never dim or fade away.\n\n"

]

# function for the question and answer

def ask_user(questions):
        while True :
            score = 0
            
            for index, question in enumerate(questions):
                print(f"                                                  Question No {index+1}")
                print()
                answer = input(question.prompt)
                print()

    # answer choice if correct code
                if answer == question.answer:
                    quotes_items = random.choice(quotes_correct)
                    
                    print("Your answer is correct" , quotes_items)
                    
                    score += 1
                
    # answer choice if incorrect code  
            
                if answer != question.answer:
                    quotes_item = random.choice(quotes_incorrect)
                    print("Your answer is incorrect", quotes_item)
                    
                print()
                time.sleep(2)
                print_line("*" * 35)
            print("                            You score is " +  str(score) + "/" + str(len(questions)) + "correct")
            print()
            time.sleep(2)
            print_line("*"* 35)
            print()
# answerchoice if no  input code
            if answer == None:
                print("We havent received any input for this question")
# final score board and play again option
            if score >= 5 :
                print("Congratulations! No one needs a second look at you to realize what a great achiever you are. You can accomplish anything that you desire for.")
                time.sleep(1)
                play_again = input("If you'd like to play again, please type yes\n").lower()
                print_line("*"* 35)
                if play_again == "yes":
                    continue
                else :
                    exit()
            if score < 5:
                print("Success and failure will be determined by approach towards them…. Always be cheerful and positive .")
                time.sleep(2)
                play_again = input("If you'd like to play again, please type yes\n").lower()
                print_line("*"* 35)
                if play_again == "yes":  
                    continue
                else :
                    exit()

            

                    
        

        

# line division with *
def print_line(delimiter= ""):
    try:
        print(delimiter * 4)
    except:
        return None


# Welcome message at the start of game
name = input("Please enter your name?\n")
print(f"                             Hey {name}!!!!!!!\n                    **Welcome to Minutes to relax!!**")
print()

answer = input("Lets Play are you ready?\n").lower()
if answer == "yes":
    time.sleep(1)

    print("*********************Tension is who you think you should be. Relaxation is who you are.****************\n")
    time.sleep(2)

    # game instructions
    print("Lets get started.This is a game that will help you relax your mind so that you can have more focus.\n\n You need to answer the next 5 questions trust me its not that hard...... nahhh I was joking :)")
    time.sleep(2)
    print()     
    print("                             OK Let the fun begin!!\n")
    time.sleep(1)

elif answer == "no":
    print("We gonna miss you :( . But when you ready lets spend some time together. Bye!")
    exit()
else :
    exit()

#user choice of difficulty


while True:
    difficulty = input("Well, "+ name + ". What dificulty would you like ? easy, medium or hard?\n").lower()
    time.sleep(1)


    
    if difficulty == "easy":
        print("                                     Ok let us begin!!")
        print_line("" * 35)
        ask_user(questions_easy)
    if difficulty == "medium":
        print("                                      Ok let us begin!!")
        print_line("" * 35)
        ask_user(questions_medium)

    if difficulty == "hard":
        print("                                       Ok let us begin!!")
        print_line("" * 35)
        ask_user(questions_hard)
    print("incorrect input. Try again")
      
        
    
    continue
            
        
        





