from inspect import cleandoc
from typing import Callable, Dict, NoReturn


class ROTBase:
    ROT_KEY: str = ""
    ROT_MODULES: Dict[str, Callable] = {}

    def __init__(self) -> NoReturn:
        self.cipher_type: int = 0
        self.user_input: str = ""
        self.encrypted_text: str = ""

    def __init_subclass__(cls, **kwargs) -> NoReturn:
        cls.ROT_MODULES[cls.ROT_KEY] = cls

    @classmethod
    def show_menu(cls) -> NoReturn:
        print(cleandoc(
            """
            1. Zakoduj podany wyraz przy użyciu ROT13
            2. Zakoduj podany wyraz przy użyciu ROT47
            """
        ))
        rot_choice = input("> ")
        if rot_choice in cls.ROT_MODULES:
            ROTBase().get_text_from_user()
            cls.ROT_MODULES[rot_choice]().encrypt_text()

    def get_text_from_user(self) -> NoReturn:
        self.user_input = input("Type a text: ").upper()

    def show_encrypted_text(self) -> str:
        return self.encrypted_text


class ROT13(ROTBase):
    ROT_KEY: str = "1"

    def __init__(self):
        super().__init__()

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


class ROT47(ROTBase):
    ROT_KEY: str = "2"

    def encrypt_text(self) -> NoReturn:
        pass
