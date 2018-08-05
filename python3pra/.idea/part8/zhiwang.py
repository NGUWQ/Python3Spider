__author__ = 'WQ'
# *_*coding:utf-8 *_*
#利用tesserocr库来识别图形验证码(识别率低y)
import tesserocr
from PIL import Image


image=Image.open('Code.jpg')
image=image.convert('L')#将图片转化为灰度图像
threshold=174
table=[]
for i in range(256):
    if i<threshold:
        table.append(0)
    else:
        table.append(1)
image=image.point(table,'1')
image.show()
result=tesserocr.image_to_text(image)
print(result)
