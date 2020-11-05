# Django

- 新建一个虚拟环境

  - 

  ```python
  django-admin startproject 项目名
  ```

  


- 开启项目

  - ```
    
    python manage.py startapp App # 创建应用
    把名添加到settings.py INSTALLED_APPS 里
    改用中国语言 zh-hans
    ALLOWED_HOSTS 改为['*']
    USE_TZ 改为 False
    python manage.py runserver 9000 # 运行代码
    
    ```

    

- 项目结构

  - ├─.idea
    │  └─inspectionProfiles
    ├─App
    │  └─migrations
    ├─django_py
    │  └─__pycache__
    └─templates

  -  django_py 项目的管理目录
  - APP 项目的应用目录 

## Django ORM

Django 模型使用自带的 ORM。

对象关系映射（Object Relational Mapping，简称 ORM ）用于实现面向对象编程语言里不同类型系统的数据之间的转换。

ORM 在业务逻辑层和数据库层之间充当了桥梁的作用。

ORM 是通过使用描述对象和数据库之间的映射的元数据，将程序中的对象自动持久化到数据库中。



使用   ORM 的好处：

- 提高开发效率。
- 不同数据库可以平滑切换。

使用 ORM 的缺点：

- ORM 代码转换为 SQL 语句时，需要花费一定的时间，执行效率会有所降低。
- 长期写 ORM 代码，会降低编写 SQL 语句的能力。

ORM 解析过程:

- 1、ORM 会将 Python 代码转成为 SQL 语句。
- 2、SQL 语句通过 pymysql 传送到数据库服务端。
- 3、在数据库中执行 SQL 语句并将结果返回。

## 数据库配置

### Django 如何使用 mysql 数据库

创建 MySQL 数据库( ORM 无法操作到数据库级别，只能操作到数据表)语法：

```python
DATABASES = { 
    'default': 
    { 
        'ENGINE': 'django.db.backends.mysql',    # 数据库引擎
        'NAME': 'runoob', # 数据库名称
        'HOST': '127.0.0.1', # 数据库地址，本机 ip 地址 127.0.0.1 
        'PORT': 3306, # 端口 
        'USER': 'root',  # 数据库用户名
        'PASSWORD': '123456', # 数据库密码
    }  
}

# 在与 settings.py 同级目录下的 __init__.py 中引入模块和进行配置
import pymysql
pymysql.install_as_MySQLdb()


django-admin.py startapp TestModel


HelloWorld
|-- HelloWorld
|-- manage.py
...
|-- TestModel
|   |-- __init__.py
|   |-- admin.py
|   |-- models.py
|   |-- tests.py
|   `-- views.py


# models.py
from django.db import models
 
class Test(models.Model):
    name = models.CharField(max_length=20)
    
'''
以上的类名代表了数据库表名，且继承了models.Model，类里面的字段代表数据表中的字段(name)，数据类型则由CharField（相当于varchar）、DateField（相当于datetime）， max_length 参数限定长度。

接下来在 settings.py 中找到INSTALLED_APPS这一项，如下：

'''
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'TestModel',               # 添加此项
)

# 在命令行中运行：

$ python3 manage.py migrate   # 创建表结构 

$ python3 manage.py makemigrations TestModel  # 让 Django 知道我们在我们的模型有一些变更
$ python3 manage.py migrate TestModel   # 创建表结构



```

## 数据库操作

### 添加数据

```python
# 添加数据需要先创建对象，然后再执行 save 函数，相当于SQL中的INSERT：

# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
 
from TestModel.models import Test
 
# 数据库操作
def testdb(request):
    test1 = Test(name='runoob')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p
                        
```

### 获取数据

```python
# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
 
from TestModel.models import Test
 
# 数据库操作
def testdb(request):
    # 初始化
    response = ""
    response1 = ""
    
    
    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = Test.objects.all()
        
    # filter相当于SQL中的WHERE，可设置条件过滤结果
    response2 = Test.objects.filter(id=1) 
    
    # 获取单个对象
    response3 = Test.objects.get(id=1) 
    
    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    Test.objects.order_by('name')[0:2]
    
    #数据排序
    Test.objects.order_by("id")
    
    # 上面的方法可以连锁使用
    Test.objects.filter(name="runoob").order_by("id")
    
    # 输出所有数据
    for var in list:
        response1 += var.name + " "
    response = response1
    return HttpResponse("<p>" + response + "</p>")
```

### 更新数据

```python
# 修改数据可以使用 save() 或 update():

# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
 
from TestModel.models import Test
 
# 数据库操作
def testdb(request):
    # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
    test1 = Test.objects.get(id=1)
    test1.name = 'Google'
    test1.save()
    
    # 另外一种方式
    #Test.objects.filter(id=1).update(name='Google')
    
    # 修改所有的列
    # Test.objects.all().update(name='Google')
    
    return HttpResponse("<p>修改成功</p>")


```

### 删除数据

```python
# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
 
from TestModel.models import Test
 
# 数据库操作
def testdb(request):
    # 删除id=1的数据
    test1 = Test.objects.get(id=1)
    test1.delete()
    
    # 另外一种方式
    # Test.objects.filter(id=1).delete()
    
    # 删除所有数据
    # Test.objects.all().delete()
    
    return HttpResponse("<p>删除成功</p>")
```

# 反向迁移

```python
"""
	把数据库结构反向写成python文件
	python manage.py # 可以获得帮助文档
	python manage.py shell 可以打开shell变成
	python manage.py inspectdb # 反向迁移

"""
```

# urls.py

```python
# 总路由文件
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('App.urls'))
]
# 项目路由文件
app_names = 'App' # 应用名空间 ,在反向定位时用到了

urlpatterns = [
    # 不能以斜线开头
    path('home/', views.home, name='home'),
    path('apps/<path:app>/', views.apps, name='apps'),
    path('main_app', views.main_app, name='main_app')
]

```



# HttpRequest 对象

```python
# QueryDict
# views 文件里的函数

# request.GET =>> QueryDict

# 获取单一值 /tel/?username=yby
request.GET.get('username')

# 获取多值 /tel/?age=18&age=24
request.GET.getlist('age')

# 请求路径 PATH
request.PATH

# FILES 文件

# META 请求头的键值对
	# HTTP_REFERER 来源页面
    # REMOTE_ADDR 客户端ip
    # REMOTR_HOST 客户端主机

# encoding 字符编码

# scheme 协议

# SESSION

# COOKIES

get_host() # 获取主机+端口
get_full_path() # 请求路径加查询字符串
is_ajax() # 如果是ajax 返回true
build_absulote_url() # 完整的url
dict() # 参数变成字典格式


```

#  HttpResponse

```python
content # 字节字符串 b'good bye'
charset # 字符编码 'utf-8'
status_code # http 状态码  'text/html'
content_type # 指定输出的MIME类型
```

# JsonResponse

```python
return JsonResponse({'name':'yby'},safe=False) # 如果是字典不用设置safe=False,不是字典设置safe=False
```

# 重定向 HttpResponseRedirect

```python
# 使用时需导入模块
return HttpResponseRedirect('/user/')
return redirect('/user/') # 上面那个的快捷方式
# 不带参数
return redirect(reverse("App:home")) # 反向定位，由name 来确定路由，不能直接用name 重定向
reverse("App:home")

