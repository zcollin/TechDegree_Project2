"""
Runs a program that prompts the user to choose a cipher.
Providing the ability for the user to encrypt or decrypt a word/phrase.
Author: Zachary Collins
Date: July, 2018
"""

import os

from affine import Affine

from caesar import Caesar

from key import Keyword

from polybius_square import Polybius


def clear_screen():
    """Clears the contents of the console"""

    os.system('cls' if os.name == 'nt' else 'clear')


def help():
    """Provides instructions/menu on how to operate the program"""

    clear_screen()
    print("*"*10)
    print("Affine: 'A' ")
    print("Caesar: 'C' ")
    print("Keyword: 'K' ")
    print("Polybius Square: 'P' ")
    print("Hit 'Q' to quit")
    print("Type 'HELP' for instructions")
    print("*"*10)
    print("Choose from one of the Ciphers above!")


def start():
    """Controls the function of choosing a cipher. Encryption/Decryption"""

    help()
    answer = input().upper()

    # Controls the logic of answer to Cipher choice
    if answer == 'A':
        affine()
    elif answer == 'C':
        caesar()
    elif answer == 'K':
        keyword()
    elif answer == 'P':
        polybius()
    elif answer == 'Q':
        pass
    elif answer == 'HELP':
        start()
    else:
        print("That was not a valid option. Please try again")
        start()


def prompt():
    """Controls the prompt when a cipher is chosen. Encryption or Decryption"""

    clear_screen()
    print("*"*10)
    answer = input("Do you want to encrypt:'E' or decrpyt 'D' ").upper()
    if answer == 'E' or 'D':
        return answer
    else:
        print("not a valid response")
        prompt()


def caesar():
    """Prompts the user on operating a Caesar Cipher"""

    answer = prompt()

    # Controls the choice of encrpytion or decryption
    if answer == 'E':
        word = input("Enter the word you want to encrpyt: ")
        test = Caesar()
        output = test.encrypt(word)
        print("The encrpyted word is:  {} ".format(output))

        # Prompts the user on if they wish to decrpyt the word
        yes_no = input("Do you want to decrypt this word? [Y/N]: ").upper()
        if yes_no == 'Y':
            print("The decrypted word is: {} ".format(test.decrypt(output)))
    elif answer == 'D':
        word = input("Enter the word you want to decrpyt: ")
        test = Caesar()
        output = test.decrypt(word)
        print("The decrpyted word is:  {} ".format(output))
    else:
        caesar()

    # Asks if the user would like to use another cipher
    restart = input("Hit 'R' to restart program. Hit enter to quit").upper()
    if restart == 'R':
        start()


def affine():
    """Prompts the user on operating a Affine Cipher."""

    answer = prompt()

    # Controls the choice of encrpytion or decryption
    if answer == 'E':
        word = input("Enter the word you want to encrpyt: ")
        test = Affine()
        output = test.encrypt(word)
        print("The encrpyted word is:  {} ".format(output))

        # Prompts the user on if they wish to decrpyt the word
        yes_no = input("Do you want to decrypt this word? [Y/N]: ").upper()
        if yes_no == 'Y':
            print("The decrypted word is: {} ".format(test.decrypt(output)))
    elif answer == 'D':
        word = input("Enter the word you want to decrpyt: ")
        test = Affine()
        output = test.decrypt(word)
        print("The decrpyted word is:  {} ".format(output))
    else:
        affine()

    # Asks if the user would like to use another cipher
    restart = input("Hit 'R' to restart program. Hit enter to quit").upper()
    if restart == 'R':
        start()


def polybius():
    """Prompts the user on using a Polybius Square Cipher."""

    answer = prompt()

    # Controls the choice of encrpytion or decryption
    if answer == 'E':
        word = input("Enter the word you want to encrpyt: ")
        test = Polybius()
        output = test.encrypt(word)
        print("In this cipher I and J are interchangeable. Read Careful.")
        print("The encrpyted word is:  {} ".format(output))

        # Prompts the user on if they wish to decrpyt the word
        yes_no = input("Do you want to decrypt this word? [Y/N]: ").upper()
        if yes_no == 'Y':
            print("*Warning: The output doesn't include spaces between words*")
            print("The decrypted word is: {} ".format(test.decrypt(output)))
    elif answer == 'D':
        print("Uses a sequence of numbers: '12 34 45'. No numbers < 5.")
        word = input("Enter the sequence you want to decrpyt: ")
        test = Polybius()
        output = test.decrypt(word)
        print("In this cipher I and J are interchangeable. Read Careful.")
        print("The decrpyted word is:  {} ".format(output))
    else:
        polybius()

    # Asks if the user would like to use another cipher
    restart = input("Hit 'R' to restart program. Hit enter to quit").upper()
    if restart == 'R':
        start()


def keyword():
    """Prompts the user on operating a Keyword Cipher."""

    answer = prompt()

    # Controls the choice of encrpytion or decryption
    if answer == 'E':
        key = input("what is the key for your Cipher? ").lower()
        test = Keyword(key)
        word = input("Enter the word you want to encrpyt: ")
        output = test.encrypt(word)
        print("The encrpyted word is:  {} ".format(output))

        # Prompts the user on if they wish to decrpyt the word
        yes_no = input("Do you want to decrypt this word? [Y/N]: ").upper()
        if yes_no == 'Y':
            print("The decrypted word is: {} ".format(test.decrypt(output)))
    elif answer == 'D':
        key = input("what is the key for your Cipher? ").lower()
        test = Keyword(key)
        word = input("Enter the word you want to decrpyt: ")
        output = test.decrypt(word)
        print("The decrpyted word is:  {} ".format(output))
    else:
        affine()

    # Asks if the user would like to use another cipher
    restart = input("Hit 'R' to restart program. Hit enter to quit").upper()
    if restart == 'R':
        start()


# Ensures this only runs upon the main method being called.
if __name__ == "__main__":
    start()

