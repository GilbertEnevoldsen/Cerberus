import random
import string

def encrypt(file, key):

    if key == None:

        charpool = string.ascii_letters + string.digits
        key = "".join([random.choice(charpool) for _ in range(32)])

    print(f" key: {key}\n")

    def encode(file, key):

        max_index = len(key) - 1

        with open(file, 'rb') as f:
            data = f.read()

        with open(file, 'wb') as f:
            index = 0

            for byte in data:
                
                xor_byte = byte ^ ord(key[index])
                f.write(xor_byte.to_bytes(1, 'little'))
                
                if index >= max_index:
                    index = 0
                    
                else:
                    index += 1

    print(" encoding 1/7")
    encode(file, key)
    print(" encoding 2/7")
    encode(file, key[:16])
    print(" encoding 3/7")
    encode(file, key[16:])
    print(" encoding 4/7")
    encode(file, key[:8])
    print(" encoding 5/7")
    encode(file, key[8:16])
    print(" encoding 6/7")
    encode(file, key[16:24])
    print(" encoding 7/7")
    encode(file, key[24:32])
    print()