import jieba
from PIL import Image,ImageSequence
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
text_read = open('三国演义.txt','r',encoding='gb18030',errors='ignore').read()
jieba.load_userdict("C:/Users/TTT/Desktop/杂/test_dic.txt")
c = jieba.cut(text_read, cut_all=False, HMM=True)
word_list = []
for i in c:
    word_list.append(i)
word_dic = {}
for i in word_list:
    if i not in word_dic:
        word_dic[i] = 1
    else :
        word_dic[i] += 1
over_list = sorted(word_dic.items(), key = lambda x : x[1], reverse=True)

font_path = "./fonts/simhei.ttc"#字体路径
dizi_path = "C:/Users/TTT/Desktop/杂/图片/5486633.png"#底子图片路径

back_coloring = plt.imread(dizi_path)#使用PIL来读取图像

wc = WordCloud(background_color="white", #背景颜色
               font_path=font_path, #字体选择
               max_words=1000, #最大词数
               mask=back_coloring ,#背景图片
               max_font_size=100, #最大字体大小
               width=1000, height=860, margin=2)

wc.fit_words(dict(over_list[20:]))

plt.figure()
#显示图片
plt.imshow(wc)
plt.axis("off")
plt.show()
#保存图片
wc.to_file(path.join(path.dirname(__file__), "C:/Users/TTT/Desktop/杂/wordcloud1.png"))
#改变颜色
image_color = ImageColorGenerator(back_coloring)#从背景图片生成颜色值
plt.imshow(wc.recolor(color_func=image_color))#使用新的颜色值布局着色
plt.axis('off')#关闭坐标轴
#绘制背景颜色的词云
plt.figure()
plt.imshow(back_coloring, cmap = plt.cm.gray)
plt.axis('off')
plt.show()
wc.to_file(path.join(path.dirname(__file__), "C:/Users/TTT/Desktop/杂/wordcloud2.png"))