# 带参数
reverse("App:home",args=(1,2)) # 位置参数可以是列表或者元组
reverse("App:home",kwargs={'name':'yby','age':'18'})
```

# 错误视图

```python
# 当服务器找不到路径，django 会自己调用template 里的404.html
# 当服务器发生错误，django 会自己调用django.views.defaults.server_error加载template 里的500.html
```

# 模板

```python
render(request,'index.html',context=locals()) # locals() 获取当前未知的全部局部变量
# 可以在每个项目下新建templates 文件夹，路由走到这会检索文件夹看看有没有匹配，不过不建议使用这种方法，会拖慢运行速度，可以再根目录的templates 里面新建项目名文件夹，将项目所需要的模板文件加入到对应的文件夹下，方便管理。
# 如果想要在根目录下建templates 需要在settings.py文件下申明DIRS,因为他默认查找的是项目下的templates文件夹


1:loader加载
# 好处是家再一次模板可以进行多次渲染
from django.template import loader
temp = loader.get_template('index.html')
print(template.__dict__)
# 渲染模板，生成HTML源码
res = temp.render(context={'context':'hellow index'})
print(res)
return HttpResponse(res)


2:render
from django.shortcuts import render
render(request,template.context=None)
'''
参数
request 请求对象
templatesname 模板名称
context 参数字典，必须是字典	

'''

'''
模板语法

{# 单行注释 #}
{% comment %}
	多行注释
{% endcomment %}

{{ 变量 }}
{{ student.0 }}-----{{ student[0] }} 不支持下标,对象属性统统用点

过滤器 djangoprojects
{{student | add:'10'}}
{{age | default_if_none:'19'}} 缺省值 默认值 如果age为None 则展示缺省值（默认值）
{{age | default:'19'}} 如果变量age不存在显示19
{{date | date:'Y-m-d H:i:s'}} 年月日时分秒
自动转义
如果你的变量里面有html标签 模板会自动转义成普通字符
加
{% autoescape %}
{{ content }} 在这里写变量就不会转义了
{% endautoescape %}

自定义过滤器
在项目里创建一个templatetags 包
在包里创建一个py文件
from django import template
# 实例化注册对象
register = template.Library() # 必须是register 不是会报错
# name代表要在模板中使用的过滤器名称
@register.filter(name='hellow')
def hellow(value,arg):
/*
	:params value 传给hellow 过滤的值
	:params arg hellow 自带的参数 
	:return
*/
	return value + str(arg)
	
	
在模板里加载模块
{% load customfilter %} # 这个customfilter 必须是你创建的文件夹名不能是别的


出现错误有可能是
1:yempaltetags 里没有__init__.py
2:在settings里install_apps未设置 可以加一条 App.templatetags
3:必须是register 其他的报错，不知道为啥


{% if num > 10 %}
	hahaha
{% elif num > 20 %}
	hahahah
{% else %}
	hahaha
{% endif %}

# 不要再if表达式里使用（）

{% for i in num %} # 反向迭代 在 num 后面加一个 reversed
	{{ forloop.counter0 }}--{{ i }} # forloop.conter0 下标从零开始，并显示下标
{% empty %}
	没有数据
{% endfor %}
'''


{% csrf_token %} # 防跨站攻击

'''
	不检测跨站防御的方法有两种
	1：直接把settings.py 中间件里的'django.middleware.csrf.CsrfViewMiddleware' 注释掉
	2：在view里加一个装饰器csrf_exempt （局部禁止）
	from django.views.decorators.csrf import csrf_exempt
	@csrf_exempt
	def csrf(request):
    	return HttpResponse({'name': 'js', 'lan': 'china'})
'''

# 在使用ajax 请求的时候需要添加一个{'csrfmiddlewaretoken':'Ku5hjPqhDwBsCMAFghtBTYD4fq5Cqs0fmD5nyjuQB5uqa8AzcUu0GRp0MhQz0fXl'} 键值对

'''
{% include "app/index.html" %} # components 组件
'''

'''
<a href-"{% url 'App:home' name='yby' %}">show</a> # 应用路由名进行跳转
'''

'''
{% block title %}		 # 类似于插槽 ,这里用于继承
{% endblock %}
'''

'''
{% extents "app/base.html" %}
{% block content %}
	<h1>意大利炮</h1>
{% endblock %}
'''
```

# jinja2

```python
pip install jinja2
# 只是用jinja2 settings template 配置
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [os.path.join(BASE_DIR, 'jinja2_templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'environment': "App.jinja2_env.environment",
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# jinja2_env.py 文件
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from jinja2 import Environment

def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse
    })
    return env


# 用jinja2 必须注释掉用django模板做的后台网站

# settings.py ==> INSTALLED_APPS ==> 'django.contrib.admin'
# urls.py ==> urlpatterns ==> path('admin/', admin.site.urls)


```

# 模型 

```python
pip install mysqlclient

准备表
创建如下几张表

from django.shortcuts import HttpResponse, render, redirect
from django.db import models


class Class(models.Model):
    id = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=32)
    cdata = models.DateField()

    def __str__(self):
        return "%s" % [self.__class__, self.cname]


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=32)

    # 一对多
    # cid = models.ForeignKey(to="Class",to_field="id",related_name="students")
    cid = models.ForeignKey(to="Class", to_field="id",on_delete=models.CASCADE,db_cloumn='id')
    
    # on_delete = set_null DO_NOTHING(什么也不做，也不报错) SET_DEFAULT PRCTECT(保护，不删除主表不能删除附表)
    # db_cloumn 自己定义的变量名和数据库里的字段名不一样可以写这个
    # related_name 为互相调用留下合适的名字 cls.students.all() 如果没写就用 表名_set 查询

    # 一对一
    detail = models.OneToOneField("StudentDetail", to_field="id")
    # 等同于如下的代码
    # detail = models.ForeignKey(to="StudentDetail",to_field="id",unique=True)

    def __str__(self):
        return "%s" % [self.sname]


# #建立多对多  第一种方法
# class Teacher(models.Model):
#     id = models.AutoField(primary_key=True)
#     tname = models.CharField(max_length=32)
#
#
# class Teacher2Class(models.Model):m
#     id = models.AutoField(primary_key=True)
#     tid = models.ForeignKey(to="Teacher",to_field="id")
#     cid = models.ForeignKey(to="Class",to_field="id")
#
#     class Meta:
#         unique_together = ("tid","cid")


# 建立多对多  第二种方法
class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    tname = models.CharField(max_length=32)
    cid = models.ManyToManyField(to="Class",name="teacher")


# 建立多对多  第3种方法
# class Teacher(models.Model):
#     id = models.AutoField(primary_key=True)
#     tname = models.CharField(max_length=32)
#     cid_tid = models.ManyToManyField(to="Class",
#                                      through="Teacher2Class",
#                                      through_fields=("tid", "cid"))
#
# class Teacher2Class(models.Model):
#     id = models.AutoField(primary_key=True)
#     tid = models.ForeignKey(to="Teacher", to_field="id")
#     cid = models.ForeignKey(to="Class", to_field="id")
#
#     class Meta:
#         unique_together = ("tid", "cid")


class StudentDetail(models.Model):
    id = models.AutoField(primary_key=True)
    height = models.PositiveIntegerField()
    email = models.EmailField()
    memo = models.CharField(max_length=128)

需要注意的如下：

  # 一对多
    # cid = models.ForeignKey(to="Class",to_field="id",related_name="student")
    cid = models.ForeignKey(to="Class", to_field="id")

    # 一对一
    detail = models.OneToOneField("StudentDetail", to_field="id")
    # 等同于如下的代码
    # detail = models.ForeignKey(to="StudentDetail",to_field="id",unique=True)

