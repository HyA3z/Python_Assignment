letter_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # Alphabet


# Generate a key list based on the input key
def Get_KeyList(key):
    key_list = []
    for ch in key:
        key_list.append(ord(ch.upper()) - 65)
    return key_list


# Encryption functions
def Encrypt(plaintext, key):
    key_list = Get_KeyList(key)
    ciphertext = ""

    i = 0
    for ch in plaintext:  # Traversing the plaintext
        if 0 == i % len(key_list):
            i = 0
        if ch.isalpha():  # If the plaintext is alphabetic, if so, the case is determined and encryption is performed separately.
            if ch.isupper():
                ciphertext += letter_list[(ord(ch) - 65 + key_list[i]) % 26]
                i += 1
            else:
                ciphertext += letter_list[(ord(ch) - 97 + key_list[i]) % 26].lower()
                i += 1
        else:  # If the ciphertext is not alphabetic, add it directly to the ciphertext string
            ciphertext += ch
    return ciphertext


# Decryption functions
def Decrypt(ciphertext, key):
    key_list = Get_KeyList(key)
    plaintext = ""

    i = 0
    for ch in ciphertext:  # Iterate through the ciphertext
        if 0 == i % len(key_list):
            i = 0
        if ch.isalpha():
            # If the ciphertext is alphabetic or not, if it is, the ciphertext will be decrypted
            # and the case will be determined.
            if ch.isupper():
                plaintext += letter_list[(ord(ch) - 65 - key_list[i]) % 26]
                i += 1
            else:
                plaintext += letter_list[(ord(ch) - 97 - key_list[i]) % 26].lower()
                i += 1
        else:  # If the ciphertext is not alphabetic, add it directly to the plaintext string
            plaintext += ch
    return plaintext
