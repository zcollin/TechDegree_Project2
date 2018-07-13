"""
Creates a class for the Polybius Square Cipher. Encryption and Decryption
Author: Zachary Collins
Date: July, 2018
"""

import string

from ciphers import Cipher


class Polybius(Cipher):
    
    def __init__(self):
        """Creates an Instance of the Polybius Square Cipher"""
        
        self.alpha = list(string.ascii_lowercase)
        
        #Fills the Polybius Square with the alphabetical values
        self.square = []
        line = []
        for letter in self.alpha:
            if letter == "i":
                continue
            if len(line) == 5:
                self.square.append(line)
                line = []
            line.append(letter)
        self.square.append(line)
        
           
    def encrypt(self, text):
        """Encrpyts a given piece of text"""
        
        #Removes spaces from the phrase. Causes errors in encryption
        text = text.split(" ")
        text = "".join(text)
        text = text.lower()
        encrypted_word = []
        
        for letter in text:
            try:
                if letter == "i":
                    letter = "j"
                for i in range(len(self.square)):
                    if letter in self.square[i]:
                        index_1 = i
                index_2 = self.square[index_1].index(letter)
            except ValueError:
                encrypted_word.append(letter)
            else:
                index_1 = index_1 + 1
                index_2 = index_2 + 1
                encrypted_word.append(str(index_1)+ str(index_2))
                encrypted_word.append(" ")
        return "".join(encrypted_word)
        
        
    def decrypt(self, text):
        """Decrpyts a given piece of text"""
        
        decrypted_word = []
        nums = text.split(" ")
        for sequence in nums:
            try:
                seq = int(sequence)
                index_2 = int(sequence[1]) - 1
                index_1 = int(sequence[0]) - 1
            except ValueError:
                decrypted_word.append(sequence)
            else:
                decrypted_word.append(self.square[index_1][index_2])
        return "".join(decrypted_word)

