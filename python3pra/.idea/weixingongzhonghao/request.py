__author__ = 'WQ'
# *_*coding:utf-8 *_*
from config import *
from requests import Request


class WeixinRequest(Request):
    def __init__(self, url, callback, method='GET', headers=None, need_proxy=False, fail_time=0, timeout=TIMEOUT):
        Request.__init__(self, method, url, headers)
        self.callback = callback#回调函数
        self.need_proxy = need_proxy#是否需要代理爬取
        self.fail_time = fail_time#失败次数
        self.timeout = timeout#超时时间