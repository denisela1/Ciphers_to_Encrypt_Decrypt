class Cipher:

    def encrypt(self, text):
        self.text = text
        raise NotImplementedError()

    def decrypt(self, text):
        self.text = text
        raise NotImplementedError()