一对一操作
正向查询（由学生信息表查询学生详情表）

stu = models.Student.objects.first()
stu.detail.email
'1@qq'

反向查询（由学生详情表反向查询学生信息表）

detail = models.StudentDetail.objects.get(id=1)
detail.student.sname
'小一

一对多操作
正向查询（由学生表查询班级表）

from app01 import models
stu = models.Student.objects.first()
stu.cid_id
1
stu.cid.cname
'全栈1期'

反向查询（由班级表查询学生表）

cls = models.Class.objects.first()
cls.student_set.all()
<QuerySet [<Student: ['小一']>, <Student: ['小二']>]>

注意：

如果不在外键的字段中设置related_name的话，默认就用表名_set。
如果设置了related_name=”students”，反向查询时可直接使用students进行反向查询。

cls.students.all() 

多对多操作
正向查询（由老师表查询班级表）

from app01 import models
tea = models.Teacher.objects.first()
tea.cid_tid
<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0x05C110F0>

tea.cid_tid.all()
<QuerySet [<Class: [<class 'app01.models.Class'>, '全栈1期']>, <Class: [<class 'app01.models.Class'>, '全栈2期']>]>

first = tea.cid_tid.first()
first
<Class: [<class 'app01.models.Class'>, '全栈1期']>

first.cname
'全栈1期'

first.student_set
<django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager object at 0x03283870>

first.student_set.all()
<QuerySet [<Student: ['小一']>, <Student: ['小二']>]>

反向查询（由班级表反向查询老师表）

cls = models.Class.objects.first()
cls.student_set
<django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager object at 0x03283070>

cls.teacher_set
<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0x03224710>

cls.teacher_set.all()
<QuerySet [<Teacher: Teacher object>, <Teacher: Teacher object>]>

cls.teacher_set.all().first()
<Teacher: Teacher object>

cls.teacher_set.all().first().cid_tid
<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0x032A2790>

cls.teacher_set.all().first().tname
'王老师'

常用方法
create()

from app01 import models
import datetime
teacher = models.Teacher.objects.get(id=1)
teacher.cid.create(cname="linux2",cdata=datetime.datetime.now())
<Class: [<class 'app01.models.Class'>, 'linux2']>

多对对

cls = models.Class.objects.get(id=1)
cls.teacher_set.create(tname="egon")
<Teacher: Teacher object>

import datetime
cls = models.Class.objects.first()
cls.student_set.create(sname="王七",detail_id=4)

stu = models.Student.objects.create(sname="wyf",detail_id=5,cid_id=2)

以下方式对多对多不行！！
这里写图片描述

add()

from app01 import models
import datetime
cls = models.Class.objects.all()
models.Teacher.objects.first().cid.add(*cls)

set\remove\clear

tea = models.Teacher.objects.first()
tea.cid.set([4,3])
tea.cid.remove(3)
tea.cid.clear()

了不起的双下划线
这里写图片描述

models.Class.objects.filter(student__sname__contains="d")
<QuerySet [<Class: [<class 'app01.models.Class'>, 'python']>, <Class: [<class 'app01.models.Class'>, 'sfsdf']>]>

models.Class.objects.values("cname")
<QuerySet [{'cname': 'linux'}, {'cname': 'python'}, {'cname': 'sfsdf'}]>

models.Class.objects.values("cname","student__sname")
<QuerySet [{'cname': 'linux', 'student__sname': 'wyf'}, {'cname': 'python', 'student__sname': 'wfdsd'}, {'cname': 'sfsdf', 'student__sname': 'fdgerter'}]>

以下方法不可行！！

models.Class.objects.first().values("cname","student__sname")
Traceback (most recent call last):
  File "<input>", line 1, in <module>
AttributeError: 'Class' object has no attribute 'values'

models.Class.objects.all().values("cname","student__detail__email")

<QuerySet [{'cname': 'linux', 'student__detail__email': '1@qq'}, {'cname': 'python', 'student__detail__email': '2@werwe'}, {'cname': 'sfsdf', 'student__detail__email': '4@fds'}, {'cname': 'linux', 'student__detail__email': '2@werw'}]>
```

# 继承

```python
class Student(models.Model):
	pass
	class Meta:
        abstract = True
    	# abstract 抽象父类不生成表 子类生成表，并继承所有父类属性
class Graduate(Student):
    pass

