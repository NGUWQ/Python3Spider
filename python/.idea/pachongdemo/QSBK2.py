#Created by TTT
import  urllib.request
import  urllib.error as e
import re

class QSBK2:
    def __init__(self):
        self.pageIndex=1
        self.user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        self.headers={'user-agent':self.user_agent}
        self.stories=[]
        self.enable=False

    def getStories(self,pageIndex):
        try:
            url='https://www.qiushibaike.com/8hr/page/'+str(pageIndex)+'/'
            request=urllib.request.Request(url,headers=self.headers)
            response=urllib.request.urlopen(request)
            content=response.read().decode('utf-8')
            pattern=re.compile('''<div class="author.*?<h2>(.*?)</h2>'''
                               + '''.*?<span>(.*?)</span>'''
                               + '''.*?<!-- 图片或gif -->(.*?)<div class="stats">'''
                               + '''.*?<span class="stats-vote"><i class="number">(.*?)</i>''', re.S)
            items=re.findall(pattern,content)
            pageStories=[]
            for item in items:
                haveImg=re.search('img',item[2])
                if not haveImg:
                    replaceBR=re.compile('<br/>')
                    text=re.sub(replaceBR,'\n',item[1])
                    pageStories.append([item[0].strip(),text.strip(),item[3].strip()])
            return pageStories

        except e.HTTPError as es:
            if hasattr(es,'code'):
                print(es.code)
                return None
            if hasattr(es,'reason'):
                print(es.reason)
                return None

    def getOneStory(self,pageStories,page):
        for story in pageStories:
            inputs=input()
            self.loadpage()
            if inputs=='Q':
                self.enable=False
                return
            print('第%d页\t发布人:%s\t赞:%s\n%s'%(page,story[0],story[2],story[1]))

    def loadpage(self):
        if self.enable==True:
            if len(self.stories)<2:
                pageStories=self.getStories(self.pageIndex)
                if pageStories:
                    self.stories.append(pageStories)
                    self.pageIndex+=1

    def start(self):
        print('正在读取糗事百科,按enter翻页,按Q退出！')
        self.enable=True
        self.loadpage()
        nowPage=0
        while self.enable:
            if len(self.stories)>0:
                pageStories=self.stories[0]
                nowPage=nowPage+1
                del self.stories[0]
                self.getOneStory(pageStories,nowPage)
q=QSBK2()
q.start()