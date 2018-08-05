#Created by TTT
import urllib.request
import urllib.error as u
import re
import threading
import time
class QSBK:
    #初始化方法,定义一些变量
    def __init__(self):
        self.pageIndex=1
        self.user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        #初始化headers
        self.headers={'user-agent':self.user_agent}
        #存放段子的变量,每一个元素是每一页的段子
        self.stories=[]
        #存放程序是否继续运行的变量
        self.enable=False
    #传入某一页的索引获得页面代码
    def getPage(self,pageIndex):
        try:
            url='https://www.qiushibaike.com/8hr/page/'+str(pageIndex)+'/'
            #构建请求的request
            request=urllib.request.Request(url,headers=self.headers)
            #利用urlopen获取页面代码
            response=urllib.request.urlopen(request)
            #将页面转化为utf-8编码
            content=response.read().decode('utf-8')
            return content
        except u.URLError as e:
            if hasattr(e,'code'):
                print(e.code)
                return  None
            if hasattr(e,'reason'):
                print('连接失败!',e.reason)
                return None
    #传入某一页代码,返回本页不带图片的段子列表
    def getPageItems(self,pageIndex):
        content=self.getPage(pageIndex)
        if not pageIndex:
            print('页面加载失败')
            return None
        pattern=re.compile('''<div class="author.*?<h2>(.*?)</h2>'''
                           + '''.*?<span>(.*?)</span>'''
                           + '''.*?<!-- 图片或gif -->(.*?)<div class="stats">'''
                           + '''.*?<span class="stats-vote"><i class="number">(.*?)</i>''', re.S)
        items=re.findall(pattern,content)
        #用来存储每页的段子们
        pageStories=[]
        #遍历正则表达式匹配的信息
        for item in items:
            #是否含有图片
            haveImg=re.search('img',item[2])
            #如果不含有图片,就加入到list中
            if not haveImg:
                replaceBR=re.compile('<br/>')
                text=re.sub(replaceBR,'\\n',item[1])
                #item[0]是一个段子的作者,item[3]是点赞数
                pageStories.append([item[0].strip(),text.strip(),item[3].strip()])
            return pageStories
    #加载并提取页面的内容,加入到列表中
    def loadpage(self):
        if self.enable==True:
            if len(self.stories)<2:
                #获取新的一页
                pageStories=self.getPageItems(self.pageIndex)
                #将该页的段子放进全局list中
                if pageStories:
                    self.stories.append(pageStories)
                    #获取完之后页码索引加1,表示下次读取下一页
                    self.pageIndex+=1
    #调用该方法,每次敲回车打印一个段子
    def getOneStory(self,pageStories,page):
        for story in pageStories:
            #等待用户输入
            inputs=input()
            #每当输入回车一次,判断一下是否要加载新页面
            self.loadpage()
            #如果输入Q则程序结束
            if inputs=='Q':
                self.enable=False
                return
            print('第%d页\t发布人:%s\t赞:%s\n%s'%(page,story[0],story[2],story[1]))

    #开始方法
    def start(self):
        print('正在读取糗事百科,按回车查看新段子,Q退出')
        #使变量变为True,程序可以正常运行
        self.enable=True
        #先加载每一页的内容
        self.loadpage()
        #局部变量,控制当前读到了第几页
        nowpage=0
        while self.enable:
            if len(self.stories)>0:
                #从全局list中获得一页的段子
                pageStories=self.stories[0]
                #当前读到的页数加1
                nowpage+=1
                #将全局list中第一个元素删除,因为已经取除
                del self.stories[0]
                #输出该页的段子
                self.getOneStory(pageStories,nowpage)
spider=QSBK()
spider.start()



#me
re.compile('<div class="author.*?<h2>(.*?)</h2>.*?'+
           '.*?<span>(.*?)</span>'+
           '.*?<!-- 图片或gif -->(.*?).*?'+
           '<div class="stats">.*?<span class="stats-vote"><i class="number">(.*?)</i>',re.S)

#other
re.compile('''<div class="author.*?<h2>(.*?)</h2>'''
           + '''.*?<span>(.*?)</span>'''
           + '''.*?<!-- 图片或gif -->(.*?)<div class="stats">'''
           + '''.*?<span class="stats-vote"><i class="number">(.*?)</i>''', re.S)