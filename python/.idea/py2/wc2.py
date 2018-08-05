#ÔÆ´ÊÍ¼,
import jieba.analyse
from PIL import Image,ImageSequence
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
lyric= ''
f=open('Èý¹úÑÝÒå.txt','r',encoding='gb18030',errors='ignore')
for i in f:
    lyric+=f.read()
result=jieba.analyse.textrank(lyric,topK=50,withWeight=True)
keywords = dict()
for i in result:
    keywords[i[0]]=i[1]
print(keywords)
image= Image.open('.idea/inspectionProfiles/img/5486633.png')
graph = np.array(image)
wc = WordCloud(font_path='./fonts/simhei.ttc',background_color='White')
wc.generate_from_frequencies(keywords)
image_color = ImageColorGenerator(graph)
plt.imshow(wc)
plt.imshow(wc.recolor(color_func=image_color))
plt.axis("off")
plt.show()
wc.to_file('.idea/inspectionProfiles/img/548663.png')