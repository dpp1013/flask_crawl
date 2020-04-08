from bs4 import BeautifulSoup
import urllib.request


def spider(url):
    global urls  # 记录访问过的url
    if url not in urls:
        urls.append(url)
        try:
            data = urllib.request.urlopen(url)
            data = data.read().decode()
            soup = BeautifulSoup(data, 'lxml')
            print(soup.find('h3').text)
            links = soup.select('a')
            for link in links:
                href = link['href']
                url = start_url + '/' + href
                spider(url)
        except Exception as err:
            print(err)


if __name__ == '__main__':
    start_url = 'http://127.0.0.1:5000'
    urls = []
    spider(start_url)
    print('The end')
