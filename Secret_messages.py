import os
from affine import Affine
from atbash import Atbash
from polybius import Polybius

"""The first screen shows all avalaible options to encrypt and decrypt text."""
def cipher_selection():
    selection = input("Encrypt or decrypt via cipher?\n"
                               "Via Affine: To encrypt, enter AFE. To decrypt, enter AFD.\n"
                               "Via Atbash: To encrypt, enter ABE. To decrypt, enter ABD.\n"
                               "Via Polybius: To encrypt, enter POE. To decrypt, enter POD.\n")
    """Based on the selection and user input(text), associated cipher script will run."""
    if selection == "AFE":
        a = int(input('Enter an alpha. Available values: 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25'))
        b = int(input('Enter a beta value.'))
        text = input('What is your message?\n')
        x = Affine(a,b)
        x.encrypt(text)
    if selection == "AFD":
        alpha = input('Enter an alpha. Available values: 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25\n')
        beta = input('Enter a beta value.')
        x = Affine(alpha, beta)
        text = upper(input('What is your message?\n'))
        x.encrypt(text)
    if selection == 'ABE':
        self.text = input('What is your message?\n')
        x = Atbash()
        text = input('What is your message?\n')
        return x.encrypt(text)
    if selection == 'ABD':
        x = Atbash()
        text = input('What is your message?\n')
        return x.decrypt(text)
    if selection == ' POE':
        x = Polybius()
        text = input('What is your message?\n')
        return x.encrypt(text)
    if selection == 'POD':
        x = Polybius()
        text = input('What is your message?\n')
        return x.decrypt(text)
    else:
        return "Your selection is not valid. Please try again."

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    cipher_selection()
    clear_screen()
