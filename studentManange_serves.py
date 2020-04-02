import flask
import os, json
import sqlite3

app = flask.Flask(__name__)


class StudentDB:
    def openDB(self):
        self.con = sqlite3.connect(':memory:')  # 连接数据库
        self.cursor = self.con.cursor()  # 获取游标

    def closeDB(self):
        self.con.commit()
        self.con.close()

    def initTable(self):
        res = {}
        try:
            self.cursor.execute(
                "create table student (No varchar(16) primary key,Name varchar(16),Sex varchar(8),Age int)")
            res['msg'] = 'ok'
        except Exception as err:
            res['msg'] = str(err)
        return res

    def insertRow(self, No, Name, Sex, Age):
        res = {}
        try:
            self.cursor.execute("insert into student(No,Name,Sex,Age) values (?,?,?,?)", (No, Name, Sex, Age))
            res['msg'] = 'ok'
        except Exception as err:
            res['msg'] = str(err)
        return res

    def deleteRow(self, No):
        res = {}
        try:
            self.cursor.execute("delete from student where No=?", (No,))
            res['msg'] = 'ok'
        except Exception as err:
            res['msg'] = str(err)
        return res

    def selectRow(self):
        res = {}
        try:
            data = []  # 记录下来
            self.cursor.execute("select * from student order by No")
            rows = self.cursor.fetchall()  # fetchall()接收全部的返回结果行
            for row in rows:
                d = {}
                d['No'] = row[0]
                d['Name'] = row[1]
                d['Sex'] = row[2]
                d['Age'] = row[3]
                data.append(d)
            res['msg'] = 'ok'
        except Exception as err:
            res['msg'] = str(err)
        return res


@app.route('/', methods=['GET', 'POST'])
def process():
    # 获取操作
    opt = flask.request.values.get('opt') if 'opt' in flask.request.values else ""
    res = {}
    db = StudentDB()
    db.openDB()  # 初始化数据库，进行数据库的连接，设置游标
    if opt == 'init':
        res = db.initTable()
    elif opt == 'insert':
        No = flask.request.values.get('No') if 'No' in flask.request.values.get else ""
        Name = flask.request.values.get('Name') if 'Name' in flask.request.values.get else ""
        Sex = flask.request.values.get('Sex') if 'Sex' in flask.request.values.get else ""
        Age = flask.request.values.get('Age') if 'Age' in flask.request.values.get else ""
        res = db.insertRow(No, Name, Sex, Age)
    elif opt == 'delete':
        No = flask.request.values.get('No') if 'No' in flask.request.values.get else ""
        res = db.deleteRow(No)
    else:
        res = db.selectRow()
    db.closeDB()
    return json.dumps(res)  # dumps 将字典转化为str


if __name__ == '__main__':
    app.run()
