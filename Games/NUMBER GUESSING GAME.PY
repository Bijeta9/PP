#quit() quits the whole program to bottom
#break() breaks out 0f the current loop and goes to next line of code
#continue() comes out of loop and goes to the top of the loop

import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit(): #so if the input is digit then we will convert it to integer; if hello is typed it will be error 
   top_of_range = int(top_of_range) #if this is not done then mathi top_of_range ma hamile deko input is considered"25" not number 25 so ot needs to be converted into integer first

   if top_of_range <= 0:
      print("Please type a number larger than 0 next time")
      quit()
    
else:
  print("Please type a number next time")
  quit()


random_number = random.randint(0, top_of_range) #randint for including 11, for including 0 just put 11
guesses = 0

while True:
   guesses += 1
   user_guess = input('Make a guess: ')
   if user_guess.isdigit():
     user_guess = int(user_guess)
   else:
     print("Please type a number next time")
     continue
   
   if user_guess == random_number:
      print('You got it!')
      break
   else:
      print("You got it wrong!")

print("You got it in", guesses, "guesses")  
  