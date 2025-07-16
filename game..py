import random

def get_computer_choice():
    return random.randint(1, 3)

def get_choice_name(choice):
    return {1: "snake", 2: "water", 3: "gun"}.get(choice, "invalid")

def play_round(user, computer):
    if computer == user:
        return "draw", 0
    elif (computer == 1 and user == 2) or (computer == 2 and user == 3) or (computer == 3 and user == 1):
        return "computer", 0
    else:
        return "user", 1
