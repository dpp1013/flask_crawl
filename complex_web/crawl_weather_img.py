import urllib.request
from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
import threading


# 自己写
def getImg(url):
    try:
        headers = {
            'Cookie': 'vjuids=13e447486.170b02bd331.0.3b4be6e4c53b5; Hm_lvt_36dcc28125c1b7e65fa2190352951396=1583503628; Wa_lvt_7=1583503628; vjlast=1583503627.1583550351.13; UM_distinctid=171335b56cb2c9-067fb71109fde7-4313f6a-100200-171335b56cc232; userNewsPort0=1; f_city=%E4%B8%8A%E6%B5%B7%7C101020100%7C; HttpOnly; Hm_lvt_24b77a56c77ce27d009359b331cde12e=1585704559,1585704613; defaultCty=101021200; defaultCtyName=%u5F90%u6C47; CNZZDATA1278586243=460469860-1585702704-https%253A%252F%252Fwww.baidu.com%252F%7C1585891729; CNZZDATA1278586247=1012826771-1585702751-https%253A%252F%252Fwww.baidu.com%252F%7C1585891831; CNZZDATA1278586248=843440044-1585702829-https%253A%252F%252Fwww.baidu.com%252F%7C1585891938; CNZZDATA1278582114=1984202104-1585703006-https%253A%252F%252Fwww.baidu.com%252F%7C1585892088; CNZZDATA1278566949=82363663-1585702866-https%253A%252F%252Fwww.baidu.com%252F%7C1585891983; CNZZDATA1278535746=1071204121-1585703293-https%253A%252F%252Fwww.baidu.com%252F%7C1585892355; CNZZDATA1278535754=290105049-1585703298-https%253A%252F%252Fwww.baidu.com%252F%7C1585892349; CNZZDATA1278586242=561024244-1585703594-https%253A%252F%252Fwww.baidu.com%252F%7C1585892676; CNZZDATA1278548395=371422958-1585700754-https%253A%252F%252Fwww.baidu.com%252F%7C1585895245; cityListHty=101200101%7C101210101%7C101020600%7C101010100%7C101020100%7C101280101%7C101280601%7C101010300; Hm_lpvt_24b77a56c77ce27d009359b331cde12e=1585897111; cityListCmp=%E5%8C%97%E4%BA%AC-101010100-20200410%7C%E4%B8%8A%E6%B5%B7-101020100-20200411%7C%E5%B9%BF%E5%B7%9E-101280101-20200412%7C%E6%B7%B1%E5%9C%B3-101280601-20200413%2Cdefault%2C20200410; Hm_lpvt_080dabacb001ad3dc8b9b9049b36d43b=1586503133; Hm_lvt_080dabacb001ad3dc8b9b9049b36d43b=1585704561,1585704614,1585892098,1586503133; CNZZDATA1262608253=1908197961-1585892120-https%253A%252F%252Fwww.baidu.com%252F%7C1586501345; Wa_lvt_1=1585704615,1585892103,1586499048,1586503133; Wa_lpvt_1=1586503133; Wa_lvt_3=1586503301; Wa_lpvt_3=1586503301',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'

        }
        req = urllib.request.Request(url, headers=headers)
        html = urllib.request.urlopen(req)
        data = html.read()
        dammit = UnicodeDammit(data, ['utf-8', 'gbk'])
        data = dammit.unicode_markup
        soup = BeautifulSoup(data, 'lxml')
        links = soup.select('img')
        for link in links:
            print(link)
            url_img = url + '/' + link['src']
            urllib.request.urlretrieve(link['src'], 'image/' + link['src'].split('/')[-1])
    except Exception as err:
        print(err)


# 单线程
def imageSpider(start_url):
    try:
        urls = []
        req = urllib.request.Request(start_url, headers=headers)
        data = urllib.request.urlopen(req)
        data = data.read()
        dammit = UnicodeDammit(data, ['gbk', 'utf-8'])
        data = dammit.unicode_markup
        soup = BeautifulSoup(data, 'lxml')
        images = soup.select('img')
        for image in images:
            try:
                src = image['src']
                url = urllib.request.urljoin(start_url, src)
                if url not in urls:
                    urls.append(url)
                    print(url)
                    download(url)
            except Exception as err:
                print(err)
    except Exception as err:
        print(err)


