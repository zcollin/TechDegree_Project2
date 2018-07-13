"""
Creates a class for the Affine Cipher. Encryption and Decryption
Author: Zachary Collins
Date: July, 2018
"""

import string

from ciphers import Cipher


class Affine(Cipher):
    
    def __init__(self, a=5, b=8, m=26):
        """Creates an instance of the Affine Cipher"""
        
        self.a = a
        self.b = b
        self.m = m
        self.alpha = list(string.ascii_lowercase)


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
                #Uses Affine encryption function to encrypt the word
                new_index = ((self.a*index)+self.b)%self.m
                encrypted_word.append(self.alpha[new_index])
        return "".join(encrypted_word)

    
    def decrypt(self, text):
        """Decrpyts a given piece of text"""
        
        decrypted_word = []
        for letter in text:
            try:
                index = self.alpha.index(letter)
            except ValueError:
                decrypted_word.append(letter)
            else:
                #Uses Affine decryption function to decrypt the word
                new_index = ((21*(index-self.b))%self.m)
                decrypted_word.append(self.alpha[new_index])
        return "".join(decrypted_word)

