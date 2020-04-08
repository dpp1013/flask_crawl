import urllib.request
import urllib.parse
import os

'''
上传文件到服务器
'''


def upfile():
    url = 'http://127.0.0.1:5000/upload'
    fileName = input('Enter the file:')
    if os.path.exists(fileName):
        fobj = open(fileName, 'rb')
        data = fobj.read()
        fobj.close()
        p = fileName.rfind('\\')  # 返回字符串最后出现的位置，即找到\最后出现的位置
        fileName = fileName[p + 1:]
        print('准备上传：' + fileName)
        headers = {'content-type': 'application/octet-stream'}
        purl = url + '?fileName=' + urllib.parse.quote(fileName)
        req = urllib.request.Request(purl, data, headers)  # 声明一个Request对象，这个Request对象包含了url，data，headers
        msg = urllib.request.urlopen(req)  # 传递给服务器，获得服务器返回的msg
        msg = msg.read().decode()  # 检验是否上传成功
        if msg == 'ok':
            print('上传成功:', len(data), '字节')
        else:
            print(msg)
    else:
        print('文件不存在！')


if __name__ == '__main__':
    upfile()
