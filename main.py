from game import get_computer_choice, get_choice_name, play_round

opt = "y"
score = 0

while opt.lower() == 'y':
    print("Enter your choice:\n(1) for snake\n(2) for water\n(3) for gun")
    user_choice = int(input("Your choice: "))
    comp_choice = get_computer_choice()

    result, points = play_round(user_choice, comp_choice)
    score += points

    print(f"Computer chooses: {get_choice_name(comp_choice)}")
    if result == "draw":
        print("It's a draw!")
    elif result == "computer":
        print("Computer wins this round.")
    else:
        print("You win this round!")

    print(f"Your score: {score}")
    opt = input("Do you want to play again? (press y for yes): ")
