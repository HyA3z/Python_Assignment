from PIL import Image


def gen_Data(data):
    text = []

    for i in data:
        text.append(format(ord(i), '08b'))
    return text


def Pixel(pix, data):
    data_list = gen_Data(data)
    len_data = len(data_list)
    imdata = iter(pix)

    for i in range(len_data):

        pix = [value for value in imdata.__next__()[:3] +
               imdata.__next__()[:3] +
               imdata.__next__()[:3]]

        for j in range(0, 8):
            if data_list[i][j] == '0' and pix[j] % 2 != 0:
                pix[j] -= 1

            elif data_list[i][j] == '1' and pix[j] % 2 == 0:
                if pix[j] != 0:
                    pix[j] -= 1
                else:
                    pix[j] += 1
        if i == len_data - 1:
            if pix[-1] % 2 == 0:
                if pix[-1] != 0:
                    pix[-1] -= 1
                else:
                    pix[-1] += 1

        else:
            if pix[-1] % 2 != 0:
                pix[-1] -= 1

        pix = tuple(pix)
        yield pix[0:3]
        yield pix[3:6]
        yield pix[6:9]


def encode_enc(new_img, data):
    w = new_img.size[0]
    (x, y) = (0, 0)

    for pixel in Pixel(new_img.getdata(), data):
        new_img.putpixel((x, y), pixel)
        if x == w - 1:
            x = 0
            y += 1
        else:
            x += 1


# Encode data into image
def encode():
    img = input("Enter image name : ")
    image = Image.open(img, 'r')

    data = input("Enter data : ")
    if len(data) == 0:
        raise ValueError('data is empty')

    newimg = image.copy()
    encode_enc(newimg, data)

    new_img_name = input("Enter the name of new image(with extension) : ")
    newimg.save(new_img_name, str(new_img_name.split(".")[1].upper()))


# Decode the data in the image
def decode():
    img = input("Enter image name(with extension) : ")
    image = Image.open(img, 'r')

    data = ''
    imgdata = iter(image.getdata())

    while True:
        pixels = [value for value in imgdata.__next__()[:3] +
                  imgdata.__next__()[:3] +
                  imgdata.__next__()[:3]]

        binstr = ''

        for i in pixels[:8]:
            if i % 2 == 0:
                binstr += '0'
            else:
                binstr += '1'

        data += chr(int(binstr, 2))
        if pixels[-1] % 2 != 0:
            return data


# Main Function
def main():
    a = int(input("1. Encode\n2. Decode\n"))
    if a == 1:
        encode()

    elif a == 2:
        print("Decoded Word : " + decode())
    else:
        raise Exception("Enter correct input")


if __name__ == '__main__':
    main()
