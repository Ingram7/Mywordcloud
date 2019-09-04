import jieba
from wordcloud import WordCloud
import os
import numpy
import PIL.Image as Image
import re

cur_path = os.path.dirname(__file__)

def chinese_jieba(txt):
    wordlist_jieba = jieba.cut(txt)          # 将文本分割，返回列表
    txt_jieba = " ".join(wordlist_jieba)     # 将列表拼接为以空格为间断的字符串
    return txt_jieba

stopwords = {'用户','https', 'weibo', 'com'}  # 噪声词
# 设置背景图
# 背景图片的画布一定要设置为白色（#FFFFFF）
# 然后显示的形状为不是白色的其他颜色
# 可以用ps或画图工具将自己要显示的形状复制到一个纯白色的画布上再保存
mask_pic = numpy.array(Image.open(os.path.join(cur_path, 'in.png')))
# 设置采用的文本
with open(os.path.join(cur_path, 'weibo.txt'), encoding='utf-8') as fp:
    txt = fp.read()

    # 下面两行  不需要去某些字符  可注释掉
    # pattern = re.compile(r'http://t.cn/(.*)"}')  # 定义正则表达式匹配模式
    # txt = re.sub(pattern, '', txt)  # 将符合模式的字符去除

    txt = chinese_jieba(txt)
    wordcloud = WordCloud(
                         # font_path = 'STXINWEI.TTF',   # 字体
                         font_path='MSYH.TTF',
                         background_color='white',       # 背景色
                         max_words=600,                  # 最大显示单词数
                         max_font_size=150,              # 频率最大单词字体大小
                         stopwords=stopwords,            # 过滤噪声词
                         mask=mask_pic                   # 自定义显示的效果图
                         ).generate(txt)

    wordcloud.to_file("out.png")    # 保存为图片
    image = wordcloud.to_image()
    image.show()