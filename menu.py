import os
from affine import Affine
from atbash import Atbash
from polybius import Polybius

class Menu():
    """The first screen shows all avalaible options to encrypt and decrypt text."""
    def __init__(self):
        self.selection = input("Encrypt or decrypt via cipher?\n"
                              "Via Affine: To encrypt, enter AFE. To decrypt, enter AFD.\n"
                              "Via Atbash: To encrypt, enter ABE. To decrypt, enter ABD.\n"
                              "Via Polybius: To encrypt, enter POE. To decrypt, enter POD.\n")
    def select_cipher(self):
        """Based on the selection and user input(text), associated cipher script will run."""
        if self.selection == "AFE":
            alpha = input('Enter an alpha. Available values: 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25')
            beta = input('Enter a beta value.')
            x = Affine(alpha,beta)
            text = input('What is your message?')
            return x.encrypt(text)
        if self.selection == "AFD":
            alpha = input('Enter an alpha. Available values: 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25')
            beta = input('Enter a beta value.')
            x = Affine(alpha, beta)
            text = input('What is your message?')
            return x.decrypt(text)
        if self.selection == 'ABE':
            self.text = input('What is your message?')
            x = Atbash()
            text = input('What is your message?')
            return x.encrypt(text)
        if self.selection == 'ABD':
            x = Atbash()
            text = input('What is your message?')
            return x.decrypt(text)
        if self.selection == ' POE':
            x = Polybius()
            text = input('What is your message?')
            return x.encrypt(text)
        if self.selection == 'POD':
            x = Polybius()
            text = input('What is your message?')
            return x.decrypt(text)
        else:
            return "Your selection is not valid. Please try again."

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
