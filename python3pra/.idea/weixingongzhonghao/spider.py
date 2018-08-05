__author__ = 'WQ'
# *_*coding:utf-8 *_*
from requests import Session
from config import *
from db import RedisQueue
from mysql import MySQL
from request import WeixinRequest
from urllib.parse import urlencode
import requests
from pyquery import PyQuery as pq
from requests import ReadTimeout, ConnectionError


class Spider():
    base_url = 'http://weixin.sogou.com/weixin?type=2&s_from=input&query='
    keyword = 'NBA'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'CXID=D4E8EAA2564D90FBC285BAECF3078601; SUID=AEF72BAB5E68860A5B25128E00099457; SUV=00A00B5AAB2BF7AE5B2512C0E549F141; ad=Plllllllll2bJS3nlllllV7f1w9lllll$hsTrkllll9llllllZlll5@@@@@@@@@@; IPLOC=CN4403; ABTEST=0|1532415249|v1; SNUID=ABF409F180850E3945E004EF802B5D16; weixinIndexVisited=1; JSESSIONID=aaav6mr8OopuEawYdpHsw; ppinf=5|1532422896|1533632496|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTozOk5HVXxjcnQ6MTA6MTUzMjQyMjg5NnxyZWZuaWNrOjM6TkdVfHVzZXJpZDo0NDpvOXQybHVHN1RDWjZBU0E0TjgzM2JvaGs5aGJFQHdlaXhpbi5zb2h1LmNvbXw; pprdig=UAPBSEKKv9ua27yywPBP0BKxd4FAEtELVT8yK7dxy7N57B3yS-PA3M-C3d-VEOBxc-N-IIRP7khJM3Amnnol_WBt5RTD-V0pgVuxqNVf0EqfwLJwDWkiI3OA0-rCrBJrdOnCK0vj3IZvheDE1yjLjv-mdw0tv5MSeqlFOWZyhPk; sgid=22-36203267-AVtW6vAowj2ViaOuOVGM5Mto; ppmdig=153242289600000060a71b68c3ad711211acdaf46fde1281',
        'Host': 'weixin.sogou.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    session = Session()
    queue = RedisQueue()
    mysql = MySQL()


    def get_proxy(self):
        """
        从代理池获取代理
        :return:
        """
        try:
            response = requests.get(PROXY_POOL_URL)
            if response.status_code == 200:
                print('Get Proxy', response.text)
                return response.text
            return None
        except requests.ConnectionError:
            return None



    def start(self):
        """
        初始化工作
        """
        # 全局更新Headers

        self.session.headers.update(self.headers)
        start_url = self.base_url + self.keyword
        weixin_request = WeixinRequest(url=start_url, callback=self.parse_index, need_proxy=True)
        # 调度第一个请求
        self.queue.add(weixin_request)

    def parse_index(self, response):
        """
        解析索引页
        :param response: 响应
        :return: 新的响应
        """
        doc = pq(response.text)
        items = doc('.news-box .news-list li .txt-box h3 a').items()
        for item in items:
            url = item.attr('href')
            weixin_request = WeixinRequest(url=url, callback=self.parse_detail)
            yield weixin_request
        next = doc('#sogou_next').attr('href')
        if next:
            url = self.base_url + str(next)
            weixin_request = WeixinRequest(url=url, callback=self.parse_index, need_proxy=True)
            yield weixin_request

    def parse_detail(self, response):
        """
        解析详情页
        :param response: 响应
        :return: 微信公众号文章
        """
        doc = pq(response.text)
        data = {
            'title': doc('.rich_media_title').text(),
            'content': doc('.rich_media_content').text(),
            #'date': doc('#post-date').text(),
            'nickname': doc('#js_profile_qrcode > div > strong').text(),
            'wechat': doc('#js_profile_qrcode > div > p:nth-child(3) > span').text()
        }
        yield data


    def request(self, weixin_request):
        """
        执行请求
        :param weixin_request: 请求
        :return: 响应
        """
        try:
            if weixin_request.need_proxy:
                proxy = self.get_proxy()
                if proxy:
                    proxies = {
                        'http': 'http://' + proxy,
                        'https': 'https://' + proxy
                    }
                    return self.session.send(weixin_request.prepare(),
                                             timeout=weixin_request.timeout, allow_redirects=False, proxies=proxies)
            return self.session.send(weixin_request.prepare(), timeout=weixin_request.timeout, allow_redirects=False)
        except (ConnectionError, ReadTimeout) as e:
            print(e.args)
            return False


    def error(self, weixin_request):
        """
        错误处理
        :param weixin_request: 请求
        :return:
        """
        weixin_request.fail_time = weixin_request.fail_time + 1
        print('Request Failed', weixin_request.fail_time, 'Times', weixin_request.url)
        if weixin_request.fail_time < MAX_FAILED_TIME:
            self.queue.add(weixin_request)

    def schedule(self):
        """
        调度请求
        :return:
        """
        while not self.queue.empty():
            weixin_request = self.queue.pop()
            callback = weixin_request.callback
            print('Schedule', weixin_request.url)
            response = self.request(weixin_request)
            if response and response.status_code in VALID_STATUSES:
                results = list(callback(response))
                if results:
                    for result in results:
                        print('New Result', type(result))
                        if isinstance(result, WeixinRequest):
                            self.queue.add(result)
                        if isinstance(result, dict):
                            self.mysql.insert('articles', result)
                else:
                    self.error(weixin_request)
            else:
                self.error(weixin_request)

    def run(self):
        """
        入口
        :return:
        """
        self.start()
        self.schedule()


if __name__ == '__main__':
    spider = Spider()
    spider.run()