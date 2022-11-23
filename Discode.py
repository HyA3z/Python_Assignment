# Implement column shift password
# Lowercase dictionary
lowDict = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# Capitalization Dictionary
capDict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


# Convert letters to numbers
def switch(ele):
    flag = 0
    if ele in lowDict:
        ele = lowDict.index(ele)
    elif ele in capDict:
        ele = capDict.index(ele)
        flag = 1
    return [int(ele), flag]


def Dis(choose, text, key):
    dict = {}
    lis = ''
    text = list(text)

    # Encryption
    if choose == 1:
        while text:
            for i in key:
                [ele, flag] = switch(i)

                # Add dictionary
                dict.setdefault(ele, '')
                if not text:
                    break

                # Replacement
                else:
                    temp = dict[ele] + text.pop(0)
                    dict[ele] = temp

        # Sort
        while dict != {}:
            minindex = min(dict.keys())
            lis += dict[minindex]
            dict.pop(minindex)

        return lis

    # Decryption
    elif choose == 2:
        textNum = len(text)
        keyNum = len(key)

        # num used to calculate the number of each array
        num = textNum // keyNum

        # re for counting redundant characters
        re = textNum % keyNum

        while text:
            for i in key:
                [ele, flag] = switch(i)
                dict.setdefault(ele, '')

                # Replacement
                if re != 0:
                    dict[ele] = text[0:num + 1]
                    re -= 1
                    for j in range(0, num + 1):
                        text.pop(0)
                else:
                    dict[ele] = text[0:num]
                    for j in range(0, num):
                        text.pop(0)

        # Sort
        tempList = sorted(dict.keys())
        tempLen = len(tempList)

        while tempLen > 0:
            for i in tempList:
                if not dict[i]:
                    tempLen -= 1
                elif dict[i]:
                    lis += dict[i][0]
                    dict[i] = dict[i][1:]

        return lis


