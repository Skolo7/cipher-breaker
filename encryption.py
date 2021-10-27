# PSL
from typing import Dict, NoReturn, Union


class ROT13Encryption:
    def __init__(self) -> NoReturn:
        self.cipher_type: int = 13
        self.encrypted_text: str = ""
        self.result: Dict[int, str] = {}

    def get_text_from_user(self) -> NoReturn:
        word_to_encrypt: str = input("Type a text: ").upper()
        self.rot_13_encryption_mech(word_to_encrypt)

    def rot_13_encryption_mech(self, word_to_encrypt: str, tests=False) -> Union[NoReturn, str]:
        for num in range(len(word_to_encrypt)):
            pos = ord(word_to_encrypt[num]) + self.cipher_type
            if ord(word_to_encrypt[num]) == 32:
                self.encrypted_text += " "
            elif pos > 90:
                pos -= 26
                self.encrypted_text += chr(pos)
            else:
                self.encrypted_text += chr(pos)

        if tests:
            return self.encrypted_text

        print(self.show_encrypted_text())
        self.save_cipher()

    def show_encrypted_text(self) -> str:
        return f"Encrypted text: {self.encrypted_text}"

    def save_cipher(self) -> NoReturn:
        self.result[self.cipher_type] = self.encrypted_text
        with open("ciphers.txt", "a") as text_file:
            text_file.write(f"{self.result}\n")


class ROT47Encryption(ROT13Encryption):
    def __init__(self) -> NoReturn:
        super().__init__()
        self.cipher_type: int = 47

    def get_text_from_user(self) -> NoReturn:
        word_to_encrypt: str = input("Type a text: ").upper()
        self.encrypt_text(word_to_encrypt)

    def encrypt_text(self, word_to_encrypt: str, tests=False) -> Union[NoReturn, str]:
        for num in range(len(word_to_encrypt)):
            pos = ord(word_to_encrypt[num]) + self.cipher_type
            if ord(word_to_encrypt[num]) == 32:
                self.encrypted_text += " "
            elif pos > 126:
                pos -= 94
                self.encrypted_text += chr(pos)
            else:
                self.encrypted_text += chr(pos)

        if tests:
            return self.encrypted_text

        print(self.show_encrypted_text())
        self.save_cipher()
