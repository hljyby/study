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

    - settings.py


```python

import os
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9xp4*ivq_5h6jvtxs%^cbk@s+byrxiyeq+^5wwjz940ec1skdr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'App.apps.AppConfig',
    'rest_framework'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_rest_framework.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_rest_framework.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'admins',
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': '127.0.0.1',
        'PORT': 3306
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'Zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
# 收集静态资源 你安装的插件什么的用的静态资源就会调用这个文件夹下的资源
# 在settings.py 里加下面一段
# 运行 python manage.py collectstatic
STATIC_ROOT = os.path.join('BASE_DIR', 'collectstatic') 

# 这几个STATIC的区别
# 指的是url 访问静态资源时所请求的位置参数 例：
STATIC_URL = '/static/' 
lcoalhost/static/image/1.jpg
STATIC_URL = '/mystatic/'
lcoalhost/mystatic/image/1.jpg

#　部署django项目的时候需要用到STATIC_ROOT ，它是收集所有的静态文件并放在一个目录里，即STATIC_ROOT指向的目录里：
# 当URL访问的时候 会先访问工程文件下的公共资源再访问各个app的资源
```



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
from django.contrib.auth.hashers import make_password, check_password

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
        # password = make_password('123')
        # print(check_password('123',password))
        # 用上面两个函数有可能需要在settings 里加 PASSWORD_HASHERS[上网搜]
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

INSTALLED_APPS = [
    '...'
    'captcha'
]

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

# 富文本编辑器

```python
pip install django-tinymce

在 settings install_apps = [
    ...
    'tinymce'
]

TINYMCE_DEFAULT_CONFIG = {
    'theme':'advanced', # 外观 样式
    'width':600,
    'height':400
}
# /static/tinymce/tinymce.min.js 文件在site-package 文件夹 tinymce 文件夹下粘贴到static里
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <script src="/static/tinymce/tinymce.min.js"></script>
    <script>

        tinyMCE.init({
            'mode': 'textareas',
            'width': 800,
            'height': 600
        })

    </script>
    <title>Document</title>
</head>
<body>
<form action="{% url 'APP03:artical' %}" method="post">

    {% csrf_token %}
    <textarea name="content" id="" cols="30" rows="10"></textarea>
    <input type="submit">
</form>
</body>
</html>

```

# 上传下载

```python
# 通过form 表单提交
# enctype="multipart/form-data"
# settings.py  MEDIA_ROOT =  os.path.join(BASE_DIR, 'static/upload')
'''
	file.name
	file.size
	file.read	读取全部（适合小文件）
	file.chunks	按块来返回文件通过for循环迭代，可以将文件按块来写入服务器
	file.multiple_chunks() 判段文件是否大于2.5M 返回True 或 False

'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <form action="/upload/" method="post" enctype="multipart/form-data">
        <input type="file" name="fafafa">
        <input type="submit">
    </form>
</body>
</html>

def uploads(request):
    if request.method == 'POST':  # 获取对象
        obj = request.FILES.get('fafafa')
        import os
        # 上传文件的文件名 　　　　
        f = open(os.path.join(MEDIA_ROOT, 'pic', obj.name), 'wb')
        if obj.multiple_chunks():
            for chunk in obj.chunks():
                f.write(chunk)
            print('大于2.5')
        else:
            f.write(obj.read())
            print('小于2.5')
        f.close()
        return HttpResponse('OK')
    return render(request, 'uploads.html')

```

```python
# 封装上传模块

import os
from datetime import datetime
from random import randint


class FileUpload:
    def __init__(self, file, exts=['png', 'jpg', 'jpeg'], size=1024 * 1024 * 1024, is_ramdom_name=False):
        """
        :param file:  文件上传对象
        :param exts:  文件类型
        :param size:  文件大小 默认1M
        :param is_ramdom_name: 是否随机文件名 默认否
        """
        self.file = file
        self.exts = exts
        self.size = size
        self.is_ramdom_name = is_ramdom_name

    def upload(self, dest):
        """
        :param dest: 文件上传的目标目录
        :return:
        """
        # 判断文件类型是否匹配
        if not self.check_type():
            return -1
        # 判断文件大小是否符合要求
        if not self.check_size():
            return -2
        # 如果是随机文件名，要生成随机文件名
        if self.is_ramdom_name:
            self.file_name = self.random_filename()
        else:
            self.file_name = self.file.name
        # 拼接目标文件路径
        path = os.path.join(dest, self.file_name)

        # 保存文件
        self.write_file(path)
        return 1

    def check_type(self):
        ext = os.path.splitext(self.file.name)  # 作用是分离文件名与扩展名，返回一个元组。 ('a_3', '.py')
        if len(ext) > 1:
            ext = ext[len(ext) - 1].lstrip('.')  # 返回截掉字符串左边的空格或指定字符后生成的新字符串。
            if ext in self.exts:
                return True
        return False

    def check_size(self):
        if self.size < 0:
            return False
        return self.file.size <= self.size

    def random_filename(self):
        filename = datetime.now().strftime('%Y%m%d%H%%M%S') + str(randint(1, 10000))
        ext = os.path.splitext(self.file.name)
        # 获取文件后缀
        ext = ext[len(ext) - 1] if len(ext) > 1 else ''
        filename += ext
        return filename

    def write_file(self, path):
        with open(path, 'wb') as fp:
            if self.file.multiple_chunks():
                for chunk in self.file.chunks():
                    fp.write(chunk)
            else:
                fp.write(self.file.read())
                
                
# 调用

        path = os.path.join(MEDIA_ROOT, 'pic')
        print(path)
        fp = FileUpload(obj, exts=['MOV'])
        result = fp.upload(path)
        if result == -1:
            return HttpResponse('文件类型不匹配')
        elif result == -2:
            return HttpResponse('文件大小不匹配')
        else:
            return HttpResponse('上传成功')
```

