#Created by TTT
#爬取手机百度翻译
import requests
import json
content=0
while True:
    content=input('请输入您要翻译的句子\n')
    if content!='':
        url = "http://fanyi.baidu.com/basetrans"
        data = {
            "query": content,
            "from": "zh",
            "to": "en",
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36",
        }
        response = requests.post(url,data=data,headers=headers)
        html = response.content.decode('unicode-escape')
        target = json.loads(html)
        print(target['trans'][0]['dst'])  # 显示出来unicode的中文
    else:
        break
