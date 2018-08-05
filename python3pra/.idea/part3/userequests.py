__author__ = 'WQ'
# *_*coding:utf-8 *_*
import requests
import socket

proxies={'https':'203.130.46.108:9090','http':'222.41.154.119:61202'}
headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                       '(KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
         'host':'www.zhihu.com',
         'referer': 'https://www.zhihu.com/',
         'cookie': 'd_c0="AEDmtvylrw2PTjgGcgn0aB7ekvQa7I2PGGk=|1527905863"; _zap=a636d264-dc6f-4081-8720-a682748ed85f; z_c0=Mi4xYUluWUFRQUFBQUFBUU9hMl9LV3ZEUmNBQUFCaEFsVk5hMHpfV3dCcTZUTzh4ZGF3X2J6c1JJRVdHVXQxaF9SN1NR|1527905899|1d825851309e6376126ca10dee0186c5fd61c971; q_c1=6e7afb7ad9c44fa7a2cc151b8f6eb7cf|1530753153000|1527905863000; __utmv=51854390.100--|2=registration_date=20150713=1^3=entry_date=20150713=1; __utma=51854390.1924231716.1530753171.1531118074.1531638088.5; __utmz=51854390.1531638088.5.5.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/collections/mine; _xsrf=2771115d-2aca-42ef-8116-e671edf4a8c2; tgw_l7_route=4902c7c12bebebe28366186aba4ffcde'}

url='https://www.zhihu.com'
r=requests.get(url,headers=headers,proxies=proxies)
print(r.text)
#print(r.headers)
'''
print(socket.gethostbyname(socket.gethostname()))

pattern=re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)
tittle=re.findall(pattern,r.text)
print(tittle)
'''