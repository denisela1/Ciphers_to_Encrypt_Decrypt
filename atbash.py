import string
from ciphers import Cipher

class Atbash(Cipher):

    """Cipher method is to map each letter in the alphabet to its reverse, so that the first letter
    becomes the last letter, the second letter becomes the second to last letter, and so on."""

    def __init__(self):
        """Creates an instance of the class using the Latin alphabet and reversing it for mapping."""

        self.alphabet = string.ascii_uppercase
        self.cipher_list = self.alphabet[::-1]


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


