import urllib.request
import urllib.parse


def getMess():
    url = 'http://127.0.0.1:5000?'
    # 以get方式向服务器发送请求
    try:
        province = urllib.parse.quote('河南')
        city = urllib.parse.quote('郑州')
        data = 'province=' + province + '&city=' + city
        url = url + data
        html = urllib.request.urlopen(url)
        html = html.read()
        html = html.decode()
        print(html)
    except Exception as err:
        print(err)


def postMess():
    '''
    以post方式向服务器发送请求
    '''
    try:
        province = urllib.parse.quote('河北')
        city = urllib.parse.quote('石家庄')
        data = "province=" + province + "&city=" + city
        # post方法发送请求时，data需要编码
        data = data.encode()
        urllib.request.urlopen('http://127.0.0.1:5000/postExample', data=data)
    except Exception as err:
        return err


def get_post_mix():
    '''
    get+post混合使用，get发送省份和城市名，post发送城市简介
    '''
    url = 'https://127.0.0.1:5000/mix?'
    note = '深圳依山傍水，气候宜人，实在是适合人类居住的绝佳地'
    try:
        province = urllib.parse.quote('广东')
        city = urllib.parse.quote('深圳')
        note = "note=" + urllib.parse.quote(note)
        param = 'province=' + province + '&city=' + city
        html = urllib.request.urlopen(url + param, data=note.encode())
        html = html.read().decode()
        print(html)
    except Exception as err:
        print(err)


if __name__ == '__main__':
    get_post_mix()
