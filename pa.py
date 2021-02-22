# 分析豆瓣唐探3的影评，生成词云
import requests
from stylecloud import gen_stylecloud
import jieba
import re
from bs4 import BeautifulSoup
headers = {
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'
}
def jieba_cloud(file_name):
    with open(file_name, 'r', encoding='utf8') as f:
        word_list = jieba.cut(f.read(),cut_all=True)

        result = " ".join(word_list)   
        # 制作中文词云
        icon_name = " "
        icon = "ciyun"
        pic = icon + '.png'
        gen_stylecloud(text=result, font_path='simsun.ttc', output_name=pic)
        return pic
