'''
爬取服务器中的table表
'''
import urllib.request
import urllib.parse
import re
import sqlite3


# urllib.request.urlretrieve(filename=)

def readHtml():
    '''
    :return: table
    '''
    try:
        url = 'http://127.0.0.1:5000'
        html = urllib.request.urlopen(url)
        html = html.read().decode()
        m = re.search(r"<tr>", html)  # 一行开始tr
        n = re.search(r"</tr>", html)  # 一行结束/tr
        while m != None and n != None:
            row = html[m.end():n.start()]
            a = re.search(r'<td>', row)  # 一个td开始
            b = re.search(r'</td>', row)  # 一个/td结束
            while a != None and b != None:
                s = row[a.end():b.start()]  # 一个td的值
                print(s, end='\t')
                row = row[b.end():]
                a = re.search(r'<td>', row)  # 继续搜索td
                b = re.search(r'</td>', row)
            print()  # 搜索完毕之后换行
            html = html[n.end():]
            m = re.search(r"<tr>", html)  # 继续搜索下一行tr
            n = re.search(r"</tr>", html)
    except Exception as err:
        print(err)


if __name__ == '__main__':
    readHtml()
