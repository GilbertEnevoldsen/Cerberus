import socket

def scan_address(address):
    
    target = socket.gethostbyname(address)
    
    print(f" scanning: {target}\n")
    
    socket.setdefaulttimeout(1)
    
    common_ports = [80, 443, 8080]
    
    for port in common_ports:
    
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((target, port))
        
        if result == 0: print(f" port open at {port}")
            
        s.close()
    
    socket.setdefaulttimeout(0.25)
    
    try:
        
        for port in range(1, 65535):
            
            if not port in common_ports:
            
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = s.connect_ex((target, port))
                
                if result == 0: print(f" port open at {port}")
                    
                s.close()
        
        print()
            
    except:
        
        print("\033[31m\n [!] session quit unexpectedly\033[39m\n")