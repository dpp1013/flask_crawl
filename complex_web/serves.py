import flask

app = flask.Flask(__name__)


def getFile(fileName):
    try:
        file = open(fileName, 'rb')
        data = file.read()
        file.close()
        return data
    except Exception as err:
        return ""


# 初始页面
@app.route('/')
def index():
    return getFile('books.html')


# 跳转页面
@app.route('/<name>', methods=['GET'])
def page(name):
    data = ''
    if name != '':
        data = getFile(name)
    return data


if __name__ == '__main__':
    app.run()
