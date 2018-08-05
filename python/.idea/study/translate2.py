#Created by TTT
import urllib.request
import urllib.parse
import json
content='你好'
url = "http://fanyi.baidu.com/basetrans"
data = {
    "query": content,
    "from": "zh",
    "to": "en",
}
data=urllib.parse.urlencode(data).encode('utf-8')
response=urllib.request.urlopen(url,data)
html=response.read().decode('utf-8')
target=json.loads(html)
print(target)