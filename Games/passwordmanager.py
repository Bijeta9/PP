from cryptography.fernet import Fernet #for encryption of the password

#use this fucntion once to generate the key -> encrypted one
'''def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)'''
#write_key()

def load_key(): #decryption
    file = open("key.key", "rb") #reading bytes
    key = file.read()
    file.close()
    return key


key = load_key()  #encode takes your string and turns it into bytes
fer = Fernet(key)

'''key + password + text to encrypt = random text
 random text + key + password = text to encrypt'''


def view():
    with open("passwords.txt", 'r') as f: #passwords.txt is a file, a is a mode ..other modes are w-write(always rewrites and replaces) r-read(only reading) a-append (add somthing to the end of the existing file and create a new file if one doesnot already exists)
        for line in f.readlines():
            data = line.rstrip() #remove extra new line in the output
            user, passw = data.split("|")
            #user, passw = ["hello","biju"] we only have two characters name and password so user and passw is used ; if more use more
            #removes all the pipe characters and does this hello|Biju|yes -> ["hello","yes","2"]
            print("User: ",user,"\nPassword: ", fer.decrypt(passw.encode()).decode())


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt", 'a') as f: #passwords.txt is a file, a is a mode ..other modes are w-write(always rewrites and replaces) r-read(only reading) a-append (add somthing to the end of the existing file and create a new file if one doesnot already exists)
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")    
while True:
    mode = input("Would you like to add a new password or view existing ones (view,add), press q to quit ").lower()

    if mode == "q":
        break

    if mode == "view":
        view()

    elif mode == "add":
        add()

    else:
        print("Invalid mode")
        continue
