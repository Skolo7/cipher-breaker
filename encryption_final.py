# PSL
from typing import Dict, NoReturn


class ROT13Encryption:

    def __init__(self):
        self.cipher_type: int = 13
        self.user_input: str = ""
        self.encrypted_text: str = ""
        self.result: Dict[int, str] = {}

    def get_text_from_user(self) -> NoReturn:
        self.user_input = input("Type a text: ").upper()

    def show_encrypted_text(self) -> str:
        return f"Encrypted text: {self.encrypted_text}"

    def encrypt_text(self) -> NoReturn:
        for num in range(len(self.user_input)):
            pos = ord(self.user_input[num]) + self.cipher_type
            if ord(self.user_input[num]) == 32:
                self.encrypted_text += " "
            elif pos > 90:
                pos -= 26
                self.encrypted_text += chr(pos)
            else:
                self.encrypted_text += chr(pos)
        print(self.show_encrypted_text())

        self.result[self.cipher_type] = self.encrypted_text
        self.save_cipher()

    def save_cipher(self) -> NoReturn:
        with open('ciphers.txt', 'a') as text_file:
            text_file.write(f'{self.result}\n')


class ROT47Encryption(ROT13Encryption):

    def __init__(self):
        super().__init__()
        self.cipher_type: int = 47

    def encrypt_text(self) -> NoReturn:
        for num in range(len(self.user_input)):
            pos = ord(self.user_input[num]) + self.cipher_type
            if ord(self.user_input[num]) == 32:
                self.encrypted_text += " "
            elif pos > 126:
                pos -= 94
                self.encrypted_text += chr(pos)
            else:
                self.encrypted_text += chr(pos)
        print(self.show_encrypted_text())



