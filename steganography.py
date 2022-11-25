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


def encode_en(new_img, data):
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
def encode(path, data, new_img_name):
    image = Image.open(path, 'r')
    new_img = image.copy()
    encode_en(new_img, data)
    # save image
    new_img.save(new_img_name, str(new_img_name.split(".")[1].upper()))


# Decode the data in the image
def decode(path):
    image = Image.open(path, 'r')

    data = ''
    imgdata = iter(image.getdata())

    while True:
        pixels = [value for value in imgdata.__next__()[:3] +
                  imgdata.__next__()[:3] +
                  imgdata.__next__()[:3]]

        bin_str = ''

        for i in pixels[:8]:
            if i % 2 == 0:
                bin_str += '0'
            else:
                bin_str += '1'

        data += chr(int(bin_str, 2))
        if pixels[-1] % 2 != 0:
            return data