def download(url, count):
    try:
        count += 1
        ext = url.split('.')[-1]
        req = urllib.request.Request(url, headers=headers)
        data = urllib.request.urlopen(req, timeout=100)
        data = data.read()
        fobj = open('image/' + str(count) + '.' + ext, 'wb')
        fobj.write(data)
        fobj.close()
        print('downloaded' + str(count) + '.' + ext)
    except Exception as err:
        print(err)


# 多线程
def threadimageSpider(url):
    global threads
    global count
    try:
        urls = []
        req = urllib.request.Request(start_url, headers=headers)
        data = urllib.request.urlopen(req)
        data = data.read()
        dammit = UnicodeDammit(data, ['gbk', 'utf-8'])
        data = dammit.unicode_markup
        soup = BeautifulSoup(data, 'lxml')
        images = soup.select('img')
        for image in images:
            try:
                src = image['src']
                url = urllib.request.urljoin(start_url, src)
                if url not in urls:
                    urls.append(url)
                    print(url)
                    count += 1
                    T = threading.Thread(target=download, args=(url, count))
                    T.setDaemon(False)
                    T.start()
                    threads.append(T)
            except Exception as err:
                print(err)
    except Exception as err:
        print(err)


if __name__ == '__main__':
    start_url = 'http://www.weather.com.cn'
    headers = {
        'Cookie': 'vjuids=13e447486.170b02bd331.0.3b4be6e4c53b5; Hm_lvt_36dcc28125c1b7e65fa2190352951396=1583503628; Wa_lvt_7=1583503628; vjlast=1583503627.1583550351.13; UM_distinctid=171335b56cb2c9-067fb71109fde7-4313f6a-100200-171335b56cc232; userNewsPort0=1; f_city=%E4%B8%8A%E6%B5%B7%7C101020100%7C; HttpOnly; Hm_lvt_24b77a56c77ce27d009359b331cde12e=1585704559,1585704613; defaultCty=101021200; defaultCtyName=%u5F90%u6C47; CNZZDATA1278586243=460469860-1585702704-https%253A%252F%252Fwww.baidu.com%252F%7C1585891729; CNZZDATA1278586247=1012826771-1585702751-https%253A%252F%252Fwww.baidu.com%252F%7C1585891831; CNZZDATA1278586248=843440044-1585702829-https%253A%252F%252Fwww.baidu.com%252F%7C1585891938; CNZZDATA1278582114=1984202104-1585703006-https%253A%252F%252Fwww.baidu.com%252F%7C1585892088; CNZZDATA1278566949=82363663-1585702866-https%253A%252F%252Fwww.baidu.com%252F%7C1585891983; CNZZDATA1278535746=1071204121-1585703293-https%253A%252F%252Fwww.baidu.com%252F%7C1585892355; CNZZDATA1278535754=290105049-1585703298-https%253A%252F%252Fwww.baidu.com%252F%7C1585892349; CNZZDATA1278586242=561024244-1585703594-https%253A%252F%252Fwww.baidu.com%252F%7C1585892676; CNZZDATA1278548395=371422958-1585700754-https%253A%252F%252Fwww.baidu.com%252F%7C1585895245; cityListHty=101200101%7C101210101%7C101020600%7C101010100%7C101020100%7C101280101%7C101280601%7C101010300; Hm_lpvt_24b77a56c77ce27d009359b331cde12e=1585897111; cityListCmp=%E5%8C%97%E4%BA%AC-101010100-20200410%7C%E4%B8%8A%E6%B5%B7-101020100-20200411%7C%E5%B9%BF%E5%B7%9E-101280101-20200412%7C%E6%B7%B1%E5%9C%B3-101280601-20200413%2Cdefault%2C20200410; Hm_lpvt_080dabacb001ad3dc8b9b9049b36d43b=1586503133; Hm_lvt_080dabacb001ad3dc8b9b9049b36d43b=1585704561,1585704614,1585892098,1586503133; CNZZDATA1262608253=1908197961-1585892120-https%253A%252F%252Fwww.baidu.com%252F%7C1586501345; Wa_lvt_1=1585704615,1585892103,1586499048,1586503133; Wa_lpvt_1=1586503133; Wa_lvt_3=1586503301; Wa_lpvt_3=1586503301',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'

    }
    count = 0
    threads = []
    threadimageSpider(start_url)
    for t in threads:
        t.join()
    print('the end')