# 后台管理

```python
python manage.py createsuperuser

from django.contrib import admin

# Register your models here.
from APP03.models import StudentDetail, User


class StudentDetailAdmin(admin.ModelAdmin):
    list_display = ['email', 'memo']  # 展示什么字段
    search_fields = ['pk']
    # 分页
    list_per_page = 5
    # 过滤字段
    list_filter = ['memo']


admin.site.register(StudentDetail, StudentDetailAdmin)
admin.site.register(User)
```

# 中间件

```python
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class MyMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print(request.user.is_authenticated)
        if request.user.is_authenticated:
            return
        else:
            return redirect('APP03:login') # <======= 如果没登录重定向

        
 # 在setting 中间件中注册

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'APP03.MyMiddleware.MyMiddleware', # <======== 注册中间件
]
# 全局路由保护
class MyMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print(request.path)
        if request.user.is_authenticated or request.path.find('login') != -1 or request.path.find('captcha') != -1:
            return
        else:
            return redirect('APP03:login')
    def process_response(self,request,response):
        # 响应走这
        print('process_response')
        return response
    def process_view(self,request,view_func,view_args,view_kwargs):
        print('在自己的视图函数执行之前执行，每个函数返回的都是None ,如果返回render 或者 response 对象 则跳过自己写的view 直接到 process_response 里')
        return
process_request =====> process_view =======> 自己写的view ======> process_response 

"""
作用有
统计
黑白名单
界面友好化
"""


import sys

from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

# 如果
from django.views.debug import technical_500_response


class MyMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print(request.path)
        if request.user.is_authenticated or request.path.find('login') != -1 or request.path.find('captcha') != -1:
            return
        else:
            return redirect('APP03:login')

    def process_response(self, request, response):
        # 响应走这
        print('process_response')
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('在自己的视图函数执行之前执行，每个函数返回的都是None ,如果返回render 或者 response 对象 则跳过自己写的view 直接到 process_response 里')
        return

    def process_exception(self, request, exception):
        # 异常处理 如果你是本地地址可以看到错误信息，如果不是调到登录页，可以照例写判断404 或者 500
        ip = request.META.get('REMOTE_ADDR')
        if ip == '127.0.0.1':
            return technical_500_response(request, *sys.exc_info())
        return redirect(reverse('APP03:login'))
       
```

# 缓存

```python
# settings 
# 数据库缓存配置
CACHES = {
 'default': {
  'BACKEND': 'django.core.cache.backends.db.DatabaseCache',  # 指定缓存使用的引擎
  'LOCATION': 'cache_table',          # 数据库表    
  'OPTIONS':{
   'MAX_ENTRIES': 300,           # 最大缓存记录的数量（默认300）
   'CULL_FREQUENCY': 3,          # 缓存到达最大个数之后，剔除缓存个数的比例，即：1/CULL_FREQUENCY（默认3）
  }  
 }   
}

# 开发调试
CACHES = {
 'default': {
  'BACKEND': 'django.core.cache.backends.dummy.DummyCache',  # 缓存后台使用的引擎
  'TIMEOUT': 300,            # 缓存超时时间（默认300秒，None表示永不过期，0表示立即过期）
  'OPTIONS':{
   'MAX_ENTRIES': 300,          # 最大缓存记录的数量（默认300）
   'CULL_FREQUENCY': 3,          # 缓存到达最大个数之后，剔除缓存个数的比例，即：1/CULL_FREQUENCY（默认3）
  },
 }
}

# 内存缓存
CACHES = {
 'default': {
  'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',  # 指定缓存使用的引擎
  'LOCATION': 'unique-snowflake',         # 写在内存中的变量的唯一值 
  'TIMEOUT':300,             # 缓存超时时间(默认为300秒,None表示永不过期)
  'OPTIONS':{
   'MAX_ENTRIES': 300,           # 最大缓存记录的数量（默认300）
   'CULL_FREQUENCY': 3,          # 缓存到达最大个数之后，剔除缓存个数的比例，即：1/CULL_FREQUENCY（默认3）
  }  
 }
}

# 文件缓存
CACHES = {
 'default': {
  'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache', #指定缓存使用的引擎
  'LOCATION': '/var/tmp/django_cache',        #指定缓存的路径
  'TIMEOUT':300,              #缓存超时时间(默认为300秒,None表示永不过期)
  'OPTIONS':{
   'MAX_ENTRIES': 300,            # 最大缓存记录的数量（默认300）
   'CULL_FREQUENCY': 3,           # 缓存到达最大个数之后，剔除缓存个数的比例，即：1/CULL_FREQUENCY（默认3）
  }
 }   
}

python manage.py createcachetable # 命令
```

