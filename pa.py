# 分析豆瓣唐探3的影评，生成词云
import requests
from stylecloud import gen_stylecloud
import jieba
import re
from bs4 import BeautifulSoup
headers = {
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'
}
def spider_comment(movie_id, page):
    comment_list = []
    with open("douban.txt", "a+", encoding='utf-8') as f:
        for i in range(1,page+1):

            url = 'https://movie.douban.com/subject/%s/comments?start=%s&limit=20&sort=new_score&status=P' \
                  % (movie_id, (i - 1) * 20)

            req = requests.get(url, headers=headers)
            req.encoding = 'utf-8'
            comments = re.findall('<span class="short">(.*)</span>', req.text)
            f.writelines('\n'.join(comments))
    print(comments)
def jieba_cloud(file_name, icon):
    with open(file_name, 'r', encoding='utf8') as f:
        word_list = jieba.cut(f.read())

        result = " ".join(word_list)   
        icon_name = " "
        if icon == "1":
            icon_name = ''
        elif icon == "2":
            icon_name = "fas fa-dragon"
        elif icon == "3":
            icon_name = "fas fa-dog"
        elif icon == "4":
            icon_name = "fas fa-cat"
        elif icon == "5":
            icon_name = "fas fa-dove"
        elif icon == "6":
            icon_name = "fab fa-qq"
        pic = str(icon) + '.png'
        if icon_name is not None and len(icon_name) > 0:
            gen_stylecloud(text=result, icon_name=icon_name, font_path='simsun.ttc', output_name=pic)
        else:
            gen_stylecloud(text=result, font_path='simsun.ttc', output_name=pic)
        return pic
# 主函数
if __name__ == '__main__':
    movie_id = '27619748'
    page = 10
    spider_comment(movie_id, page)
    jieba_cloud("douban.txt", "1")
    jieba_cloud("douban.txt", "2")
    jieba_cloud("douban.txt", "3")
    jieba_cloud("douban.txt", "4")
    jieba_cloud("douban.txt", "5")
    jieba_cloud("douban.txt", "6")
