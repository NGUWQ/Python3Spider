from selenium import  webdriver
from lxml import etree
import time

#Chrome Headless模式(无界面模式)
chrome_options=webdriver.ChromeOptions()#创建ChromeOptions对象
chrome_options.add_argument('--headless')#添加headless参数
browser=webdriver.Chrome(chrome_options=chrome_options)
url='http://fanyi.youdao.com/'
browser.get(url)


def translate(words):
    """
    翻译文本,支持任何语言
    :param words: 待翻译的文本
    :return:
    """
    input=browser.find_element_by_id('inputOriginal')
    input.send_keys(words)
    time.sleep(1)
    response=browser.page_source
    html=etree.HTML(response)
    output=html.xpath('//div[@class="input__target__text"]/p/span/text()')[0]
    #output=''.join(output).strip()
    input.clear()
    #返回翻译的文本
    return output


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
    browser.close()