## 全局缓存局部缓存

```python
# 局部缓存
    {% load cache %}
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport"
              content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>cache</title>
    </head>
    <body>
    {% cache 30 'current_time' %}
        {{ current_time }}
    {% endcache %}
    </body>
    </html>

# view缓存

    from datetime import datetime

    from django.shortcuts import render

    # Create your views here.
    from django.views.decorators.cache import cache_page


    # 缓存20秒
    @cache_page(20)
    def index(request):
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(current_time)
        return render(request, 'index.html', locals())
    
# 自定义缓存
    def SetCache(request):
        from django.core.cache import cache
        from django.template import loader

        mycache = cache.get('mycache')
        if mycache:
            html = mycache
        else:
            tem = loader.get_template('mycache.html')
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            html = tem.render({'app': current_time})
            cache.set('mycache', html, 10)
        return HttpResponse(html)
```

# 邮箱验证

```python
# pip install itsdangerous
# token.py
from itsdangerous import URLSafeTimedSerializer as utsr

import base64
from django.conf import settings as django_settings


class Token():
    def __init__(self, security_key):
        self.security_key = security_key
        self.salt = base64.encodebytes(self.security_key.encode('utf8'))

    def generate_validate_token(self, username):
        serializer = utsr(self.security_key)
        return serializer.dumps(username, self.salt)

    def confirm_validate_token(self, token, expiration=3600):
        serializer = utsr(self.security_key)
        return serializer.loads(token, salt=self.salt, max_age=expiration)

    def remove_validate_token(self, token):
        serializer = utsr(self.security_key)
        return serializer.loads(token, salt=self.salt)


token_confirm = Token(django_settings.SECRET_KEY)

```

```python
# views.py
def checkUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        form = {'username': username, 'password': password, 'is_active': 0}
        if User.objects.filter(username=username).first():
            return HttpResponse('用户已存在')
        else:
            user = User.objects.create(**form)
            token = token_confirm.generate_validate_token(user.id)
            print(token)
            url = 'http://' + request.get_host() + reverse('App04:activeuser', kwargs={'token': token})
            print(url)
            html = loader.get_template('email_template.html').render({'url': url})
            # 发送单个
            send_mail('激活账号', '', settings.DEFAULT_FROM_EMAIL,
                      [email], html_message=html, fail_silently=False)
            return HttpResponse('邮件已发送')
    return render(request, 'checkUser.html')


def activeuser(request, token):
    try:
        id = token_confirm.confirm_validate_token(token) # 在上面你传什么进去就接什么出来
    except:
        id = token_confirm.remove_validate_token(token)
        users = User.objects.filter(pk=id)
        for user in users:
            user.delete()
        return HttpResponse('链接过期请重新注册') # 链接过期就删除用户
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return HttpResponse('您验证的用户不存在，请重新注册')
    user.is_active = True
    user.save()
    return HttpResponse('验证成功,请登录')
```

# 异步执行 celery

```python
Celery大于3.1.25的版本不再支持Windows。Windows下推荐安装 3.1.25。(因为我使用的 Windows，这里就以3.1.25为例）
pip install celery== 3.1.25
pip install django-celery django-redis

# python 3.7 async 是关键字 所以在用的时候会出现错误，要把所有async 换成别的字 ，或者安装python 低版本
# 

python manage.py migrate

# celery.py
    # encoding: utf-8
    from __future__ import absolute_import  # 避免就近原则

    import os
    from celery import Celery
    from django.conf import settings

    # 设置项目运行的环境变量DJANGO_SETTINGS_MODULE
    os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                          "DAdmin.settings")   # DAdmin为settings所在的文件（模块）

    #创建celery应用
    app = Celery('AdminCelery')

    # Celery加载配置
    app.config_from_object('django.conf:settings')

    # 如果在工程的应用中创建了tasks.py模块，那么Celery应用就会自动去检索创建的任务。
    # 比如你添加了一个任务，在django中会实时地检索出来。
    app.autodiscover_tasks(lambda :settings.INSTALLED_APPS)
# settings.py
	
######django-celery配置######
import djcelery
from celery.schedules import timedelta,crontab
 
djcelery.setup_loader()  # 开始加载当前所有安装app中的task
 
# 使用redis代理来分发任务
BROKER_URL = 'redis://127.0.0.1:6379/8'
CELERY_IMPORTS = ('post.tasks')  # 导入任务，可以执行的异步任务
CELERY_TIMEZONE = 'Asia/Shanghai'   # 中国时区
 
# 任务存入到数据库中
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
 
# 定时器策略
CELERYBEAT_SCHEDULE = {

        u'邮件发送': {
            "task": "post.tasks.tsend_email",  # 有必要注意该位置的post指tasks.py所在文件夹tsend_email为异步函数之一
            # "schedule": crontab(minute='*/2'),
            "schedule": timedelta(seconds=5),
            "args": (),
        },
        u'性能计算': {
            "task": "post.tasks.add",
            "schedule": crontab(minute='*/2'),
            "args": (1, 4),
        },
    }
	
    CELERYD_CONCURRENCY = 2  # celery worker并发数
    CELERYD_MAX_TASKS_PER_CHILD = 5  # 每个worker最大执行任务数 执行5个就销毁
    CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24  # 后端存储任务超过一天则自动清理
                                                  
    #####django-celery end########
# 在views.py调用
	任务函数名.delay(参数)

    from post.tasks import tsend_email，add

    def sendmail(request):
        ...
        tsend_email.delay()  # 执行任务
        # add.delay(1,2)  # delay(add函数的参数列表)

        return HttpResponse(json.dumps({'status':'ok'}), 'application/json')
# tasks.py
	
    # coding:utf-8
    import time
    from DAdmin.celery import app  #导入celery的实例对象

    @app.task
    def tsend_email():
        time.sleep(10)
        print('send email ok!')


    @app.task
    def add(x, y):
        time.sleep(5)
        return x+y
# 启动work (改动tasks 后必须重启worker)
	celery -A 你的工程名 worker -l info
	
                                                  
                                                  
```

