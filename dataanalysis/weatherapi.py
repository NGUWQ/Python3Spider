import requests
import pandas as pd
import pymongo
#用API爬取天气预报数据


mongouri='localhost'
mongodb='weather'
collection='forecast'

client=pymongo.MongoClient(mongouri)
db=client[mongodb]

def getweather():
    # 利用pandas库进行数据清洗
    df = pd.read_csv('file/china-city-list.csv')
    for location in df.get('City_CN'):
        url='https://free-api.heweather.com/s6/weather/forecast?parameters&location='+location+'&key=a1535e144edd487ba80864dbf9f20f7e'
        response=requests.get(url)
        response.encoding='utf8'
        dic=response.json()
        for item in dic['HeWeather6'][0]['daily_forecast']:
            yield {
                '城市':location,
                '天气':item['cond_txt_d'],
                '最高温度':item['tmp_max'],
                '最低温度': item['tmp_min'],
                '时间':item['date']
            }

def savetomongo(item):
    db[collection].insert(dict(item))


def select():
    for item in db[collection].find({'最高温度':{'$lt':'20'}}):
        print(item)


def main():
    items=getweather()
    for item in items:
        print(item)
        savetomongo(item)
    client.close()

if __name__ == '__main__':
    select()


'''
法2
#with open('file/china-city-list.csv','r',encoding='utf-8') as csvfile:
    reader=csv.reader(csvfile)
    for row in reader:
        print(row[0])
'''













