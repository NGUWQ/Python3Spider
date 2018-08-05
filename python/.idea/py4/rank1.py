from bs4 import BeautifulSoup
import requests
import bs4

def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""

def fillUniversityList(UList,text):
    soup=BeautifulSoup(text,'html.parser')
    for tr in soup.find("tbody").children:
        #tr必须是一个标签的内容，每一行tr表示一个大学信息，用td标签对隔开大学信息
        if isinstance(tr,bs4.element.Tag):
            tdlist=tr.find_all("td")
            UList.append([tdlist[0].string,tdlist[1].string,tdlist[3].string])

def printUniversityList(UList):
    #使3列数据居中显示，域宽为10
    demo="{0:^10}{1:{3}^10}{2:^10}"
    #chr(12288)采用中文的空格填充
    print(demo.format("排名:","大学:","分数:",chr(12288)))
    for info in UList:
        print(demo.format(info[0],info[1],info[2],chr(12288)))


def main():
    UInfo=[]
    html=getHTMLText("http://www.zuihaodaxue.cn/zuihaodaxuepaiming2017.html")
    fillUniversityList(UInfo,html)
    printUniversityList(UInfo)

main()