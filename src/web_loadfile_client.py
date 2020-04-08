import urllib.parse
import urllib.request

url = 'http://127.0.0.1:5000'
if __name__ == '__main__':
    try:
        html = urllib.request.urlopen(url)
        html = html.read()
        fileName = html.decode()
        print('准备下载:' + fileName)
        urllib.request.urlretrieve(url + '?fileName=' + urllib.parse.quote(fileName))  # 直接下载文件
        data = urllib.request.urlopen(url + '?fileName=' + urllib.parse.quote(fileName))  # 通过打开读取文件进行下载
        data = data.read()
        # 写入要下载的文件
        fobj = open('download' + fileName, 'wb')
        fobj.write(data)
        fobj.close()
        print('下载完毕：', len(data), '字节')
    except Exception as err:
        print(err)
