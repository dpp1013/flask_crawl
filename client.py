import urllib.request
import urllib.parse


def getMess():
    url = 'http://127.0.0.1:5000?'
    # 以get方式向服务器发送请求，request默认的方式是get
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
    try:
        province = urllib.parse.quote('河北')
        city = urllib.parse.quote('石家庄')
        data = "province=" + province + "&city=" + city
        # post方法发送请求时，data需要编码
        data = data.encode()
        urllib.request.urlopen('http://127.0.0.1:5000', data=data)
    except Exception as err:
        return err


if __name__ == '__main__':
    print(postMess())
