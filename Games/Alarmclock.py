from playsound import playsound
import time
#ANSI characters/escape sequences are used to manipulate the terminal, are invisible themselves but can bold,clear,underline, change colours etc
 
CLEAR = "\033[2J" #clear the terminal, so everything is on the same line and it looks like its constantly updating
CLEAR_AND_RETURN = "\033[H" #clears and returns to home postion and prints over what we had before

def alarm(seconds): #for how long until alarm is gonna buzz
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1) #wait for a second
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60 #integer division is two forward slashes eg 125//60 =2
        seconds_left = time_left % 60 #125 % 60 = 5


        print(f"{CLEAR_AND_RETURN}Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}") #using f it will not matter if lowercase or uppercase 
                              #02d adds 0 to the front of the digit and make two digits 
    playsound("losttime.mp3")    

minutes = int(input("How many minutes to wait: "))  
seconds = int(input("How many seconds to wait: ")) 
total_seconds = minutes * 60 + seconds         
alarm(total_seconds)