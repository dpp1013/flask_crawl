import urllib.request
import urllib.parse
import json


class Student:
    def __init__(self, No, Name, Sex, Age):
        self.No = No
        self.Name = Name
        self.Sex = Sex
        self.Age = Age

    def show(self):
        print('%-16s %-16s %-8s %-4d' % (self.No, self.Name, self.Sex, self.Age))


# 列举所有学生
def listStudent():
    global students
    print('%-16s %-16s %-8s %-4s' % ('No', 'Name', 'Sex', 'Age'))
    for s in students:
        s.show()


# 插入学生s
def insertStudent(s):
    global students
    i = 0
    while (i < len(students) and s.No > students[i].No):
        i = i + 1
        if (i < len(students) and s.No == students[i].No):
            print(s.No + 'already exists')
            return False
        students.insert(i, s)
        print('测试')
        return True


# 删除学生
def deleteStudent():
    global students
    No = input('Enter No=')
    if (No != ""):
        for i in range(len(students)):
            if (students[i].No == No):
                st = ''
                try:
                    st = 'No=' + urllib.parse.quote(No)
                    st = st.encode()
                    content = urllib.request.urlopen(url + '?opt=delete', st)
                    st = content.read()
                    st = json.load(st.decode())  # 请求回来的是json数据
                    st = st['msg']
                except Exception as err:
                    st = str(err)
                if (st == 'ok'):
                    del students[i]
                    print('删除成功')
                else:
                    print(st)
                break


# 插入员工
def insertRaw():
    No = input('No=')
    Name = input('Name=')
    while True:
        Sex = input('Sex=')
        if Sex == '男' or Sex == '女':
            break
        else:
            print('Sex is not valid')
    Age = input('Age=')
    if (Age == ""):
        Age = 0
    else:
        Age = int(Age)
    if No != "" and Name != "":
        s = Student(No, Name, Sex, Age)
        if len(students) == 0:
            print('测试1')
            insertStudent(s)
            print('新增成功')
        for x in students:
            # print('测试2')
            # print(x)
            if x.No == No:
                print(No + 'already exists')
                return
            else:
                st = ''
                try:
                    st = 'No=' + urllib.request.quote(No) + '&Name=' + urllib.request.quote(Name) + \
                         '&Sex=' + urllib.request.quote(Sex) + '&Age=' + urllib.request.quote(Age)
                    st = st.encode()
                    content = urllib.request.urlopen(url + '?opt=insert', st)
                    st = content.read()
                    st = json.loads(st.decode())
                    print('测试2')
                    print(st)
                    st = st['msg']
                except Exception as err:
                    st = str(err)
                if (st == 'ok'):
                    insertStudent(s)
                    print('增加成功')
                else:
                    print(st)
    else:
        print('学号、姓名不能为空')


# 初始化
def initalize():
    st = ''
    try:
        content = urllib.request.urlopen(url + '?opt=init')
        st = content.read()
        st = json.loads(st.decode())  # json格式
        st = st['msg']
    except Exception as err:
        st = str(err)
    if (st == 'ok'):
        print('初始化成功')
    else:
        print(st)
    return st


def readStudent():
    global students
    try:
        students.clear()
        content = urllib.request.urlopen(url)
        data = b''
        while True:
            # 一次读1024个
            buf = content.read(1024)
            if (len(buf) > 0):
                data = data + buf
            else:
                break
            data = json.loads(data.decode())  # 将字符串变成Json格式
            if data['msg'] == 'ok':
                data = data['data']
                for d in data:
                    s = Student(d['No'], d['Name'], d['Sex'], d['Age'])
                    students.append(s)
    except Exception as err:
        print(err)


if __name__ == '__main__':
    students = []
    url = 'http://127.0.0.1:5000'
    try:
        readStudent()
        while True:
            print("")
            print('***学生名单***')
            print('0.初始化学生表')
            print('1.查看学生表')
            print('2.增加学生表')
            print('3.删除学生表')
            print('4.退出这个程序')
            s = input('请选择(0,1,2,3,4):')
            if (s == "0"):
                initalize()
            elif s == '1':
                listStudent()
            elif s == '2':
                insertRaw()
            elif s == '3':
                deleteStudent()
            elif s == '4':
                break
    except Exception as err:
        print(err)
