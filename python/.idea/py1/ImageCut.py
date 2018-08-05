#压缩图片

import os
from PIL import Image

def resizeImg():
    im = Image.open('C:/Users/TTT/Desktop/杂/图片/548663.jpg')
    w, h = im.size
    ims=os.path.getsize('C:/Users/TTT/Desktop/杂/图片/548663.jpg')
    while ims>10240:
        w=w*0.9
        h=h*0.9
        im.thumbnail((w,h))
        im.save('C:/Users/TTT/Desktop/杂/图片/548663s.jpg')
        ims=os.path.getsize('C:/Users/TTT/Desktop/杂/图片/548663s.jpg')
    return ims
size=resizeImg()
print(size)

