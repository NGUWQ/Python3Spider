from selenium import webdriver
from lxml import etree
import time
import os
import photomosaic as pm
import cv2
import requests


Image_Path='王者荣耀'

def Crawl_image():
    """
    抓取王者荣耀皮肤
    :return:
    """
    browser=webdriver.PhantomJS
    url='http://news.4399.com/gonglue/wzlm/pifu/'
    browser.get(url)
    more = browser.find_element_by_id('hero_more')
    for i in range(9):
            js = "var q=document.documentElement.scrollTop=100000"
            browser.execute_script(js)
            time.sleep(0.5)
            more.click()
    time.sleep(2)
    html=browser.page_source
    html=etree.HTML(html)
    pictures=html.xpath('//*[@id="hreo_list"]/li')
    isexist(Image_Path)
    for picture in pictures:
        url=picture.xpath('./a/img/@src')[0]
        name=picture.xpath('./a/span/text()')[0]
        response = requests.get(url)
        image_path = name + '.jpg'
        with open(image_path, 'wb') as f:
            f.write(response.content)
            print(name+ ' success')


def isexist(path):
    """
    判断文件是否存在
    :param path:
    :return:
    """
    if not os.path.exists(path):
        os.makedirs(path)
        os.chdir(path)
    else:
        os.chdir(path)


def Montage():
    """
    将所有的王者荣耀皮肤合并在一张图片上
    :return:
    """
    img=cv2.imread('./1.jpg')#所需要拼图的原图
    print(img.shape)
    res=cv2.resize(img,(1100,1200))#修改原图的大小并保存,
    cv2.imwrite('./1.jpg',res)
    image=pm.imread('./1.jpg')
    pool=pm.make_pool('./王者荣耀/*.jpg',sample_size=10000)#读取文件夹下的所有图片
    mosaic=pm.basic_mosaic(image,pool,(100,100))
    pm.imsave('2s.jpg',mosaic)#保存拼图图片


if __name__ == '__main__':
    if not os.path.exists('./'+Image_Path):
        Crawl_image()
        Montage()
    else:
        Montage()