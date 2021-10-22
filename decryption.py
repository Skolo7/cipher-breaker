from typing import Dict, NoReturn


class ROTDecryption:
    def __init__(self):
        self.picked_cipher: str = ""
        self.rot_key: int = 0
        self.decrypted_text = ""
        self.saved_ciphers: Dict[str, int] = {}

    def show_decrypted_cipher(self) -> str:
        return f"Decrypted text: {self.decrypted_text}"

    def decrypt_rot13cipher(self) -> NoReturn:
        for num in range(len(self.picked_cipher)):
            pos = ord(self.picked_cipher[num]) - self.rot_key
            if ord(self.picked_cipher[num]) == 32:
                self.decrypted_text += " "
            elif pos < 65:
                pos += 26
                self.decrypted_text += chr(pos)
            else:
                self.decrypted_text += chr(pos)
        print(self.show_decrypted_cipher())

    def get_saved_ciphers(self) -> NoReturn:
        with open('ciphers.txt', 'r') as ciphers_file:
            self.saved_ciphers = {line[6:-3]: line[1:3] for line in ciphers_file}

    def show_saved_ciphers(self) -> NoReturn:
        for count, key in enumerate(self.saved_ciphers, 1):
            print(f"{count}.{key}")

    def choose_cipher(self) -> NoReturn:
        chosen_num = int(input("Pick number of chosen cipher:\n>"))
        self.picked_cipher = list(self.saved_ciphers)[chosen_num-1]
        self.rot_key = self.saved_ciphers[self.picked_cipher]

    def decrypt_rot47cipher(self) -> NoReturn:
        for num in range(len(self.picked_cipher)):
            pos = ord(self.picked_cipher[num]) - self.rot_key
            if ord(self.picked_cipher[num]) == 32:
                self.decrypted_text += " "
            elif pos < 32:
                pos += 94
                self.decrypted_text += chr(pos)
            else:
                self.decrypted_text += chr(pos)
        print(self.show_decrypted_cipher())