# 可以建立一个基础父类
class BaseModel(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
class FaterModel(BaseModel):
    pass
    class Meta:
        db_table = 'faterModel'
```

# 短信验证

```python
pip install ronglian_sms_sdk


from ronglian_sms_sdk import SmsSDK

accId = '8aaf070875774c6d0175819b8f4f02ff'
accToken = 'f47258de51bb441bb7d87e36959f64c7'
appId = '8aaf070875774c6d0175819b90450305'


def send_messages(mobile, datas):
    sdk = SmsSDK(accId, accToken, appId)
    tid = '1' # 模板id 默认模板id 为1
    # print(tid, datas, mobile)
    # mobile 手机号
    # datas 数据元组，根据模板设置元组里有几个元素
    resp = sdk.sendMessage(tid, mobile, datas)
    print(resp)


# 调用发送短信 https://www.yuntongxun.com/  https://doc.yuntongxun.com/p/5f029ae7a80948a1006e776e


def send_message(request):
    try:
        code = random.randint(100000, 999999)
        send_messages('18249241924', (code, 10))
    except Exception as e:
        print(e)
        return HttpResponse('bad')
    else:
        return HttpResponse('ok')

```

# 分页

```python
# 导入分页模块
from django.core.paginator import Paginator
# 查询所有数据列表queryset对象
book_list = BorrotBook.objects.all()
# 实例化对象
paginator = Paginator(book_list, 10) # 10 代表每页10个数据
# Paginator类对象的属性
序号	属性名	说明
1	num_pages	返回分页之后的总页数
2	page_range	返回分页后的页码列表

# Paginator类对象的方法
序号	方法名	说明
1	page(self, number)	返回第numbe r页的page类实例对象

# Page实例对象的属性
序号	属性名	说明
1	number	返回当前页的页码
2	object_list	返回当前页的数据查询集
3	paginator	返回对应的Paginator类对象

# page实例对象的方法
序号	方法名	说明
1	has_previous	判断当前页是否有前一页
2	has_next	判断当前页是否有下一页
3	previous_page_number	返回前一页的页码
4	next_page_number	返回下一页的页码
```

```python
# 带返回值参数的views函数
def borrow_show(request, pindex):
    """
    已借图书查询并展示到前端页面
    """
    book_obj = BorrowBook.objects.all()  # 获取借书表中所有的数据
    book_list = []  # 创建一个空列表，存放当前登陆人所借过的书
    for i in book_obj:  # 遍历所有的借书记录，查找到当前登陆人所借的书，并放入空列表
        if i.reader.read_code == request.session["user_id"]:
            book_list.append(i)
    paginator = Paginator(book_list, 5)  # 实例化Paginator, 每页显示5条数据
    if pindex == "":  # django中默认返回空值，所以加以判断，并设置默认值为1
        pindex = 1
    else:  # 如果有返回在值，把返回值转为整数型
        int(pindex) 
    page = paginator.page(pindex)  # 传递当前页的实例对象到前端
    context = {"message": request.session["user_name"], "page": page}
    return render(request, "books/borrow_show.html", context)

# urls配置

from django.urls import path
from .import views

app_name = "books"
urlpatterns = [
    # 已借图书查询并展示
    path("borrow_show/<pindex>", views.borrow_show, name="borrow_show"),
    ]

# Html中配置

<--当前页内容遍历展示-->
    {%for item in page%}
        <tr>
            <td width="120px">{{forloop.counter}}</td>
            <td width="150px"><a href="" style="color: #0f0f0f">										{{item.books.book_name}}</a></td>
            <td width="120px">{{item.books.book_author}}</td>
            <td width="120px">{{item.books.book_price}}</td>
            <td width="120px">{{item.books.book_concern}}</td>
            <td width="120px">{{item.books.book_type.book_type}}</td>
            <td width="120px">{{message}}</td>
            <td width="120px">{{item.borrow_book}}</td>
        </tr>
    {%endfor%}

<--底部分页按钮显示-->
    <nav aria-label="Page navigation">
		<div class="pagination">
			<ul class="pagination">
			{% if page.has_previous %}   # 判断当前页是否有上一页
				<li><a href="/books/borrow_show/{{page.previous_page_number}}" aria-label="Previous">
					<span aria-hidden="true">&laquo;</span></a></li>
            {% endif %}

            {% for num in page.paginator.page_range%}  # 循环遍历页码列表，并展示到底部
            	{%if pindex == page.number%}
                	<li><a href="">{{ num }}</a></li>
                {%else%}
                    <li><a href="/books/borrow_show/{{num}}">{{ num }}</a></li>
                {%endif%}
             {% endfor %}

             {% if page.has_next %}  # 判断当前页是否有下一页
                 <li><a href="/books/borrow_show/{{page.next_page_number}}" aria-label="Next">
                      <span aria-hidden="true">&raquo;</span></a></li>
              {% endif %}
       		</ul>
		</div>
    </nav>
```

# 自定分页

``` python
from django.core.paginator import Paginator

class BaiduPaginator(Paginator):
    def custom_range(self,page,per_range):
        '''
        params page :当前页
        params per_range:每页显示多少页码
        return range对象，页码范围
        '''
        # 页码数大于总页数
        if per_range > self.num_pages:
            return range(1,self.num_pages+1) # 加一视为取到range函数左闭右开。
        elif page <= per_range // 2:
            return range(1,per_range+1)
        elif page + per_range // 2 > self.num_pages
            return range(self.num_pages-per_range+1,self.num_pages+1) 
        else:
            return range(page-per_range//2,page + math.ceil(per_range/2))
```

# cookie

```python
def login(request):
    if request.method == 'POST':
        print(request.POST.dict())

        response = redirect('App02:home')
        future = datetime.now() + timedelta(days=3)  # timedelate 时间间隔
        # 过期时间expires
        # response.set_cookie('username', request.POST.get('username'), expires=future)
        response.set_signed_cookie('username', request.POST.get('username'), salt='', expires=future)  # 加盐
        # 加盐的作用是不让随意自己修改不是为了保密
        return response
    return render(request, 'login.html')


def home(request):
    # username = request.COOKIES.get('username')
    username = request.get_signed_cookie('username', salt='') # 获取加盐

    return render(request, 'home1.html', locals())


def logout(request):
    response = redirect('App02:login')
    response.delete_cookie('username')
    return response
```

# 路由守卫

```python
def check_login(func):
    def inner(*args, **kwargs):
        if args[0].COOKIES.get('username'):
            return func(*args, **kwargs)
        else:
            return redirect('App02:login')

    return inner
    

@check_login
def home(request):
    username = request.COOKIES.get('username')

    return render(request, 'home1.html', locals())
```

# 权限设计

```python
user_permission = 9 # 1001

DEL_PERMISSION = 8 # 1000
READ_PERMISSION = 4 # 0100
WRITE_PERMISSION = 2 # 0010
EXE_PERMISSION = 1 # 0001


def check_permission(x,y):
    def handel_action(fn):
        def do_action():
            if x & y != 0:
                fn()
            else:
                print('对不起，您没有该权限')
        return do_action
    return handel_action

@check_permission(user_permission,READ_PERMISSION)
def read():
    print('我正在读')

@check_permission(user_permission,WRITE_PERMISSION)
def write():
    print('我正在写')
    
@check_permission(user_permission,EXE_PERMISSION)
def exe():
    print('我正在执行')
    
@check_permission(user_permission,DEL_PERMISSION)
def delete():
    print('我正在删除')

# 有执行和删除权限
# 1001 & 与运算 0001 是 0001 说明 他有执行权限
# 1001 & 与运算 0010 是 0000 说明 他没有写权限
# 1001 & 与运算 0100 是 0000 说明 他没有读权限
# 1001 & 与运算 1000 是 1000 说明 他有删除权限

# 最大因子15 从16开始轮回 0-16 1-17 。。。。

read()
delete()
exe()
write()

```

# session

```python
    'django.contrib.sessions.middleware.SessionMiddleware', # 中间件
	'django.contrib.sessions', # 安装
	必须迁移一下，数据库里要有django_session 表才可以
	
def login(request):
    if request.method == 'POST':
        print(request.POST.dict())
        response = redirect('App02:home')
        future = datetime.now() + timedelta(days=3)  # timedelate 时间间隔
        # 过期时间expires
        request.session['username'] = request.POST.get('username')
        request.session['password'] = request.POST.get('password')
        request.session.set_expiry(future) # 默认两周
        return response
    return render(request, 'login.html')


def home(request):
    session = request.session.get('username')
    print('session=',session)
    return render(request, 'home1.html', locals())


def logout(request):
    # session 删除
    request.session.clear() # 清空所有session 但不会将session表中的数据删除
    request.session.flush() # 清空所有 并删除表中的数据
    request.session.logout() # 退出登录，清空所有 并删除表中的数据
    del request.session[key] # 删除摸一个session的值
    return response
```

# Form Field

```python
Django表单字段汇总
Field.clean(value)[source]
虽然表单字段的Field类主要使用在Form类中，但也可以直接实例化它们来使用，以便更好地了解它们是如何工作的。每个Field的实例都有一个clean()方法，它接受一个参数，然后返回“清洁的”数据或者抛出一个django.forms.ValidationError异常：

>>> from django import forms
>>> f = forms.EmailField()
>>> f.clean('foo@example.com')
'foo@example.com'
>>> f.clean('invalid email address')
Traceback (most recent call last):
...
ValidationError: ['Enter a valid email address.']
这个clean方法经常被我们用来在开发或测试过程中对数据进行验证和测试。

一、核心字段参数
以下的参数是每个Field类都可以使用的。

1. required
给字段添加必填属性，不能空着。

>>> from django import forms
>>> f = forms.CharField()
>>> f.clean('foo')
'foo'
>>> f.clean('')
Traceback (most recent call last):
...
ValidationError: ['This field is required.']
>>> f.clean(None)
Traceback (most recent call last):
...
ValidationError: ['This field is required.']
>>> f.clean(' ')
' '
>>> f.clean(0)
'0'
>>> f.clean(True)
'True'
>>> f.clean(False)
'False'
若要表示一个字段不是必需的，设置required=False：

>>> f = forms.CharField(required=False)
>>> f.clean('foo')
'foo'
>>> f.clean('')
''
>>> f.clean(None)
''
>>> f.clean(0)
'0'
>>> f.clean(True)
'True'
>>> f.clean(False)
'False'



2. label
label参数用来给字段添加‘人类友好’的提示信息。如果没有设置这个参数，那么就用字段的首字母大写名字。比如：

下面的例子，前两个字段有，最后的comment没有label参数：

>>> from django import forms
>>> class CommentForm(forms.Form):
...     name = forms.CharField(label='Your name')
...     url = forms.URLField(label='Your website', required=False)
...     comment = forms.CharField()
>>> f = CommentForm(auto_id=False)
>>> print(f)
<tr><th>Your name:</th><td><input type="text" name="name" required /></td></tr>
<tr><th>Your website:</th><td><input type="url" name="url" /></td></tr>
<tr><th>Comment:</th><td><input type="text" name="comment" required /></td></tr>
    
    
    
3. label_suffix
Django默认为上面的label参数后面加个冒号后缀，如果想自定义，可以使用label_suffix参数。比如下面的例子用“？”代替了冒号：

>>> class ContactForm(forms.Form):
...     age = forms.IntegerField()
...     nationality = forms.CharField()
...     captcha_answer = forms.IntegerField(label='2 + 2', label_suffix=' =')
>>> f = ContactForm(label_suffix='?')
>>> print(f.as_p())
<p><label for="id_age">Age?</label> <input id="id_age" name="age" type="number" required /></p>
<p><label for="id_nationality">Nationality?</label> <input id="id_nationality" name="nationality" type="text" required /></p>
<p><label for="id_captcha_answer">2 + 2 =</label> <input id="id_captcha_answer" name="captcha_answer" type="number" required /></p>




4. initial
为HTML页面中表单元素定义初始值。也就是input元素的value参数的值，如下所示：

>>> from django import forms
>>> class CommentForm(forms.Form):
...     name = forms.CharField(initial='Your name')
...     url = forms.URLField(initial='http://')
...     comment = forms.CharField()
>>> f = CommentForm(auto_id=False)
>>> print(f)
<tr><th>Name:</th><td><input type="text" name="name" value="Your name" required /></td></tr>
<tr><th>Url:</th><td><input type="url" name="url" value="http://" required /></td></tr>
<tr><th>Comment:</th><td><input type="text" name="comment" required /></td></tr>
你可能会问为什么不在渲染表单的时候传递一个包含初始化值的字典给它，不是更方便？因为如果这么做，你将触发表单的验证过程，此时输出的HTML页面将包含验证中产生的错误，如下所示：

>>> class CommentForm(forms.Form):
...     name = forms.CharField()
...     url = forms.URLField()
...     comment = forms.CharField()
>>> default_data = {'name': 'Your name', 'url': 'http://'}
>>> f = CommentForm(default_data, auto_id=False)
>>> print(f)
<tr><th>Name:</th><td><input type="text" name="name" value="Your name" required /></td></tr>
<tr><th>Url:</th><td><ul class="errorlist"><li>Enter a valid URL.</li></ul><input type="url" name="url" value="http://" required /></td></tr>
<tr><th>Comment:</th><td><ul class="errorlist"><li>This field is required.</li></ul><input type="text" name="comment" required /></td></tr>
这就是为什么initial参数只用在未绑定的表单上。

还要注意，如果提交表单时某个字段的值没有填写，initial的值不会作为“默认”的数据。initial值只用于原始表单的显示：

>>> class CommentForm(forms.Form):
...     name = forms.CharField(initial='Your name')
...     url = forms.URLField(initial='http://')
...     comment = forms.CharField()
>>> data = {'name': '', 'url': '', 'comment': 'Foo'}
>>> f = CommentForm(data)
>>> f.is_valid()
False
# The form does *not* fall back to using the initial values.
>>> f.errors
{'url': ['This field is required.'], 'name': ['This field is required.']}
除了常量之外，你还可以传递一个可调用的对象：

>>> import datetime
>>> class DateForm(forms.Form):
...     day = forms.DateField(initial=datetime.date.today)
>>> print(DateForm())
<tr><th>Day:</th><td><input type="text" name="day" value="12/23/2008" required /><td></tr>
    
    
    
    
5. widget
最重要的参数之一，指定渲染Widget时使用的widget类，也就是这个form字段在HTML页面中是显示为文本输入框？密码输入框？单选按钮？多选框？还是别的....





6. help_text
该参数用于设置字段的辅助描述文本。

>>> from django import forms
>>> class HelpTextContactForm(forms.Form):
...     subject = forms.CharField(max_length=100, help_text='100 characters max.')
...     message = forms.CharField()
...     sender = forms.EmailField(help_text='A valid email address, please.')
...     cc_myself = forms.BooleanField(required=False)
>>> f = HelpTextContactForm(auto_id=False)
>>> print(f.as_table())
<tr><th>Subject:</th><td><input type="text" name="subject" maxlength="100" required /><br /><span class="helptext">100 characters max.</span></td></tr>
<tr><th>Message:</th><td><input type="text" name="message" required /></td></tr>
<tr><th>Sender:</th><td><input type="email" name="sender" required /><br />A valid email address, please.</td></tr>
<tr><th>Cc myself:</th><td><input type="checkbox" name="cc_myself" /></td></tr>
>>> print(f.as_ul()))
<li>Subject: <input type="text" name="subject" maxlength="100" required /> <span class="helptext">100 characters max.</span></li>
<li>Message: <input type="text" name="message" required /></li>
<li>Sender: <input type="email" name="sender" required /> A valid email address, please.</li>
<li>Cc myself: <input type="checkbox" name="cc_myself" /></li>
>>> print(f.as_p())
<p>Subject: <input type="text" name="subject" maxlength="100" required /> <span class="helptext">100 characters max.</span></p>
<p>Message: <input type="text" name="message" required /></p>
<p>Sender: <input type="email" name="sender" required /> A valid email address, please.</p>
<p>Cc myself: <input type="checkbox" name="cc_myself" /></p>
    
    
    
    
    
7. error_messages
该参数允许你覆盖字段引发异常时的默认信息。 传递的是一个字典，其键为你想覆盖的错误信息。 例如，下面是默认的错误信息：

>>> from django import forms
>>> generic = forms.CharField()
>>> generic.clean('')
Traceback (most recent call last):
  ...
ValidationError: ['This field is required.']
而下面是自定义的错误信息：

>>> name = forms.CharField(error_messages={'required': 'Please enter your name'})
>>> name.clean('')
Traceback (most recent call last):
  ...
ValidationError: ['Please enter your name']
可以指定多种类型的键，不仅仅针对‘requeired’错误，参考下面的内容。





8. validators
指定一个列表，其中包含了为字段进行验证的函数。也就是说，如果你自定义了验证方法，不用Django内置的验证功能，那么要通过这个参数，将字段和自定义的验证方法链接起来。





9. localize
localize参数帮助实现表单数据输入的本地化。





10. disabled
设置有该属性的字段在前端页面中将显示为不可编辑状态。

该参数接收布尔值，当设置为True时，使用HTML的disabled属性禁用表单域，以使用户无法编辑该字段。即使非法篡改了前端页面的属性，向服务器提交了该字段的值，也将依然被忽略。





二、 Django表单内置的Field类
对于每个字段类，介绍其默认的widget，当输入为空时返回的值，以及采取何种验证方式。‘规范化为’表示转换为PYthon的何种对象。可用的错误信息键，表示该字段可自定义错误信息的类型（字典的键）。

1. BooleanField
默认的Widget：CheckboxInput
空值：False
规范化为：Python的True或者False
可用的错误信息键：required




2. CharField
默认的Widget：TextInput
空值：与empty_value给出的任何值。
规范化为：一个Unicode 对象。
验证max_length或min_length，如果设置了这两个参数。 否则，所有的输入都是合法的。
可用的错误信息键：min_length, max_length, required
有四个可选参数：

max_length，min_length：设置字符串的最大和最小长度。
strip：如果True（默认），去除输入的前导和尾随空格。
empty_value：用来表示“空”的值。 默认为空字符串。




3. ChoiceField
默认的Widget：Select
空值：''（一个空字符串）
规范化为：一个Unicode 对象。
验证给定的值是否在选项列表中。
可用的错误信息键：required, invalid_choice
参数choices：用来作为该字段选项的一个二元组组成的可迭代对象（例如，列表或元组）或者一个可调用对象。格式与用于和ORM模型字段的choices参数相同。





4. TypedChoiceField
像ChoiceField一样，只是还有两个额外的参数：coerce和empty_value。

默认的Widget：Select
空值：empty_value参数设置的值。
规范化为：coerce参数类型的值。
验证给定的值在选项列表中存在并且可以被强制转换。
可用的错误信息的键：required, invalid_choice





5. DateField
默认的Widget：DateInput
空值：None
规范化为：datetime.date对象。
验证给出的值是一个datetime.date、datetime.datetime 或指定日期格式的字符串。
错误信息的键：required, invalid
接收一个可选的参数：input_formats。一个格式的列表，用于转换字符串为datetime.date对象。

如果没有提供input_formats，默认的输入格式为：

['%Y-%m-%d',      # '2006-10-25'
 '%m/%d/%Y',      # '10/25/2006'
 '%m/%d/%y']      # '10/25/06'
另外，如果你在设置中指定USE_L10N=False，以下的格式也将包含在默认的输入格式中：

['%b %d %Y',      # 'Oct 25 2006'
 '%b %d, %Y',     # 'Oct 25, 2006'
 '%d %b %Y',      # '25 Oct 2006'
 '%d %b, %Y',     # '25 Oct, 2006'
 '%B %d %Y',      # 'October 25 2006'
 '%B %d, %Y',     # 'October 25, 2006'
 '%d %B %Y',      # '25 October 2006'
 '%d %B, %Y']     # '25 October, 2006'





6. DateTimeField
默认的Widget：DateTimeInput
空值：None
规范化为：Python的datetime.datetime对象。
验证给出的值是一个datetime.datetime、datetime.date或指定日期格式的字符串。
错误信息的键：required, invalid
接收一个可选的参数：input_formats

如果没有提供input_formats，默认的输入格式为：

['%Y-%m-%d %H:%M:%S',    # '2006-10-25 14:30:59'
 '%Y-%m-%d %H:%M',       # '2006-10-25 14:30'
 '%Y-%m-%d',             # '2006-10-25'
 '%m/%d/%Y %H:%M:%S',    # '10/25/2006 14:30:59'
 '%m/%d/%Y %H:%M',       # '10/25/2006 14:30'
 '%m/%d/%Y',             # '10/25/2006'
 '%m/%d/%y %H:%M:%S',    # '10/25/06 14:30:59'
 '%m/%d/%y %H:%M',       # '10/25/06 14:30'
 '%m/%d/%y']             # '10/25/06'






7. DecimalField
默认的Widget：当Field.localize是False时为NumberInput，否则为TextInput。
空值：None
规范化为：Python decimal对象。
验证给定的值为一个十进制数。 忽略前导和尾随的空白。
错误信息的键：max_whole_digits, max_digits, max_decimal_places,max_value, invalid, required,min_value
接收四个可选的参数：

max_value,min_value:允许的值的范围，需要赋值decimal.Decimal对象，不能直接给个整数类型。

max_digits：值允许的最大位数（小数点之前和之后的数字总共的位数，前导的零将被删除）。

decimal_places：允许的最大小数位。






8. DurationField
默认的Widget：TextInput
空值：None
规范化为：Python timedelta。
验证给出的值是一个字符串，而且可以转换为timedelta对象。
错误信息的键：required, invalid.





9. EmailField
默认的Widget：EmailInput
空值：''（一个空字符串）
规范化为：Unicode 对象。
使用正则表达式验证给出的值是一个合法的邮件地址。
错误信息的键：required, invalid
两个可选的参数用于验证，max_length 和min_length。





10. FileField
默认的Widget：ClearableFileInput
空值：None
规范化为：一个UploadedFile对象，它封装文件内容和文件名到一个对象内。
验证非空的文件数据已经绑定到表单。
错误信息的键：missing, invalid, required, empty, max_length
具有两个可选的参数用于验证：max_length 和 allow_empty_file。





11. FilePathField
默认的Widget：Select
空值：None
规范化为：Unicode 对象。
验证选择的选项在选项列表中存在。
错误信息的键：required, invalid_choice
这个字段允许从一个特定的目录选择文件。 它有五个额外的参数，其中的path是必须的：

path：要列出的目录的绝对路径。 这个目录必须存在。

recursive：如果为False（默认值），只用直接位于path下的文件或目录作为选项。如果为True，将递归访问这个目录，其内所有的子目录和文件都将作为选项。

match：正则表达模式；只有具有与此表达式匹配的文件名称才被允许作为选项。

allow_files：可选。默认为True。表示是否应该包含指定位置的文件。它和allow_folders必须有一个为True。

allow_folders可选。默认为False。表示是否应该包含指定位置的目录。





12. FloatField
默认的Widget：当Field.localize是False时为NumberInput，否则为TextInput。
空值：None
规范化为：Float 对象。
验证给定的值是一个浮点数。
错误信息的键：max_value, invalid, required, min_value
接收两个可选的参数用于验证，max_value和min_value，控制允许的值的范围。





13. ImageField
默认的Widget：ClearableFileInput
空值：None
规范化为：一个UploadedFile 象，它封装文件内容和文件名为一个单独的对象。
验证文件数据已绑定到表单，并且该文件是Pillow可以解析的图像格式。
错误信息的键：missing, invalid, required, empty, invalid_image
使用ImageField需要安装Pillow（pip install pillow）。如果在上传图片时遇到图像损坏错误，通常意味着使用了Pillow不支持的格式。





14. IntegerField
默认的Widget：当Field.localize是False时为NumberInput，否则为TextInput。
空值：None
规范化为：Python 整数或长整数。
验证给定值是一个整数。 允许前导和尾随空格，类似Python的int()函数。
错误信息的键：max_value, invalid, required, min_value
两个可选参数：max_value和min_value，控制允许的值的范围。





15. GenericIPAddressField
包含IPv4或IPv6地址的字段。

默认的Widget：TextInput
空值：''（一个空字符串）
规范化为：一个Unicode对象。
验证给定值是有效的IP地址。
错误信息的键：required, invalid
有两个可选参数：protocol和unpack_ipv4






16. MultipleChoiceField
默认的Widget：SelectMultiple
空值：[]（一个空列表）
规范化为：一个Unicode 对象列表。
验证给定值列表中的每个值都存在于选择列表中。
错误信息的键：invalid_list, invalid_choice, required






17. TypedMultipleChoiceField
类似MultipleChoiceField，除了需要两个额外的参数，coerce和empty_value。

默认的Widget：SelectMultiple
空值：empty_value
规范化为：coerce参数提供的类型值列表。
验证给定值存在于选项列表中并且可以强制。
错误信息的键：required, invalid_choice





18. NullBooleanField
默认的Widget：NullBooleanSelect
空值：None
规范化为：Python None, False 或True 值。
不验证任何内容（即，它从不引发ValidationError）。






19.RegexField
默认的Widget：TextInput
空值：''（一个空字符串）
规范化为：一个Unicode 对象。
验证给定值与某个正则表达式匹配。
错误信息的键：required, invalid
需要一个必需的参数：regex，需要匹配的正则表达式。

还可以接收max_length，min_length和strip参数，类似CharField。






20. SlugField
默认的Widget：TextInput
空值：''（一个空字符串）
规范化为：一个Unicode 对象。
验证给定的字符串只包括字母、数字、下划线及连字符。
错误信息的键：required, invalid
此字段用于在表单中表示模型的SlugField。






21. TimeField
默认的Widget：TextInput
空值：None
规范化为：一个Python 的datetime.time 对象。
验证给定值是datetime.time或以特定时间格式格式化的字符串。
错误信息的键：required, invalid
接收一个可选的参数：input_formats，用于尝试将字符串转换为有效的datetime.time对象的格式列表。

如果没有提供input_formats，默认的输入格式为：

'%H:%M:%S',     # '14:30:59'
'%H:%M',        # '14:30'






22. URLField
默认的Widget：URLInput
空值：''（一个空字符串）
规范化为：一个Unicode 对象。
验证给定值是个有效的URL。
错误信息的键：required, invalid
可选参数：max_length和min_length






23. UUIDField
默认的Widget：TextInput
空值：''（一个空字符串）
规范化为：UUID对象。
错误信息的键：required, invalid






24. ComboField
默认的Widget：TextInput
空值：''（一个空字符串）
规范化为：Unicode 对象。
根据指定为ComboField的参数的每个字段验证给定值。
错误信息的键：required, invalid
接收一个额外的必选参数：fields，用于验证字段值的字段列表（按提供它们的顺序）。

>>> from django.forms import ComboField
>>> f = ComboField(fields=[CharField(max_length=20), EmailField()])
>>> f.clean('test@example.com')
'test@example.com'
>>> f.clean('longemailaddress@example.com')
Traceback (most recent call last):
...
ValidationError: ['Ensure this value has at most 20 characters (it has 28).']
    
    
    
    
    
    
25. MultiValueField
默认的Widget：TextInput
空值：''（一个空字符串）
规范化为：子类的compress方法返回的类型。
根据指定为MultiValueField的参数的每个字段验证给定值。
错误信息的键：incomplete, invalid, required






26. SplitDateTimeField
默认的Widget：SplitDateTimeWidget
空值：None
规范化为：Python datetime.datetime 对象。
验证给定的值是datetime.datetime或以特定日期时间格式格式化的字符串。
错误信息的键：invalid_date, invalid, required, invalid_time

三、创建自定义字段
如果内置的Field真的不能满足你的需求，还可以自定义Field。

只需要创建一个django.forms.Field的子类，并实现clean()和__init__()构造方法。__init__()构造方法需要接收前面提过的那些核心参数，比如widget、required,、label、help_text、initial。

还可以通过覆盖get_bound_field()方法来自定义访问字段的方式。
```

```python
# forms.py

from django import forms

# 有两种发发进行校验
from django.core.exceptions import ValidationError

'''
第一种：结合model,继承django.forms.ModelForm
    class xxx(models.Model):
        字段 = models.CharField(max_length=30)
        
    class xxxForm(ModelForm):
        class Meta
            model = xxx
            field = ('字段') # 只显示model中指定的字段 ，显示所有用__all__
            
第二种：直接继承form # 推荐用第二种，可以用他自带的校验规则
    from django import forms
    class xxxForm(forms.Form):
        pass
'''
def mobile_validate(value):
    import re
    mobile_re = re.compile("^(13[0-9]|14[579]|15[0-3,5-9]|1 6[6]|17[0135678]|18[0-9]|19[89])\\d{8}$")
    if not mobile_re.match(value):
        print('123123')
        raise forms.ValidationError('手机号码格式不对哦')

class RegisterForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=20, required=True, label='请输入用户名', error_messages={
        'min_length': '用户名最少3位',
        'max_length': '用户名最多20位',
        'required': '用户名不能为空',
    })  # 用户名最多20个字符最少三个字符
    password = forms.CharField(min_length=3, max_length=20, required=True, label='请输入密码', error_messages={
        'min_length': '密码最少3位',
        'max_length': '密码最多20位',
        'required': '密码不能为空',
    })

    confirm = forms.CharField(min_length=3, max_length=20, required=True, label='请输入密码', error_messages={
        'min_length': '密码最少3位',
        'max_length': '密码最多20位',
        'required': '密码不能为空',
    })

    regtime = forms.DateTimeField(required=True, label='请输入时间', error_messages={
        'invalid': '时间格式错误',
        'required': '时间不能为空',
    })

    sex = forms.BooleanField(required=False)

    mobile = forms.CharField(
        validators=[mobile_validate],
        error_messages={'required': '手机号不填不行'},
    )


    # 单个字段验证 clean_xxxx
    def clean_password(self):
        if self.cleaned_data.get('password').isdigit() or self.cleaned_data.get('password').isalpha():
            raise ValidationError('密码必须包含字母和数字')
        else:
            return self.cleaned_data['password']

    # def clean_valid_code(self):
    #     if self.cleaned_data.get('valid_code').upper() == self.request.session.get('valid_code'):
    #         return self.cleaned_data['valid_code']
    #     else:
    #         raise ValidationError('验证码不正确')

    # 全局验证
    def clean(self):
        if self.cleaned_data.get('password') != self.cleaned_data.get('confirm'):
            raise ValidationError({'confirm': '密码不一致'})
        # 这块必须有键值对，没有键值对不知道是哪错了
        else:
            return self.cleaned_data


