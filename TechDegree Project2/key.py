"""
Creates a class for the Keyword Cipher. Encryption and Decryption
Author: Zachary Collins
Date: July, 2018
"""

import string

from ciphers import Cipher


class Keyword(Cipher):
    
    def __init__(self, keyword):
        """Creates an instance of the Keyword Cipher with the provided keyword"""
        
        #Makes sure the key doesn't have repeat letters
        self.key = "".join([j for i,j in enumerate(keyword) if j not in keyword[:i]])
        self.alpha = list(string.ascii_lowercase)
        
        #Creates the encrypted alphabelt. Used for encryption and decryption
        self.encrypted_alpha = list(self.key)
        for letter in self.alpha:
            if letter not in self.key:
                self.encrypted_alpha.append(letter)
        
    
    def encrypt(self, text): 
        """Encrpyts a given piece of text"""
        
        text = text.lower()
        encrypted_word = []
        for letter in text:
            try:
                index = self.alpha.index(letter)
            except ValueError:
                encrypted_word.append(letter)
            else:
                encrypted_word.append(self.encrypted_alpha[index])
        return "".join(encrypted_word)

    
    def decrypt(self, text):
        """Decrpyts a given piece of text"""
        
        text = text.lower()
        decrypted_word = []
        for letter in text:
            try:
                index = self.encrypted_alpha.index(letter)
            except ValueError:
                decrypted_word.append(letter)
            else:
                decrypted_word.append(self.alpha[index])
        return "".join(decrypted_word)

