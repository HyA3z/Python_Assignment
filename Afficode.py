# Determining Mutual Elements
import tkinter
import tkinter.messagebox


def gcd(k1, m):
    t = 0
    while m != 0:
        t = m
        m = k1 % m
        k1 = t
    return k1


# Seeking inverse elements
def cal_e(k1):
    n = 1
    while (k1 * n) % 26 != 1:
        n += 1
    return n


# Encryption algorithms
def encrypt(Text, k1, k2):
    while gcd(k1, 26) != 1:
        tkinter.messagebox.showerror('error', 'k1 and k2 are not mutually exclusive')
    plain = Text
    # print(plain)
    c = []
    for i in range(len(plain)):
        # Lowercase letters
        if plain[i].islower():
            c.append(chr(((ord(plain[i]) - 97) * k1 + k2) % 26 + 97))
        # Capital letters
        elif plain[i].isupper():
            c.append(chr(((ord(plain[i]) - 65) * k1 + k2) % 26 + 65))
        # Other
        else:
            c.append(plain[i])

    cipher = ''.join(c)
    return cipher


# Decryption algorithm
def decrypt(Text, k1, k2):
    # inverse element
    ny = cal_e(k1)

    cipher = Text
    p = []
    for i in range(len(cipher)):
        # Lowercase letters
        if cipher[i].islower():
            t1 = ord(cipher[i]) - 97 - k2
            if t1 < 0:
                t1 += 26
            p.append(chr((ny * t1) % 26 + 97))
        # Capital letters
        elif cipher[i].isupper():
            t2 = ord(cipher[i]) - 65 - k2
            if t2 < 0:
                t2 += 26
            p.append(chr((ny * t2) % 26 + 65))
        # Other
        else:
            p.append(cipher[i])

    plain = ''.join(p)
    return plain
