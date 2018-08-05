import requests
import time


headers = {
    'cookie': 'QN99=8770; QN1=eIQjmVtYQgbBDaEiPevvAg==; csrfToken=zKMVroGqYK6fdBphXg8rqQ3MpcaiZ7TZ; QN269=AA9586A58FEC11E88A24FA163E233FC1; QN601=3f55b4673bbd18ac3206bfea7c5996d3; QunarGlobal=10.86.213.148_6291bf49_164d0ba9dbf_-1a4d|1532510727219; _i=RBTKSaIAM3KBlurx6OwRjfuQ8pEx; QN300=auto_4e0d874a; QN163=0; QN6=auto_4e0d874a; QN48=tc_427b9f2555dccb4c_164d9787381_d960; _RSG=Ue4lzWGVuXAKnGpozKI.OB; _RDG=28c738c8ddc979203b2642a9f86b2ac273; _RGUID=a8787d08-3dbc-4a1e-b63e-494f72cd0c54; QN205=auto_4e0d874a; QN234=home_free_t; _vi=Xan8_FldA2NGBwqzRSKDNIYHisxd4ARxiomsg1mowQsC4OV3wCXnooJECkbZWsL9_3XGq9mmj5lTyMlGPRfgZD0jC_eS-Vas8fJyOdtOVO02USpBUqqwRZ1LfhiofVGvkPVi9NW0omogB1BkpWCaX2atkxba7uWItHjFuSd5R2NK; QN162=%E6%B7%B1%E5%9C%B3; _pk_ref.1.8600=%5B%22%22%2C%22%22%2C1533374400%2C%22http%3A%2F%2Ftouch.qunar.com%2F%22%5D; _pk_ses.1.8600=*; QN233=FreetripTouchin; _RF1=122.91.2.150; DJ12=eyJxIjoi5p2t5bee6Ieq55Sx6KGMIiwic3UiOiI0MDk1MTE3NjY5IiwiZCI6Iua3seWcsyIsImUiOiJBIiwibCI6IjAsMjgiLCJ0cyI6IjgxYmUwZjQ3LTdmYTAtNDliYy1iYTA0LWFlYTU4NzM0ZmRkMSJ9; _pk_id.1.8600=92302397325aca81.1533353790.3.1533375421.1533368101.; QN243=125',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Referer': 'https://touch.dujia.qunar.com/p/list?cfrom=zyx&dep=%E6%B7%B1%E5%9C%B3&query=%E6%9D%AD%E5%B7%9E%E8%87%AA%E7%94%B1%E8%A1%8C&it=FreetripTouchin&et=home_free_t'
}
resulturl ='https://touch.dujia.qunar.com/list?modules=list%2CbookingInfo%2CactivityDetail&dep=%E6%B7%B1%E5%9C%B3&query=%E6%9D%AD%E5%B7%9E%E8%87%AA%E7%94%B1%E8%A1%8C&dappDealTrace=false&mobFunction=%E6%89%A9%E5%B1%95%E8%87%AA%E7%94%B1%E8%A1%8C&cfrom=zyx&it=FreetripTouchin&date=&configDepNew=&needNoResult=true&originalquery=%E6%9D%AD%E5%B7%9E%E8%87%AA%E7%94%B1%E8%A1%8C&limit=0,28&includeAD=true&qsact=search'
time.sleep(2)
response = requests.get(resulturl, headers=headers)
print(response.json()['data']['list']['results'][0]['price'])
print(response.json()['data']['list']['results'][0]['accomInclude'])
print(response.json()['data']['list']['results'][0]['brightspots'])
print(response.json()['data']['list']['results'][0]['backtraffic'])
print(response.json()['data']['list']['results'][0]['ttsRouteType'])