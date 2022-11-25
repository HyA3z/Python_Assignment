# Implementing RSA passwords
import math


# Determining whether a number is prime or not
def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def RSA(choose, text, p, q, e):
    text = int(text)
    p = int(p)
    q = int(q)
    e = int(e)

    # Encryption
    if choose == 1:
        if not isPrime(p):
            return 'The p you entered is not a prime number'

        if not isPrime(q):
            return 'The q you entered is not a prime number'

        n = p * q
        phiN = (p - 1) * (q - 1)

        # Determine whether e and φ(n) are mutually exclusive
        if math.gcd(e, phiN) != 1:
            falE = 'The e you entered is not commutative with φ(n)\n' \
                   + 'n = ' + str(n) + '\n' \
                   + 'φ(n) = ' + str(phiN)

            return falE

        # Compute the inverse element d of e
        k = 1
        while (k * phiN + 1) % e != 0:
            k += 1
        d = int((k * phiN + 1) / e)

        plai = text
        ciph = pow(plai, e, n)
        tru = 'n = ' + str(n) + '\n' \
              + 'φ(n) = ' + str(phiN) + '\n' \
              + 'd = ' + str(d) + '\n' \
              + 'The cipher text is' + str(ciph)

        return tru

    # Decryption
    elif choose == 2:
        if not isPrime(p):
            return 'The p you entered is not a prime number'

        if not isPrime(q):
            return 'The q you entered is not a prime number'

        n = p * q
        phiN = (p - 1) * (q - 1)

        # Determine whether e and φ(n) are mutually exclusive
        if math.gcd(e, phiN) != 1:
            falE = 'The e you entered is not commutative with φ(n)\n' \
                   + 'n = ' + str(n) + '\n' \
                   + 'φ(n) = ' + str(phiN)

            return falE

        # Compute the inverse element d of e
        k = 1
        while (k * phiN + 1) % e != 0:
            k += 1
        d = int((k * phiN + 1) / e)

        ciph = text
        plai = pow(ciph, d, n)
        tru = 'n = ' + str(n) + '\n' \
              + 'φ(n) = ' + str(phiN) + '\n' \
              + 'd = ' + str(d) + '\n' \
              + 'The plain text is' + str(plai)

        return tru