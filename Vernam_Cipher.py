# Character to binary conversion
def CtoB(ch):
    OrdCh = ord(ch)
    BinarySequence = ''
    while True:
        if OrdCh % 2 == 0:
            BinarySequence += '0'
        else:
            BinarySequence += '1'
        OrdCh = OrdCh // 2
        if OrdCh == 1:
            break
        # print(OrdCh,BinarySequence)
    BinarySequence += '1'
    # Make up 8 places
    length = 8 - len(BinarySequence)
    while length:
        BinarySequence += '0'
        length -= 1
    # print('BinarySequence:{}'.format(BinarySequence))
    return BinarySequence[::-1]


# Binary to Character
def BtoC(Bin):
    St = ''
    OrdCh = 0
    length = 8
    for i in Bin:
        length -= 1
        OrdCh += (ord(i) - ord('0')) * (2 ** length)
        # print(length,i,OrdCh)
        if length == 0:
            St += chr(OrdCh)
            length = 8
            OrdCh = 0
    return St


# Core algorithm: binary iso-or operation (common for encryption and decryption)
def Execute_Unit(m_c, k):
    result_unit = ''
    for i, j in zip(m_c, k):
        if i == j:
            result_unit += '0'
        else:
            result_unit += '1'
    return result_unit


# Calling the Vernam algorithm for encryption
def Encrypt(Message, K):
    result = ''
    for m, k in zip(Message, K):
        result += Execute_Unit(CtoB(m), CtoB(k))
    return result


# Call Vernam algorithm for decryption
def Decrypt(Ciphertext, K):
    # Bk holds a sequence of binary K values
    BK = ''
    for k in K:
        BK += CtoB(k)
    # BM stores binary plaintext sequences
    BM = Execute_Unit(Ciphertext, BK[:len(Ciphertext)])
    return BtoC(BM)

