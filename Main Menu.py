# "X" - TimMiller32
# Project Started: 07/24/2019 2:00 AM - NC, USA

import os

# Read "TimMiller32" header from "TIM.txt"

f = open('TIM.txt', 'r')
timmiller32 = f.read()
f.close()

# Print Menu and Header from "TIM.txt"
print(timmiller32)

# +1 line
print("\n")

# Ask for input
input_var = input(">>>")

if int(input_var) == 1:
    exec(open("Cryptography.py").read());

if int(input_var) == 2:
    exec(open("Deauther.py").read());

if int(input_var) == 3:
    exec(open("SlowLoris.py").read());

if int(input_var) == 4:
    exec(open("Bruteforce.py").read());

if int(input_var) == 5:
    os.system("Py NetworkScanner.py -i " + input("Enter Network Interface (Monitor Mode) >>> "))

if int(input_var) == 6:
    print(" Goodbye!\n - TimMiller32"),
    exit()
