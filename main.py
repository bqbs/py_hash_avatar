# -*- coding:utf-8 -*-
import random
import string
import hashlib
from PIL import Image, ImageDraw


def gen(s, image_size):
    # some color code
    colors = ["#DDE5FF", "#597FFF"]
    # generate hash string and take the first 16 chars
    hs = md5(s)[0:16]
    # get the array of colors
    icon_color = []
    for c in hs:
        icon_color.append(colors[hex_2_dex(c) % 2])
    # define the image size
    step = image_size / 4
    img = Image.new("RGB", (image_size, image_size))
    draw = ImageDraw.Draw(img)
    for idx, color in enumerate(icon_color):
        x = idx % 4 * step
        y = idx // 4 * step
        draw.rectangle([x, y, x + step, y + step], color, color)
    # image size
    rs = image_size // 2
    img_rs = img.resize((rs, rs), Image.ANTIALIAS)
    # get mirror images and paste them to the target image
    rt = img_rs.transpose(Image.FLIP_LEFT_RIGHT)
    lb = img_rs.transpose(Image.FLIP_TOP_BOTTOM)
    rb = lb.transpose(Image.FLIP_LEFT_RIGHT)
    new_img = Image.new("RGB", (image_size, image_size))
    new_img.paste(img_rs, (0, 0))
    new_img.paste(rt, (img_rs.width, 0))
    new_img.paste(lb, (0, img_rs.height))
    new_img.paste(rb, (img_rs.width, img_rs.height))
    # save
    filename = "./avatar/icon_" + s + ".png"
    new_img.save(filename, "PNG")


def hex_2_dex(h):
    return int(h, 16)


def md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


def main():
    for i in range(15):
        # get a random string for test
        s = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        gen(s, 96)


if __name__ == '__main__':
    main()