# views.py
def register(request):
    form = RegisterForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():  # 只有当所有的字段都校验通过才会返回True
            data = form.cleaned_data
            errors = form.errors # 这个里面放的是所有校验未通过的字段及错误提示
            print('data=', data)

            print('username=', data.get('username'))

            return HttpResponse('ok')
        else:
            return render(request, 'register.html', {'form': form})
    return render(request, 'register.html')

# 下面的 网上找的
"""
第一步需要一个form类
    from django import forms

    class MyForm(forms.Form):
      name = forms.CharField(max_length=6)
      password = forms.CharField(max_length=8,min_length=3)
      email = forms.EmailField(required=True)
      
第二步实例化form对象
		form_obj = MyForm({'name':'jason'})
        
第三步查看数据校验是否合法
		form_obj.is_valid()  # 只有当所有的字段都校验通过才会返回True

第四步查看校验错误的信息
    form_obj.errors  # 这个里面放的是所有校验未通过的字段及错误提示
    
第五步查看校验通过的数据
		form_obj.cleaned_data  # 符合校验规则数据都会被放到该对象中
	ps:form组件校验数据的规则从上往下依次取值校验
		 校验通过的放到cleaned_data
		 校验失败的放到errors
注意:
   自定义的校验有一个错了就会停止接下来的校验，返回错误
   form中所有的字段默认都是必须传值的(required=True)
   校验数据的时候可以都传(多传的数据不会做任何的校验>>>不会影响form校验规则)，也可以传空
   
"""
# 设置标签样式
		from django import forms
		from django.forms import widgets
		password = forms.CharField(max_length=8,min_length=3,error_messages={
							'max_length': '密码最长8位',
							'required': '密码不能为空',
							'min_length':'密码最少3位'
							},widget=widgets.PasswordInput(attrs={'class':'c1 form-control'}))
		
		
				hobby = forms.ChoiceField(
				choices=((1, "篮球"), (2, "足球"), (3, "双色球"),),
				label="爱好",
				initial=3,
				widget=forms.widgets.Select()
			)
			hobby1 = forms.MultipleChoiceField(
				choices=((1, "篮球"), (2, "足球"), (3, "双色球"),),
				label="爱好",
				initial=[1, 3],
				widget=forms.widgets.SelectMultiple()
			)

			keep = forms.ChoiceField(
				label="是否记住密码",
				initial="checked",
				widget=forms.widgets.CheckboxInput()
			)
