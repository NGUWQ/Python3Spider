import requests
from json import loads

def translate(words=None):
    url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    #表单文件
    from_data={
    'i': words,
    'from':'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': '1533303808767',
    'sign': 'c50e6308dc705cbc8b0e7098be1a1f85',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTIME',
    'typoResult': 'false'
    }
    #头文件 防止反爬
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Referer': 'http://fanyi.youdao.com/',
        'Host': 'fanyi.youdao.com'
    }
    #请求表单数据
    response=requests.post(url,data=from_data,headers=headers)
    #将json格式字符串转化为字典
    content=loads(response.text)
    #打印翻译后的数据
    result=content['translateResult'][0][0]['tgt']
    return result

def main():
    """
    调用translate函数
    :return:
    """
    print('欢迎使用此翻译程序,按exit退出')
    words=input('请输入你要翻译的文字(api接口会自动检测你所输入的语言):\n')
    if words:
        result=translate(words)
        print('翻译的结果为:\n',result)
        while True:
            words = input('请输入你要翻译的文字(api接口会自动检测你所输入的语言):\n')
            if words!='exit':
                result = translate(words)
                print('翻译的结果为:\n', result)
            else:
                break
        print('感谢您的使用...')

if __name__ == '__main__':
    main()