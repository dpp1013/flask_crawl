import flask

app = flask.Flask(__name__)
'''
上传文件：在服务器端获取上传文件的文件名
'''


@app.route('/upload', methods=["POST"])
def uploadFile():
    msg = ''
    try:
        if 'fileName' in flask.request.values:
            fileName = flask.request.values.get('fileName')  # 得到request请求中要上传的文件名
            data = flask.request.get_data()  # get_data 获取完全没有经过任何改变过的纯的二进制数据的方法
            fobj = open('upload' + fileName, 'wb')  # 打开服务器中要写入的文件
            fobj.write(data)  # 将request中的data写入打开的文件
            fobj.close()
            msg = 'ok'
        else:
            msg = '没有按要求上传文件'
    except Exception as err:
        print(err)
        msg = str(err)
    return msg


if __name__ == '__main__':
    app.run()
