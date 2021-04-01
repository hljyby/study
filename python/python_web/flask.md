# Flask数据的增删改查(CRUD)

数据的查询

```python

all():查询全部的数据,其结果是一个列表，每一个元素都是一个对象
    students = Student.query.all()
 
过滤查询:
    第一种:filter,结果是baseQuery objects,
    过滤条件的格式:对象.属性==值
    studnets = Student.query.filter(Student.id==1)
    第二种:filter_by,结果是baseQuery objects,可以进行遍历
    students = Student.query.filter_by(id=1)
    第三种:原生sql查询id=1的信息，结果是一个可以遍历的对象
    sql = 'select * from student where id=1;'
    students = db.session.execute(sql)
    
模糊查询:
    语法:filter(模型名.属性.运算符('xx'))
    运算符:
        contains：包含
        startswith：以什么开始
        endswith：以什么结束
        in_：在范围内
        like：模糊
        __gt__: 大于
        __ge__：大于等于
        __lt__：小于
        __le__：小于等于
        
例子:
# 模糊查询，查询姓名中包含小花的学生信息
# django中filter(s_name__contains='小花')
    students = Student.query.filter(Student.s_name.contains('小花'))
    
# 以什么开始
    students = Student.query.filter(Student.s_name.startswith('小'))
    
 # 以什么结束
    students = Student.query.filter(Student.s_name.endswith('1'))
    
# 查询年龄大于等于16的学生信息
    students = Student.query.filter(Student.s_age.__gt__(15))
    
# 查询id在10到20之间的学生的学生信息
    students = Student.query.filter(Student.s_age.in_([10,11,12]))
# 查询年龄小于17的学生信息
    Student.query.filter(Student.s_age < 17)
    students = Student.query.filter(Student.s_age.__lt__(17))
        
# 模糊查询，使用like，查询姓名中第二位为花的学生信息
# like '_花%',_代表必须有一个数据，%任何数据
    students = Student.query.filter(Student.s_name.like('_花%'))
        
    
筛选:
 
offset()
    # 跳过3个数据
    stus = Student.query.offset(3)
 
limit()
    # 跳过3个数据，查询5个信息
    stus = Student.query.offset(3).limit(5)
 
order_by()
    # 按照id降序,升序
    students = Student.query.order_by('id')
    students = Student.query.order_by('-id')
 
    students = Student.query.order_by(desc('id'))
    students = Student.query.order_by(asc('id'))
 
    students = Student.query.order_by('id desc')
    students = Student.query.order_by('id asc')
 
get()
    #使用get，获取id=1的学生对象,get()默认接收id
    # 拿不到值不会报错，返回空
    students = Student.query.get(4)
 
first()
    # 获取年龄最大的一个
    stus = Student.query.order_by('-s_age').first()
 
    
逻辑运算
    与
	    and_
	    filter(and_(条件),条件…)
    
    或
    	or_
    	filter(or_(条件),条件…)
    
    非
    	not_
    	filter(not_(条件),条件…)
 
例子：
and_  
    students = Student.query.filter(Student.s_age==16,
                                    Student.s_name.contains('花'))
 
    students = Student.query.filter(and_(Student.s_age==16,
                                    Student.s_name.contains('花')))
 
not_
    students = Student.query.filter(or_(Student.s_age==16,
                                    Student.s_name.contains('花')))
or_
    students = Student.query.filter(not_(Student.s_age==16),
                                    Student.s_name.contains('花'))
 
    
    
注意: 
1. fliter和filter_by的结果可遍历
2. 可以通过对其结果使用all()方法将其转换成一个列表或者first()转换成objects对象。
3. all()获得的是列表，列表没有first()方法
4. fliter和filter_by有flrst()方法，没有last方法
```

数据的添加

在flask中修改数据后需要添加事务和提交事务

```python
事务: 完整，一致，持久，原子
第一种:保存数据
将数据放入缓存
db.session.add(stu)
将缓存中的数据提交
db.session.commit()xxxxxxxxxx 事务: 完整，一致，持久，原子第一种:保存数据将数据放入缓存db.session.add(stu)将缓存中的数据提交db.session.commit()事务: 完整，一致，持久，原子第一种:保存数据将数据放入缓存db.session.add(stu)将缓存中的数据提交db.session.commit()
```

在学生表中添加数据

```python

@blue.route('/createstu/')
def create_stu():
    s = Student()
    s.s_name = '小花'
    s.s_age = 19
 
    db.session.add(s)
    db.session.commit()
 
    return '添加成功'
    
提交事务，使用commit提交我们的添加数据的操作
```

批量创建数据

```python

批量添加数据时可以使用add()、add_list()添加事务
add():
     db.session.add_all(stu)
     db.session.commit()
stu是一个对象
     
     
add_list()：
    db.session.add_all(stus_list)
            db.session.commit()
stus_list是一个列表，其每个元素都是一个对象
```

第一种

```python

@app_blue.route('create_many_stu/',methods=['GET'])
def create_many_stu():
if request.method == 'GET':
    stu = Student()
    stus_list = []
    for i in range(5):
        stu = Student()
        stu.s_name = '小花%s' % random.randrange(10, 1000)
        stu.s_age = random.randint(10,20)
        stus_list.append(stu)
 
    db.session.add_all(stus_list)
    db.session.commit()
        # db.session.add(stu)
    # db.session.commit
    return '批量创建'
    
db.session.add_all(stus_list)
db.session.commit()
将列表中的数据统一添加到缓存区中，并提交
```

第二种

```python

第二种:重写init
 
models中:
 
def __init__(self, name, age):
    # 2，给对象赋值
    self.s_name = name
    self.s_age = age
 
 
views中:
@app_blue.route('create_many_stu_init/',methods=['GET'])
def create_many_stu():
    if request.method == 'GET':
        stus_list = []
        for i in range(5):
            stu = Student('小花%s' % random.randrange(10,1000), random.randint(10,20))
            stus_list.append(stu)
 
        db.session.add_all(stus_list)
        db.session.commit()
 
            # db.session.add(stu)
        # db.session.commit
        return '批量创建成功'
```

修改数据

