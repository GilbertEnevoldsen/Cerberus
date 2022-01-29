import socket

def scan_address(address):
    
    target = socket.gethostbyname(address)
    
    print(f"scanning: {target}\n")
    
    try:
        
        for port in range(1,65535):
            
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(5)
            
            result = s.connect_ex((target, port))
            
            if result == 0:
                
                print(f"port open at {port}")
                
            s.close()
        
        print()
            
    except:
        
        print("\033[31m\n[!] session quit unexpectedly\033[39m\n")