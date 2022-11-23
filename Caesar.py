import string


def Encrypt(s, k):
    lower = string.ascii_lowercase  # Lowercase English letters
    upper = string.ascii_uppercase  # Uppercase English letters
    before = string.ascii_letters  # All letters of the alphabet
    after = lower[k:] + lower[:k] + upper[k:] + upper[:k]  # Create circular letters
    table = ''.maketrans(before, after)  # Create mapping table
    return s.translate(table)


def decrypt(s, k):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    before = string.ascii_letters
    after = lower[k:] + lower[:k] + upper[k:] + upper[:k]
    table = ''.maketrans(after, before)
    return s.translate(table)


def Count(CountDict, Text):
    # Get the probability of occurrence of each letter in the ciphertext
    lst = Text

    for i in lst:
        if i in CountDict:
            CountDict[i] += 1
    for i in CountDict.keys():
        CountDict[i] /= len(lst)


def Analysis(p, CountDict):
    # Decryption functions
    eps = 1  # Difference with the result
    key = 0
    q = list(CountDict.values())
    for j in range(26):
        # Traversing various secret keys
        s = 0
        for i in range(26):
            # calculate sum(pi*qi)
            t = (i + j) % 26
            s += p[i] * q[t]
        tem = abs(s - 0.065379)
        if tem < eps:
            eps = tem
            key = j
    return key


def DeDecrypt(Text):
    # Table of frequencies of known English letters in words
    p = [0.082, 0.015, 0.028, 0.042, 0.127, 0.022, 0.02, 0.061, 0.07, 0.001, 0.008, 0.04, 0.024, 0.067, 0.075, 0.019,
         0.001,
         0.06, 0.063, 0.09, 0.028, 0.01, 0.024, 0.02, 0.001, 0.001]
    # p is a table of known frequency distributions
    q = [0 for i in range(26)]
    letter = list("abcdefghijklmnopqrstuvwxyz")
    CountDict = dict(zip(letter, q))
    Count(CountDict, Text)
    key = Analysis(p, CountDict)
    return decrypt(Text, key)

