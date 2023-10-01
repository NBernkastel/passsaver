import os
import json
from cryptography.fernet import Fernet


class Cryptography:
    def __init__(self, key: bytes):
        self.__key = key
        self.__cipher_suite = Fernet(key)

    def encrypt(self, data: bytes, file_name: str):
        encrypted_data = self.__cipher_suite.encrypt(data)
        with open(file_name, 'wb') as file:
            file.write(encrypted_data)

    def decrypt(self, file_name: str):
        if not os.path.exists(file_name):
            raise FileExistsError('Database does not exist')
        with open(file_name, 'rb') as file:
            encrypted_data = file.read()
            decrypted_data = self.__cipher_suite.decrypt(encrypted_data).decode()
            return json.loads(decrypted_data)
