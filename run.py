# PSL
from typing import NoReturn
# Own
from decryption import ROTDecryption
from encryption import ROT13Encryption, ROT47Encryption
from main import show_menu

print("Cipher Breaker")


def main_menu() -> NoReturn:
    while True:
        show_menu()
        choose_num = int(input("Choose number:\n>")) - 1
        available_choices = [
            ROT13Encryption().get_text_from_user,
            ROT47Encryption().get_text_from_user,
            ROTDecryption().get_saved_ciphers,
            say_bye
        ]
        if choose_num in available_choices:
            available_choices[choose_num]()
        else:
            print("Wrong number!")


def say_bye():
    print("Goodbye!")
    exit(0)


if __name__ == '__main__':
    main_menu()
