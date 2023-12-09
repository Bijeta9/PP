import random
user_wins = 0
computer_wins = 0

options = ["rock", "paper","scissors"]


while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit. ").lower()
    if user_input == "q":
        break
    

    if user_input not in options:
        continue
    

    random_number = random.randint(0,2) #random_number ma 0 1 ra 2 ma euta generate huncha ra bascha
    #rock:0 paper:1 scissors:2
    computer_pick = options[random_number] #options rock ma 0 aayo, paper ma 1 aaayo and scissors ma 2 aayo.. among this randomly jun number generate huncha tyei gayera bascha
    print("Computer picked", computer_pick + "." )


    if user_input == "rock" and computer_pick == "scissors":
        print("You won!") 
        user_wins += 1
        continue

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!") 
        user_wins += 1
        

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!") 
        user_wins += 1
        
    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins , "times.")
print("The computer won", computer_wins ,"times.")
print("Goodbye!")