# 日志 django log

```python
import time

cur_path = os.path.dirname(os.path.realpath(__file__))  # log_path是存放日志的路径
log_path = os.path.join(os.path.dirname(cur_path), 'logs')
if not os.path.exists(log_path): os.mkdir(log_path)  # 如果不存在这个logs文件夹，就自动创建一个

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        # 日志格式
        'standard': {
            'format': '[%(asctime)s] [%(filename)s:%(lineno)d] [%(module)s:%(funcName)s] '
                      '[%(levelname)s]- %(message)s'},
        'simple': {  # 简单格式
            'format': '%(levelname)s %(message)s'
        },
    },
    # 过滤
    'filters': {
        # 要求debug false 才记录
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    # 定义具体处理日志的方式
    'handlers': {
        'mail_admins': {  # 上线后出错邮件报错
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false']
        },
        # 默认记录所有日志
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(log_path, 'all-{}.log'.format(time.strftime('%Y-%m-%d'))),
            'maxBytes': 1024 * 1024 * 5,  # 文件大小
            'backupCount': 5,  # 备份数
            'formatter': 'standard',  # 输出格式
            'encoding': 'utf-8',  # 设置默认编码，否则打印出来汉字乱码
        },
        # 输出错误日志
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(log_path, 'error-{}.log'.format(time.strftime('%Y-%m-%d'))),
            'maxBytes': 1024 * 1024 * 5,  # 文件大小
            'backupCount': 5,  # 备份数
            'formatter': 'standard',  # 输出格式
            'encoding': 'utf-8',  # 设置默认编码
        },
        'debug': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(log_path, 'debug-{}.log'.format(time.strftime('%Y-%m-%d'))),
            'maxBytes': 1024 * 1024 * 5,  # 文件大小
            'backupCount': 5,  # 备份数
            'formatter': 'standard',  # 输出格式
            'encoding': 'utf-8',  # 设置默认编码
        },
        # 控制台输出
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        # 输出info日志
        'info': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(log_path, 'info-{}.log'.format(time.strftime('%Y-%m-%d'))),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
            'encoding': 'utf-8',  # 设置默认编码
        },
    },
    # 配置用哪几种 handlers 来处理日志
    'loggers': {
        # 类型 为 django 处理所有类型的日志， 默认调用
        'django': {
            'handlers': ['default', 'console'],
            'level': 'INFO',
            'propagate': False  # 继承父类的信息
        },
        'django.request': {  # 用户请求发生错误
            'handlers': ['debug', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True  # 继承父类的信息
        },
        # log 调用时需要当作参数传入
        'log': {
            'handlers': ['error', 'info', 'console', 'default'],
            'level': 'INFO',
            'propagate': True
        },
    }
}

ADMINS = (('yby', '2694286031@qq.com'),)
# 发送邮件设置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # 固定写法
EMAIL_HOST = 'smtp.163.com'  # SMTP地址
EMAIL_PORT = 25  # SMTP端口
EMAIL_HOST_USER = '18249241924@163.com'  # 发送邮件的邮箱
EMAIL_HOST_PASSWORD = 'LGAGMGHTETRLUCRQ'  # 授权码
EMAIL_SUBJECT_PREFIX = '[杨xx测试] '  # 为邮件Subject-line前缀,默认是'[django]'
EMAIL_USE_TLS = True  # 与SMTP服务器通信时，是否启动TLS链接(安全链接)默认false
DEFAULT_FROM_EMAIL = '贪婪玩月客服中心<18249241924@163.com>'  # 收件人看到的发件人<此处要和发邮件的邮箱相同>

# 配置邮件
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
SERVER_EMAIL = EMAIL_HOST_USER

```

