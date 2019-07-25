# "X" - TimMiller32
# Project Started: 07/24/2019 2:00 AM - NC, USA

import os

# Read "TimMiller32" header from "TIM.txt"

while 1:

    f = open('TIM.txt', 'r')
    timmiller32 = f.read()
    f.close()

    # Print Menu and Header from "TIM.txt"
    print(timmiller32)

    # +1 line
    print("\n")

    # Ask for input
    input_var = input(" >>> ")

    if int(input_var) == 1:
        exec(open("Cryptography.py").read());

    if int(input_var) == 2:
        exec(open("Deauther.py").read());

    if int(input_var) == 3:
        exec(open("SlowLoris.py").read());

    if int(input_var) == 4:
        exec(open("Bruteforce.py").read());

    if int(input_var) == 5:
        exec(open("NetworkScanner.py").read());

    if int(input_var) == 6:
        choice1 = input("1. Run Email Spoofer\n2. How to Use\n\n >>> ")
        if int(choice1) == 1:
            esF = input("Enter Path to Email File (HTML) >>> ")
            esT = input("Enter TO Address >>> ")
            esF1 = input("Enter FROM Address >>> ")
            esFN = input("Enter FROM Name >>> ")
            esFN2 = input("Enter Email Subject >>> ")
            os.system(
                "python3 SimpleEmailSpoofer.py -e" + esF + ' -t ' + esT + ' -f ' + esF1
                + ' -n ' + esFN + ' -f ' + esFN2)
        if int(choice1) == 2:
            f1 = open("SESinfo.txt", "r")
            SESinfo = f1.read()
            print(SESinfo)
            f1.close()

    if int(input_var) == 7:
        print(" Goodbye!\n - TimMiller32"),
        exit()
    else:
        print("Invalid Choice")