```python
思路:获取到需要修改的对象，通过对象.属性的方式将属性重新赋值，然后使用commit提交事务

```

写法1

```python

students = Student.query.filter_by(s_id=3).first()
 
students.s_name = '哈哈'
 
db.session.commit()
```

写法2

```python

Student.query.filter_by(s_id=3).update({'s_name':'娃哈哈'})
 
db.session.commit()
```

删除数据

```python

格式:db.session.delete(对象)
     db.session.commit()
     
注意:在修改数据(增删改)中如果使用commit()的话，只会修改本地缓存中的数据，数据库中的数据不会更新。
必须使用:db.session.commit()
```

写法1

```python

students = Student.query.filter_by(s_id=2).first()
db.session.delete(students)
db.session.commit()
```

写法2

```python

students = Student.query.filter_by(s_id=1).all()
db.session.delete(students[0])
db.session.commit()
```

```python

模型
和Django的区别:
    a. 模型中不定义数据库的表名:
        在django中默认表名为:'应用appming_模型名小写'
        在flask中默认的表名为:模型名的小写
    b. 主键自增字段:
        django中会默认创建自增的主键id
        flask中需要手动创建自增的id: id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    c.查询所有数据的结果all()
        在django结果中查询的结果是QuerySet
        在flask中查询结果是List
    d.查询满足条件的数据的结果，filter()
        在django查询结果是QuerySet
        在flask中查询结果是baseQuery objects
```

# [flask-sqlalchemy用法详解](https://www.cnblogs.com/aibabel/p/11571196.html)

## 一. 安装

```
$ pip install flask-sqlalchemy
```

## 二. 配置

配置选项列表 :

| 选项                      | 说明                                                         |
| ------------------------- | ------------------------------------------------------------ |
| SQLALCHEMY_DATABASE_URI   | 用于连接的数据库 URI 。例如:sqlite:////tmp/test.db 或 mysql://username:password@server/db |
| SQLALCHEMY_BINDS          | 一个映射 binds 到连接 URI 的字典。更多 binds 的信息见 用 Binds 操作多个数据库 。 |
| SQLALCHEMY_ECHO           | 如果设置为 Ture ， SQLAlchemy 会记录所有 发给 stderr 的语句，这对调试有用。 |
| SQLALCHEMY_RECORD_QUERIES | 可以用于显式地禁用或启用查询记录。查询记录 在调试或测试模式自动启用。更多信息见 get_debug_queries() 。 |

SQLALCHEMY_NATIVE_UNICODE | 可以用于显式禁用原生 unicode 支持。当使用 不合适的指定无编码的数据库默认值时，这对于 一些数据库适配器是必须的（比如 Ubuntu 上某些版本的 PostgreSQL ）。|
| SQLALCHEMY_POOL_SIZE | 数据库连接池的大小。默认是引擎默认值（通常 是 5 ） |
| SQLALCHEMY_POOL_TIMEOUT | 设定连接池的连接超时时间。默认是 10 。 |
| SQLALCHEMY_POOL_RECYCLE | 多少秒后自动回收连接。这对 MySQL 是必要的， 它默认移除闲置多于 8 小时的连接。注意如果 使用了 MySQL ， Flask-SQLALchemy 自动设定这个值为 2 小时。|

1.  

   app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI

2.  

   app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True/False # 每次请求结束后都会自动提交数据库中的变动.

3.  

    

4.  

   app.config[""] =

5.  

   app.config[""] =

6.  

   app.config[""] =

7.  

   app.config[""] =

8.  

    

9.  

   DATABASE_URI :

10.  

    mysql : mysql://username:password@hostname/database

11.  

     

12.  

    pgsql : postgresql://username:password@hostname/database

13.  

     

14.  

    sqlite(linux) : sqlite:////absolute/path/to/database

15.  

     

16.  

    sqlite(windows) : sqlite:///c:/absolute/path/to/database

## 三. 初始化示例

1.  

   from flask import Flask

2.  

   from flask_sqlalchemy import SQLAlchemy

3.  

   base_dir = os.path.abspath(os.path.dirname(__file__))

4.  

    

5.  

   app = Flask(__name__)

6.  

    

7.  

   app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')

8.  

   app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True

9.  

    

10.  

    db = SQLAlchemy(app)

## 四. 定义模型

模型 表示程序使用的持久化实体. 在 ORM 中, 模型一般是一个 Python 类, 类中的属性对应数据库中的表.

Flaks-SQLAlchemy 创建的数据库实例为模型提供了一个基类以及一些列辅助类和辅助函数, 可用于定义模型的结构.

1.  

   db.Model # 创建模型,

2.  

   db.Column # 创建模型属性.

模型属性类型 :

| 类型名       | Python类型         | 说明                                                  |
| ------------ | ------------------ | ----------------------------------------------------- |
| Integer      | int                | 普通整数，一般是 32 位                                |
| SmallInteger | int                | 取值范围小的整数，一般是 16 位                        |
| Big Integer  | int 或 long        | 不限制精度的整数                                      |
| Float        | float              | 浮点数                                                |
| Numeric      | decimal.Decimal    | 定点数                                                |
| String       | str                | 变长字符串                                            |
| Text         | str                | 变长字符串，对较长或不限长度的字符串做了优化          |
| Unicode      | unicode            | 变长 Unicode 字符串                                   |
| Unicode Text | unicode            | 变长 Unicode 字符串，对较长或不限长度的字符串做了优化 |
| Boolean      | bool               | 布尔值                                                |
| Date         | datetime.date      | 日期                                                  |
| Time         | datetime.time      | 时间                                                  |
| DateTime     | datetime.datetime  | 日期和时间                                            |
| Interval     | datetime.timedelta | 时间间隔                                              |
| Enum         | str                | 一组字符串                                            |
| PickleType   | 任何 Python 对象   | 自动使用 Pickle 序列化                                |
| LargeBinary  | str                | 二进制文件                                            |

常用 SQLAlchemy 列选项

