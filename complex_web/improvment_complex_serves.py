'''
由于上一个例子中web网站是本地的，因此下载图片非常快，实际中web网站是一个远程的服务器，由于网络原因下载速度很慢
为了模拟这个过程我们修改了服务器
模拟真实的场景
'''
import flask
import os
import random
import time

app = flask.Flask(__name__)


def getFile(name):
    if os.path.exists(name):
        file = open('name', 'rb')
        data = file.read()
        file.close()
        time.sleep(random.randint(1,10))
        return data
    else:
        return ""


@app.route('/')
def index():
    return getFile('books.html')


@app.route('/<name>', methods=['GET'])
def file(name):
    data = ''
    if name != '':
        data = getFile(name)
    return data


if __name__ == '__main__':
    app.run()