```python
import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler("log.txt")
fomatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')

handler.setFormatter(fomatter)
logger.addHandler(handler)

logger.info('start print log')
logger.debug('start print debug')
logger.warning('start print warning')
logger.info('finish')

```

# model 参数

```python
1、null=True
　　数据库中字段是否可以为空
2、blank=True
　　django的 Admin 中添加数据时是否可允许空值
3、primary_key = False
　　主键，对AutoField设置主键后，就会代替原来的自增 id 列
4、auto_now 和 auto_now_add
　　auto_now   自动创建---无论添加或修改，都是当前操作的时间
　　auto_now_add  自动创建---永远是创建时的时间
5、choices
GENDER_CHOICE = (
        (u'M', u'Male'),
        (u'F', u'Female'),
    )
gender = models.CharField(max_length=2,choices = GENDER_CHOICE)
6、max_length
7、default　　默认值
8、verbose_name　　Admin中字段的显示名称
9、name|db_column　　数据库中的字段名称
10、unique=True　　不允许重复
11、db_index = True　　数据库索引
12、editable=True　　在Admin里是否可编辑
13、error_messages=None　　错误提示
14、auto_created=False　　自动创建
15、help_text　　在Admin中提示帮助信息
16、validators=[]
17、upload-to

更多参数
```

# model 数据类型

```python
1、models.AutoField　　自增列 = int(11)
　　如果没有的话，默认会生成一个名称为 id 的列，如果要显示的自定义一个自增列，必须将给列设置为主键 primary_key=True。
2、models.CharField　　字符串字段
　　必须 max_length 参数
3、models.BooleanField　　布尔类型=tinyint(1)
　　不能为空，Blank=True
4、models.ComaSeparatedIntegerField　　用逗号分割的数字=varchar
　　继承CharField，所以必须 max_lenght 参数
5、models.DateField　　日期类型 date
　　对于参数，auto_now = True 则每次更新都会更新这个时间；auto_now_add 则只是第一次创建添加，之后的更新不再改变。
6、models.DateTimeField　　日期类型 datetime
　　同DateField的参数
7、models.Decimal　　十进制小数类型 = decimal
　　必须指定整数位max_digits和小数位decimal_places
8、models.EmailField　　字符串类型（正则表达式邮箱） =varchar
　　对字符串进行正则表达式
9、models.FloatField　　浮点类型 = double
10、models.IntegerField　　整形
11、models.BigIntegerField　　长整形
　　integer_field_ranges = {
　　　　'SmallIntegerField': (-32768, 32767),
　　　　'IntegerField': (-2147483648, 2147483647),
　　　　'BigIntegerField': (-9223372036854775808, 9223372036854775807),
　　　　'PositiveSmallIntegerField': (0, 32767),
　　　　'PositiveIntegerField': (0, 2147483647),
　　}
12、models.IPAddressField　　字符串类型（ip4正则表达式）
13、models.GenericIPAddressField　　字符串类型（ip4和ip6是可选的）
　　参数protocol可以是：both、ipv4、ipv6
　　验证时，会根据设置报错
14、models.NullBooleanField　　允许为空的布尔类型
15、models.PositiveIntegerFiel　　正Integer
16、models.PositiveSmallIntegerField　　正smallInteger
17、models.SlugField　　减号、下划线、字母、数字
18、models.SmallIntegerField　　数字
　　数据库中的字段有：tinyint、smallint、int、bigint
19、models.TextField　　字符串=longtext
20、models.TimeField　　时间 HH:MM[:ss[.uuuuuu]]
21、models.URLField　　字符串，地址正则表达式
22、models.BinaryField　　二进制
23、models.ImageField   图片
24、models.FilePathField 文件

更多字段
```

# model 操作

