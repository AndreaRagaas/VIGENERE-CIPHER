# VIGENERE-CIPHER
A program that asks the user for the plaintext (all uppercase letters, no spaces) and the keyword (all uppercase letters) and produce the ciphertext using the Vigenère cipher. 
     
The Vigenère Cipher works as follows:
Your key is a keyword, which you then translate into corresponding letter values 0 – 25. Then, to encrypt, write your message on one row (letters 0 – 25), and repeatedly write the keyword below it, adding each column, taking the result mod 26. These resultant numbers are the ciphertext.

To run the program:
     Install a pyfiglet (for creative font style).
     Install a termcolor (for creative colors).
