import random
opt="y"
counter=0
while(opt=='y'):

    computer=(random.randint(1,3))
    user=int(input("Enter your choice: \n(1) for snake \n(2) for water \n(3) for gun\n"))
    _1="snake"
    _2="water"
    _3="gun"
    
    if (computer==1 and user== 2):
        print(f"Computer chooses {_1} \nComputer win")
        print(f"Your score is : {counter} ")
    elif(computer==2 and user==3):
        print(f"Computer chooses {_2} \nComputer win")
        print(f"Your score is : {counter} ")  
    elif(computer==3 and user==1):
        print(f"Computer chooses {_3} \nComputer win")
        print(f"Your score is : {counter} ") 
    elif(computer==user):
        print("Game Draw!")
        print(f"Your score is:  {counter}")
    else:
        if computer == 1:
            computer_choice = _1
        elif computer == 2:
            computer_choice = _2
        elif computer == 3:
            computer_choice = _3
        print(f"Computer chooses {computer_choice} \nYou Won")
        counter=counter+1
        print(f"Your score is: {counter}")
        
    print("Do you want to play again? (enter y for yes)")    
    opt=input()
    continue




