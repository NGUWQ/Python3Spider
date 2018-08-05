__author__='WQ'
# *_*coding:utf-8 *_*
import urllib.request
import urllib.error as err
import re
import time

#处理页面标签类
class Tool:
    #去除img标签,7位长空格
    removeImg=re.compile('<img.*?>| {7}|')
    #删除超链接标签
    removeAddr=re.compile('<a.*?>|</a>')
    #把换行的标签换位\n
    replaceLine=re.compile('<tr>|<div>|</div>|</p>')
    #将表格制表<td>替换为\t
    repalceTd=re.compile('<td>')
    #把段落开头换为\n加空两格
    replacePara=re.compile('<p.*?>')
    #将换行符或双换行符替换为\n

    
    replaceBr=re.compile('<br><br>|<br>')
    #将其余标签剔除
    repalceExtraTag=re.compile('<.*?>')

    def replace(self,x):
        x=re.sub(self.removeImg,'',x)
        x=re.sub(self.removeAddr,'',x)
        x=re.sub(self.replaceLine,'\n',x)
        x=re.sub(self.repalceTd,'\t',x)
        x=re.sub(self.replacePara,'\n  ',x)
        x=re.sub(self.replaceBr,'\n',x)
        x=re.sub(self.repalceExtraTag,'',x)
        #strip()将前后多余内容删除
        return x.strip()


#百度贴吧爬虫类
class BDTB:
    #初始化,传入基地址,是否只看楼主的参数
    def __init__(self,baseUrl,seeLZ,floorTag):
        #base连接地址
        self.baseUrl=baseUrl
        #是否只看楼主
        self.seeLZ='?see_lz='+str(seeLZ)
        self.user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        self.headers={'user-agent':self.user_agent}
        #HTML标签剔除工具类对象
        self.tool=Tool()
        #全局file变量,文件写入操作对象
        self.file=None
        #楼层标号,初始为1
        self.floor=1
        #默认标题,如果没有成功获取到标题的话就会用这个标题
        self.defaultTittle='百度贴吧'
        #是否写入分隔符标记
        self.floorTag=floorTag

    #传入页码,获取该页帖子的代码
    def getPage(self,pageNum):
        try:
            url=self.baseUrl+self.seeLZ+'&pn='+str(pageNum)
            request=urllib.request.Request(url,headers=self.headers)
            response=urllib.request.urlopen(request)
            page=response.read().decode('utf-8')
            return page
        except err.URLError as e:
            if hasattr(e,'reason'):
                print('连接百度贴吧失败,错误原因',e.reason)
                return None
    #获取帖子标题
    def getTittle(self,page):
        pattern=re.compile('<h3 class="core_title_txt pull-left text-overflow  ".*?>(.*?)</h3>',re.S)
        result=re.search(pattern,page)
        if result:
            #print(result.group(1))
            return result.group(1).strip()
        else:
            return None


    #获取帖子总共的页数
    def getPageNum(self,page):
        pattern=re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)
        result=re.search(pattern,page)
        if result:
            #print(result.group(1))
            return result.group(1).strip()
        else:
            return None

    #获取每一层楼的内容,传入页面内容
    def getContent(self,page):
        pattern=re.compile('<div id="post_content.*?>(.*?)</div>',re.S)
        items=re.findall(pattern,page)
        contents=[]
        for item in items:
            #将文本进行去除标签处理,同时在前后加入换行符
            content='\n'+self.tool.replace(item)+'\n'
            contents.append(content.encode('utf-8'))
        return contents

    def setFileTittle(self,tittle):
        #如果标题不为None,即成功获取到标题
        if tittle is not None:
            self.file=open(tittle+'.txt','w+',encoding='utf-8')
        else:
            self.file=open(self.defaultTittle+'.txt','w+',encoding='utf-8')

    def writeData(self,contents):
        #向文件写入每一楼的信息
        for item in contents:
            if self.floorTag==1:
                #楼之间的分隔符
                floorLine='\n'+str(self.floor)+'楼  ------------------------------------------------------------' \
                                               '------------------------------------------------------------\n'
                self.file.write(floorLine)
            self.file.write(item.decode('utf-8'))
            self.floor+=1

    def start(self):
        indexPage=self.getPage(1)
        pageNum=self.getPageNum(indexPage)
        tittle=self.getTittle(indexPage)
        self.setFileTittle(tittle)
        if pageNum==None:
            print('url已失效,请重试')
            return
        try:
            print('该帖共有'+str(pageNum)+'页')
            for i in range(1,int(pageNum)+1):
                print('正在写入第'+str(i)+'页数据')
                page=self.getPage(i)
                contents=self.getContent(page)
                self.writeData(contents)
            #出现写入异常
        except IOError as err:
            print('写入异常,原因'+err.message)
        finally:
            print('写入任务完成')


baseUrl='https://tieba.baidu.com/p/5176659692'
seeLZ=1
floorTag=1
bdtb=BDTB(baseUrl,seeLZ,floorTag)
bdtb.start()