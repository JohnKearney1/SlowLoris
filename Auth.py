# import hashlib for creating and checking user DB hexes
import hashlib

# Display menu prompt and capture response in var 'input1'
input1 = input("\n\n1. Login\n2. Create User (Local)\n3. Info & usage\n\n>>> ")

# Login
if int(input1) == 1:
    # Open text file in read mode
    f = open("auth.txt", "r")
    # Ask for UID
    UID = input("Enter Username >> ")
    # Read text file into variable 'auth_txt'
    auth_txt = f.read()

    # If the username is found within the text file do:
    if UID in auth_txt:
        password1 = input("Enter Password >> ")
        password2 = hashlib.sha512(b'password1')
        pass_hex = password2.hexdigest()
        if pass_hex in auth_txt:
            exec(open("Main Menu.py").read())
            f.close()
            exit()
        else:
            print("Invalid Password; Exiting.")
            f.close()
            exit()
    else:
        print("Invalid Username; Exiting. ")
        f.close()
        exit()

if int(input1) == 2:
    print("New User:\n\n\n")
    SUUN = input("Enter New Username >> ")
    SUPW = input("Enter New Password >> ")
    print("********************************************************")
    print("                     Confirm (y/n)                      ")
    print("Username: " + SUUN)
    print("Password: " + SUPW)
    print("********************************************************")

    choice = input("(y/n) >> ")

    if choice == 'y':
        f = open("auth.txt", "a")
        SUPW_swap = hashlib.sha512(b'SUPW')
        SUPW_hex = SUPW_swap.hexdigest()

        f.write(SUPW_hex)
        f.write("\n")

        f.write(SUUN)
        f.write("\n")
        f.close()
        print("Registered! Run Auth.py again to login!")
    else:
        print("Invalid Selection; Exiting.")

if int(input1) == 3:
    f = open("info.txt", "r")
    print(f.read())
    f.close()
else:
    print("Invalid Selection; Exiting.")
    f.close()
