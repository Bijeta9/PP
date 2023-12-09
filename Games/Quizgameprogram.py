print("Welcome to the Biju Quiz!!")

play = input("Do you want to play? ")

if play.lower() != "yes":
    quit()

print("Okay!! Let's start the game!! ")
score=0

ans = input("What is the capital city of Nepal? ")
if ans.lower() == "kathmandu":
    print("Correct! You've scored a point! ")
    score += 1

else:
    print("Sorry! You've got it wrong! ")

ans = input("How many countries lies in the continent Asia? ")
if ans == "48":
    print("Correct! You've scored a point!")
    score += 1

else:
    print("Sorry! You've got it wrong! ")

ans = input("What is the national sport of Nepal? ")
if ans.lower() == "volleyball":
    print("Correct! You've scored a point! ")
    score += 1

else:
    print("Sorry! You've got it wrong! ")

ans = input("Who is the prime minister of Nepal of 2022? ")
if ans.lower() == "sher bahadur deuba":
     print("Correct! You've scored a point! ")
     score += 1

else:
    print("Sorry! You've got it wrong! ")

ans = input("Who is the president of Nepal of 2022? ")
if ans.lower() == "bidhya devi bhandari":
     print("Correct! You've scored a point! ")
     score += 1

else:
    print("Sorry! You've got it wrong! ")

print("You've got " +str(score)+ " Questions correct! ")
print("You scored " +str((score/5)*100)+ "%")
