#Created by TTT
#用正则表达式抓取ip地址
import urllib.request
import urllib
import re
import time
import random
import os
import sys
sys.path.append('.idea/study/jiandan.py')
import jiandan
jiandan.url_open()
#抓取代理ip
def ipget(folder='iplist'):
    os.mkdir(folder)
    os.chdir(folder)
    ip_list = []
    url = 'http://www.xicidaili.com/nn/'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    request = urllib.request.Request(url=url, headers=headers)
    reponse = urllib.request.urlopen(request)
    content = reponse.read().decode('utf-8')
    pattern = re.compile('<td>(\d.*?)</td>')  # 截取<td>与</td>之间第一个数为数字的内容
    ip_page = re.findall(pattern, str(content))
    ip_list.extend(ip_page)
    time.sleep(random.choice(range(1, 3)))
    ip_list=ip_list[::4]
    save(ip_list)
def save(ip_list):
    for each in ip_list:
        #print(each)
        with open('ipget.txt','a') as f:#这里写文件要用到的模式为'a'意为写入一行后追加在后面,用'w'只有一行数据
            f.writelines(each+'\n')
if __name__=='__main__':
    ipget()
'''
print('代理IP地址     ','\t','端口','\t','速度','\t','验证时间')
for i in range(0,len(ip_list),4):
    print(ip_list[i],'    ','\t',ip_list[i+1],'\t',ip_list[i+2],'\t',ip_list[i+3])
'''