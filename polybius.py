from ciphers import Cipher

class Polybius(Cipher):
    """Polybius cipher method: Each letter is represented by 5x5 square's coordinates in the grid. A 5x5 array will be
    created and letters in the text entered by a user will be mapped to x,y values."""
    def __init__(self):
        """Creates an instance of the class by creating a 5x5 array. I and J are given the same coordinates as
        suggested. No additional argument other than self."""
        self.alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                         'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.coordinates = []
        for y in range(6):
            for x in range(6):
                self.coordinates.append(str(y)+str(x))
        self.coordinates.insert(9,'12')

    def encrypt(self,text):
        """Encrypts the text entered by a user."""
        output = []
        for char in text:
            try:
                text_index = self.alphabet.index(char)
                output.append(self.coordinates[text_index])
            except ValueError:
                output.append(char)
        print(''.join(output))

    def decrypt(self,text):
        """Decrypts text entered by a user"""
        output = []
        text = (str(text)).replace(" ", "  ")
        for i in range(0, len(text), 2):
            try:
                combined_numbers = text[i] + text[i + 1]
                text_index = self.coordinates.index(combined_numbers)
                output.append(self.alphabet[text_index])
            except ValueError:
                output.append(text[i])
        print(''.join(output))
