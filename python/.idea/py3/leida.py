#雷达分析图
# encoding: utf-8
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['KaiTi']  # 显示中文
labels = np.array([u'得分', u'篮板', u'助攻',u'抢断',u'盖帽',u'失误']) # 标签
dataLenth = 6 # 数据长度
data = np.array([[27.5,8.6,9.1,1.41,0.87,4.23],
                    [26.4,8.6,8.7,1.24,0.59,4.09],
                    [25.3,7.4,6.8,1.37,0.64,3.28],
                 [25.3,6.0,7.4,1.58,0.71,3.94],
                 [27.1,6.9,6.3,1.57,0.34,3.51],
                 [26.8,8.0,7.2,1.7,0.88,2.97]]) # 数据
angles = np.linspace(0, 2*np.pi, dataLenth, endpoint=False)  # 分割圆周长
data = np.concatenate((data, [data[0]]))  # 闭合
angles = np.concatenate((angles, [angles[0]]))  # 闭合
fig=plt.figure(facecolor="white")
plt.subplot(111,polar=True)
plt.plot(angles,data,'bo-',color='gray',linewidth=1,alpha=0.2)
plt.plot(angles,data,'o-',linewidth=1.5,alpha=0.2)
plt.fill(angles, data, alpha=0.25)# 填充
plt.thetagrids(angles * 180/np.pi, labels,frac=1.2)  # 做标签
plt.figtext(0.52,0.95,'勒布朗詹姆斯各项数据分析',ha='center',size=20)
legend=plt.legend(labels,loc=(0.94,0.80),labelspacing=0.1)
#plt.step(legend.get_texts(),fontsize='small')
plt.grid(True)
plt.savefig('james.jpg')
plt.show()