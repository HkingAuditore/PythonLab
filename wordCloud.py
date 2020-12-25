import jieba
import wordcloud
import imageio

mk = imageio.imread("cloud.png")
w = wordcloud.WordCloud(mask=mk)

w = wordcloud.WordCloud(width=1000,
                        height=700,
                        background_color='white',
                        font_path='方正细圆简体.ttf',
                        mask=mk,
                        # min_font_size=40,
                        # max_font_size=40,
                        scale=15)

f = open('2001.txt',encoding='utf-8')
txt = f.read()
txtlist = jieba.lcut(txt)
string = " ".join(txtlist)
w.generate(string)
w.to_file('output.png')