print("-------------------------------------")
print('\n"File Encryption and Decryption"' '\n"Geovani"''\n"5/04/2020"')
print('\n'"-------------------------------------")


def Encryption():

    codes_encrypt = {'A': '!', 'B': '@', 'C': '#', 'D': '$', 'E': '%', 'F': '^', 'G': '&', 'H': '*', 'I': '(',
                     'J': ')', 'K': '-', 'L': '_', 'M': '+', 'N': '=', 'O': '`', 'P': '~', 'Q': '{', 'R': '[',
                     'S': '}', 'T': ']', 'U': ':', 'V': ';', 'W': '"', 'X': '<', 'Y': '>', 'Z': '0', 'a': '1',
                     'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': 'a',
                     'k': 'b', 'l': 'c', 'm': 'd', 'n': 'e', 'o': 'f', 'p': 'g', 'q': 'h', 'r': 'i', 's': 'j',
                     't': 'k', 'u': 'l', 'v': 'm', 'w': 'n', 'x': 'o', 'y': 'p', 'z': 'q', '0': '/', '1': 'v',
                     '2': 'z', '3': 'N', '4': 's', '5': 'G', '6': 'Q', '7': 'P', '8': '|', '9': 'Y'}

    origin_file = open('Text_File.txt', 'r')
    file_read = origin_file.read()
    origin_file.close()
    encrypt_file = open('ENCRYPTED_File.txt', 'w')

    for ch in file_read:
        if ch in codes_encrypt:
            encrypt_file.write(codes_encrypt[ch])
        else:
            encrypt_file.write(ch)

    encrypt_file.close()
    encrypt_file = open('Text_File.txt', 'r')
    file_read = encrypt_file.read()
    encrypt_file.close()
    codes_items = codes_encrypt.items()

    for ch in file_read:
        if not ch in codes_encrypt.values() or ch == '.' or ch == ',' or ch == '!':
            print(ch)
        else:
            for k, v in codes_items:
                if ch == v and ch != '.':
                    print(k, end='')


Encryption()