| 选项名      | 说明                                                         |
| ----------- | ------------------------------------------------------------ |
| primary_key | 如果设为 True，这列就是表的主键                              |
| unique      | 如果设为 True，这列不允许出现重复的值                        |
| index       | 如果设为 True，为这列创建索引，提升查询效率                  |
| nullable    | 如果设为 True，这列允许使用空值；如果设为 False，这列不允许使用空值 |
| default     | 为这列定义默认值                                             |

Flask-SQLAlchemy 要求每个模型都要定义主键, 这一列通常命名为 id .

示例 :

1.  

   class Role(db.Model):

2.  

   __tablename__ = "roles"

3.  

   id = db.Column(db.Integer, primary_key=True)

4.  

   name = db.Column(db.String(64), unique=True)

5.  

    

6.  

   def __repr__(self):

7.  

   """非必须, 用于在调试或测试时, 返回一个具有可读性的字符串表示模型."""

8.  

   return '<Role %r>' % self.name

9.  

    

10.  

    class User(db.Model):

11.  

    __tablename__ = 'users'

12.  

    id = db.Column(db.Integer, primary_key=True)

13.  

    username = db.Column(db.String(64), unique=True, index=True)

14.  

     

15.  

    def __repr__(self):

16.  

    """非必须, 用于在调试或测试时, 返回一个具有可读性的字符串表示模型."""

17.  

    return '<Role %r>' % self.username
    
    **如果使用定义的BaseModel 必须加 tablename 不然生成的表名为basemodel**
    
    **或者在BaseModel 里面加__abstract__ = True**

## 五. 关系

关系型数据库使用关系把不同表中的行联系起来.

常用 SQLAlchemy 关系选项 :

| 选项名        | 说明                                                         |
| ------------- | ------------------------------------------------------------ |
| backref       | 在关系的另一个模型中添加反向引用                             |
| primaryjoin   | 明确指定两个模型之间使用的联结条件。只在模棱两可的关系中需要指定. |
| lazy          | 指定如何加载相关记录。可选值如下 :                           |
|               | select（首次访问时按需加载）                                 |
|               | immediate（源对象加载后就加载）                              |
|               | joined（加载记录，但使用联结）                               |
|               | subquery（立即加载，但使用子查询）                           |
|               | noload（永不加载）                                           |
|               | dynamic（不加载记录，但提供加载记录的查询）                  |
| uselist       | 如果设为 Fales，不使用列表，而使用标量值                     |
| order_by      | 指定关系中记录的排序方式                                     |
| secondary     | 指定多对多关系中关系表的名字                                 |
| secondaryjoin | SQLAlchemy 无法自行决定时，指定多对多关系中的二级联结条件    |

### 1) 一对多

原理 : 在 “多” 这一侧加入一个外键, 指定 “一” 这一侧联结的记录.

示例代码 : 一个角色可属于多个用户, 而每个用户只能有一个角色.

1.  

   class Role(db.Model):

2.  

   \# ...

3.  

   users = db.relationship('User', backref='role')

4.  

    

5.  

   class User(db.Model):

6.  

   \# ...

7.  

   role_id = db.Column(db.Integer, db.ForeignKey('roles.id')) # 外键关系.

8.  

    

9.  

    

10.  

    \###############

11.  

    db.ForeignKey('roles.id') : 外键关系,

12.  

     

13.  

    Role.users = db.relationship('User', backref='role') : 代表 外键关系的 面向对象视角. 对于一个 Role 类的实例, 其 users 属性将返回与角色相关联的用户组成的列表.

14.  

    db.relationship() 第一个参数表示这个关系的另一端是哪个模型.

15.  

    backref 参数, 向 User 模型添加了一个 role 数据属性, 从而定义反向关系. 这一属性可替代 role_id 访问 Role 模型, 此时获取的是模型对象, 而不是外键的值.

### 2) 多对多

最复杂的关系类型, 需要用到第三章表, 即 *关联表* , 这样多对多关系可以分解成原表和关联表之间的两个一对多关系.

查询多对多关系分两步 : 遍历两个关系来获取查询结果.

代码示例:

1.  

   registrations = db.Table("registrations",

2.  

   db.Column("student_id", db.Integer, db.ForeignKey("students.id")),

3.  

   db.Column("class_id", db.Integer, db.ForeignKey("classes.id"))

4.  

   )

5.  

    

6.  

   class Student(db.Model):

7.  

   __tablename__ = "students"

8.  

   id = db.Column(db.Integer, primary_key=True)

9.  

   name = db.Column(db.String)

10.  

    classes = db.relationship("Class",

11.  

    secondary=registrations,

12.  

    backref=db.backref("students", lazy="dynamic"),

13.  

    lazy="dynamic")

14.  

     

15.  

    class Class(db.Model):

16.  

    __tablename__ = "classes"

17.  

    id = db.Column(db.Integer, primary_key=True)

18.  

    name = db.Column(db.String)

多对多关系仍然使用定义一对多关系的 db.relationship() 方法进行定义, 但在多对多关系中, 必须把 secondary 参数设为 关联表.

多对多关系可以在任何一个类中定义, backref 参数会处理好关系的另一侧.

关联表就是一个简单的表, 不是模型, SQLAlchemy 会自动接管这个表.

classes 关系使用列表语义, 这样处理多对多关系比较简单.

Class 模型的 students 关系有 参数 db.backref() 定义. 这个关系还指定了 lazy 参数, 所以, 关系两侧返回的查询都可接受额外的过滤器.

自引用关系
自引用关系可以理解为 多对多关系的特殊形式 : 多对多关系的两边由两个实体变为 一个实体.

高级多对多关系
使用多对多关系时, 往往需要存储所联两个实体之间的额外信息. 这种信息只能存储在关联表中. 对用户之间的关注来说, 可以存储用户关注另一个用户的日期, 这样就能按照时间顺序列出所有关注者.

为了能在关系中处理自定义的数据, 必须提升关联表的地位, 使其变成程序可访问的模型.

关注关联表模型实现:

1.  

   class Follow(db.Model):

2.  

   __tablename__ = "follows"

3.  

   follower_id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)

4.  

   followed_id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)

5.  

   timestamp = db.Column(db.DateTime, default=datetime.utcnow)

6.  

    

