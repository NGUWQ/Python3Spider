import requests
from bs4 import BeautifulSoup as BS
import pandas as pd
import time
import random
import json
import csv
import urllib.parse as p


#读取上次爬取的CSV文件,以便断点爬取
def init_df():
    global df_sights
    try:
        df_sights=pd.read_csv('qunaer_sights.csv')
    except:
        df_sights=pd.DataFrame()


#初始化CSV writer,第一次需写入列名
def init_csv():
    global f
    global writer
    global df_sights
    csvfile='qunaer_sights.csv'
    f=open(csvfile,'a+',newline='',encoding='utf-8')
    writer=csv.writer(f)
    if df_sights.columns.empty:
        writer.writerow(['景点名','等级','地址','介绍','热度','价格','月销量','经度','纬度'])
        #writer.writerow(['景点名', '等级', '地址', '介绍', '热度', '价格', '月销量'])


#程序结束前关闭CSV文件
def close_csv():
    global f
    f.close()


#调用百度地图API获取景点地址对应的经纬度
def get_geo_info(address):
    geo_uri='http://api.map.baidu.com/geocoder/v2/?'
    geo_params={
        'output':'json',
        'ak':'qmnKZsgNE3NWxwRvoiuVrhuRujDRDQQa'
    }
    #更新url中的地址参数
    geo_params.update({'address':address})
    data=p.urlencode(geo_params)
    cur_geo_uri=geo_uri+data
    geo_resp=requests.get(cur_geo_uri)
    json_data=json.loads(geo_resp.text)

    #调用成功,获取JSON data中的经纬度信息
    if json_data['status']==0:
        longitude=json_data['result']['location']['lng']
        latitude=json_data['result']['location']['lat']
    else:
        longitude=''
        latitude=''

    return longitude,latitude


#抓取去哪儿网站热门景点销售信息
def dump_qunaer_sights(pages):
    global df_sights
    global writer
    base_url='http://piao.qunar.com/ticket/list.htm?keyword=热门景点&page='
    for i in range(pages):
        print('page:{0}'.format(i+1))
        url=base_url+str(i+1)
        resp=requests.get(url)
        time.sleep(random.uniform(1,3))

        #通过BeautifulSoup解析当前页面HTML,获取景点列表信息
        soup=BS(resp.text,'lxml')
        sight_list=soup.select('.sight_item_detail')
        for sight in sight_list:
            #获取景点名
            name=sight.select('.name')[0].text
            #如该景点已存在CSV文件中,则跳过该页,继续抓取下一页(断点续爬)
            if not df_sights.empty and not df_sights[df_sights['景点名']==name].empty:
                break

            #获取景点等级
            try:
                level=sight.select('.level')[0].text.replace('景区','')
            except:
                level=''

            #获取景点地址
            #address=sight.select('.area > a')[0].text.split('·')[-1]
            address = sight.select('.address color999 span')[0].text.replace('地址:','')


            #获取景点介绍
            intro=sight.select('.intro.color999')[0].text

            #获取景点热度
            star=sight.select('.product_star_level em span')[0].text.replace('热度 ','')

            #获取门票价格,月销量
            try:
                price=sight.select('.sight_item_price em')[0].text
                sales=sight.select('.hot_num')[0].text
            except:
                continue

            #将景点地址转换为经纬度
            longitude,latitude=get_geo_info(address)

            #向CSV文件中插入一条景点信息
            #sight_item=[name,level,address,intro,star,price,sales]
            sight_item = [name, level, address, intro, star, price, sales,longitude,latitude]
            print(sight_item)
            writer.writerow(sight_item)



if __name__ == '__main__':
    init_df()
    init_csv()
    dump_qunaer_sights(50)
    close_csv()
