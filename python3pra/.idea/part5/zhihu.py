__author__ = 'WQ'
# *_*coding:utf-8 *_*
import requests
import pyquery
from requests.exceptions import RequestException
def getonepage(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Referer': 'https://www.zhihu.com/'
        }
        html=requests.get(url,headers=headers)
        if html.status_code==200:
            return html.text
        return None
    except RequestException:
        return None

def parseonepage(html):
    doc=pyquery.PyQuery(html)
    items=doc('.explore-tab .feed-item').items()
    for item in items:
        question=item.find('h2').text()
        author=item.find('.author-link').text()
        answer=pyquery.PyQuery(item.find('.content').html()).text()
        print(question)
        '''
        with open('知乎热门回答.txt','a',encoding='utf-8') as f:
            f.write('\n'.join([question,author,answer]))
            f.write('\n'+'='*50+'\n')
            '''

def main():
    url='https://www.zhihu.com/explore#daily-hot'
    html=getonepage(url)
    parseonepage(html)

if __name__ == '__main__':
    main()