7.  

   \# SQLAlchemy 不能直接使用这个关联表, 因为如果这个做程序就无法访问其中的自定义字段. 相反的, 要把这个多对多关系的左右两侧拆分成两个基本的一对多关系, 而且要定义成标准的关系.

使用两个一对多关系实现的多对多关系:

```python
class User(UserMixin, db.Model):
    # ...
    followd = db.relationship("Follow",
                              foreign_keys=[Follow.follower_id],
                              backref=db.backref("follower", lazy="joined"),
                              lazy="dynamic",
                              cascade="all, delete-orphan")
    followrs = db.relationship("Follow",
                              foreign_keys=[Follow.followed_id],
                              backref=db.backref("followed", lazy="joined"),
                              lazy="dynamic",
                              cascade="all, delete-orphan")

# 这段代码中, followed 和 follower 关系都定义为 单独的 一对多关系. 
# 注意: 为了消除外键歧义, 定义关系是必须使用可选参数 foreign_keys 指定的外键. 而且 db.backref() 参数并不是指定这两个关系之间的引用关系, 而是回引 Follow 模型. 回引中的 lazy="joined" , 该模式可以实现立即从连接查询中加载相关对象.
# 这两个关系中, user 一侧设定的 lazy 参数作用不一样. lazy 参数都在 "一" 这一侧设定, 返回的结果是 "多" 这一侧中的记录. dynamic 参数, 返回的是查询对象.
# cascade 参数配置在父对象上执行的操作相关对象的影响. 比如, 层叠对象可设定为: 将用户添加到数据库会话后, 要自定把所有关系的对象都添加到会话中. 删除对象时, 默认的层叠行为是把对象联结的所有相关对象的外键设为空值. 但在关联表中, 删除记录后正确的行为是把执行该记录的实体也删除, 因为这样才能有效销毁联结. 这就是 层叠选项值 delete-orphan 的作用. 设为 all, delete-orphan 的意思是启动所有默认层叠选项, 并且还要删除孤儿记录.
```



### 3) 一对一

可以看做特殊的 一对多 关系. 但调用 db.relationship() 时 要把 uselist 设置 False, 把 多变为 一 .

### 4) 多对一

将 一对多 关系,反过来即可, 也是 一对多关系.

## 六. 数据库操作

### 1) 创建数据库及数据表

创建数据库

```python
db.create_all()
```

示例 :
$ python myflask.py shell
\> from myflask import db
\> db.create_all()

如果使用 sqlite , 会在 SQLALCHEMY_DATABASE_URI 指定的目录下 多一个文件, 文件名为该配置中的文件名.

如果数据库表已经存在于数据库中, 那么 db.create_all() 不会创建或更新这个表.

更新数据库
方法一 :
先删除, 在创建 –> 原有数据库中的数据, 都会消失.

1.  

   \> db.drop_all()

2.  

   \> db.create_all()

方法二 :
数据库迁移框架 : 可以跟自动数据库模式的变化, 然后增量式的把变化应用到数据库中.

SQLAlchemy 的主力开发人员编写了一个 迁移框架 Alembic, 除了直接使用 Alembic wait, Flask 程序还可使用 Flask-Migrate 扩展, 该扩展对 Alembic 做了轻量级包装, 并集成到 Flask-Script 中, 所有操作都通过 Flaks-Script 命令完成.

① 安装 Flask-Migrate
$ pip install flask-migrate

② 配置

1.  

   from flask_migrate import Migrate, MigrateCommand

2.  

    

3.  

   \# ...

4.  

   migrate = Migrate(app, db)

5.  

   manager.add_command('db', MigrateCommand)

③ 数据库迁移
a. 使用 init 自命令创建迁移仓库.
$ python myflask.py db init # 该命令会创建 migrations 文件夹, 所有迁移脚本都存在其中.

1.  

   b. 创建数据路迁移脚本.

2.  

   $ python myflask.py db revision # 手动创建 Alemic 迁移

3.  

   创建的迁移只是一个骨架, upgrade() 和 downgrade() 函数都是空的. 开发者需要使用 Alembic 提供的 Operations 对象指令实现具体操作.

4.  

    

5.  

   $ python myflask.py db migrate -m COMMONT # 自动创建迁移.

6.  

   自动创建的迁移会根据模型定义和数据库当前的状态之间的差异生成 upgrade() 和 downgrade() 函数的内容.

7.  

    

8.  

   ** 自动创建的迁移不一定总是正确的, 有可能漏掉一些细节, 自动生成迁移脚本后一定要进行检查.

9.  

    

10.  

     

11.  

    c. 更新数据库

12.  

    $ python myflask.py db upgrade # 将迁移应用到数据库中.

### 2) 插入行

模型的构造函数, 接收的参数是使用关键字参数指定的模型属性初始值. 注意, role 属性也可使用, 虽然他不是真正的数据库列, 但却是一对多关系的高级表示. 这些新建对象的 id 属性并没有明确设定, 因为主键是由 Flask-SQLAlchemy 管理的. 现在这些对象只存在于 Python 解释器中, 尚未写入数据库.

 

```python
>> from myflask import db, User, Role

>> db.create_all()

>> admin_role = Role(name="Admin")

>> mod_role = Role(name="Moderator")

>> user_role = Role(name="User")

>> user_john = User(username="john", role=admin_role)

>> user_susan = User(username="susan", role=mod_role)

>> user_david = User(username="david", role=user_role)

>> admin_role.name
'Admin'

>> admin_role.id
None

---------

>> db.session.add_all([admin_role, mod_role, user_role, user_john, user_susan, user_david])   # 把对象添加到会话中.
>> db.session.commit()      # 把对象写入数据库, 使用 commit() 提交会话.
```



### 3) 修改行

1.  

   \>> admin_role = "Administrator"

2.  

   \>> db.session.add(admin_role)

3.  

   \>> db.session.commit()

### 4) 删除行

1.  

   \>> db.session.delete(mod_role)

2.  

   \>> db.session.commit()

### 5) 查询行

Flask-SQLAlchemy 为每个模型类都提供了 query 对象.

*获取表中的所有记录*

1.  

   \>> Role.query.all()

