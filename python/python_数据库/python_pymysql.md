# Python之pymysql数据库操作

## **pymysql介绍及安装**

### 01 pymysql介绍

MySQL应该说是如今使用最为普遍的数据库了，没有之一，而Python作为最为流行的语言之一，自然少不了与MySQL打交道，其中`PyMySQL`就是使用最多的工具库。

- PyMySQL是一个纯Python写的MySQL客户端，可以在CPython、PyPy、IronPython和Jython环境下运行；
- PyMySQL的性能和MySQLdb几乎相当，如果对性能要求 不是特别的强，使用PyMySQL将更加方便；
- PyMySQL的使用方法和MySQLdb几乎一样；

### **02 pymysql安装**[#](https://www.cnblogs.com/x1you/p/12848961.html#02-pymysql安装)

**方式一：使用命令\**安装\****

> **pip install pymysql**

**方式二：PyCharm内部安装**

[![YnNSV1.png](https://s1.ax1x.com/2020/05/08/YnNSV1.png)](https://s1.ax1x.com/2020/05/08/YnNSV1.png)

**导入模块：**

> import pymysql

## **pymysql流程及模块说明**

### 01 pymysql操作流程

1. 导入pymysql；
2. 建立数据库连接：使用pymysql的connect()方法连接数据，返回连接对象；
3. 使用连接对象创建游标对象（用于操作sql）;
4. 准备写sql语句（select * from student）;
5. 使用游标对象执行sql;
6. 查询数据使用游标获取;
7. 关闭游标（先）和数据库连接（后）。

[![YnNi8O.png](https://s1.ax1x.com/2020/05/08/YnNi8O.png)](https://s1.ax1x.com/2020/05/08/YnNi8O.png)

### 02 pymysql模块说明

#### ****▌Connection对象\****

**表示**：`conn=connect(参数列表)`

**作用**：用于建立与数据库的连接；

**创建对象：**调用connect()方法；

**参数列表：**

- host：连接的mysql主机，如本机是'localhost'；
- port：连接的mysql主机的端口，默认是3306；
- database：数据库的名称；
- user：连接的用户名；
- password：连接的密码；
- charset：通信采用的编码方式，推荐使用utf8；

#### ****▌对象的方法\****

对象方法如下：

- close()：关闭连接；
- commit()：提交；
- cursor()：返回Cursor对象，用于执行sql语句并获得结果；
- execute(operation [, parameters ])：执行语句，返回受影响的行数，主要用于执行insert、update、delete语句，也可以执行create、alter、drop等语句；
- fetchone()：执行查询语句时，获取查询结果集的第一个行数据，返回一个元组；
- fetchall()：执行查询时，获取结果集的所有行，一行构成一个元组，再将这些元组装入一个元组返回；
- 关于pymysql防注入，字符串拼接查询，容易造成注入，为了避免注入，使用pymysql提供的参数化语句;

#### **▌Cursor对象**

游标（cursor）就是游动的标识,通俗的说，一条sql取出对应n条结果资源的接口/句柄，就是游标，沿着游标可以一次取出一行。

- 用于执行sql语句，使用频度最高的语句为select、insert、update、delete；
- 获取Cursor对象：调用Connection对象的cursor()方法:`cs1=conn.cursor()`

#### **▌对象的属性**

- rowcount只读属性，表示最近一次execute()执行后受影响的行数；
- connection获得当前连接对象；

## **pymysql语法基础**

### 01 代码示例

```python
import pymysql
from pymysql.cursors import DictCursor # 查询到的数据以字典形式存在
# 连接数据库
conn = pymysql.connect(host='127.0.0.1', user='ITester', password='123456',
                       database='ITester', charset='utf8')
# 创建游标
cursor = conn.cursor(cursor=DictCursor)
# 执行sql语句
sql = 'select * from user limit 3;'
res = cursor.execute(sql)
# 获取查询结果的1条数据
data = cursor.fetchone()
print(data)
# 关闭游标连接
cursor.close()
# 关闭数据库连接
conn.close()
```

### **02 语法总结**

1. 连接数据库，需要host、user、password、database、charset等信息；

2. 操作数据库先创建游标；

3. 执行指定的sql语句，如果涉及到增、删、改数据库必须要conn.commit()，提交事务

4. 查询获取数据条数有三种方法fetchone、fetchmany、fetchall。
   - cursor.fetchone() ：默认获取查询结果的第一条数据；
   - cursor.fetchmany(2) ：获取查询结果的指定条数，比如获取2条数据；
   - cursor.fetchall() ：获取查询结果的所有数据；

5. 需要注意的是，fetch获取的数据默认是元组，如果想要字典类型，

   ```python
   cursor=pymysql.cursors.DictCursor；
   ```

6. 先关闭游标，后关闭数据库连接；

## **封装数据库类**

### 01 封装说明

在实际项目中，很多地方都有用到数据库的操作，所以需要将数据库相关操作进行封装，方便其他模块调用。

如下，在common目录下，新建文件db_handler.py 用于封装数据库操作。

[![YnNmVI.png](https://s1.ax1x.com/2020/05/08/YnNmVI.png)](https://s1.ax1x.com/2020/05/08/YnNmVI.png)

**db_handler.py**

```python
import pymysql
class DBHandler:
    def __init__(self,host,port,user,password,
                 database,charset,**kwargs):
        # 连接数据库服务器
        self.conn = pymysql.connect(host=host, port=port, user=user,password=password,
                                    database=database,cursorclass=pymysql.cursors.DictCursor,
                                    charset=charset,**kwargs)
        # 获取游标
        self.cursor = self.conn.cursor()
    
    def query(self, sql, args=None,one=True):
        self.cursor.execute(sql, args)
        # 提交事务
        self.conn.commit()
        if one:
            return self.cursor.fetchone()
        else:
            return self.cursor.fetchall()
    def close(self):
        self.cursor.close()
        self.conn.close()
if __name__ == "__main__":
    db = DBHandler(host='127.0.0.1', port=3306,
                   user='ITester', password='123456',
                   database='ITester', charset='utf8')
    sql = 'select * from user limit 1;'
    data = db.query(sql)
    print(data)
```

总结：本文主要介绍pymysql安装、操作流程、语法基础及封装操作数据库类。

## 还可以这样写

```python
sql = 'insert into %s(%s) values(%s)'
fields = ",".join(item.keys()) # 字段
field_placeholds = ",".join(['%%(%s)s' % key for key in item]) # 字段站位符
cursor.execute(sql % (table_name,fields,field_placeholds),item)

# sql % (table_name,fields,field_placeholds) == 
# insert into t_book(id,name,age) values(%(id)s,%(name)s,%(age)s)
```

