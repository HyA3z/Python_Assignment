# Implementing Base64 encoding
# A - Z: 65 - 90  a - z: 97 - 122

# Base64 index table + '='
Base64 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
          'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
          'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
          '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/', '=']


def Base(choose, text):
    if choose == 1:
        tru = ''
        # Binary form
        binary = []

        # Convert text to the corresponding ASCII code, then to binary bits
        for i in text:
            num = ord(i)
            # div: Divisor  re: Remainder  ele: Single-letter binary elements
            div = 1
            ele = []

            while div != 0:
                div = num // 2
                re = num % 2
                num = div
                ele.append(re)

            # Single byte complementary 8 bits
            while len(ele) < 8:
                ele.append(0)
            ele.reverse()
            binary += ele

        # Completes 24 bits every 3 bytes
        while len(binary) % 24 != 0:
            binary.append(0)

        # Every 6 binary digits is a Base64 encoded index
        while binary:
            flag = 0
            num = ''
            while flag < 6:
                num += str(binary.pop(0))
                flag += 1
            index = int(num, 2)

            # Determine whether the all-0 index is 'A' or '='
            if index == 0 and 1 not in binary:
                index = 64
            tru += Base64[index]
            tru += ''

        return tru

    # Decoding
    elif choose == 2:
        tru = ''
        coding = text
        binary = []

        for i in coding:
            index = Base64.index(i)
            if index != 64:
                div = 1
                ele = []

                while div != 0:
                    div = index // 2
                    re = index % 2
                    index = div
                    ele.append(re)

                # Single byte complement of 6 bits
                while len(ele) < 6:
                    ele.append(0)
                ele.reverse()

            else:
                ele = [0, 0, 0, 0, 0, 0]
            binary += ele

        while binary:
            flag = 0
            num = ''
            while flag < 8:
                num += str(binary.pop(0))
                flag += 1
            index = int(num, 2)

            # Determine whether the all-0 index is 'A' or '='
            if index == 0 and 1 not in binary:
                break
            tru += chr(index)
            tru += ''

        return tru