2.  

   [<Role u'Admin'>, <Role u'Moderator'>, <Role u'User'>]

3.  

   \>> User.query.all()

4.  

   [<Role u'john'>, <Role u'susan'>, <Role u'david'>]

*查询过滤器*

filter_by() 等过滤器在 query 对象上调用, 返回一个更精确的 query 对象. 多个过滤器可以一起调用, 直到获取到所需的结果.

1.  

   \>> User.query.filter_by(role=user_role).all() # 以列表形式,返回所有结果,

2.  

   \>> User.query.filter_by(role=user_role).first() # 返回结果中的第一个.

filter() 对查询结果过滤，比”filter_by()”方法更强大，参数是布尔表达式

1.  

   \# WHERE age<20

2.  

   users = User.query.filter(User.age<20)

3.  

   \# WHERE name LIKE 'J%' AND age<20

4.  

   users = User.query.filter(User.name.startswith('J'), User.age<20)

查询过滤器 :

| 过滤器      | 说明                                                   |
| ----------- | ------------------------------------------------------ |
| filter()    | 把过滤器添加到原查询上, 返回一个新查询                 |
| filter_by() | 把等值过滤器添加到原查询上, 返回一个新查询             |
| limit()     | 使用是zing的值限制原查询返回的结果数量, 返回一个新查询 |
| offset()    | 偏移原查询返回的结果, 返回一个新查询                   |
| order_by()  | 根据指定条件对原查询结果进行排序, 返回一个新查询       |
| group_by()  | 根据指定条件对原查询结果进行分组, 返回一个新查询       |

查询执行函数 :

| 方法    | 说明                                            |
| ------- | ----------------------------------------------- |
| all()   | 以列表形式返回查询的所有结果                    |
| first() | 返回查询的第一个结果，如果没有结果，则返回 None |

first_or_404() | 返回查询的第一个结果，如果没有结果，则终止请求，返回 404 错误响应 | |
| get() | 返回指定主键对应的行，如果没有对应的行，则返回 None |
get_or_404() | 返回指定主键对应的行，如果没找到指定的主键，则终止请求，返回 404 | |错误响应
| count() | 返回查询结果的数量 |
| paginate() | 返回一个 Paginate 对象，它包含指定范围内的结果 |

### 6) 会话管理, 事务管理

*单个提交*

1.  

   \>> db.session.add(ONE)

2.  

   \>> db.session.commit()

*多个提交*

1.  

   \>> db.session.add_all([LIST_OF_MEMBER])

2.  

   \>> db.session.commit()

*删除会话*

1.  

   \>> db.session.delete(mod_role)

2.  

   \>> db.session.commit()

*事务回滚* : 添加到数据库会话中的所有对象都会还原到他们在数据库时的状态.

```
>> db.session.rollback()
```

## 七. 视图函数中操作数据库

```python
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session["known"] = False
        else:
            session["known"] = True

        session["name"] = form.name.data
        form.name.data = ""             # why empty it ?
        return redirect(url_for("index"))
    return render_template("index.html", current_time=datetime.utcnow(), form=form, name=session.get("name"), known=session.get("known"))
```



## 八. 分页对象 Pagination

### 1. paginate() 方法

paginate() 方法的返回值是一个 Pagination 类对象, 该类在 Flask-SQLAlchemy 中定义, 用于在模板中生成分页链接.

1.  

   paginate(页数[,per_page=20, error_out=True])

2.  

   页数 : 唯一必须指定的参数,

3.  

   per_page : 指定每页现实的记录数量, 默认 20.

4.  

   error_out : True 如果请求的页数超出了返回, 返回 404 错误; False 页数超出范围时返回一个,空列表.

示例代码:

 

```python
@main.route("/", methods=["GET", "POST"])
def index():
    # ...
    page = request.args.get('page', 1, type=int)    # 渲染的页数, 默认第一页, type=int 保证参数无法转换成整数时, 返回默认值.
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(page, per_page=current_app.config["FLASKY_POSTS_PER_PAGE"], error_out=False)

    posts = pagination.items
    return render_template('index.html', form=form, posts=posts,pagination=pagination)
```



### 2. 分页对象的属性及方法:

Flask_SQLAlchemy 分页对象的属性:

| 属性     | 说明                    |
| -------- | ----------------------- |
| items    | 当前分页中的记录        |
| query    | 分页的源查询            |
| page     | 当前页数                |
| prev_num | 上一页的页数            |
| next_num | 下一页的页数            |
| has_next | 如果有下一页, 返回 True |
| has_prev | 如果有上一页, 返回 True |
| pages    | 查询得到的总页数        |
| per_page | 每页显示的记录数量      |
| total    | 查询返回的记录总数      |

在分页对象可调用的方法:

| 方法                                                         | 说明                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| iter_pages(left_edge=2,left_current=2,right_current=5,right_edge=2) | 一个迭代器, 返回一个在分页导航中显示的页数列表. 这个列表的最左边显示 left_edge 页, 当前页的左边显式 left_current 页, 当前页的右边显示 right_currnt 页, 最右边显示 right_edge 页. 如 在一个 100 页的列表中, 当前页为 50 页, 使用默认配置, 该方法返回以下页数 : 1, 2, None, 48,49,50,51,52,53,54,55, None, 99 ,100. None 表示页数之间的间隔. |
| prev()                                                       | 上一页的分页对象                                             |
| next()                                                       | 下一页的分页对象                                             |

### 3. 在模板中与 BootStrap 结合使用示例

使用 Flaks-SQLAlchemy 的分页对象与 Bootstrap 中的分页 CSS, 可以轻松的构造出一个 分页导航.

分页模板宏 _macros.html : 创建一个 Bootstrap 分页元素, 即一个有特殊样式的无序列表.

