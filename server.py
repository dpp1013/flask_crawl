from flask import Flask
from flask import request, jsonify, render_template
import flask

app = Flask(__name__)

'''
获取服务器的参数1：从query中获取参数
'''


@app.route('/helloworld', methods=['GET'])
def hello_world():
    a = request.args.get('a')
    b = request.args.get('b')
    return jsonify({'result': int(a) + int(b)})


'''
获取服务器的参数2：从请求头header中获取参数
'''


@app.route('/v1/readhearder', methods=['GET'])
def api1():
    return jsonify(request.headers.get('User-Agent'))


'''
获取服务器的参数3：从请求体中获取参数
'''


@app.route('/v1/addUser', methods=['POST'])
def api2():
    user = request.json
    print(user['username'])
    print(user['password'])
    return user


'''
获取服务器的参数4.从url的path中获取参数
'''


@app.route('/hello/<name>/')
def api3(name):
    '''
    :param name:
    :return: 将path获取的参数，显示到网页上
    '''
    return render_template('hello.html', name=name)


@app.route('/')
def getindex():
    '''
    服务器对与客户端以get方式发送的请求，接受该请求的方式
    '''
    try:
        province = flask.request.args.get('province') if "province" in flask.request.args else ""
        city = flask.request.args.get('city') if "city" in flask.request.args else ""
        return province + ',' + city
    except Exception as err:
        return str(err)


@app.route('/postExample', methods=['GET', 'POST'])
def postindex():
    try:
        province = flask.request.form.get('province') if 'province' in flask.request.form else ""
        city = flask.request.form.get('province') if 'city' in flask.request.form else ""
        return province + "," + city
    except Exception as err:
        return str(err)


@app.route('/mix', methods=['POST'])
def mix():
    try:
        province = flask.request.args.get('province') if "province" in flask.request.args else ""
        city = flask.request.args.get('city') if "city" in flask.request.args else ""
        note = flask.request.form.get('note') if 'note' in flask.request.form else ""
        return 'province=' + province + 'city=' + city + 'note=' + note
    except Exception as err:
        return str(err)


if __name__ == '__main__':
    app.run()
