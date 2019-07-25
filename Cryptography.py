#!/usr/bin/env python3

import hashlib

while 1:
    # Ask for input and encode it in bytes
    print(" ___________________________________________________________")
    print("|     This program gives you a SHA512 hex for a string.     |\n"
          "|              SHA512 ENCODER - TimMiller32                 |\n"
          "|___________________________________________________________|")

    ES = input("\n  Enter the string to be encrypted, or type 'Exit' to quit: \n>>>").encode()

    # Create SHA512 Hash
    str = hashlib.sha512(ES)
    str_hex = str.hexdigest()

    # Define SHA512 Hash that matches "Exit"
    str_exit = "136b06685db6433ea160711ff0cfd88ca58b6d24bab6a39c3cdba68be6652b1e987c7772ed85bdbcb31ca45d5949831358803d15bc0cbea8da3d7cee89a0fc22"

    # Check if the input is = to "Exit"
    if str_hex == str_exit:
        exit()

    # if not, print the input in its hashed form:
    else:
        print("Your SHA512 hex is: " + str_hex)