```python
{% macro pagination_widget(pagination,endpoint) %}
<ul class="pagination">
    <li {% if not pagination.has_prev %} class="disabled" {% endif %}>
        <a href="{% if pagination.has_prev %}{{url_for(endpoint, page=paginatin.page - 1, **kwargs)}}{% else %}#{% endif %}">
            &laquo;
        </a>
    </li>
    {% for p in pagination,.iter_pages() %}
        {% if p %}
            {% if p == pagination.page %}
            <li class="active">
                <a href="{{ url_for(endpoint, page=p, **kwargs) }}">{{p}}</a>
            </li>
            {% else %}
            <li>
                <a href="{{ url_for(endpoint, page = p, **kwargs) }}">{{p}}</a>
            </li>
            {% endif %}
        {% else %}
        <li class="disabled"><a href="#">&hellip;</a> </li>
        {% endif %}
    {% endfor %}
    <li {% if not pagination.has_next %} class="disabled" {% endif%}>
        <a href="{% if paginatin.has_next %}{{ url_for(endpoint, page=pagination.page+1, **kwargs) }}{% else %}#{% endif %}">
            &raquo;
        </a>
    </li>
</ul>
{% endmacro %}
```

导入使用分页导航

```python
{% extends "base.html" %}
{% import "_macros.html" as macros %}
...
<div class="pagination">
    {{ macro.pagination_widget(pagination, ".index")}}
</div>
```

 

## 九. 监听事件

### 1. set 事件

示例代码 :

```python
from markdown import markdown
import bleach

class Post(db.Model):
    # ...
    body = db.Colume(db.Text)
    body_html = db.Column(db.Text)
    # ...

    @staticmethod
    def on_changeed_body(target, value, oldvalue, initiator):
        allowed_tags = ["a", "abbr", "acronym", "b", "blockquote", "code", "em",
                        "i", "li", "ol", "pre", "strong", "ul", "h1", "h2","h3","h4","p"]
        target.body_html = bleach.linkify(bleach.clean(markdown(value, output_format="html"), tags=allowed_tags, strip=True))

db.event.listen(Post.body, "set", Post.on_changeed_body) 
# on_changed_body 函数注册在 body 字段上, 是 SQLIAlchemy "set" 事件的监听程序, 
# 这意味着只要这个类实例的 body 字段设了新值, 函数就会自动被调用. 
# on_changed_body 函数把 body 字段中的文本渲染成 HTML 格式, 
# 结果保存在 body_html 中, 自动高效的完成 Markdown 文本到 HTML 的转换.
```

 

## 十. 记录慢查询.

## 十一. Binds 操作多个数据库

## 十二. 其他

### 1. [ORM 在查询时做初始化操作](http://docs.sqlalchemy.org/en/latest/orm/constructors.html)

当 SQLIAlchemy ORM 从数据库查询数据时, 默认不调用`__init__` 方法, 其底层实现了 Python 类的 `__new__()` 方法, 直接实现 对象实例化, 而不是通过 `__init__` 来实例化对象.

如果需要在查询时, 依旧希望实现一些初始化操作, 可以使用 `orm.reconstructor()` 装饰器或 实现 `InstanceEvents.load()` 监听事件.

```python
# orm.reconstructor
from sqlalchemy import orm

class MyMappedClass(object):
    def __init__(self, data):
        self.data = data

        # we need stuff on all instances, but not in the database.
        self.stuff = []

    @orm.reconstructor
    def init_on_load(self):
        self.stuff = []

# InstanceEvents.load()
from sqlalchemy import event
## standard decorator style

@event.listens_for(SomeClass, 'load')
def receive_load(target, context):
    "listen for the 'load' event"

    # ... (event handling logic) ...
```

 

如果只是希望在从数据库查询生成的对象中包含某些属性, 也可以使用 `property` 实现:

```python
class AwsRegions(db.Model):
    name=db.Column(db.String(64))
    ...

    @property
    def zabbix_api(self):
        return ZabbixObj(zabbix_url)

    @zabbix_api.setter
    def zabbix_api(self):
        raise ValueError("zabbix can not be setted!")
```

本文实例讲述了Flask框架钩子函数功能与用法。分享给大家供大家参考，具体如下：

**在Flask中钩子函数是使用特定的装饰器的函数。为什么叫做钩子函数呢，是因为钩子函数可以在正常执行的代码中，插入一段自己想要执行的代码，那么这种函数就叫做钩子函数。**

- `before_first_request`:Flask项目第一次部署后会执行的钩子函数。
- `before_request`:请求已经到达了Flask，但是还没有进入到具体的视图函数之前调用。一般这个就是在函数之前，我们可以把一些后面需要用到的数据先处理好，方便视图函数使用。

**before_request**

```python
@app.before_first_request
def first_request():
  print('只有在处理第一次请求之前执行')
@app.before_request
def before_request():
  print('在视图函数执行之前执行')
```

**context_rocessor**

只用这个钩子函数，必须返回一个字典。这个字典的值在所有模板中都可以使用。这个钩子函数的作用是，如果一些在很多模板中都要用到的变量，那么就可以使用这个钩子函数来返回，而不是在每个视图函数汇总的render_template中去写，这样可以让代码更加简洁和好维护。

```python
@app.context_processor
def context_processor():
  return {{'current_user':'xxx'}}
```

**errorhandler**

在发生异常的时候，比如404，500错误，自定义错误的页面，在errorhangdler装饰的钩子函数下：

> \1. 要返回状态码
>
> \2. 必须写一个参数，来接受错误的信息

使用flask.abort可以手动的抛出相应的错误，比如开发者发现参数不正确的时候可以手动的抛出一个404错误。

```python
@app.errorhandler(500)
def server_error(error):
  return render_template('500.html'),500
@app.errorhandler(404)
def page_not_found(error):
  return render_template('404.html'),404

```

# 应用到蓝图上的钩子函数

```python
总结
钩子函数分为应用钩子函数 以及蓝图钩子函数

应用钩子函数 4个
app.before_first_request
app.before_request
app.after_request
app.teardown_request
蓝图钩子函数 7个
blue.before_app_first_request
blue.before_app_request
blue.before_request
blue.after_request
blue.after_app_request
blue.teardown_app_request
blue.teardown_request
在不发生错误的前提下, blue.before_app_first_request / blue.before_app_request / blue.before_request / blue.after_request / blue.after_app_request 都可以返回响应
```

# g 全局变量 传递参数