```

```html
form组件只帮你渲染获取用户输入的标签,不会帮你渲染提交按钮，需要手动添加
			<h1>第一种渲染方式(可扩展性较差)</h1>
			{{ form_obj.as_p }}
			{{ form_obj.as_ul }}
			
			<h1>第二种渲染方式</h1>
			<form action="">
				<p>{{ form_obj.name.label }}{{ form_obj.name }}</p>
				<p>{{ form_obj.password.label }}{{ form_obj.password }}</p>
				<p>{{ form_obj.email.label }}{{ form_obj.email }}</p>
				<input type="submit">
			</form>
			
			<h1>第三种渲染标签的方式</h1>
				<form action="">
					{% for foo in form_obj %}
						<p>{{ foo.label }}{{ foo }}</p>
					{% endfor %}
				</form>
		
		前端取消校验
			<form action="" method="post" novalidate>
			</form>
		
		
		form组件提交数据如果数据不合法，页面上会保留之前用户输入的信息
		在使用form组件对模型表进行数据校验的时候，只需要保证字段一致
		那么在创建的对象的时候你就直接**form_obj.cleaned_data
		
		<form action="" method="post" novalidate>
			{% for foo in form_obj %}
				<p>
					{{ foo.label }}{{ foo }}
					<span>{{ foo.errors.0 }}</span>
				</p>
			{% endfor %}
			<input type="submit">
		</form>



