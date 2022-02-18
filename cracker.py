# Function for cracking hashed passwords

import itertools
import hashlib
import string
import time

def crack(passwords, presalt, sufsalt, iterations, algorithm, charpool, wordlist=None, out=None):

    start_time = time.time()
    
    running = True
    cracked = []

    if wordlist != None:

        print("\033[36m [*] cracking using wordlist\033[39m\n")

        for plain in wordlist:
            
            if running == False: break
            
            plain_hash = f"{presalt}{plain}{sufsalt}"
            
            for _ in range(int(iterations)):

                if algorithm == "sha1": plain_hash = hashlib.sha1(plain_hash.encode('utf-8')).hexdigest()
                elif algorithm == "sha224": plain_hash = hashlib.sha224(plain_hash.encode('utf-8')).hexdigest()
                elif algorithm == "sha256": plain_hash = hashlib.sha256(plain_hash.encode('utf-8')).hexdigest()
                elif algorithm == "sha384": plain_hash = hashlib.sha384(plain_hash.encode('utf-8')).hexdigest()
                elif algorithm == "sha512": plain_hash = hashlib.sha512(plain_hash.encode('utf-8')).hexdigest()
                elif algorithm == "blake2b": plain_hash = hashlib.blake2b(plain_hash.encode('utf-8')).hexdigest()
                elif algorithm == "blake2s": plain_hash = hashlib.blake2s(plain_hash.encode('utf-8')).hexdigest()
                elif algorithm == "md5": plain_hash = hashlib.md5(plain_hash.encode('utf-8')).hexdigest()

            if plain_hash in passwords and not plain in cracked:

                print(f" {plain_hash}   {plain}   {round(time.time() - start_time, 1)}s")

                cracked.append(plain)

                if out != None:
                    
                    with open(out, 'a') as file: file.write(f"{plain_hash}   {plain}\n")

                if len(cracked) == len(passwords): running = False
                
                if running == False: break
            
            if running == False: break
        
        print()

    if charpool == None: characters = f"{string.ascii_lowercase}{string.ascii_uppercase}{string.digits}" + " !#¤%&/()=?@£$€{[]}',.-;:_"
    else: characters = charpool

    print("\033[36m [*] cracking using bruteforce\033[39m\n")

    for password_length in range(1, 64):

        for plain in itertools.product(characters, repeat=password_length):
            
            if running == False: break

            plain = "".join(plain)
            plain_hash = f"{presalt}{plain}{sufsalt}"
            
            for _ in range(int(iterations)):

                if algorithm == "sha1": plain_hash = hashlib.sha1(plain_hash.encode('utf-8')).hexdigest()
                elif algorithm == "sha224": plain_hash = hashlib.sha224(plain_hash.encode('utf-8')).hexdigest()
                elif algorithm == "sha256": plain_hash = hashlib.sha256(plain_hash.encode('utf-8')).hexdigest()
                elif algorithm == "sha384": plain_hash = hashlib.sha384(plain_hash.encode('utf-8')).hexdigest()
                elif algorithm == "sha512": plain_hash = hashlib.sha512(plain_hash.encode('utf-8')).hexdigest()
                elif algorithm == "blake2b": plain_hash = hashlib.blake2b(plain_hash.encode('utf-8')).hexdigest()
                elif algorithm == "blake2s": plain_hash = hashlib.blake2s(plain_hash.encode('utf-8')).hexdigest()
                elif algorithm == "md5": plain_hash = hashlib.md5(plain_hash.encode('utf-8')).hexdigest()

            if plain_hash in passwords and not plain in cracked:

                print(f" {plain_hash}   {plain}   {round(time.time() - start_time, 1)}s")
                
                cracked.append(plain)
                
                if out != None:
                    
                    with open(out, 'a') as file: file.write(f"{plain_hash}   {plain}\n")

                if len(cracked) == len(passwords): running = False
                
                if running == False: break
            
            if running == False: break