from inspect import cleandoc


def menu():
    while True:
        print(cleandoc(
            """
            1. Zakoduj podany wyraz przy użyciu rot-13!
            2. Zakoduj podany wyraz przy użyciu rot-47!
            3. Odkoduj wyraz!
            4. Wyjdź z programu!
            """
        ))
        choice: int = int(input("> "))


def say_goodbey():
    print("Bay")
    exit(0)


if __name__ == '__main__':
    menu()
