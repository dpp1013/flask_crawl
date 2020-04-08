### Web学生管理程序约定
1. 学号No，姓名Name，性别Sex，年龄Age

2. 服务器的作用是建立与维护一个Sqllite的学生数据库Student.db中的学生记录表students：

       ` create table student
            (No varchar(16) primary key,
             Name varchar(16),
             Sex varchar(8),
             Age int)`
   服务器建立一个web网站，同时提供查询学生记录、增加学生记录、删除学生记录等
   接口服务。服务器为了与客户端通讯，建立一个opt的参数如下表：
   
   |opt值|含义|
   |----|----|
   |init|初始化学生表|
   |insert|增加学生|
   |delete|删除学生|
   | |获取学生记录|

3. SQLite 是一个软件库，实现了自给自足、无服务器的、零配置的、事务性的SQL
数据库引擎。SQLite是在世界上最广泛部署的SQL数据库引擎。

数据库引擎是将查询语句转化为对数据库的操作。实现了对用户的一个接口，不同的语言
用不同的引擎。
 