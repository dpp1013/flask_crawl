'''
服务器任务：读取student.txt文件的学生数据，以表格的形式呈现在网页上
'''
import flask, os

app = flask.Flask(__name__)


@app.route('/')
def writefile():
    if os.path.exists('图像.jpg'):
        st="<img scr='图像.jpg' width='165' height='60' background-color='red'>"
    if os.path.exists('students.txt'):
        st =st+ "<h3>学生信息表</h3>" + "<table border='1' width='300'>"
        file = open('students.txt', 'r', encoding='utf-8')
        while True:
            s = file.readline().strip('\n')
            if s == '':
                break
            s = s.split(',')
            print(s)
            st = st + '<tr>'
            for i in range(len(s)):
                st = st + "<td>" + s[i] + "</td>"
            st = st + '</tr>'
        file.close()
        st = st + "</table>"
        return st
    else:
        return '文件不存在'


if __name__ == '__main__':
    app.run()
