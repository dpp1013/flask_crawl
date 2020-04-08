from Stack import Stack
from bs4 import BeautifulSoup
import urllib.request


def spider(url):
    global urls
    stack = Stack()
    stack.push(url)
    while not stack.empty():
        url = stack.pop()  # 出栈
        if url not in urls:
            urls.append(url)  # 如果url不在urls里，追加u到urls
            try:
                data = urllib.request.urlopen(url)
                data = data.read()
                data = data.decode()
                soup = BeautifulSoup(data, 'lxml')
                print(soup.find('h3').text)
                links = soup.select('a')
                for i in range(len(links) - 1, -1, -1):
                    link = start_url + '/' + links[i]['href']
                    stack.push(link)
            except Exception as err:
                print(err)


if __name__ == '__main__':
    start_url = 'http://127.0.0.1:5000'
    urls = []
    spider(start_url)