```python
基本操作
 1     # 增
 2     #
 3     # models.Tb1.objects.create(c1='xx', c2='oo')  增加一条数据，可以接受字典类型数据 **kwargs
 4 
 5     # obj = models.Tb1(c1='xx', c2='oo')
 6     # obj.save()
 7 
 8     # 查
 9     #
10     # models.Tb1.objects.get(id=123)         # 获取单条数据，不存在则报错（不建议）
11     # models.Tb1.objects.all()               # 获取全部
12     # models.Tb1.objects.filter(name='seven') # 获取指定条件的数据
13 
14     # 删
15     #
16     # models.Tb1.objects.filter(name='seven').delete() # 删除指定条件的数据
17 
18     # 改
19     # models.Tb1.objects.filter(name='seven').update(gender='0')  # 将指定条件的数据更新，均支持 **kwargs
20     # obj = models.Tb1.objects.get(id=1)
21     # obj.c1 = '111'
22     # obj.save()                                                 # 修改单条数据


进阶操作（双下划线）
 1 # 获取个数
 2     #
 3     # models.Tb1.objects.filter(name='seven').count()
 4 
 5     # 大于，小于
 6     #
 7     # models.Tb1.objects.filter(id__gt=1)              # 获取id大于1的值
 8     # models.Tb1.objects.filter(id__lt=10)             # 获取id小于10的值
 9     # models.Tb1.objects.filter(id__lt=10, id__gt=1)   # 获取id大于1 且 小于10的值
10 
11     # in
12     #
13     # models.Tb1.objects.filter(id__in=[11, 22, 33])   # 获取id等于11、22、33的数据
14     # models.Tb1.objects.exclude(id__in=[11, 22, 33])  # not in
15 
16     # contains
17     #
18     # models.Tb1.objects.filter(name__contains="ven")
19     # models.Tb1.objects.filter(name__icontains="ven") # icontains大小写不敏感
20     # models.Tb1.objects.exclude(name__icontains="ven")
21 
22     # range
23     #
24     # models.Tb1.objects.filter(id__range=[1, 2])   # 范围bettwen and
25 
26     # 其他类似
27     #
28     # startswith，istartswith, endswith, iendswith,
29 
30     # order by
31     #
32     # models.Tb1.objects.filter(name='seven').order_by('id')    # asc
33     # models.Tb1.objects.filter(name='seven').order_by('-id')   # desc
34 
35     # limit 、offset
36     #
37     # models.Tb1.objects.all()[10:20]
38 
39     # group by
40     from django.db.models import Count, Min, Max, Sum
41     # models.Tb1.objects.filter(c1=1).values('id').annotate(c=Count('num'))
42     # SELECT "app01_tb1"."id", COUNT("app01_tb1"."num") AS "c" FROM "app01_tb1" WHERE "app01_tb1"."c1" = 1 GROUP BY "app01_tb1"."id"

可以看查询的sql语句，用query方法：
ret = models.UserType.objects.all().values('nid')
print(type(ret), ret.query)
<class 'django.db.models.query.QuerySet'> SELECT `app01_usertype`.`nid` FROM `app01_usertype`

```

class A(models.Model):
name = models.CharField(u’名称’)
class B(models.Model):
aa = models.ForeignKey(A)
B.objects.filter(aa__name__contains=‘searchtitle’)

1.5 我叫它反向查询，后来插入记录1.5，当我知道的时候瞬间就觉得django太太太NX了。
class A(models.Model):
name = models.CharField(u’名称’)
class B(models.Model):
aa = models.ForeignKey(A,related_name=“FAN”)
bb = models.CharField(u’名称’)
查A: A.objects.filter(FAN__bb=‘XXXX’)，都知道related_name的作用，A.FAN.all()是一组以A为外键的B实例，可前面这样的用法是查询出所有(B.aa=A且B.bb=XXXX)的A实例，然后还可以通过__各种关系查找，真赤激！！！

2.条件选取querySet的时候，filter表示=，exclude表示!=。
querySet.distinct() 去重复
__exact 精确等于 like ‘aaa’
__iexact 精确等于 忽略大小写 ilike ‘aaa’
__contains 包含 like ‘%aaa%’
__icontains 包含 忽略大小写 ilike ‘%aaa%’，但是对于sqlite来说，contains的作用效果等同于icontains。
__gt 大于
__gte 大于等于
__lt 小于
__lte 小于等于
__in 存在于一个list范围内
__startswith 以…开头
__istartswith 以…开头 忽略大小写
__endswith 以…结尾
__iendswith 以…结尾，忽略大小写
__range 在…范围内
__year 日期字段的年份
__month 日期字段的月份
__day 日期字段的日
__isnull=True/False

例子：

> > q1 = Entry.objects.filter(headline__startswith=“What”)
> > q2 = q1.exclude(pub_date__gte=datetime.date.today())
> > q3 = q1.filter(pub_date__gte=datetime.date.today())
> >
> > > q = q.filter(pub_date__lte=datetime.date.today())
> > > q = q.exclude(body_text__icontains=“food”)

即q1.filter(pub_date__gte=datetime.date.today())表示为时间>=now，q1.exclude(pub_date__gte=datetime.date.today())表示为<=now

# model 操作详解

