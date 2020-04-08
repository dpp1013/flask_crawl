'''
图的广度优先遍历BFS是一个分层搜索的过程，和树的层序遍历算法类似，它也需要一个队列以保持遍历过的顶点顺序，以便按出队的顺序再去访问这些顶点的
临接顶点，基本实现思想：
1. 顶点v入队列
2.当队列非空时继续执行，否则退出
3.当队列取得头顶点v;访问顶点v并标记顶点v已被访问
4.查找顶点v的第一个邻接顶点col
5.若v的邻接点col未被访问，则col入队列
6.继续查找顶点v的另一个新的邻接顶点col，找到步骤(5)。直到顶点v的所有未被访问过的邻接点处理完。转到步骤(2)
'''

from Queue import Queue
import urllib.request
from bs4 import BeautifulSoup


def spider(start_url):
    global urls
    queue = Queue()
    queue.enter(start_url)
    while not queue.empty():
        url = queue.fetch()  # 出队列
        if url not in urls:
            try:
                html = urllib.request.urlopen(url)
                data = html.read()
                data = data.decode()
                soup = BeautifulSoup(data, 'lxml')
                print(soup.find('h3').text)
                links = soup.select('a')
                for link in links:
                    href = link['href']
                    url = start_url + '/' + href
                    queue.enter(url)
            except Exception as err:
                print(err)


if __name__ == '__main__':
    urls = []
    start_url = 'http://127.0.0.1:5000'
    spider(start_url)
