import pyfiglet as pyg
from termcolor import colored

print("NOTE: TYPE THE MESSAGE AND KEYWORK IN ALL UPPERCASE LETTERS WITH NO SPACES")

def generateKey(string, key): 
    key = list(key) 
    if len(string) == len(key): 
        return(key) 
    else: 
        for i in range(len(string) -len(key)): 
            key.append(key[i % len(key)]) 
    return("" . join(key))
  
def cipher(string, key): 
    cipher_text = [] 
    for i in range(len(string)): 
       x = (ord(string[i]) +ord(key[i])) % 26
       x += ord('A') 
       cipher_text.append(chr(x)) 
    return("" . join(cipher_text)) 

if __name__ == "__main__": 
    string = input("ENTER THE MESSAGE: ")
    keyword = input("ENTER THE KEYWORD: ")