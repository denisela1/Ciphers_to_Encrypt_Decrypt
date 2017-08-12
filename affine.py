import string
from ciphers import Cipher

class Affine(Cipher):
    """Encrypts or decrypts text using the Affine cipher method. __init__ method takes two arguments: alpha and beta."""
    alpha_values = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]

    def __init__(self, alpha, beta):
        """Creates an instance of the class using alpha and beta values. Each letter is ciphered with the formula
        below. Cipher list is created to map the letters. Therefore, for any given index, we can map the
        alphabet to Affine cipher letters."""
        self.a = alpha
        self.b = beta
        self.alphabet = string.ascii_uppercase
        self.cipher_list = []
        for i in range(26):
            self.cipher_list.append((self.a * i + self.b) % 26)

    def encrypt(self,text):
        """Encrypts text entered by a user."""
        output = []
        text = text.upper
        for char in text:
            try:
                text_index = self.alphabet.index(char)
                output.append(self.cipher_list[text_index])
            except ValueError:
                output.append(char)
        return ''.join(output)

    def decrypt(self,text):
        """Decrypts text entered by a user"""
        output = []
        text = text.upper
        for char in text:
            try:
                text_index = self.cipher_list.index(char)
                output.append(self.alphabet[text_index])
            except ValueError:
                output.append(char)
        return ''.join(output)


