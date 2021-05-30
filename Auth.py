# Import hashlib for creating and checking user DB hexes

import hashlib

while 1:
    # Display menu prompt and record response in var 'input1'
    input1 = int(input("\n\n1. Login\n2. Create User (Local)\n3. Info & usage\n\n>>> "))

    # Login
    if int(input1) == 1:
        # Open text file in read mode
        f = open("auth.txt", "r")
        # Ask for UID
        UID = input("\nEnter Username >> ")
        # Read text file into variable 'auth_txt'
        auth_txt = f.read()

        # If the username is found within the text file do:
        if UID in auth_txt:
            password1 = input("\nEnter Password >> ")
            password2 = hashlib.sha512(b'password1')
            pass_hex = password2.hexdigest()
            if pass_hex in auth_txt:
                print(f'\nWelcome {username}!')
                exec(open("Main Menu.py").read())
                f.close()
                exit()
            elif pass_hex not in auth_txt:
                print("\n\nInvalid Password; Exiting.")
                f.close()
                exit()
        else:
            print("\n\nInvalid Username; Exiting. ")
            f.close()
            exit()

    if int(input1) == 2:
        print("\nNew User:\n\n\n")
        SUUN = input("\n\nEnter New Username >> ")
        SUPW = input("\n\nEnter New Password >> ")
        print("\n\n********************************************************")
        print("                     Confirm (y/n)                      ")
        print("Username: " + SUUN)
        print("Password: " + SUPW)
        print("********************************************************")

        choice = input("(y/n) >> ").upper()

        if choice == 'Y':
            f = open("auth.txt", "a")
            SUPW_swap = hashlib.sha512(b'SUPW')
            SUPW_hex = SUPW_swap.hexdigest()

            f.write(SUPW_hex)
            f.write("\n")

            f.write(SUUN)
            f.write("\n")
            f.close()
            print("\n\nRegistered! Re-run Auth.py again to login!")

        elif choice != 'Y':
            print("\n\nInvalid Selection; Exiting.")

    if int(input1) == 3:
        f = open("info.txt", "r")
        print(f.read())
        f.close()
    elif int(input1) > 3 or int(input1) < 1:
        print("\n\nInvalid Selection; Exiting.")
        f.close()