def getImg(url):
    try:
        headers = {
            'Cookie': 'vjuids=13e447486.170b02bd331.0.3b4be6e4c53b5; Hm_lvt_36dcc28125c1b7e65fa2190352951396=1583503628; Wa_lvt_7=1583503628; vjlast=1583503627.1583550351.13; UM_distinctid=171335b56cb2c9-067fb71109fde7-4313f6a-100200-171335b56cc232; userNewsPort0=1; f_city=%E4%B8%8A%E6%B5%B7%7C101020100%7C; HttpOnly; Hm_lvt_24b77a56c77ce27d009359b331cde12e=1585704559,1585704613; defaultCty=101021200; defaultCtyName=%u5F90%u6C47; CNZZDATA1278586243=460469860-1585702704-https%253A%252F%252Fwww.baidu.com%252F%7C1585891729; CNZZDATA1278586247=1012826771-1585702751-https%253A%252F%252Fwww.baidu.com%252F%7C1585891831; CNZZDATA1278586248=843440044-1585702829-https%253A%252F%252Fwww.baidu.com%252F%7C1585891938; CNZZDATA1278582114=1984202104-1585703006-https%253A%252F%252Fwww.baidu.com%252F%7C1585892088; CNZZDATA1278566949=82363663-1585702866-https%253A%252F%252Fwww.baidu.com%252F%7C1585891983; CNZZDATA1278535746=1071204121-1585703293-https%253A%252F%252Fwww.baidu.com%252F%7C1585892355; CNZZDATA1278535754=290105049-1585703298-https%253A%252F%252Fwww.baidu.com%252F%7C1585892349; CNZZDATA1278586242=561024244-1585703594-https%253A%252F%252Fwww.baidu.com%252F%7C1585892676; CNZZDATA1278548395=371422958-1585700754-https%253A%252F%252Fwww.baidu.com%252F%7C1585895245; cityListHty=101200101%7C101210101%7C101020600%7C101010100%7C101020100%7C101280101%7C101280601%7C101010300; Hm_lpvt_24b77a56c77ce27d009359b331cde12e=1585897111; cityListCmp=%E5%8C%97%E4%BA%AC-101010100-20200410%7C%E4%B8%8A%E6%B5%B7-101020100-20200411%7C%E5%B9%BF%E5%B7%9E-101280101-20200412%7C%E6%B7%B1%E5%9C%B3-101280601-20200413%2Cdefault%2C20200410; Hm_lpvt_080dabacb001ad3dc8b9b9049b36d43b=1586503133; Hm_lvt_080dabacb001ad3dc8b9b9049b36d43b=1585704561,1585704614,1585892098,1586503133; CNZZDATA1262608253=1908197961-1585892120-https%253A%252F%252Fwww.baidu.com%252F%7C1586501345; Wa_lvt_1=1585704615,1585892103,1586499048,1586503133; Wa_lpvt_1=1586503133; Wa_lvt_3=1586503301; Wa_lpvt_3=1586503301',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'

        }
        req = urllib.request.Request(url, headers=headers)
        html = urllib.request.urlopen(req)
        data = html.read()
        dammit = UnicodeDammit(data, ['utf-8', 'gbk'])
        data = dammit.unicode_markup
        soup = BeautifulSoup(data, 'lxml')
        links = soup.select('img')
        for link in links:
            print(link)
            url_img = url + '/' + link['src']
            urllib.request.urlretrieve(link['src'], 'image/' + link['src'].split('/')[-1])
    except Exception as err:
        print(err)