```

# Admin 模块 自带登录验证，设置密码，路由守护

```python
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from APP03.forms import RegisterForm
from APP03.models import User

def form(request):
    form = {'username': 'yby', 'password': 'a123'}
    user = User.objects.create_user(**form)
    # 用户写入数据库，他会自动签名加密
    # user.set_password('123') # 修改密码
    # user.save()
    if user:
        return HttpResponse('ok')
    return HttpResponse('bad')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            print(locals())
            return redirect('APP03:logout')
        else:
            return HttpResponse('登陆失败，请从新登录 ')
    return render(request, 'login.html', locals())

# 路由守护 login_url 代表你没登录跳转到那个页面上去
@login_required(login_url='APP03:login')
def user_logout(request):
    username = request.user
    is_login = username.is_authenticated
    if request.GET.get('logout'):
        logout(request)
        return redirect('APP03:login')
    return render(request, 'home1.html', locals())

```

```python
from django.contrib.auth.models import AbstractUser
from django.db import models

class StudentDetail(models.Model):
    height = models.PositiveIntegerField()
    email = models.EmailField()
    memo = models.CharField(max_length=128)

    class Meta:
        db_table = 'studentDetail'

# 新建这个表必须要迁移
class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)

    class Meta:
        db_table = 'user'

        
