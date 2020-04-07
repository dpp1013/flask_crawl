'''
广度优先遍历:
1.第一个url入队列
2.如果列空，程序结束，如不为空出队url，爬取其h3
3.获取该url的<a>并入队
4.回到（2）
'''

import urllib.request
from bs4 import BeautifulSoup
from Queue import Queue


def spider(url):
    try:
        st = Queue()
        st.enter(url)  # 第一个进栈
        while st.empty() != True:
            url_recive = st.fetch()
            html = urllib.request.urlopen(url_recive)
            data = html.read()
            data = data.decode()
            soup = BeautifulSoup(data, 'lxml')
            soup.prettify()
            print(soup.find('h3').text)
            links = soup.select('a')
            for link in links:
                linkUrl = link['href']
                linkUrl = url + '/' + linkUrl
                # print(linkUrl)
                st.enter(linkUrl)
    except Exception as err:
        print(err)


if __name__ == '__main__':
    spider('http://127.0.0.1:5000')