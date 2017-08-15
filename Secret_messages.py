import os
from affine import Affine
from atbash import Atbash
from polybius import Polybius

def cipher_selection():
    """The first screen shows all the cipher options to encrypt and decrypt."""
    selection_ed= input("To encrypt a message, press E.\n"
                        "To decrypt a message, press D.\n"
                        "To quit, press Q.\n")
    if selection_ed == 'E':
        cipher_option = input("Please select one of these cipher options:\n"
                                "Affine: Press AFE\n"
                                "Atbash: Press ABE\n"
                                "Polybius: Press POE\n"
                                "To quit, press Q.\n")
        if cipher_option == "AFE":
            a = int(input('Enter an alpha. Available values: 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25\n'))
            if a not in [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]:
                print('Alpha value is not accepted. Please try again.\n')
                a = int(input('Enter an alpha. Available values: 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25\n'))
            b = int(input('Enter a beta value. Integer numbers only.\n'))
            text = (input('What is your message?\n')).upper()
            x = Affine(a, b)
            x.encrypt(text)
            menu_back()
        if cipher_option == 'ABE':
            text = (input('What is your message?\n')).upper()
            x = Atbash()
            x.encrypt(text)
            menu_back()
        if cipher_option == 'POE':
            text = (input('What is your message?\n')).upper()
            x = Polybius()
            x.encrypt(text)
            menu_back()
        if cipher_option == 'Q':
            print('You quit.\n')
            os.system('clear')
        else:
            print('Not valid. Please try again.')
            menu_back()

    if selection_ed == 'D':
        cipher_option = input("Please select one of these cipher options:\n"
                              "Affine: Press AFD\n"
                              "Atbash: Press ABD\n"
                              "Polybius: Press POD\n"
                              "To quit, enter Q.\n")
        if cipher_option == "AFD":
            a = int(input('Enter an alpha. Available values: 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25\n'))
            b = int(input('Enter a beta value.\n'))
            text = (input('What is your message?\n')).upper()
            x = Affine(a, b)
            x.decrypt(text)
            menu_back()
        if cipher_option == 'ABD':
            text = (input('What is your message?\n')).upper()
            x = Atbash()
            x.decrypt(text)
            menu_back()
        if cipher_option == 'POD':
            text = (input('What is your message?\n')).upper()
            x = Polybius()
            x.decrypt(text)
            menu_back()
        else:
            print('Not valid. Please try again.\n')
            menu_back()
    if cipher_option == 'Q':
        print('You quit.\n')
        os.system('clear')
    else:
        print('Not valid.\n')
        menu_back()

def menu_back():
    y = input("To go back to the main menu, press M. To quit, press Q.\n")
    if y == 'M':
        cipher_selection()
    if y == 'Q':
        print("You quit")
        os.system('clear')


if __name__ == '__main__':
    cipher_selection()