```
在钩子函数内通过验证了，把user_id 赋值给g 在后续视图中可以使用
g 的生命周期是这一个请求
request 类似
```

# 七牛云

```python
# 上传七牛云本地的图片 查看官方sdk 实例就有
上传前端传过来的二进制图片数据就得 put_data(token,key,FileStorage.read())
# FileStorage = request.files.get('phone') # FileStorage
# FileStorage.read() # 二进制文件
# FileStorage.save() # 保存
```

# Redis

```python
# pip install redis
# pip install flask-caching

# 在exts里 初始化
cache = Cache()

# 在 create_app函数里添加到app实例里
config = {
	'CACHE_TYPE':'redis',
	'CACHE_REDIS_HOST':'127.0.0.1',
	'CACHE_REDIS_PORT':6379

}
cache.init_app(app=app,config=config)
```

# Restful API规范

`restful api`是用于在前端与后台进行通信的一套规范。使用这个规范可以让前后端开发变得更加轻松。以下将讨论这套规范的一些设计细节。

### 协议：

采用`http`或者`https`协议。

### 数据传输格式：

数据之间传输的格式应该都使用`json`，而不使用`xml`。

### url链接：

url链接中，不能有动词，只能有名词。并且对于一些名词，如果出现复数，那么应该在后面加`s`。

比如：获取文章列表，应该使用`/articles/`，而不应该使用/get_article/

### HTTP请求的方法：

1. `GET`：从服务器上获取资源。
2. `POST`：在服务器上新创建一个资源。
3. `PUT`：在服务器上更新资源。（客户端提供所有改变后的数据）
4. `PATCH`：在服务器上更新资源。（客户端只提供需要改变的属性）
5. `DELETE`：从服务器上删除资源。

**示例如下：**

- GET /users/：获取所有用户。
- POST /user/：新建一个用户。
- GET /user/id/：根据id获取一个用户。
- PUT /user/id/：更新某个id的用户的信息（需要提供用户的所有信息）。
- PATCH /user/id/：更新某个id的用户信息（只需要提供需要改变的信息）。
- DELETE /user/id/：删除一个用户。

### 状态码：

| 状态码 | 原生描述              | 描述                                                         |
| ------ | --------------------- | ------------------------------------------------------------ |
| 200    | OK                    | 服务器成功响应客户端的请求。                                 |
| 400    | INVALID REQUEST       | 用户发出的请求有错误，服务器没有进行新建或修改数据的操作     |
| 401    | Unauthorized          | 用户没有权限访问这个请求                                     |
| 403    | Forbidden             | 因为某些原因禁止访问这个请求                                 |
| 404    | NOT FOUND             | 用户发送的请求的url不存在                                    |
| 406    | NOT Acceptable        | 用户请求不被服务器接收（比如服务器期望客户端发送某个字段，但是没有发送）。 |
| 500    | Internal server error | 服务器内部错误，比如出现了bug                                |

# Flask-Restful插件

> 通过`pip install flask-restful`即可安装。

如果使用`Flask-Restful`，那么定义视图函数的时候，就要继承自`flask_restful.Resource`类，然后再根据当前请求的`method`来定义相应的方法。比如期望客户端是使用`get`方法发送过来的请求，那么就定义一个`get`方法。类似于`MethodView`。示例代码如下：

```python
from flask import Flask,render_template,url_for
from flask_restful import Api,Resource

app = Flask(__name__)
# 用Api来绑定app
api = Api(app)

class IndexView(Resource):
    def get(self):
        return {"username":"donghao"}

api.add_resource(IndexView,'/',endpoint='index')
```

注意事项：

1. `endpoint`是用来给`url_for`反转`url`的时候指定的。如果不写`endpoint`，那么将会使用视图的名字的小写来作为`endpoint`。
2. `add_resource`的第二个参数是访问这个视图函数的`url`，这个`url`可以跟之前的`route`一样，可以传递参数。并且还有一点不同的是，这个方法可以传递多个`url`来指定这个视图函数。

### 参数解析：

`Flask-Restful`插件提供了类似`WTForms`来验证提交的数据是否合法的包，叫做`reqparse`。以下是基本用法：

 

```python
parser = reqparse.RequestParser()
parser.add_argument('username',type=str,help='请输入用户名')
args = parser.parse_args()
```

`add_argument`可以指定这个字段的名字，这个字段的数据类型等。以下将对这个方法的一些参数做详细讲解：

1. `default`：默认值，如果这个参数没有值，那么将使用这个参数指定的值。
2. `required`：是否必须。默认为False，如果设置为`True`，那么这个参数就必须提交上来。
3. `type`：这个参数的数据类型，如果指定，那么将使用指定的数据类型来强制转换提交上来的值。
4. `choices`：选项。提交上来的值只有满足这个选项中的值才符合验证通过，否则验证不通过。
5. `help`：错误信息。如果验证失败后，将会使用这个参数指定的值作为错误信息。
6. `trim`：是否要去掉前后的空格。

其中的`type`，可以使用`python`自带的一些数据类型，也可以使用`flask_restful.inputs`下的一些特定的数据类型来强制转换。比如一些常用的：

1. `url`：会判断这个参数的值是否是一个url，如果不是，那么就会抛出异常。
2. `regex`：正则表达式。
3. `date`：将这个字符串转换为`datetime.date`数据类型。如果转换不成功，则会抛出一个异常。

### 输出字段：

对于一个视图函数，你可以指定好一些字段用于返回。以后可以使用ORM模型或者自定义的模型的时候，他会自动的获取模型中的相应的字段，生成`json`数据，然后再返回给客户端。这其中需要导入`flask_restful.marshal_with`装饰器。并且需要写一个字典，来指示需要返回的字段，以及该字段的数据类型。示例代码如下：

```python
class ProfileView(Resource):
    resource_fields = {
        'username': fields.String,
        'age': fields.Integer,
        'school': fields.String
    }

    @marshal_with(resource_fields)
    def get(self,user_id):
        user = User.query.get(user_id)
        return user
```

在`get`方法中，返回`user`的时候，`flask_restful`会自动的读取`user`模型上的`username`以及`age`还有`school`属性。组装成一个`json`格式的字符串返回给客户端。

