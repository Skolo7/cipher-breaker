# PSL
from inspect import cleandoc

# Own
from decryption import ROTDecryption
from encryption import ROT13Encryption, ROT47Encryption
from main import show_menu

print("Cipher Breaker")
while True:
    show_menu()
    choose_num = int(input("Choose number:\n>"))
    if choose_num == 1:
        rot13encrypt = ROT13Encryption()
        rot13encrypt.get_text_from_user()
        rot13encrypt.encrypt_text()
    elif choose_num == 2:
        rot47encrypt = ROT47Encryption()
        rot47encrypt.get_text_from_user()
        rot47encrypt.encrypt_text()
    elif choose_num == 3:
        rot_decrypt = ROTDecryption()
        rot_decrypt.get_saved_ciphers()
        rot_decrypt.show_saved_ciphers()
        rot_decrypt.choose_cipher()
        if rot_decrypt.rot_key == 13:
            rot_decrypt.decrypt_rot13cipher()
        if rot_decrypt.rot_key == 47:
            rot_decrypt.decrypt_rot47cipher()
    elif choose_num == 4:
        print("Goodbye!")
        break
    else:
        print("Wrong number!")

