'''
设计的思路如下：
1.从books.html出发
2.访问一个网页，获取h3标题
3.获取这个网页中所有<a>的href值形成的link列表
4.循环links列表，对于每个连接link都指向另外一个网页，递归回到（2）
5.继续links的下一个link，直到遍历所有link为止
明显的程序在使用深度优先遍历这棵树，递归这种程序都是采用深度优先的方法遍历树
'''
from bs4 import BeautifulSoup
import urllib.request


def spider(url):
    try:
        data = urllib.request.urlopen(url)
        data = data.read()
        data = data.decode()
        soup = BeautifulSoup(data, 'lxml')
        print(soup.find('h3').text)  # 找到第一个h3的文本内容
        links = soup.select('a')  # 找到所有a标签
        for link in links:
            href = link['href']  # 获取网页的名称
            url = start_url + '/' + href  # 获取网页的绝对地址
            spider(url)
    except Exception as err:
        print(err)

if __name__ == '__main__':
    start_url = 'http://127.0.0.1:5000'
    spider(start_url)
    print('The end')