重命名属性：

很多时候你面向公众的字段名称是不同于内部的属性名。使用 attribute可以配置这种映射。比如现在想要返回`user.school`中的值，但是在返回给外面的时候，想以`education`返回回去，那么可以这样写：

```python
resource_fields = {
    'education': fields.String(attribute='school')
}
```

默认值：

在返回一些字段的时候，有时候可能没有值，那么这时候可以在指定`fields`的时候给定一个默认值，示例代码如下：

```python
resource_fields = {
    'age': fields.Integer(default=18)
}
```

复杂结构：

有时候想要在返回的数据格式中，形成比较复杂的结构。那么可以使用一些特殊的字段来实现。比如要在一个字段中放置一个列表，那么可以使用`fields.List`，比如在一个字段下面又是一个字典，那么可以使用`fields.Nested`。以下将讲解下复杂结构的用法：

```python
class ProfileView(Resource):
    resource_fields = {
        'username': fields.String,
        'age': fields.Integer,
        'school': fields.String,
        'tags': fields.List(fields.String),
        'more': fields.Nested({
            'signature': fields.String
        })
        'then':fields.List(fields.Nested(别的序列化fields)) # 列表套字典
    }
    
    或者
    
        resource_fields = {
        'username': fields.String,
        'age': fields.Integer,
        'school': fields.String,
        'tags': fields.List(fields.String),
        'more': marshal(没有序列化的json，按什么格式序列化（resource_fields）)
    }
```

### 自定义过滤

```python
    resource_fields = {
        'username': fields.String,
        'age': fields.Integer,
        'school': fields.String,
        'tags': fields.List(fields.String),
        'more': fields.Nested({
            'signature': fields.String
        })
        'is_del':IsDel(attribute='is_delete')
    }
    
    class IsDel(fields.Raw):
    	def format(self,value):
    		print(value):
    		return 'True' if value == 1 else 'False'
```

# cors

```
pip install flask-cors
```

##### 如果你的试图函数是以装饰器为 路由url的，则可以使用以下方法

1. 使用@cross_origin装饰器

```python
from flask_cors import cross_origin

@app.route("/")
@cross_origin()
def helloWorld():
  return "Hello, cross-origin-world!"
```

1. 使用CORS函数
   应用全局配置：

```python
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

# 或者
# cors = CORS()
# cors.init_app(app=app,supports_credentials=True)
# supports_credentials 写他保险一点

@app.route("/api/v1/users")
def list_users():
  return "user example"
```

当然,在CORS函数中是可以进行自由参数配置的.
CORS函数的参数说明:

| 参数                 | 类型                     | Head字段                         | 说明                                  |
| -------------------- | ------------------------ | -------------------------------- | ------------------------------------- |
| resources            | 字典、迭代器或字符串     | 无                               | 全局配置允许跨域的API接口             |
| origins              | 列表、字符串或正则表达式 | Access-Control-Allow-Origin      | 配置允许跨域访问的源，*表示全部允许   |
| methods              | 列表、字符串             | Access-Control-Allow-Methods     | 配置跨域支持的请求方式，如：GET、POST |
| expose_headers       | 列表、字符串             | Access-Control-Expose-Headers    | 自定义请求响应的Head信息              |
| allow_headers        | 列表、字符串或正则表达式 | Access-Control-Request-Headers   | 配置允许跨域的请求头                  |
| supports_credentials | 布尔值                   | Access-Control-Allow-Credentials | 是否允许请求发送cookie，false是不允许 |
| max_age              | 整数、字符串             | Access-Control-Max-Age           | 预检请求的有效时长                    |

##### 如果你是 继承Resource类来写的RESTful-API接口，则不能使用上述办法

在需要支持跨域请求的API类下，添加一个类方法`options`，就可以解决跨域问题

```python
class YourAPI(Resource):
    def options(self):
        return {'Allow': '*'}, 200, {'Access-Control-Allow-Origin': '*',
                                     'Access-Control-Allow-Methods': 'HEAD, OPTIONS, GET, POST, DELETE, PUT',
                                     'Access-Control-Allow-Headers': 'Content-Type, Content-Length, Authorization, Accept, X-Requested-With , yourHeaderFeild',
                                     }
```

可能的原因:

> 在出现跨域问题的请求的时候,无论是POST请求还是PUT请求,前端都会优先发起一个OPTIONS请求.然后再结合前端页面的报错信息,最后得出结论.前端在处理跨域请求时,总会先发起一个OPTIONS请求确认请求允许范围.那么在解决跨域请求时,只需要在每个资源url中加入options请求方式,并返回适当的响应头信息,应该能解决跨域问题.

具体可配置参数解释:

- Access-Control-Allow-Origin
  这个头部信息由服务器返回，用来明确指定那些客户端的域名允许访问这个资源。它的值可以是：

  -使用" * " —— 允许任意域名

  - 一个完整的域名名字（比如：https://example.com）

  如果你需要客户端传递验证信息到头部（比如：cookies）。这个值不能为 * —— 必须为完整的域名（这点很重要）。

- Access-Control-Allow-Credentials
  这个头部信息只会在服务器支持通过cookies传递验证信息的返回数据里。它的值只有一个就是 true。跨站点带验证信息时，服务器必须要争取设置这个值，服务器才能获取到用户的cookie。

- Access-Control-Allow-Headers
  提供一个逗号分隔的列表表示服务器支持的请求数据类型。假如你使用自定义头部(比如：x-authentication-token 服务器需要在返回OPTIONS请求时，要把这个值放到这个头部里，否则请求会被阻止)。

- Access-Control-Expose-Headers
  相似的，这个返回信息里包含了一组头部信息，这些信息表示那些客户端可以使用。其他没有在里面的头部信息将会被限制（译者注：这个头信息实战中使用较少）。

- Access-Control-Allow-Methods
  一个逗号分隔的列表，表明服务器支持的请求类型（比如：GET, POST）

- Origin
  这个头部信息，属于请求数据的一部分。这个值表明这个请求是从浏览器打开的哪个域名下发出的。出于安全原因，浏览器不允许你修改这个值。