'''
爬取去哪儿网所有城市自由行数据
爬取速度过快时会引发服务器返回错误
反反爬策略:设置cookies池和ip代理池以及延长爬虫休眠时间

'''
import requests
import time
from urllib.parse import quote
from multiprocessing import Pool
import pymongo

def begin():
    """
    获取去哪儿网出发地站点列表
    :return:
    """
    depurl='https://touch.dujia.qunar.com/depCities.qunar'
    response=requests.get(depurl)
    deps=response.json()
    for dep_item in deps['data']:
        for dep in deps['data'][dep_item]:
            yield dep#出发城市

def main(dep):
    """
    获取去哪儿网出发地可旅行的目的地列表
    :param dep: 出发地
    :return: 目的地列表
    """
    a = []
    desurl = 'https://touch.dujia.qunar.com/golfz/sight/arriveRecommend?dep={}&exclude=&extensionImg=255,175'.format(
        quote(dep))
    time.sleep(4)
    response = requests.get(desurl)
    des = response.json()
    for des_item in des['data']:
        for des_item_1 in des_item['subModules']:
            for query in des_item_1['items']:
                if query['query'] not in a:#去重,目的城市中有重复出现
                    a.append(query['query'])#目的城市列表
    get(a, dep)

def get(array,dep):
    """
    得到去哪儿网自由行数据搜索结果
    :param array: 目的城市列表
    :param dep: 出发城市
    :return:出发城市到目的城市的自由行结果
    """
    for item in array:
        # 头文件 防止反爬
        headers = {
            'cookie':'QN99=8770; QN1=eIQjmVtYQgbBDaEiPevvAg==; csrfToken=zKMVroGqYK6fdBphXg8rqQ3MpcaiZ7TZ; QN269=AA9586A58FEC11E88A24FA163E233FC1; QN601=3f55b4673bbd18ac3206bfea7c5996d3; QunarGlobal=10.86.213.148_6291bf49_164d0ba9dbf_-1a4d|1532510727219; _i=RBTKSaIAM3KBlurx6OwRjfuQ8pEx; QN300=auto_4e0d874a; QN163=0; QN6=auto_4e0d874a; QN48=tc_427b9f2555dccb4c_164d9787381_d960; _RSG=Ue4lzWGVuXAKnGpozKI.OB; _RDG=28c738c8ddc979203b2642a9f86b2ac273; _RGUID=a8787d08-3dbc-4a1e-b63e-494f72cd0c54; QN205=auto_4e0d874a; QN234=home_free_t; _vi=Xan8_FldA2NGBwqzRSKDNIYHisxd4ARxiomsg1mowQsC4OV3wCXnooJECkbZWsL9_3XGq9mmj5lTyMlGPRfgZD0jC_eS-Vas8fJyOdtOVO02USpBUqqwRZ1LfhiofVGvkPVi9NW0omogB1BkpWCaX2atkxba7uWItHjFuSd5R2NK; QN162=%E6%B7%B1%E5%9C%B3; QN233=FreetripTouchin; DJ12=eyJxIjoi5p2t5bee6Ieq55Sx6KGMIiwic3UiOiI4MDU5MjU4OTIiLCJkIjoi5rex5ZyzIiwiZSI6IkEiLCJsIjoiMCwyOCIsInRzIjoiZGQxNDZmZWYtMWY2NC00N2U5LWIyNjAtMTY0ODE2ZTlmYmQ0In0; _RF1=113.110.176.137; _pk_ref.1.8600=%5B%22%22%2C%22%22%2C1533395038%2C%22http%3A%2F%2Ftouch.qunar.com%2F%22%5D; _pk_ses.1.8600=*; _pk_id.1.8600=92302397325aca81.1533353790.5.1533395068.1533392908.; QN243=168',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Referer': 'https://touch.dujia.qunar.com/p/list?cfrom=zyx&dep={}&query={}&it=FreetripTouchin&et=home_free_t'.format(quote(dep),quote(item))
        }
        resulturl = 'https://touch.dujia.qunar.com/list?modules=list%2CbookingInfo%2CactivityDetail&dep={}&query={}&dappDealTrace=false&mobFunction=%E6%89%A9%E5%B1%95%E8%87%AA%E7%94%B1%E8%A1%8C&cfrom=zyx&it=FreetripTouchin&date=&configDepNew=&needNoResult=true&originalquery={}&limit=0,28&includeAD=true&qsact=search'.format(
            quote(dep), quote(item), quote(item))
        time.sleep(4)
        response = requests.get(resulturl, headers=headers).json()

        #容错处理,防止json文件中有不存在的项引起报错
        try:
            routecount = int(response['data']['limit']['routeCount'])#获取
            for limit in range(0, routecount, 28):
                resulturl = 'https://touch.dujia.qunar.com/list?modules=list%2CbookingInfo%2CactivityDetail&dep={}&query={}' \
                            '&dappDealTrace=false&mobFunction=%E6%89%A9%E5%B1%95%E8%87%AA%E7%94%B1%E8%A1%8C&cfrom=zyx&' \
                            'it=FreetripTouchin&date=&configDepNew=&needNoResult=true&originalquery={}&limit={},28&' \
                            'includeAD=true&qsact=search'.format(quote(dep), quote(item), quote(item), limit)
                time.sleep(4)
                response = requests.get(resulturl, headers=headers)
                items=response.json()['data']['list']['results'][0]
                result = {
                    '时间': time.strftime('%Y-%m-%d', time.localtime(time.time())),
                    '出发地': dep,
                    '目的地': item,
                    '价格':items['price'],
                    '天数': items['accomInclude'],
                    '亮点': items['brightspots'],
                    '出行工具':items['backtraffic'],
                    '类别':items['ttsRouteType']
                }
                print(result)
                savetomongo(result)
                time.sleep(2)
        except:
            return


mongo_uri='localhost'#mongodb端口号
mongo_db='qunar'#mongodb数据库
collection='travel'#mongodb集合
client=pymongo.MongoClient(mongo_uri)#连接mongodb
db=client[mongo_db]#创建qunar.travel

def savetomongo(result):
    """
    保存到mongodb数据库
    :param result: 出发城市到目的城市自由行搜索结果
    :return:
    """
    db[collection].insert(result)#插入数据到mongodb


if __name__ == '__main__':
    deps = begin()
    #开启多线程
    pool=Pool()
    pool.map(main,[dep for dep in deps])
    client.close()
