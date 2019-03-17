# coding=utf-8
from PIL import Image, ImageDraw, ImageFont
import numpy as np
# 用这个来生成随机数
# im = Image.open("path", "r")
# im.show()
# # 这样子来读图片显示出来
# 各种属性自己百度如何显示出来


# 生成随机的背景色
def bgcolor():
    # 用RGB形式画填充背景色RGB红绿蓝三色0到255
    return np.random.randint(64, 255, size=1), np.random.randint(64, 255, size=1), np.random.randint(64, 255, size=1)
#  这三个一个起始点，一个结束点，最后是个数，只取一个，也可以是0到255


# 用ASCII生成随机字符，具体多少自己百度去
def randomtxt():
    txt_list = []
    txt_list.extend([i for i in range(65, 91)])
#     列表推导式，把一个列表接另外一个后面,这个就是ASCII65到90组成的列表,就不用for然后一个个append进去了
    txt_list.extend([i for i in range(97, 123)])
    txt_list.extend([i for i in range(48, 57)])
#     这样就把所有字母和数字全部加进去了
    return chr(txt_list[np.random.randint(0, len(txt_list) - 1)])
#     chr就是给一个整数返回一个对应的字符,这样子返回随机的字符


# 给字符生成颜色,注意字符生成的颜色不能和背景色相同，尽量区分的明显一些,所以色域选择是到127
def txtcolor():
    return np.random.randint(32, 127, size=1), np.random.randint(32, 127, size=1), np.random.randint(32, 127, size=1)


# 画图
def generatecode():
    width = 200
    height = 50
    image = Image.new('RGB', (width, height), (255, 255, 255))
#     画了个白色的
    draw = ImageDraw.ImageDraw(image)
#     这个是生成可以画的对象
    for w in range(width):
        # 这个是横的像素点的循环
        for h in range(height):
            draw.point((w, h), fill=bgcolor())

    myfont = ImageFont.truetype('arial.ttf', 36)
    for i in range(4):
        # 坐标是估算的
        draw.text((50 * i + 10, 10), randomtxt(), font=myfont, fill=txtcolor())

    image.show()


generatecode()


