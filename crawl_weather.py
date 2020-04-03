'''
爬取与存储天气预报数据
'''
import urllib.request
from bs4 import BeautifulSoup
import sqlite3
from bs4 import UnicodeDammit


# 创建数据库类
class weatherDB:
    def openDB(self):
        self.con = sqlite3.connect('weathers.db')
        self.cursor = self.con.cursor()
        '''
        第一次创建表是成功的，第二次不成功，不成功就把这个表删除
        '''
        try:
            self.cursor.execute('create table weathers (wCity varchar(16),wDate varchar(16), wWeather varchar(64),\
            wTemp varchar(32),constraint pk_weather primary key(wCity,wDate))')
        except:
            self.cursor.execute('delete from weathers')

    def closeDB(self):
        self.con.commit()
        self.con.close()

    def insert(self, city, date, weather, temp):
        try:
            self.cursor.execute('insert into weathers(wCity,wDate,wWeather,wTemp) values(?,?,?,?)', \
                                (city, date, weather, temp))
        except Exception as err:
            print(err)

    def show(self):
        self.cursor.execute('select * from weathers')
        rows = self.cursor.fetchall()
        print('%-16s %-16s %-32s %-16s' % ("city", "date", 'weather', 'temp'))
        for row in rows:
            print('%-16s %-16s %-32s %-16s' % (row[0], row[1], row[2], row[3]))


# 创建weather
class WeatherForecast:
    def __init__(self):
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', \
            'Cookie': 'HttpOnly; BAIDU_SSP_lcr=https://www.baidu.com/link?url=316Y2RPCrLJng3CaqRceK5I5QMr09NMGtaLrGafmAVr0rgEnaRHPgL9Pt6KWFhs0t6wJq7sxNLEtcj1vlfh4UK&wd=&eqid=c0f1f61f0069e318000000045e83ef04; vjuids=13e447486.170b02bd331.0.3b4be6e4c53b5; Hm_lvt_36dcc28125c1b7e65fa2190352951396=1583503628; Wa_lvt_7=1583503628; vjlast=1583503627.1583550351.13; UM_distinctid=171335b56cb2c9-067fb71109fde7-4313f6a-100200-171335b56cc232; userNewsPort0=1; f_city=%E4%B8%8A%E6%B5%B7%7C101020100%7C; HttpOnly; Hm_lvt_24b77a56c77ce27d009359b331cde12e=1585704559,1585704613; cityListHty=101020600%7C101010100%7C101020100%7C101280101%7C101280601%7C101010300; Hm_lvt_080dabacb001ad3dc8b9b9049b36d43b=1583503628,1585704561,1585704614,1585892098; cityListCmp=%E5%8C%97%E4%BA%AC-101010100-20200403%7C%E4%B8%8A%E6%B5%B7-101020100-20200404%7C%E5%B9%BF%E5%B7%9E-101280101-20200405%7C%E6%B7%B1%E5%9C%B3-101280601-20200406%2Cdefault%2C20200403; CNZZDATA1262608253=1908197961-1585892120-https%253A%252F%252Fwww.baidu.com%252F%7C1585892120; defaultCty=101021200; defaultCtyName=%u5F90%u6C47; Wa_lvt_1=1583503628,1585704561,1585704615,1585892103; CNZZDATA1278586242=561024244-1585703594-https%253A%252F%252Fwww.baidu.com%252F%7C1585887276; CNZZDATA1278586243=460469860-1585702704-https%253A%252F%252Fwww.baidu.com%252F%7C1585891729; CNZZDATA1278535746=1071204121-1585703293-https%253A%252F%252Fwww.baidu.com%252F%7C1585886954; CNZZDATA1278586247=1012826771-1585702751-https%253A%252F%252Fwww.baidu.com%252F%7C1585891831; CNZZDATA1278586248=843440044-1585702829-https%253A%252F%252Fwww.baidu.com%252F%7C1585891938; CNZZDATA1278535754=290105049-1585703298-https%253A%252F%252Fwww.baidu.com%252F%7C1585886949; CNZZDATA1278582114=1984202104-1585703006-https%253A%252F%252Fwww.baidu.com%252F%7C1585892088; CNZZDATA1278566949=82363663-1585702866-https%253A%252F%252Fwww.baidu.com%252F%7C1585891983; CNZZDATA1278548395=371422958-1585700754-https%253A%252F%252Fwww.baidu.com%252F%7C1585889845; Hm_lpvt_24b77a56c77ce27d009359b331cde12e=1585892149; Hm_lpvt_080dabacb001ad3dc8b9b9049b36d43b=1585892155; Wa_lpvt_1=1585892156',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
        self.cityCode = {'北京': '101010100', '上海': '101020100', '广州': '101280101', '深圳': '101280601'}

    def forecast(self, city):
        if city not in self.cityCode.keys():
            print(city + 'code cannot be found')
            return
        url = 'http://www.weather.com.cn/weather/' + self.cityCode[city] + '.shtml'
        try:
            req = urllib.request.Request(url, headers=self.headers)
            data = urllib.request.urlopen(req)
            data = data.read()
            dammit = UnicodeDammit(data, ['utf-8', 'gbk'])
            data = dammit.unicode_markup
            soup = BeautifulSoup(data, 'lxml')
            soup.prettify()
            liall = soup.select('ul[class="t clearfix"] li')
            for li in liall:
                date = li.select('h1')[0].text
                weather = li.select('p[class="wea"]')[0].text
                temp = li.select('p[class="tem"]')[0].text.replace('\n','')
                # print(date, weather, temp)
                self.db.insert(city, date, weather, temp)
        except Exception as err:
            print(err)

    def process(self, cities):
        self.db = weatherDB()
        self.db.openDB()
        for city in cities:
            self.forecast(city)
        self.db.show()
        self.db.closeDB()


if __name__ == '__main__':
    wea = WeatherForecast()
    wea.process(['北京', '上海', '广州', '深圳'])
    print('complete')
