def rot13_decryption():
    text = input("Type en encrypted text: ").upper()
    cipher_type = 13
    decrypted_text = ""

    for num in range(len(text)):
        pos = ord(text[num]) - cipher_type
        if ord(text[num]) == 32:
            decrypted_text += " "
        elif pos < 65:
            pos += 26
            decrypted_text += chr(pos)
        else:
            decrypted_text += chr(pos)

    print(f"Text after encryption: {decrypted_text}")


