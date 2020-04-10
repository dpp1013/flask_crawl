'''
1.设置urllib.request下载图片时间，如果超过一定时间还么有完成下载就放弃
2.设置下载过程是一个于主线程不同的子线程，子线程完成下载任务，不影响主线程继续访问别的网页
'''
import urllib.request
from bs4 import BeautifulSoup
import threading


def spider(url):
    global urls
    if url not in urls:
        urls.append(url)
        try:
            html = urllib.request.urlopen(url)
            data = html.read()
            data = data.decode()
            soup = BeautifulSoup(data, 'lxml')
            print(soup.find('h3').text)
            divs = soup.select('div')
            imgs = soup.select('img')
            if len(divs) > 0 and len(imgs) > 0:
                print(divs[0].text)
                url = start_url + '/' + imgs[0]['src']
                # 加入线程
                T = threading.Thread(target=download, args=(url, imgs[0]['src']))
                T.setDaemon(False)
                T.start()
                threads.append(T)
            links = soup.select('a')
            for link in links:
                href = link['href']
                url = start_url + '/' + href
                spider(url)
        except Exception as err:
            print(err)


def download(url, img):
    urllib.request.urlretrieve(url, 'downloaded' + img)
    print('downloaded', img)


if __name__ == '__main__':
    start_url = 'http://127.0.0.1:5000'
    threads = []
    urls = []
    spider(start_url)
    # 所有线程执行完毕，主线程才结束
    for t in threads:
        t.join()
    print('the end')
