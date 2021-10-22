from inspect import cleandoc


def show_menu():
    print(cleandoc("""
    1. Encrypt text in ROT13
    2. Encrypt text in ROT47
    3. Decrypt ciphers
    4. Exit
    """))


if __name__ == '__main__':
    show_menu()
