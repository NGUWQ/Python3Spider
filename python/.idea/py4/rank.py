#获取大学排名
import requests
from  bs4 import BeautifulSoup
allUniv=[]
def gettext(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding='utf-8'
        return  r.text
    except:
        return ""
def fill(soup):
    data=soup.find_all('tr')
    for tr in data:
        ltd=tr.find_all('td')
        if len(ltd)==0:
            continue
        single=[]
        for  td in ltd:
            single.append(td.string)
        allUniv.append(single)
def printss(num):
    print("{:^4}{:^10}{:^5}{:^8}{:^10}".format("排名","学校名称","省市","总分","培养规模"))
    for i in range(num):
        u=allUniv[i]
        print("{:^4}{:^10}{:^5}{:^8}{:^10}".format(u[0],u[1],u[2],u[3],u[6]))
def main(num):
    url='http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html=gettext(url)
    soup=BeautifulSoup(html,"html.parser")
    fill(soup)
    printss(num)
main(310)