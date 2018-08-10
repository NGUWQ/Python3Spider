#提取qunaer_sights.csv文件中的经纬度和销量信息

import pandas as pd
import json

df=pd.read_csv('qunaer_sights.csv')
points=[]
df=df[['经度','纬度','月销量']]
for item in df.values:
    points.append({'lng':item[0],'lat':item[1],'count':item[2]})
strs=json.dumps(points)
print(strs)