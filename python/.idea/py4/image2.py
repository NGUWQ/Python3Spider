import requests
import os
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BeautifulPicture():
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Mobile Safari/537.36'}
        self.web_url = 'http://www.hugsmxy.com/'
        self.folder_path = '.idea/py2/img'

    def getPic(self):

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(chrome_options=chrome_options)

        driver.get(self.web_url)
        self.scrollDown(webDirver=driver,times=10) #执行网页下拉到底部操作，执行5次
        print('开始获取所有的图片标签')
        all_img = BeautifulSoup(driver.page_source,'lxml').find_all('img', class_='_2zEKz')
        print('开始创建文件夹')
        self.mkdir(self.folder_path)
        files = self.getFiles()
        print('开始切换文件夹')
        os.chdir(self.folder_path)
        print('img标签的数量是：',len(all_img))

        i = 1 #用来给文件命名，防止重复
        for img in all_img:
            img_src = img['src']
            width_pos = img_src.index('&w=')
            height_pos = img_src.index('&q=')
            width_height_str = img_src[width_pos:height_pos]
            # img_url_final = img_src.replace(width_height_str, '')
            img_url_final = img_src
            print('截取到的图片url是：', img_url_final)
            file_name = str(i) + '.jpg'
            if file_name not in files:
                self.saveImage(img_url_final, file_name)
            else:
                print("图片已经存在",file_name)
            i += 1
            if i == len(all_img):
                driver.close()

    def request(self,url):
        response = requests.get(url,headers = self.headers)
        return  response

    def mkdir(self,path):
        path = path.strip()
        isExists = os.path.exists(path)
        if not isExists:
            print('创建名字叫做',path,'的文件夹')
            os.makedirs(path)
            print('创建成功')
        else:
            print(path,'文件夹存在，不用创建')

    def saveImage(self,url,name):
        print('开始保存图片')
        img = self.request(url)
        print('开始保存文件')
        f = open(name,'ab')
        f.write(img.content)
        print(name,'文件保存成功！')
        f.close()

    def scrollDown(self,webDirver,times):
        for i in  range(times):
            print("开始执行第",str(i + 1),"次下拉操作")
            #执行JavaScript实现网页下拉到底部
            webDirver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            print("第", str(i + 1), "次下拉操作执行完毕")
            print("第", str(i + 1), "次等待网页加载......")
            time.sleep(2)

    def getFiles(self):
        return os.listdir(self.folder_path)





beautiful = BeautifulPicture()
beautiful.getPic()