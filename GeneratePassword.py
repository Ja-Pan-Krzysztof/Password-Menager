from random import sample


class GeneratePassword:
    def __init__(self, lenght):
        self.lenght = lenght
        self.all = ''
        self.up_l = 'QWERTYUIOPASDFGHJKLZXCVBNM'
        self.low_l = self.up_l.lower()
        self.number = '1234567890'
        self.symbols = '!@#$%&*'
        self.symbols_other = '^;:'"<>,./?~\\|()-_=+[{]}"

    def generate_pass(self, up=True, low=True, num=True, sym=True, sym_other=True):

        if up:
            self.all += self.up_l

        if low:
            self.all += self.low_l

        if num:
            self.all += self.number

        if sym:
            self.all += self.symbols

        if sym_other:
            self.all += self.symbols_other

        password = ''.join(sample(self.all, self.lenght))
        return password

