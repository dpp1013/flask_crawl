'''
运用深度优先遍历，栈实现
思路：
1.第一个url入栈
2.如果栈为空，程序结束，如果不为空出栈一个url，爬取其h3标签内容
3.获取url站点的所有超链接的href值，组成连接列表links，把链接入栈
4.回到2
'''
import urllib.request
from bs4 import BeautifulSoup
from Stack import Stack


def spider(url):
    try:
        st = Stack()
        st.push(url)  # 第一个进栈
        while st.empty() != True:
            url_recive = st.pop()
            html = urllib.request.urlopen(url_recive)
            data = html.read()
            data = data.decode()
            soup = BeautifulSoup(data, 'lxml')
            soup.prettify()
            print(soup.find('h3').text)
            links = soup.select('a')
            # start,end,step
            for i in range(len(links) - 1, -1, -1):
                href = links[i]['href']
                linksUrl = url + '/' + href
                st.push(linksUrl)
    except Exception as err:
        print(err)


if __name__ == '__main__':
    spider('http://127.0.0.1:5000')
    print('The end')