# 在settings.py 里 加
AUTH_USER_MODEL = 'app名.建的表名' # AUTH_USER_MODEL = 'APP03.User'


```

# 图形验证码

```python
pip install django-simple-captcha 

python manage.py migrate # 迁移一下 新建一个库 captcha

from django.conf.urls import url
url(r'^captcha/', include('captcha.urls')),


# django_simple_captcha 验证码配置其他配置项查看文档
# 默认格式
CAPTCHA_OUTPUT_FORMAT = '%(image)s %(text_field)s %(hidden_field)s '
CAPTCHA_NOISE_FUNCTIONS = ('captcha.helpers.noise_null',  # 没有样式
                           # 'captcha.helpers.noise_arcs', # 线
                           # 'captcha.helpers.noise_dots', # 点
                           )
# 图片中的文字为随机英文字母，如 mdsh
# CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge'
# 图片中的文字为数字表达式，如2+2=
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'
# 超时(minutes)
CAPTCHA_TIMEOUT = 1
# 字符个数
CAPTCHA_LENGTH = 4
# 验证码宽度和高度
CAPTCHA_IMAGE_SIZE = (100, 25)

# 配置forms.py
class LoginForms(forms.Form):
    email = forms.CharField(label="邮箱", max_length=128)
    password = forms.CharField(label="密码", max_length=128, widget=forms.PasswordInput)
    captcha = CaptchaField()
    
# 配置views.py
def login(request):
    pass
   # 图片验证码
    # hashkey验证码生成的秘钥，image_url验证码的图片地址
    hashkey = CaptchaStore.generate_key()
    image_url = captcha_image_url(hashkey)
    login_form = forms.LoginForms()
    # Python内置了一个locals()函数，它返回当前所有的本地变量字典
    return render(request, 'user/login.html', locals())
    

# html 模板中显示验证码
 <div class="field">
          <div class="ui left img input">
            <button  id='js-captcha-refresh'  class='ui icon button ' ><i class="refresh icon green"></i></button>
              <img src="{{ image_url}}" alt="captcha" class="captcha">
              <input autocomplete="off" id="id_captcha_1" name="captcha_1" type="text" placeholder="输入验证码">
              <input id="id_reg_captcha_0" name="captcha_0" type="hidden" value="{{ hashkey }}">
          </div>
        </div>

# ajax刷新验证码
<script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.js"></script>
<script>
    $('.captcha').click(function () {
        $.getJSON("/captcha/refresh/", function (result) {
            $('.captcha').attr('src', result['image_url']);
            $('#id_captcha_0').val(result['key'])
        }); 

    });
</script>
```

# 邮箱

```python
# 发送邮件设置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # 固定写法
EMAIL_HOST = 'smtp.163.com'  # SMTP地址
EMAIL_PORT = 25  # SMTP端口
EMAIL_HOST_USER = 'xxxxxxx@163.com'  # 发送邮件的邮箱
EMAIL_HOST_PASSWORD = 'xxxxxx'  # 授权码
EMAIL_SUBJECT_PREFIX = '[杨xx测试] '  # 为邮件Subject-line前缀,默认是'[django]'
EMAIL_USE_TLS = True  # 与SMTP服务器通信时，是否启动TLS链接(安全链接)默认false
DEFAULT_FROM_EMAIL = '贪婪玩月客服中心<xxxxxxx@163.com>'  # 收件人看到的发件人<此处要和发邮件的邮箱相同>


def email(request):
    from django.core.mail import send_mail
    from django.core.mail import send_mass_mail
    from django.conf import settings
    from django.template import loader
    from django.core.mail import EmailMultiAlternatives
    # 模板
    # subject, from_email, to = 'html', settings.DEFAULT_FROM_EMAIL, 'xxxxxx@qq.com'
    # html_content = loader.get_template('active.html').render({'username': '小花猫'})
    # msg = EmailMultiAlternatives(subject=subject, from_email=from_email, to=[to])
    # msg.attach_alternative(html_content, 'text/html')
    # msg.send()
    # 发送单个
    # send_mail('标题', '内容', settings.DEFAULT_FROM_EMAIL,
    #           ['xxxxxxx@qq.com'], fail_silently=False)
    # 发送多个
    msg1 = ('标题', '内容', settings.DEFAULT_FROM_EMAIL, ['xxxxx@qq.com'])
    msg2 = ('标题', '内容', settings.DEFAULT_FROM_EMAIL, ['xxxxx@qq.com'])

    send_mass_mail((msg1,msg2), fail_silently=False)
    return HttpResponse('邮件发送成功')
```

