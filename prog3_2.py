print("-------------------------------------")
print('\n"File Encryption and Decryption"' '\n"Geovani"''\n"5/04/2020"')
print('\n'"-------------------------------------")


def Decryption():
    # Assign "codes" to each letter of the alpabet and numbers for decryption
    codes_decrypt = {'!': 'A', '@': 'B', '#': 'C', '$': 'D', '%': 'E', '^': 'F', '&': 'G', '*': 'H', '(': 'I',
                     ')': 'J', '-': 'K', '_': 'L', '+': 'M', '=': 'N', '`': 'O', '~': 'P', '{': 'Q', '[': 'R',
                     '}': 'S', ']': 'T', ':': 'U', ';': 'V', '"': 'W', '<': 'X', '>': 'Y', '0': 'Z', '1': 'a',
                     '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i', 'a': 'j',
                     'b': 'k', 'c': 'l', 'd': 'm', 'e': 'n', 'f': 'o', 'g': 'p', 'h': 'q', 'i': 'r', 'j': 's',
                     'k': 't', 'l': 'u', 'm': 'v', 'n': 'w', 'o': 'x', 'p': 'y', 'q': 'z', '/': '0', 'v': '1',
                     'z': '2', 'N': '3', 's': '4', 'G': '5', 'Q': '6', 'P': '7', '|': '8', 'Y': '9'}

# opens the encrypted file and read mode
    orig_file = open('ENCRYPTED_File.txt', 'r')
    file_read = orig_file.read()  # reads the encrypted file
    orig_file.close()  # closes the encrypted file
# creates the decrypted file in write mode
    encrypt_file = open('DECRYPTED_File.txt', 'w')

    for ch in file_read:  # characters in encrypted file
        if ch in codes_decrypt:
            encrypt_file.write(codes_decrypt[ch])
        else:
            encrypt_file.write(ch)

    encrypt_file.close()
    encrypt_file = open('ENCRYPTED_File.txt', 'r')
    file_read = encrypt_file.read()
    encrypt_file.close()
    codes_items = codes_decrypt.items()

    for ch in file_read:
        if not ch in codes_decrypt.values() or ch == '.' or ch == ',' or ch == '!':
            print(ch)
        else:
            for k, v in codes_items:
                if ch == v and ch != '.':
                    print(k, end='')


Decryption()
