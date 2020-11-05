# pymysql 

```python
# pip install pymysql

import pymysql

db = pymysql.connect(host='192.168.0.107', user='ybytest', password='*****', database='ybytest')

with db.cursor() as cursor:
    cursor.execute('select * from main')
    db.commit()
    print(cursor.fetchall())
    db.close()

# 这两种都可以 但是在pymysql。connect() 不能用with ,如果用with 那么db直接就是cursor(),with 方法是找__enter__ 文件的，可以去enter文件里看，返回的是self.cursor().
    
'''
cursor = db.cursor()
cursor.execute('select * from main')
db.commit()
cursor.close()
print(cursor.fetchall())
db.close()
'''




```

# sql注入

```python
import pymysql,hashlib

user = input('请输入姓名')
password = input('请输入密码')

h = hashlib.md5()
h.update(password.encode('utf8'))
password = h.hexdigest()


db = pymysql.connect(host='192.168.0.107', user='ybytest', password='970829', database='ybytest')

with db.cursor() as cursor:
    sql = 'select * from main where name="%s" and password="%s"' % (user ,password)
    cursor.execute(sql)
    db.commit() 
    print(cursor.fetchall())
    db.close()

# 用户名输入 zhangsan"# 密码随便 就会查出所有用户信息。 mysql #号后面都是注释
# 现在都用 cursor.execute(sql,(user,password)) 别人给你处理数据就不会出现sql注入了


```

# redis

- ```python
  import redis
  
  client = Redis() # host='localhost' ，可以加用户密码自己上网查
  
  client.get('name')
  
  client.set('name','zhazha')
  
  # redis里能用的指令都可以在这里使用
  
  # redisdoc.com 指令地址
  ```

  

# mongodb

- ```python
  impport pymongo  from  MongoClient
  
  client = MongoClient(host="localhost",port="27017")
  
  db = client.数据库
  
  cursor = db.表.find()
  
  for i in cursor
  	print(i)
  ```

  