《[Django model update的各种用法介绍](https://www.jb51.net/article/165503.htm)》文章介绍了Django model的各种update操作，这篇文章就是她的姊妹篇，详细介绍Django model select的用法，配以对应MySQL的查询语句，理解起来更轻松。

**基本操作**

```python
# 获取所有数据，对应SQL：select * from User
User.objects.all()

# 匹配，对应SQL：select * from User where name = '运维咖啡吧'
User.objects.filter(name='运维咖啡吧')

# 不匹配，对应SQL：select * from User where name != '运维咖啡吧'
User.objects.exclude(name='运维咖啡吧')

# 获取单条数据（有且仅有一条，id唯一），对应SQL：select * from User where id = 724
User.objects.get(id=123)
```

**常用操作**

```python
# 获取总数，对应SQL：select count(1) from User
User.objects.count()

# 获取总数，对应SQL：select count(1) from User where name = '运维咖啡吧'
User.objects.filter(name='运维咖啡吧').count()

# 大于，>，对应SQL：select * from User where id > 724
User.objects.filter(id__gt=724)

# 大于等于，>=，对应SQL：select * from User where id >= 724
User.objects.filter(id__gte=724)

# 小于，<，对应SQL：select * from User where id < 724
User.objects.filter(id__lt=724)

# 小于等于，<=，对应SQL：select * from User where id <= 724
User.objects.filter(id__lte=724)

# 同时大于和小于， 1 < id < 10，对应SQL：select * from User where id > 1 and id < 10
User.objects.filter(id__gt=1, id__lt=10)

# 包含，in，对应SQL：select * from User where id in (11,22,33)
User.objects.filter(id__in=[11, 22, 33])

# 不包含，not in，对应SQL：select * from User where id not in (11,22,33)
User.objects.exclude(id__in=[11, 22, 33])

# 为空：isnull=True，对应SQL：select * from User where pub_date is null
User.objects.filter(pub_date__isnull=True)

# 不为空：isnull=False，对应SQL：select * from User where pub_date is not null
User.objects.filter(pub_date__isnull=True)

# 匹配，like，大小写敏感，对应SQL：select * from User where name like '%sre%'，SQL中大小写不敏感
User.objects.filter(name__contains="sre")

# 匹配，like，大小写不敏感，对应SQL：select * from User where name like '%sre%'，SQL中大小写不敏感
User.objects.filter(name__icontains="sre")

# 不匹配，大小写敏感，对应SQL：select * from User where name not like '%sre%'，SQL中大小写不敏感
User.objects.exclude(name__contains="sre")

# 不匹配，大小写不敏感，对应SQL：select * from User where name not like '%sre%'，SQL中大小写不敏感
User.objects.exclude(name__icontains="sre")

# 范围，between and，对应SQL：select * from User where id between 3 and 8
User.objects.filter(id__range=[3, 8])

# 以什么开头，大小写敏感，对应SQL：select * from User where name like 'sh%'，SQL中大小写不敏感
User.objects.filter(name__startswith='sre')

# 以什么开头，大小写不敏感，对应SQL：select * from User where name like 'sh%'，SQL中大小写不敏感
User.objects.filter(name__istartswith='sre')

# 以什么结尾，大小写敏感，对应SQL：select * from User where name like '%sre'，SQL中大小写不敏感
User.objects.filter(name__endswith='sre')

# 以什么结尾，大小写不敏感，对应SQL：select * from User where name like '%sre'，SQL中大小写不敏感
User.objects.filter(name__iendswith='sre')

# 排序，order by，正序，对应SQL：select * from User where name = '运维咖啡吧' order by id
User.objects.filter(name='运维咖啡吧').order_by('id')

# 多级排序，order by，先按name进行正序排列，如果name一致则再按照id倒叙排列
User.objects.filter(name='运维咖啡吧').order_by('name','-id')

# 排序，order by，倒序，对应SQL：select * from User where name = '运维咖啡吧' order by id desc
User.objects.filter(name='运维咖啡吧').order_by('-id')
```

**进阶操作**

```python
# limit，对应SQL：select * from User limit 3;
User.objects.all()[:3]

# limit，取第三条以后的数据，没有对应的SQL，类似的如：select * from User limit 3,10000000，从第3条开始取数据，取10000000条（10000000大于表中数据条数）
User.objects.all()[3:]

# offset，取出结果的第10-20条数据（不包含10，包含20）,也没有对应SQL，参考上边的SQL写法
User.objects.all()[10:20]

# 分组，group by，对应SQL：select username,count(1) from User group by username;
from django.db.models import Count
User.objects.values_list('username').annotate(Count('id'))

# 去重distinct，对应SQL：select distinct(username) from User
User.objects.values('username').distinct().count()

# filter多列、查询多列，对应SQL：select username,fullname from accounts_user
User.objects.values_list('username', 'fullname')

# filter单列、查询单列，正常values_list给出的结果是个列表，里边里边的每条数据对应一个元组，当只查询一列时，可以使用flat标签去掉元组，将每条数据的结果以字符串的形式存储在列表中，从而避免解析元组的麻烦
User.objects.values_list('username', flat=True)

# int字段取最大值、最小值、综合、平均数
from django.db.models import Sum,Count,Max,Min,Avg

User.objects.aggregate(Count(‘id'))
User.objects.aggregate(Sum(‘age'))
```

**时间字段**

```python
# 匹配日期，date
User.objects.filter(create_time__date=datetime.date(2018, 8, 1))
User.objects.filter(create_time__date__gt=datetime.date(2018, 8, 2))

# 匹配年，year
User.objects.filter(create_time__year=2018)
User.objects.filter(create_time__year__gte=2018)

# 匹配月，month
User.objects.filter(create_time__month__gt=7)
User.objects.filter(create_time__month__gte=7)

# 匹配日，day
User.objects.filter(create_time__day=8)
User.objects.filter(create_time__day__gte=8)

# 匹配周，week_day
 User.objects.filter(create_time__week_day=2)
User.objects.filter(create_time__week_day__gte=2)

# 匹配时，hour
User.objects.filter(create_time__hour=9)
User.objects.filter(create_time__hour__gte=9)

# 匹配分，minute
User.objects.filter(create_time__minute=15)
User.objects.filter(create_time__minute_gt=15)

# 匹配秒，second
User.objects.filter(create_time__second=15)
User.objects.filter(create_time__second__gte=15)


# 按天统计归档
today = datetime.date.today()
select = {'day': connection.ops.date_trunc_sql('day', 'create_time')}
deploy_date_count = Task.objects.filter(
 create_time__range=(today - datetime.timedelta(days=7), today)
).extra(select=select).values('day').annotate(number=Count('id'))
```

**Q 的使用**

Q对象可以对关键字参数进行封装，从而更好的应用多个查询，可以组合&(and)、|(or)、~(not)操作符。

例如下边的语句

```python
from django.db.models import Q

User.objects.filter(
 Q(role__startswith='sre_'),
 Q(name='公众号') | Q(name='运维咖啡吧')
)
```

转换成SQL语句如下：

> select * from User where role like 'sre_%' and (name='公众号' or name='运维咖啡吧')

通常更多的时候我们用Q来做搜索逻辑，比如前台搜索框输入一个字符，后台去数据库中检索标题或内容中是否包含

```python
_s = request.GET.get('search')

_t = Blog.objects.all()
if _s:
 _t = _t.filter(
 Q(title__icontains=_s) |
 Q(content__icontains=_s)
 )

return _t
```

外键：ForeignKey

表结构：

```python
class Role(models.Model):
 name = models.CharField(max_length=16, unique=True)


class User(models.Model):
 username = models.EmailField(max_length=255, unique=True)
 role = models.ForeignKey(Role, on_delete=models.CASCADE)
```

正向查询:

> \# 查询用户的角色名
> _t = User.objects.get(username='运维咖啡吧')
> _t.role.name

反向查询：

> \# 查询角色下包含的所有用户
> _t = Role.objects.get(name='Role03')
> _t.user_set.all()

另一种反向查询的方法：

> _t = Role.objects.get(name='Role03')
>
> \# 这种方法比上一种_set的方法查询速度要快
> User.objects.filter(role=_t)

第三种反向查询的方法：

如果外键字段有related_name属性，例如models如下：

```python
class User(models.Model):
 username = models.EmailField(max_length=255, unique=True)
 role = models.ForeignKey(Role, on_delete=models.CASCADE,related_name='roleUsers')
```

那么可以直接用related_name属性取到某角色的所有用户

> _t = Role.objects.get(name = 'Role03')
> _t.roleUsers.all()

**M2M：ManyToManyField**

表结构：

> class Group(models.Model):
> name = models.CharField(max_length=16, unique=True)
>
> class User(models.Model):
> username = models.CharField(max_length=255, unique=True)
> groups = models.ManyToManyField(Group, related_name='groupUsers')

正向查询:

> \# 查询用户隶属组
> _t = User.objects.get(username = '运维咖啡吧')
> _t.groups.all()

反向查询：

> \# 查询组包含用户
> _t = Group.objects.get(name = 'groupC')
> _t.user_set.all()

同样M2M字段如果有related_name属性，那么可以直接用下边的方式反查

> _t = Group.objects.get(name = 'groupC')
> _t.groupUsers.all()

**get_object_or_404**

正常如果我们要去数据库里搜索某一条数据时，通常使用下边的方法：

> _t = User.objects.get(id=734)

但当id=724的数据不存在时，程序将会抛出一个错误

abcer.models.DoesNotExist: User matching query does not exist.

为了程序兼容和异常判断，我们可以使用下边两种方式:

**方式一：get改为filter**

> _t = User.objects.filter(id=724)
> \# 取出_t之后再去判断_t是否存在

**方式二：使用get_object_or_404**

> from django.shortcuts import get_object_or_404
>
> _t = get_object_or_404(User, id=724)
> \# get_object_or_404方法，它会先调用django的get方法，如果查询的对象不存在的话，则抛出一个Http404的异常

实现方法类似于下边这样：

```python
from django.http import Http404

try:
 _t = User.objects.get(id=724)
except User.DoesNotExist:
 raise Http404
get_or_create
```

顾名思义，查找一个对象如果不存在则创建，如下：

object, created = User.objects.get_or_create(username='运维咖啡吧')

返回一个由object和created组成的元组，其中object就是一个查询到的或者是被创建的对象，created是一个表示是否创建了新对象的布尔值

实现方式类似于下边这样：

```python
try:
 object = User.objects.get(username='运维咖啡吧')
 created = False
exception User.DoesNoExist:
 object = User(username='运维咖啡吧')
 object.save()

 created = True

returen object, created
```

**执行原生SQL**

Django中能用ORM的就用它ORM吧，不建议执行原生SQL，可能会有一些安全问题，如果实在是SQL太复杂ORM实现不了，那就看看下边执行原生SQL的方法，跟直接使用pymysql基本一致了

```python
from django.db import connection

with connection.cursor() as cursor:
 cursor.execute('select * from accounts_User')
 row = cursor.fetchall()

return row
```

注意这里表名字要用app名+下划线+model名的方式