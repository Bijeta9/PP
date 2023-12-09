name = input("Type your name: ")
print("Hi!", name, "Welcome to the adventure game!")

answer = input(
    "You are on a path, and it has come to an end \n You can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input('You have come to a river, Do you want to walk around it or swim across?\nType walk to walk around and swim to swim ').lower()
    if answer == "swim":
        print("You swam across and were eaten by an alligator")

    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back?\nType cross for crossing the road and return for heading back.  ").lower()

    if answer == "cross":
        print("The bridge cracked and you fell down!")

    elif answer == "return":
        print("You are back at the main road .")
        answer = input("You see a strange man standing. Do you want to talk to him?\nType yes for talking to the man and type no for avoiding him. ").lower()
        if answer == "yes":
            print("THAT MAN HAS A WEAPON! He attacks you and you lose")
        elif answer == "no":
            print("You are back and safe. YOU WIN! ")
            
        else:
            print("Not a valid option. You lose.")

else:
    print("Not a valid option. You lose.")

print("Thank you for playing!")