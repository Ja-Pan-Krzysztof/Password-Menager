from cryptography.fernet import Fernet
from os import system
from re import match


class PasswordMenager:
    def __init__(self):
        self.key = None
        self.password_file = None
        self.password_dict = {}
        self.password = ''

    @staticmethod
    def invalid_path(path, extention):
        path = path.split('.')

        try:
            if path[1] == extention:
                return True

            else:
                return False

        except:
            return False

    def create_key(self, path):
        extention = '.key'
        if self.invalid_path(path, extention):
            self.key = Fernet.generate_key()
            with open(path, 'wb') as f:
                f.write(self.key)

        else:
            print('Invalid path !')

    def load_key(self, path):
        with open(path, 'rb') as f:
            self.key = f.read()

    def create_password_file(self, path, initial_values=None):
        self.password_file = path

        if initial_values is not None:
            for key, value in initial_values.items():
                self.add_password(key, value)

        else:
            system(f'type nul > {path}')

    def load_password_file(self, path):
        with open(path, 'r') as f:
            for line in f:
                site, encrypted = line.split(':')
                self.password_dict[site] = Fernet(self.key).decrypt(encrypted.encode()).decode()

    def add_password(self, site, password: str):
        self.password_dict[site] = password

        if self.password_file is not None:
            with open(self.password_file, 'a') as f:
                encrypted = Fernet(self.key).encrypt(password.encode())
                f.write(f'{site}:{encrypted.decode()}\n')

    def open_password_file(self, path):
        try:
            self.password_file = path

        except ValueError:
            print('Invalid path !')

    def get_password(self, site):
        return self.password_dict[site]