# 目录

[TOC]

# REST



| 标题     | 解释                                                         |
| -------- | ------------------------------------------------------------ |
| REST     | REST -- REpresentational State Transfer 直接翻译：表现层状态转移 |
| RESTful  | REST描述的是在网络中client和server的一种交互形式；REST本身不实用，实用的是如何设计 RESTful API（**REST风格的网络接口**）； |
|          | REST -- REpresentational State Transfer 首先，之所以晦涩是因为前面主语被去掉了，全称是 Resource Representational State Transfer：通俗来讲就是：资源在网络中以某种表现形式进行状态转移。分解开来： Resource：资源，即数据（前面说过网络的核心）。比如 newsfeed，friends等； <br/>Representational：某种表现形式，比如用JSON，XML，JPEG等；<br/> State Transfer：状态变化。通过HTTP动词实现。 |
| 极简解释 | **看Url就知道要什么<br/>看http method就知道干什么<br/>看http status code就知道结果如何** |
|          | **REST 是面向资源的，这个概念非常重要，而资源是通过 URI 进行暴露。** <br>URI 的设计只要负责把资源通过合理方式暴露出来就可以了。对资源的操作与它无关，操作是通过 HTTP动词来体现，所以REST 通过 URI 暴露资源时，会强调不要在 URI 中出现动词。 |

# django REST framework (drf)

- 准确的说 这应该是django REST 风格的 写前后端分离API 的框架

```python
# pip install djangorestframework
# pip freeze
# pip list
# pip install psm # 包管理
# pip ls

```

##### Django REST framework 简介

序列化和反序列化可以复用
 增：效验请求数据 > 执行反序列化过程 > 保存数据库 > 将保存的对象序列化并返回
 删：判断要删除的数据是否存在 > 执行数据库删除
 改：判断要修改的数据是否存在 > 效验请求的参数 > 执行反序列化过程 > 保存数据库 > 将保存的对象序列化并返回
 查：查询数据库 > 将数据序列化并返回
 特点:

1. 提供了定义序列化器Serializer的方法,可以快速根据Django ORM 或者其他库自动序列化/反序列化
2. 提供了丰富的类视图\MIXIN扩展类,简化视图的编写
3. 丰富的定制层级:函数视图\类视图\试图结合到自动生成API,满足各种需要
4. 多种身份认证和权限认证方式的支持
5. 内置了限流系统
6. 直观的API web界面
7. 可扩展性 , 插件丰富

##### Django rest framework核心任务

1. 多了个serializer.py文件
    这个文件的作用是`Serializers`把`querysets`和`model instances`这些复杂的数据结构转化为`native python`以便以`json`，`xml`或其他内容类型的形式`render`出去。
2. 视图的核心功能变了

1. 将数据库数据序列化为前端需要的格式并返回；
2. 将前端发送过来的数据反序列化为模型类型对象，并保存到数据库中。

### 开始Django rest framework旅程

###### 安装第三方库



```undefined
pip install django
pip install djangorestframework
```

###### 配置

- 在settings.py的app中添加



```bash
INSTALLED_APPS = [
    'rest_framework', # DRF
]
```

###### 创建模型类(Model)



```python
# 栏目
class Column(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='栏目','help_text':'帮助信息')
    link_url = models.URLField(verbose_name= '链接')
    index = models.IntegerField(verbose_name='位置')
	# null=True 不允许为空
    class Meta:  # 模型元选项
        db_table = 'tb_column'   # 在数据库中的表名，否则Django自动生成为app名字_类名
        ordering = ['index']
        verbose_name = '栏目'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
```

###### 创建一个序列化类(Serializer)

在app目录下新建`serializer.py`



```python
from rest_framework import serializers
from article.models import Column

class ColumnSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20, label='栏目')
    link_url = serializers.URLField(label= '链接')
    index = serializers.IntegerField(label='位置')


    def create(self, validated_data): # create()和update()方法定义了在调用serializer.save()时成熟的实例是如何被创建和修改的。
        return Column.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.link_url = validated_data.get('link_url', instance.link_url)
        instance.index = validated_data.get('index', instance.index)
        instance.save()
        return instance
```

**注意**
 各字段与模型类中的字段是否一致。

###### 编写视图(APIView)



```python
from article.models import Column
from .serializers import ColumnSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class ColumnView(APIView):
    def get(self, request):
        # 获取queryset
        columns = Column.objects.all()
        # 开始序列化；
        serializer_data = ColumnSerializer(columns, many=True)

        #print(serializer_data)

        # print(serializer_data.data)

        # 获取序列化后的数据，返回给客户端
        return Response(serializer_data.data)

    def post(self, request):
        # 获取数据
        client_data = request.data

        # 序列化数据
        verified_data = ColumnSerializer(data=client_data)
        #print(verified_data)
+

        # 校验数据
        if verified_data.is_valid():
            column = verified_data.save()
            #print(verified_data.data) # 需要保存之后才能获取.data
            return Response(verified_data.data)
        else:
            return Response(verified_data.errors, status=400)
    
      
     def put(self, request, column_id):
           column_obj =  Column.objects.get(pk=column_id)
           verified_data = ColumnSerializer(instance=column_obj , data=request.data)
            # 校验数据
            if verified_data.is_valid():
                column = verified_data.save()
                #print(verified_data.data) # 需要保存之后才能获取.data
                return Response(verified_data.data)
            else:
                return Response(verified_data.errors, status=400)
              
      def delete(self, request, column_id):
            column_obj =  Column.objects.get(pk=column_id)
            column_obj.delete()
            return Response({'message': 'OK'})                
           
            
```

###### 配置URL地址



```bash
app_name = 'api'
urlpatterns = [
      path('column/', ColumnView.as_view(), name='column'),
]
```

###### 利用postman测试

get获取数据列表信息



![img](https:////upload-images.jianshu.io/upload_images/9286065-b1e055972fec451d.png?imageMogr2/auto-orient/strip|imageView2/2/w/992/format/webp)

get方法中两个输出语句为

![img](https:////upload-images.jianshu.io/upload_images/9286065-edf11364ed321894.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)
 post增加数据：

![img](https:////upload-images.jianshu.io/upload_images/9286065-7ccc421c6cda1439.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

输出语句

![img](https:////upload-images.jianshu.io/upload_images/9286065-4484bbc2f66a0495.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

我们将视图修改下，获取单个数据

![img](https:////upload-images.jianshu.io/upload_images/9286065-e4b98bf157a77e3e.png?imageMogr2/auto-orient/strip|imageView2/2/w/760/format/webp)

![img](https:////upload-images.jianshu.io/upload_images/9286065-539253ad8b238e83.png?imageMogr2/auto-orient/strip|imageView2/2/w/596/format/webp)

由以上可以看出API与我们的表单(forms)很相似，除了将模型实例(model instance)序列化外，我们也能序列化查询集(querysets)，只需要添加一个序列化参数many=True。

#### 使用模型序列化ModelSerializers

我们定义的ColumnSerializer类字段和模型字段有很多是重复的，为了保证代码简洁，减少重复， 我们可以类似于Django提供表单(Form)类和模型表单(ModelForm)类相同的方式，REST framework也提供了Serializer和ModelSerializer。下面我们重写ColumnSerializer类。



```python
class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = ['name', 'link_url', 'index']
	    # fields = "__all__"
	    # exclude = ["name"] 除了name 属性的全部
        # extra_kwargs = { 额外键
        #	'bread':{'minvalue':0,'required':True,'help_text':'帮助信息'}
        #}
        # 在这里面是自动生成create 和 update 的
```

测试结果和使用

![img](https:////upload-images.jianshu.io/upload_images/9286065-4620cbef0e9d6f32.png?imageMogr2/auto-orient/strip|imageView2/2/w/558/format/webp)
**注意：**要记住 ModelSerializer 不做任何格外的配置，它只是创建序列化类的快捷方式：
 1.根据model里的字段自动定义字段集
 2.简单的实现 create() and update() 方法，不像使用还要Serializer，自定义create()和update()方法定义了在调用serializer.save()实例是如何被创建和修改的。

## validate 自定义校验

```python
# vaildate_<field_name>
class ColumnSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=20, label='栏目')
   # 1 单个校验
	def validate_name(self,value):
    	if ...
        	raise serializers.ValidationError("报错信息")
        return value
   # 2 全部校验
    def validate(self,attr):
        name = attr['name']
        if ...:
        	raise serializers.ValidationError("报错信息")
        return attr
# 3 补充校验
def about_django(value):
    if value.....:
        raise serializers.ValidationError("报错信息")
class ColumnSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20, label='栏目')
    link_url = serializers.URLField(label= '链接' validators=[about_django])
    index = serializers.IntegerField(label='位置')
```

## 自定义解析器

```python

from rest_framework.parsers import JSONParser
# views里 加
parser_classes = (JSONParser,)
```

## request response

```python
# request.query_params get 请求参数用这个查
# request.data post 用这个

response(data,status=None,template_name=None,headers=None,content_type=None)
```

## fbv 写法

```python
@api_view(['GET','POST'])
def method(request):
	pass
```

# Django使用Pyjwt、rest-framework、rest-framework-jwt 生成token

# Token

在移动端开发或者前后端分离开发时，我们会经常用到token(令牌)来验证并保留登录状态，通过向登录接口以post请求方式来发送登录表单获取token，将token保存到本地，并在请求需要身份认证的 url 时，将token放到请求头中就可以直接访问，不用再登录。

token生成的方法有很多种，我们这里不关注具体的生成算法，只是关注功能性实现。

## 注意事项

需要有一定的django基础，如果一点基础都没有，不建议查看。

```python
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
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from App.auth import token_confirm
import itsdangerous

class MyAuth(BaseAuthentication):
    def authenticate(self, request):
        token = request.query_params.get('token')
        try:
            user = token_confirm.confirm_validate_token(token, expiration=6)
        except itsdangerous.exc.SignatureExpired as e:
            raise exceptions.AuthenticationFailed({'code': 200, 'mes': 'token过期请重新登陆'})
        except:
            return None
        return user, token
```



## **1. 局部视图认证(**自定义Token认证**)**



```
model类


# Create your models here.
from django.db import models
# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=32)
    price=models.IntegerField()
    # pub_date=models.DateField(auto_now=True)
    publish=models.ForeignKey("Publish",on_delete=models.CASCADE)      # ForeignKey一对多
    authors=models.ManyToManyField("Author")        # ManyToManyField  多对多
    def __str__(self):
        return self.title

class Publish(models.Model):
    name=models.CharField(max_length=32)
    email=models.EmailField()
    def __str__(self):
        return self.name

class Author(models.Model):
    name=models.CharField(max_length=32)
    age=models.IntegerField()
    def __str__(self):
        return self.name


class User(models.Model):
    name=models.CharField(max_length=32)
    pwd=models.CharField(max_length=32)


class Token(models.Model):
    user=models.OneToOneField("User",on_delete=models.CASCADE)
    token = models.CharField(max_length=128)
    def __str__(self):
        return self.token
```



```python
viwes

from rest_framework import mixins
from rest_framework import generics
from .models import *
from rest_framework import serializers
from django.core import serializers
import  json
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views import View




from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication
# 局部视图认证  自定义认证类
class TokenAuth(BaseAuthentication):   
    def authenticate(self,request):     
        token = request.GET.get("token")
        token_obj = Token.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed("验证失败123!")
        else:
            return token_obj.user.name,token_obj.token


"""class TokenAuth2(object):
    def authenticate(self,request):
        token = request.GET.get("token")
        token_obj = Token.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed({'code': 200, 'mes': 'token过期请重新登陆'})
        else:
            return token_obj.user.name,token_obj.token
"""




# 随机字符串token值
def get_random_str(user):
    import hashlib,time
    ctime=str(time.time())
    md5=hashlib.md5(bytes(user,encoding="utf8"))
    md5.update(bytes(ctime,encoding="utf8"))
    return md5.hexdigest()

from .models import User




# 登录视窗
class LoginView(APIView):
    authentication_classes = [TokenAuth,]   # 局部视图认证
    def post(self,request):
        name=request.data.get("name")
        pwd=request.data.get("pwd")
        user=User.objects.filter(name=name,pwd=pwd).first()
        print(user,name,pwd,"222222222222222")
        res = {"state_code": 1000, "msg": None}
        if user:
            random_str=get_random_str(user.name)
            token = Token.objects.update_or_create(user=user, defaults={"token": random_str})
            res["token"]=random_str
        else:
            res["state_code"]=100               #错误状态码
            res["msg"] = "用户名或者密码错误"
        import json
        return Response(json.dumps(res,ensure_ascii=False))
```

```python
 url(r'^login/$', views.LoginView.as_view(), name="login"),
```

## **2.** 全局级别认证

```python
settings.py配置如下：

REST_FRAMEWORK={
    "DEFAULT_AUTHENTICATION_CLASSES":["myapp.auth.Authentication",]
}
```

```python
在setting中设置

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # django默认session校验：校验规则 游客 及 登录用户
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.AllowAny',
        # 全局配置：一站式网站（所有操作都需要登录后才能访问）
        # 'rest_framework.permissions.IsAuthenticated',
    ],
}
```

## 使用PyJWT生成token

首先安装pyjwt包

```python
pip install pyjwt
```

创建Pyjwt_demo项目，在settings.py文件中关闭 csrf 防护。

```python
 # 'django.middleware.csrf.CsrfViewMiddleware',
```

#### 前期工作

###### 创建 account app

```powershell
python manage.py startapp account
```

###### 自定义 User 模型

```python
from datetime import datetime, timedelta
import jwt
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from shortuuidfield import ShortUUIDField
from django.db import models


class UserManager(BaseUserManager):
    def _create_user(self,username,password,**kwargs):
        if not username:
            raise ValueError('请传入用户名！')
        if not password:
            raise ValueError('请传入密码！')

        user = self.model(username=username,**kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_user(self,username,password,**kwargs):
        kwargs['is_superuser'] = False
        return self._create_user(username,password,**kwargs)

    def create_superuser(self,username,password,**kwargs):
        kwargs['is_superuser'] = True
        kwargs['is_staff'] = True
        return self._create_user(username,password,**kwargs)


class User(AbstractBaseUser,PermissionsMixin):

    email = models.EmailField(unique=True,null=True)
    username = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    data_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'

    objects = UserManager()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username
	
	# 此处是用户模型中生成token的方法
    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        token = jwt.encode({
            'exp': datetime.utcnow() + timedelta(days=1),# 这个地方设置token的过期时间。
            'iat': datetime.utcnow(),
            'data': {
                'username': self.username
            }
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')
```

###### 注册模型

在setting.py中添加

```python
AUTH_USER_MODEL = 'account.User'
```

###### 模型迁移生成超级用户

```powershell
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 编写工具类

我们在这里编写两个工具类，一个是我们返回接口的规范，一个是我们在视图函数中验证token是否符合要求的函数。
在account目录下新建一个utils.py 文件。

```python
import jwt
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied

UserModel = get_user_model()

def auth_permission_required(perm):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            # 格式化权限
            perms = (perm,) if isinstance(perm, str) else perm

            if request.user.is_authenticated:
                # 正常登录用户判断是否有权限
                if not request.user.has_perms(perms):
                    raise PermissionDenied
            else:
                try:
                    auth = request.META.get('HTTP_AUTHORIZATION').split()
                except AttributeError:
                    return result(401,"No authenticate header")

                # 用户通过 API 获取数据验证流程
                if auth[0].lower() == 'token':
                    try:
                        dict = jwt.decode(auth[1], settings.SECRET_KEY, algorithms=['HS256'])
                        username = dict.get('data').get('username')
                    except jwt.ExpiredSignatureError:
                        return result(401,"Token expired")
                    except jwt.InvalidTokenError:
                        return result(401,"Invalid token")
                    except Exception as e:
                        return result(401,"Can not get user object")

                    try:
                        user = UserModel.objects.get(username=username)
                    except UserModel.DoesNotExist:
                        return result(401,"User Does not exist")

                    if not user.is_active:
                        return result(401,"User inactive or deleted")

                    # Token 登录的用户判断是否有权限
                    if not user.has_perms(perms):
                        return result(401,"PermissionDenied")
                else:
                    return result(401,"Not support auth type")

            return view_func(request, *args, **kwargs)

        return _wrapped_view

    return decorator

# 接口规范 code  message=""  data:{}
def result(code=200,message="",data=None,kwargs=None):
    json_dict = {"code":code,"message":message,"data":data}

    if kwargs and isinstance(kwargs,dict) and kwargs.keys():
        json_dict.update(kwargs)

    return JsonResponse(json_dict)
```

### 编写视图函数

在views.py中编写一下代码

```python
from django.contrib.auth import authenticate
from django.contrib.auth.views import login
from django.http import JsonResponse
from django.shortcuts import render
# Create your views here
from .utils import result, auth_permission_required
from django.views.decorators.http import require_POST

#登录视图分发token，只要用户名和密码正确就分发token
@require_POST
def user_login(request):

    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)
    if user is None:
        return result(200, "用户名或者密码错误！")
    login(request, user)
    # 分发token
    token = user.token

    return result(200,"登录成功", {"token":token})

#之前定义的验证函数
@auth_permission_required("account.User")
def token_test(request):
    return result(200,"认证成功")
```

### 编写路由

在urls中根据以下代码进行编写视图路由。

```python
from django.contrib import admin
from django.urls import path
from account import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", views.user_login),
    path('tokentest/', views.token_test),

]

```

到这里代码编写的任务就完成了，下一步就是测试，我们使用postman来测试。
使用post，填写好用户名和密码就可以获取token。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200803203448709.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2x3dWlzXw==,size_16,color_FFFFFF,t_70)
在请求头中添加Authentication信息，值为‘token '+token。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200803203555448.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2x3dWlzXw==,size_16,color_FFFFFF,t_70)
如果不加token，就会显示错误。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200803204403205.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2x3dWlzXw==,size_16,color_FFFFFF,t_70)

## 使用rest-framework生成token

rest-framework是通过生成一张token表的方式来验证token的。
安装rest-framework

```powershell
pip install djangorestframework

```

前期工作同上，新建drf_token_demo项目，但是在执行模型迁移之前，我们需要在settings.py中添加如下信息。

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'account',
    'rest_framework.authtoken', # 一定添加上
]
```

### 工具类

为了统一接口规范，我们还是在account文件夹下新建utils.py文件

```python
from django.http import JsonResponse


def result(code=200,message="",data=None,kwargs=None):
    json_dict = {"code":code,"message":message,"data":data}

    if kwargs and isinstance(kwargs,dict) and kwargs.keys():
        json_dict.update(kwargs)

    return JsonResponse(json_dict)
```

### 编写视图函数

```python
from django.contrib.auth import authenticate
from django.contrib.auth.views import login
from django.shortcuts import render

# Create your views here.
from django.views.decorators.http import require_POST
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated

#登录并返回token
@require_POST
def user_login(request):

    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)
    if user is None:
        return result(200, "用户名或者密码错误！")
    login(request, user)

	#把之前已经产生的token删除掉，在添加新的token
    token = Token.objects.filter(user=user)
    token.delete()
    token = Token.objects.create(user=user).key

    return result(200,"登录成功", {"token":token})

#这个地方authentication_classes((TokenAuthentication,))是用来验证token是否正确，@permission_classes((IsAuthenticated,))是用来添加权限，只有被认证的用户才能访问，api_view是限制访问的方式。
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
@authentication_classes((TokenAuthentication,))
def token_test(request):
    return result(200,"认证成功")

```

### 编写路由

```python
from django.contrib import admin
from django.urls import path
from account import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.user_login),
    path('tokentest/', views.token_test),
]
```

使用和上面相同的方法测试即可，可能生成的token看起来不一样，这个无所谓，注意这个地方还是在token前加上’token ‘的前缀。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200803210051858.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2x3dWlzXw==,size_16,color_FFFFFF,t_70)

### token过期问题

在这个地方我们发现没有给token设置期限，这是个很严重的问题，通过缺少自定义化，我们可以通过使用自定义的验证方法实现。
在utils.py中添加如下代码，注意在设置里面设置了时区 USE_TZ = False，如果使用utc这里需要改变。

```python
import jwt
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied
class ExpiringTokenAuthentication(BaseAuthentication):
    model = Token

    def authenticate(self, request):
        auth = get_authorization_header(request)
        if not auth:
            return None
        try:
            token = auth.decode().split()[-1]
            print(token)
        except UnicodeError:
            msg = ugettext_lazy("无效的Token， Token头不应包含无效字符")
            raise exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(token)

    def authenticate_credentials(self, key):
        # 尝试从缓存获取用户信息（设置中配置了缓存的可以添加，不加也不影响正常功能）
        token_cache = 'token_' + key
        cache_user = cache.get(token_cache)
        if cache_user:
            return cache_user, cache_user  # 这里需要返回一个列表或元组，原因不详
        # 缓存获取到此为止

        # 下面开始获取请求信息进行验证
        try:
            token = self.model.objects.get(key=key)
        except self.model.DoesNotExist:
            raise exceptions.AuthenticationFailed("认证失败")

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed("用户被禁用")

        # Token有效期时间判断（注意时间时区问题）
        # 我在设置里面设置了时区 USE_TZ = False，如果使用utc这里需要改变。
        if (datetime.datetime.now() - token.created) > datetime.timedelta(seconds=60):
            raise exceptions.AuthenticationFailed('认证信息已过期')

        # 加入缓存增加查询速度，下面和上面是配套的，上面没有从缓存中读取，这里就不用保存到缓存中了
        if token:
            token_cache = 'token_' + key
            cache.set(token_cache, token.user, 600)

        # 返回用户信息
        return token.user, token

    def authenticate_header(self, request):
        return 'Token'

```

修改views.py, 添加如下代码。

```python
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
@authentication_classes((ExpiringTokenAuthentication,)) #这是我们自己定义的验证类，需要将其导入进来
def token_test_timestamp(request):
    return result(200,"期限token认证成功")

```

url 里新加一条：

```python
path('tokenteststamp/', views.token_test_timestamp),

```

访问这个 url 便可以验证token是否过期。

## 使用django-rest-framework-jwt生成token

我们使用jwt有什么好处呢，目前看来它可以配置token过期时间。

```powershell
pip install djangorestframework-jwt
```

前期工作同上，新建drf_jwt_token_demo项目，但是在执行模型迁移之前，我们需要在settings.py中添加如下信息。

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'account',
    'rest_framework-jwt', # 一定添加上
]
```

同样新建utils.py,这里不再赘述。

### 编写视图函数

我们在这个地方使用api_settings来生成token，官方文档有自己自定义的方法，可以自行查看。

```python
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import permission_classes, authentication_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.settings import api_settings
# Create your views here.
from account.utils import result


def user_login(request):

    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user is None:
        return result(200, "用户名或者密码错误！")

    login(request, user)

    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

    payload = jwt_payload_handler(user)
    token = jwt_encode_handler(payload)

    return JsonResponse({"code":200, "token": token})

@api_view(["GET",])
@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))# 这里使用JSONWebTokenAuthentication来验证
def token_test(request):

    return JsonResponse({"code":200,"message":"successful"})

1234567891011121314151617181920212223242526272829303132333435363738
```

在settings.py中加入以设置过期时间

```python
JWT_AUTH = {
    # 设置token有效期时间
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=60 * 60 * 2)
}
1234
```

### 编写路由

```python
from django.contrib import admin
from django.urls import path
from account import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.user_login),
    path('tokentest/', views.token_test),
]

12345678910
```

接下来就是验证啦，这里一切同上面验证的方法一致，但是这个地方我们生成的token是JWT类型的，所以token的前缀不再是’token ‘，而是JWT。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200803212321208.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2x3dWlzXw==,size_16,color_FFFFFF,t_70)
你可能会问，这个地方我们能不能像第二种一样自定义验证类呢？完全可以，你可以把第二种里的验证类直接放到这里来使用，但是这个时候就要注意token前缀不再是’JWT‘，而是原来的’token ‘。可以自行验证。

在本篇博文编写过程中参考了以下文章：
[Django+JWT 实现 Token 认证](https://www.v2ex.com/t/530103)
[Django 用户登录校验以及接口token校验](https://www.jianshu.com/p/410208cd9b1a)
[适合小白的Django rest_framework Token入门](https://blog.csdn.net/yueguangMaNong/article/details/90519819)

历经了三天时间，终于把这个概念和源码搞清楚了，这里提醒大家多看官方说明文档，多思考，坚持就是胜利。如果有问题可以私信我或者向我的邮箱lkzhang98@163.com 发送邮件。欢迎关注我的微信公众号Pkill，之后有很多技术文章推送。
三种类型的源代码地址均已上传，地址如下：
https://download.csdn.net/download/lwuis_/12683638
https://download.csdn.net/download/lwuis_/12683634
https://download.csdn.net/download/lwuis_/12683462





# [前后端分离djangorestframework——权限组件](https://www.cnblogs.com/Eeyhan/p/10426702.html)

## 权限permissions

**权限验证必须要在认证之后验证**

 

权限组件也不用多说，读了源码你就很清楚了，跟认证组件很类似

 

具体的源码就不展示，自己去读吧，都在这里：

![img](https://img2018.cnblogs.com/blog/1249183/201902/1249183-20190224163533456-1037276799.png)

 

![img](https://img2018.cnblogs.com/blog/1249183/201902/1249183-20190224163533684-1511830361.png)

 

 

### 局部权限

 

设置model表，其中的type就是用户类型

![img](https://img2018.cnblogs.com/blog/1249183/201902/1249183-20190224161033124-758330586.png)

 

数据库：

![img](https://img2018.cnblogs.com/blog/1249183/201902/1249183-20190224161058646-939954563.png)

 

在根目录创建utils，utils创建permission文件，在其中定义权限类，自定义的权限类必须继承BasePermission类，且必须定义has_permission方法，其中message是权限验证没通过时显示的字段

![img](https://img2018.cnblogs.com/blog/1249183/201902/1249183-20190224161959414-1630584636.png)

 

url:

![img](https://img2018.cnblogs.com/blog/1249183/201902/1249183-20190224162203232-526026158.png)

![img](https://img2018.cnblogs.com/blog/1249183/201902/1249183-20190224162216068-285757073.png)

 

view:

![img](https://img2018.cnblogs.com/blog/1249183/201902/1249183-20190224162329987-1832009519.png)

 

 开始访问，刚才说了权限是在用户登录认证之后做的处理，所以也必须带上token访问：

![img](https://img2018.cnblogs.com/blog/1249183/201902/1249183-20190224162514551-706420828.png)

好现在是无权访问，修改用户的type为1看看：

![img](https://img2018.cnblogs.com/blog/1249183/201902/1249183-20190224162821946-2116437394.png)

 

重启项目再次访问：

![img](https://img2018.cnblogs.com/blog/1249183/201902/1249183-20190224162912243-501299383.png)

 

 

 

如果不带token访问：

![img](https://img2018.cnblogs.com/blog/1249183/201902/1249183-20190224162546326-1417400580.png)

 

所以其实在定义的权限类那里可以先作判断是否用户已通过认证，这个可以自行研究



主要代码：

```python
from rest_framework.views import APIView
from rest_framework.views import Response
from utils.auth import MyAuth
from utils.permisson import MyPermission
from DRF.models import User
import uuid


class DemoView(APIView):
    def get(self, request):
        return Response('简单认证')


class LoginView(APIView):
    def get(self, request):
        return Response('请登录，如果没有账号请创建')

    def post(self, request):
        user = request.data.get('user')
        pwd = request.data.get('pwd')
        token = uuid.uuid4()
        User.objects.create(user=user, pwd=pwd, token=token)
        return Response('创建用户成功')


class TestView(APIView):
    authentication_classes = [MyAuth, ]
    permission_classes = [MyPermission, ]

    def get(self, request):
        return Response('权限等级测试，VIP用户您好，欢迎访问XX。。。')
```



permission:



```python
from rest_framework.permissions import BasePermission


class MyPermission(BasePermission):
    message = '无权访问，您的用户等级太低，充值888元立得永久VIP特权 '

    def has_permission(self, request, view):
        user_obj = request.user
        if user_obj.type == 3:
            return False
        else:
            return True
```



### 全局权限

 

 根据前面的认证组件，按同样的套路，全局自然就直接在配置问题里添加就完事儿了，我空出来的地方就是需要添加的权限，自然也是一个列表，跟认证组件一样的写法

![img](https://img2018.cnblogs.com/blog/1249183/201902/1249183-20190224163729971-1784712335.png)

 

当然权限也有自带的，都在rest_framework.permissions自行研究:

![img](https://img2018.cnblogs.com/blog/1249183/201902/1249183-20190224163916959-1604450288.png)

 

## 总结 

> - 自定义权限必须继承DRF定义好的权限类，需要用什么就继承什么，且根据继承的类不同，必须要定义该基类里明确规定需要的方法或者属性
> - 权限验证按开发的逻辑必须要在认证组件验证之后才验证
> - 其实这些都跟认证组件差不太多，注意一下就行了，不用多说

# [Django Rest Framework之认证](https://www.cnblogs.com/cjaaron/p/10433325.html)

# 代码基本结构

　　url.py:

```python
from` `django.conf.urls ``import` `url, include``from` `web.views.s1_api ``import` `TestView`` ` `urlpatterns ``=` `[``  ``url(r``'^test/'``, TestView.as_view()),``]
```

 　views.py:

```python
from` `rest_framework.views ``import` `APIView``from` `rest_framework.response ``import` `Response``from` `rest_framework.authentication ``import` `BaseAuthentication``from` `rest_framework.request ``import` `Request``from` `rest_framework ``import` `exceptions` `class` `TestAuthentication(BaseAuthentication):``  ``def` `authenticate(``self``, request):``  ``'''``  ``认证代码编写区域``  ``'''``  ``return` `(用户,用户Token)` `  ``def` `authenticate_header(``self``, request):``    ``# 验证失败时，返回的响应头WWW-Authenticate对应的值``    ``pass`  `class` `TestView(APIView):``  ``authentication_classes ``=` `[TestAuthentication, ] ` `  ``def` `get(``self``, request, ``*``args, ``*``*``kwargs):``    ``pass` `  ` `   ``def` `post(``self``, request, ``*``args, ``*``*``kwargs):``    ``pass` `    ``'''``    ``等等一系列的视图功能方法``    ``'''
```

## 说明：

　　　　1）在authenticate方法的返回值是一个元组，元组中第一个元素是用户名，第二个元素是认证数据token。这个返回值会在我们的视图类中通过request.user 和 request.auth获取到。具体为什么是这两个值，会在后面的源码分析中说明。

　　　　2）认证的返回值有三种情况：

　　　　　　返回元组（如（1）中所述）：认证成功

　　　　　　返回None：处理下一个认证类

　　　　　　抛出异常：认证失败

　　　　3）上面的基本结构是做局部的类的认证方式，如果相对绝大多数的类做认证，那么可以通过全局认证的方式实现。该方法在下文中介绍。

　　　　4）authentication_classes 属性变量是一个列表，列表元素是类，一般情况只使用一个认证类。　　　　　

# 源码分析

## 1) 为什么要使用authentication_classes 属性变量？

　![img](https://img2018.cnblogs.com/blog/1196328/201902/1196328-20190225215001041-472628436.png) ![img](https://img2018.cnblogs.com/blog/1196328/201902/1196328-20190225215022198-1638075846.png)

 　python 的面向对象编程中，我们首先要执行的方法肯定是dispatch方法，所以我们的分析入口就是dispatch方法，在dispatch方法中，可以看到，通过initialize_request方法将django原生的request进行了一次封装。由initialize_request方法的实现过程可以看出，将其封装实例化成了一个Request对象。而authenticators属性就是认证属性。

　![img](https://img2018.cnblogs.com/blog/1196328/201902/1196328-20190225215906711-396856327.png)

  ![img](https://img2018.cnblogs.com/blog/1196328/201902/1196328-20190225220109665-174878326.png)

　　通过查看get_authenticators方法，可以知道，它的返回值是一个列表生成式，而这个列表生成式中所用的就是我们在认证类中赋值authenticatin_classes属性变量。在查找该变量的定义位置，就看到了它是通过settings配置文件来实现赋值的，除非，在子类中将其赋值。我们的代码就是这样做的。同时，也可以看出，我们可以修改settings配置文件来为全局定义认证规则。

## 2）为什么要认证类中要使用authenticate方法？

  ![img](https://img2018.cnblogs.com/blog/1196328/201902/1196328-20190225221252208-56664888.png)

  ![img](https://img2018.cnblogs.com/blog/1196328/201902/1196328-20190225221550174-283986091.png)

　　回到前面说是的dispatch方法来，在做完了对django原生的request的封装和实例化后，紧接着就会开始认证（try...中，捕获异常，如果没有捕获到异常，说明认证成功，就会继续执行下面的反射过程）。认证的过程就包含在上图中的inital方法中，有图可知，是通过perform_authentication方法实现的认证。

  ![img](https://img2018.cnblogs.com/blog/1196328/201902/1196328-20190225222345472-523433211.png)

  ![img](https://img2018.cnblogs.com/blog/1196328/201902/1196328-20190225222832880-1235013352.png)

　　在perform_authentication方法中可以看到，只调用了一个request.user，而这个user一定是方法，不会是属性变量，因为如果是属性变量，那么就一定有语法错误，变量一定是要赋值的，不可能孤零零的写到那里。我们在源码中找到它，就明白了，之所以它能这么写，就是因为有了property装饰器。在user方法中找到_authenticate方法，这就是认证的方法。

　![img](https://img2018.cnblogs.com/blog/1196328/201902/1196328-20190225223510337-1162497817.png)

　  在这个方法中，一切答案都就找到了。首先看authenticators，是不是很眼熟，没错它就是前面说的，封装和实例化原生request的Request类中所定义的属性变量。在实例化时，我们就将authentication_classes列表的值通过get_authenticators方法中的列表生成式赋值给了authenticators。再往下看，authenticator.autheneicate(self)中的authenticator是不是就是我们自己定义的认证类，而它在源码中要做“.authenticate(self)”的操作，那自然而然，我们定义的认证类中要实现这个方法了。

## 3）为什么认证成功后的返回值在request.user和request.auth中?

　　由 2）中最后一个图可知，当我们认证成功后会执行“self.user, self.auth = user_auth_tuple”代码，我们在认证类定义的方法authenticate的返回值就保存在 user_auth_tuple中，所以我们通过request.user 和 request.auth 就可以获取到了。

# 实例

```
from django.conf.urls import url, include
from web.viewsimport TestView

urlpatterns = [
    url(r'^test/', TestView.as_view()),
]
```

```
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BaseAuthentication
from rest_framework.request import Request
from rest_framework import exceptions

token_list = [
    'sfsfss123kuf3j123',
    'asijnfowerkkf9812',
]


class TestAuthentication(BaseAuthentication):
    def authenticate(self, request):
        """
        用户认证，如果验证成功后返回元组： (用户,用户Token)
        :param request: 
        :return: 
            None,表示跳过该验证；
                如果跳过了所有认证，默认用户和Token和使用配置文件进行设置
                self._authenticator = None
                if api_settings.UNAUTHENTICATED_USER:
                    self.user = api_settings.UNAUTHENTICATED_USER()
                else:
                    self.user = None
        
                if api_settings.UNAUTHENTICATED_TOKEN:
                    self.auth = api_settings.UNAUTHENTICATED_TOKEN()
                else:
                    self.auth = None
            (user,token)表示验证通过并设置用户名和Token；
            AuthenticationFailed异常
        """
        val = request.query_params.get('token')
        if val not in token_list:
            raise exceptions.AuthenticationFailed("用户认证失败")

        return ('登录用户', '用户token')

    def authenticate_header(self, request):
        """
        Return a string to be used as the value of the `WWW-Authenticate`
        header in a `401 Unauthenticated` response, or `None` if the
        authentication scheme should return `403 Permission Denied` responses.
        """
        # 验证失败时，返回的响应头WWW-Authenticate对应的值
        pass


class TestView(APIView):
    authentication_classes = [TestAuthentication, ]
    permission_classes = []

    def get(self, request, *args, **kwargs):
        print(request.user)
        print(request.auth)
        return Response('GET请求，响应内容')

    def post(self, request, *args, **kwargs):
        return Response('POST请求，响应内容')

    def put(self, request, *args, **kwargs):
        return Response('PUT请求，响应内容')
```

扩展：全局认证

　　如果要进行全局配置，由上面的源码分析可知，我们只需要在配置文件中配置我们存储到authentication_classes的值即可。但还要注意的是，在写配置文件时，要使用的是路径，所以最好在和views.py同级目录下新建一个文件夹（我习惯叫utils），再在该文件夹下新建一个认证文件（auth.py）,将我们的认证类都写到这里。

```
REST_FRAMEWORK ``=` `{``  ``"DEFAULT_AUTHENTICATION_CLASSES"` `:['api.utils.auth.MyAuthentication]  ``}
```

  MyAuthentication类就是我们写在utils文件夹下auth.py文件中的认证类。

**注意：**如果有部分类不需要认证的话，可以在这里类中添加“**authentication_classes = []**”,即可。



# 截流

## 自定义截流（局部限制）

```python
# mythrottle.py
from rest_framework.throttling import SimpleRateThrottle


class VisitThrottle(SimpleRateThrottle):
    rate = '5/m'
    # 频率每分钟五次 单位可以是 s（秒） m（分钟）h（小时）d（天）
    scope = 'vistor' # 自定义 名称
	# 返回一个唯一值标识用户
    def get_cache_key(self, request, view):
        return self.get_ident(request)
	# 返回None没有限制
class Index(APIView):
    throttle_scope = 'vistor' # 全局调用时用它识别 谁遵循那个截流器
    throttle_classes = (VisitThrottle,)
```

## 全局限制

```python
REST_FRAMEWORK = {
    # 自定义限制类   也可以直接继承  DRF 中 自带的限制 
    # 'DEFAULT_THROTTLE_CLASSES' = ['App.mythrottle.VisitThrottle'],
    
    # 使用内置限制类  的额外配置   
    "DEFAULT_THROTTLE_RATES": {
        # key  与定义的 scope 对应 value: 5 表示次数 / m表示分钟  s秒  h小时  d天
        "vistor": "5/m", # 自定义的截流类
        "anon": "10/d", # 匿名用户 系统自带的截流类
    }
}
```



# [Django Rest framework的限流实现流程](https://www.cnblogs.com/eric_yi/p/8424424.html)

# 一 什么是throttle

> 节流也类似于权限,它用来决定一个请求是否被授权。节流表示着一种临时的状态，常常用来控制客户端对一个
> API的请求速率。例如，你可以通过限流来限制一个用户在每分钟对一个API的最多访问次数为60次，每天的访问次数为1000次。
> 　

# 二 Django REST framework是如何实现throttle的

1. 在Django REST framework中主要是通过throttling.py文件里面的几个类来实现限流功能的。

   ![img](https://images2017.cnblogs.com/blog/1088904/201802/1088904-20180206215525966-1967322301.png)

2. 在整个流程上是在dispatch中的调用的initial方法中的self.check_throttles(request)调用到throttle类中的方法

   ![img](https://images2017.cnblogs.com/blog/1088904/201802/1088904-20180206215512826-1995233790.png)

3. throttle策略的配置：
   全局配置settings.py

```
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': (  # 定义限流类
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ),
    'DEFAULT_THROTTLE_RATES': {   # 定义限流速率，支持秒、分、时、天的限制
        'anon': '100/day',
        'user': '1000/day'
    }
}
```

1. 把限流策略设置在视图函数上
   **CBV**

```
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView
class ExampleView(APIView):
    throttle_classes = (UserRateThrottle,)
    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)
```

**FBV**

```
@api_view(['GET'])
@throttle_classes([UserRateThrottle])
def example_view(request, format=None):
    content = {
        'status': 'request was permitted'
    }
    return Response(content)
```

　

# 三 Django REST framework中throttle源码流程

1. 调用check_throttles方法，在这个方法中会遍历通过self.get_throttles()获取到的限流对象列表，默认列表里面是空的。也就是说默认不会有限流的策略。

   ![img](https://images2017.cnblogs.com/blog/1088904/201802/1088904-20180206215454170-1149856430.png)

   ![img](https://images2017.cnblogs.com/blog/1088904/201802/1088904-20180206215442998-600395698.png)

2. 在视图函数里面配置参数，让其应用上限流策略。我们这里以UserRateThrottle这个限流方法为例。(配置如第二节中的settings.py配置和FBV配置),在这里继续第二步的操作，执行UserRateThrottle对象的allow_request方法。
   由于UserRateThrottle这个类本身没有allow_request方法，所以在其父类SimpleRateThrottle中找这个方法.

   ![img](https://images2017.cnblogs.com/blog/1088904/201802/1088904-20180206215428326-41509190.png)

3. 执行allow_request方法，会首先判断是否定义了self.rate。根据self.rate执行，最终回去查找self.scope属性，而且这个属性是必须的。

   ![img](https://images2017.cnblogs.com/blog/1088904/201802/1088904-20180206215414013-87962929.png)

   ![img](https://images2017.cnblogs.com/blog/1088904/201802/1088904-20180206215358873-764347832.png)

4. 在UserRateThrottle中查找到定义的scope="user", 接着执行self.key语句。这条语句最终调用了UserRateThrottle里面的get_cache_key方法。
   此例中我们没有配置authenticate，所有会执行get_cache_key里面的get_indet方法，并最终返回了scope和ident被self.key接收(返回格式：throttle_user_127.0.0.1)。

   ![img](https://images2017.cnblogs.com/blog/1088904/201802/1088904-20180206215338998-890484565.png)

   ![img](https://images2017.cnblogs.com/blog/1088904/201802/1088904-20180206215324748-1765195197.png)

5. 返回self.key之后继续执行self.history,self.history会返回客户端的访问记录列表，并根据rate的配置去判断是否是要pop某一条访问记录。并最终根据列表长度和允许的长度做对比，判断客户端当前是否具有访问权限。

   ![img](https://images2017.cnblogs.com/blog/1088904/201802/1088904-20180206215307607-1175884531.png)

6. 若最终check_throttles返回True,则继续执行dispatch。dispatch之后的操作请参考之前写的django rest framework流程。如果返回False,则会继续执行self.throttled(request, throttle.wait())。

   ![img](https://images2017.cnblogs.com/blog/1088904/201802/1088904-20180206215248513-1322717036.png)

7. 执行父类SimpleRateThrottle里面的wait方法。这个方法主要用来向客户端返回还需要多少时间可以继续访问的提示。

   ![img](https://images2017.cnblogs.com/blog/1088904/201802/1088904-20180206215218529-256894746.png)



# DRF分页(总共三种)

1. #### PageNumberPagination(指定第n页，每页显示n条数据)

   ##### 说明

   既然要用人家的那么我们就先来看下源码,这个分页类源码中举例通过参数指定第几页和每页显示的数据:http://api.example.org/accounts/?page=4&page_size=100,所以我们可以知道,请求参数的名称和数值应该都是我们可以自定义的.来,我们来看下面的几个参数:

   ```python
   page_size = api_settings.PAGE_SIZE            # 这个是每页显示的数据,我们可以在全局定义,也可以在继承类只定义,比如每页10条记录,这里就设置10
   django_paginator_class = DjangoPaginator    # 这个是django分页的类,默认即可
   page_query_param = 'page'            # 第几页参数名称,我们也可以默认使用page,形象生动嘛
   page_size_query_param = None        # 这个是每页显示记录条数的参数名称,我们可以使用size或者page_size
   max_page_size = None                # 每页显示数据的最大值,所以page_size要小于这个,这个设置了就表示一页最多能显示多少条数据
   ```

   好了,参数看完了,那我们就来看下方法,实际上分页器核心就是调用paginate_queryset(self, queryset, request, view=None)的方法,返回的是list(self.page),也就是我们传入了queryset数据,并且配置好了页数等信息,最终就返回了第几页的n条数据对象的列表,然后我们再通过序列化之后,通过get_paginated_response(self, data)将序列化后的数据返回给前端即可.好了,我们开始写实例看下吧

   - ##### 使用

     首先定义分页器类

     ```python
     from rest_framework.pagination import PageNumberPagination
     
     
     class PageNumberPaginator(PageNumberPagination):
         page_size = 10  # 每页显示10条数据
         page_size_query_param = 'size'  # 每页显示条数的参数名称
         page_query_param = 'page'   # 页码参数名称,比如page=3&size=10 第三页显示10条
         max_page_size = 10  # 最大页码数量控制
     ```

     视图类如下:

     ```python
     from .Paginators import PageNumberPaginator
     
     
     class BookView(APIView):
         """书籍相关视图"""
     
         def get(self, request):
             book_queryset = Book.objects.all()
             # 1.实例化PageNumberPaginator
             page_obj = PageNumberPaginator()
             # 2.调用paginate_queryset方法获取当前页的数据
             page_data = page_obj.paginate_queryset(queryset=book_queryset, request=request, view=self)
             # 3.将获取的数据放入序列化器中进行匹配
             serializer_data = BookModelSerializer(page_data, many=True)
             # 4.返回带超链接的且有上一页和下一页的数据
             return page_obj.get_paginated_response(serializer_data.data)
     ```

2. #### LimitOffsetPagination (偏移n个位置, 向后查看n条数据)

   这里就不做多的说明了,直接开始使用,源码跟上一个是类似的.

   ```python
   class LimitOffsetPaginator(LimitOffsetPagination):
       default_limit = 2      # 向后查看两条数据
       limit_query_param = 'limit'     # 查看数据的参数名称
       offset_query_param = 'offset'   # 偏移参数名称, limit=2&offset=0 这个表示偏移0也就是从第一条数据开始显示,显示两条
       max_limit = 999                 # 一页查看最多999条数据
   ```

   视图类的话只需要修改实例化类那一行就行了page_obj = LimitOffsetPaginator(),其他都一样

3. #### CursorPagination (加密游标的分页,只能有上一页和下一页)

   ```python
   class CursorPaginator(CursorPagination):
       cursor_query_param = 'cursor'   # 参数名称
       page_size = 1                   # 每页显示的条数
       ordering = '-id'                # 根据id倒序排列
   ```

   视图类一样只需要修改实例化那一行 page_obj = CursorPaginator()

   访问的分页路径都是自动加密生成的,比如 http://127.0.0.1:8000/app01/books/?cursor=cD0y

   - ##### ModelViewSet视图类使用分页组件

如果是视图类是继承ModelViewSet写的呢?继承了ModelViewSet后,只需定义queryset和serializer_class序列化器即可,那么怎么玩呢?这个还是得看源码咯,来继续分析源码.

客户端get请求,所以从ModelViewSet -> ListModelMixin -> list方法, list方法中page = self.paginate_queryset(queryset) ,查看paginate_queryset的方法,self指的是视图类,所以从头再找,在GenericViewSet下的GenericAPIView中发现 paginate_queryset的方法下执行了 self.paginator.paginate_queryset(queryset, self.request, view=self) ,此时paginator 方法中又执行了self._paginator = self.pagination_class(), 而pagination_class()就是去配置里面找分页组件类并实例化,因此我们只需要配置pagination_class = PageNumberPaginator即可.

```python
class BooksView(viewsets.ModelViewSet):
    queryset = Book.objects
    serializer_class = BookModelSerializer
    # 指定分页器组件
    pagination_class = PageNumberPaginator
```

- ### 跨域

  - ##### 简单介绍CORS跨域请求

    CORS即Cross Origin Resource Sharing 跨域资源共享，跨域请求分为两种，一种叫简单请求，一种是复杂请求

  - ##### 简单请求和复杂请求

    简单请求满足下面要求:

    HTTP方法是其中方法之一: HEAD， GET，POST

    HTTP头信息不超出以下几种字段

    　　Accept， Accept-Language， Content-Language， Last-Event-ID

    　　Content-Type只能是下列类型中的一个

    　　　　application/x-www-from-urlencoded

    　　　　multipart/form-data

    　　　　text/plain

    任何一个不满足上述要求的请求，即会被认为是复杂请求~~

    复杂请求会先发出一个预请求，我们也叫预检，OPTIONS请求~~

  - ##### 浏览器的同源策略

    上面介绍的是跨域,那么跨域到底为什么会产生呢?其实就是浏览器的同源策略导致的,也就是说浏览器会阻止非同源的请求,非同源指的是域名不同或者不同端口,而且浏览器只会阻止表单及ajax请求,并不会阻止src的请求(script,img标签的)

  - ##### 解决跨域

    那么怎么解决跨域呢?

    - 方法一:通过jsonp

      jsonp的实现原理是根据浏览器不阻止src请求入手,也就是可以放在window.onload = function () {src="xxx"...}中,这样页面一加载,就会执行代码,但是这种方式太局限了,又不能发送其他类型请求还不能带请求头等,所以这种方法仅作了解

    - ##### 方法二: 添加响应头

      因为每个请求都会遇到跨域问题,所以我们可以定义一个中间件,专门处理跨域

      ```python
      from django.utils.deprecation import MiddlewareMixin
      
      
      class CorsMiddleWares(MiddlewareMixin):
          def process_response(self, request, response):
              # 针对简单请求,允许的地址是所有
              response['Access-Control-Allow-Origin'] = '*'
              # 如果是复杂请求,一定会先发送option预检
              if request.method == "OPTIONS":
                  # Content-Type也可以写成*,表示任何形式的头都允许
                  response["Access-Control-Allow-Headers"] = "Content-Type"
                  response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
              return response
      ```

- ### ContentType的应用

  - ##### 前戏

    contenttypes 是Django内置的一个应用，可以追踪项目中所有app和model的对应关系，并记录在ContentType表中。

  那么这张表有什么作用呢?接下来我举个例子,网上大部分人都是举该例子,就是商品优惠券和商品的例子,你想下,是不是每个商品都有能有优惠券,那么优惠券设计的结果就会像下面的结构一样,有没有发现如果我们新增一种商品就需要修改表结构,而且大部分字段都是null,所以我们需要修改下表结构

  ```python
     id     name       food_id        cloth_id   ....    
     1   通用优惠券      null          null    
     2   苹果满减券       1            null    
     3   衬衫满减券       null           1
  ```

  修改后的表结构及数据如下:

  ```python
     id    name       table_id       object_id   ....    
     1   通用优惠券      null          null    
     2   苹果满减券       7(food表)      1(第一行苹果记录)    
     3   衬衫满减券       8              1
  ```

  你看这样就算再多产品也不会出现空间浪费和表结构修改,而django中的ContentType表.

  - ##### 应用

  ```python
  contenttypes 应用
  
  通过使用contenttypes 应用中提供的特殊字段GenericForeignKey，我们可以很好的解决这个问题。只需要以下三步：  
  
  from django.contrib.contenttypes.models import ContentType
  在model中定义ForeignKey字段，并关联到ContentType表。通常这个字段命名为“content_type”
  
  在model中定义PositiveIntegerField字段(正整数)，用来存储关联表中的主键。通常这个字段命名为“object_id”
  
  from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
  在model中定义GenericForeignKey字段，传入上述两个字段的名字。
  
  为了更方便查询商品的优惠券，我们还可以在商品类中通过GenericRelation字段定义反向关系
  ```

  因此我们在models里面先建立表关系

  ```
  from django.db import models
  from django.contrib.contenttypes.models import ContentType
  from django.contrib.contenttypes.fields import (
      GenericForeignKey, GenericRelation
  )
  
  
  class Food(models.Model):
      name = models.CharField(max_length=32)
      price = models.FloatField()
      coupon = GenericRelation(to='Coupon')    # 用来反向查询
  
      def __str__(self):
          return self.name
  
  
  class Clothes(models.Model):
      name = models.CharField(max_length=32)
      price = models.FloatField()
      coupon = GenericRelation(to='Coupon')
  
      def __str__(self):
          return self.name
  
  
  class Coupon(models.Model):
      """优惠券表模型"""
      name = models.CharField(max_length=32)
      # 外键关联ContentType,其实这个关系就是要定位到具体的产品表
      content_type = models.ForeignKey(to=ContentType, on_delete=models.CASCADE)
      # 定位到具体的产品对象,比如苹果的id
      object_id = models.PositiveIntegerField()
      # 不会生成字段,只是用于关联对象,方便我们通过content_object快速查询到具体产品记录,插入数据时,直接content_object = 产品对象即可,就不需要再一一给content_type和object_id这两个字段赋值了
      content_object = GenericForeignKey("content_type", "object_id")
  
      def __str__(self):
          return self.name
  ```

  表模型创建完成之后,录入基础数据后我们就可以通过字段进行查询了.

  ```
  class QueryView(View):
      def get(self, request):
          from .models import Food, Coupon, Clothes
  
          # 1.根据苹果立减卷找到苹果商品的价格
          # 首先通过苹果立减劵找到coupon的对象
          coupon_obj = Coupon.objects.filter(name='苹果立减卷').first()
          # 再通过content_object字段就可以直接找到对应的food表记录
          pg = coupon_obj.content_object
          # 从记录中取出价格字段
          pg_price = pg.price
  
          # 2.根据苹果找出所有苹果的优惠券
          # 先找到苹果的记录对象
          food_obj = Food.objects.get(name='苹果')
          # 再通过coupon进行反向查询出所有结果,因为是1对多,所以存在多个,用了all()
          coupon_queset = food_obj.coupon.all()
          print(coupon_queset)    # <QuerySet [<Coupon: 苹果满减券>, <Coupon: 苹果立减卷>]>
          
          return HttpResponse("OK")
  ```

  注意：ContentType只运用于1对多的关系！！！并且多的那张表中有多个ForeignKey字段。



# django rest framework-过滤、搜索、排序

## 过滤DjangoFilterBackend：

默认情况下 DRF generic list view 会返回整个 `queryset`查询结果，但通常业务只是需要其中一部分，这种情况下就需要使用 "过滤器" 来限制返回结果集。
最笨的方式是继承`GenericAPIView`类或使用继承了`GenericAPIView`的类，然后重写`.get_queryset()` 方法 ，首先我们看类视图中增加一个方法`get_queryset`



```python
from rest_framework import generics
class ArticleViewSet(generics.ListAPIView):
    queryset = Article.objects.all()  # 查询结果集
    serializer_class = ArticleSerializer # 序列化类
    pagination_class = ArticlePagination   # 自定义分页会覆盖settings全局配置的

    def get_queryset(self):
        queryset = Article.objects.all()
        read_num = self.request.query_params.get('read_num', 0)  # 获取查询字段值
        if read_num:
            queryset = queryset.filter(read_num__gt=int(read_num))

        return queryset
```

###### 测试效果

1. 当传递的

   ```
   read_num=83
   ```

   按照方法

   ```
   get_queryset
   ```

   中判断条件找出大于

   ```
   83
   ```

   的有

   ```
   3
   ```

   条记录。

   ![img](https://upload-images.jianshu.io/upload_images/9286065-736acc5e5d03e4e7.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

   image.png

2. 

   

   我们再试一试如果不传递，查出记录有7条记录。

   ![img](https://upload-images.jianshu.io/upload_images/9286065-1b86548d132bb2e8.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

   image.png

###### 小结

上面我们通过重写`get_queryset`方法来达到过滤效果，这样做如果在过滤条件复杂的情况下，代码会显得过于冗余，而且有可能大部分代码一直在重复实现类似的功能，在日常操作中，我们需要获取指定条件的数据，例如对于文章，我们需要指定分类、浏览数、点赞数等。有时候我们需要按照浏览数进行排序。这些都需要我们对ArticleViewSet进行更多的拓展。

### 过滤OrderingFilter

REST framework提供了对于排序的支持，使用REST framework提供的OrderingFilter过滤器后端即可。OrderingFilter过滤器要使用ordering_fields 属性来指明可以进行排序的字段有哪些。



```python
from rest_framework.filters import OrderingFilter

    # 过滤器，只针对当前查询过滤，所以不在settings.py中配置
    filter_backends = (OrderingFilter,)
    # 排序
    ordering_fields = ('create_time', 'price', 'sales')
```

### 自定义过滤器 django-filter插件

```
django-filter`库包括一个`DjangoFilterBackend`类，它支持`REST`框架的高度可定制的字段过滤。
首先安装`django-filter
```



```swift
pip install django-filter
```

然后将`django_filters`添加到`Django`的`INSTALLED_APPS`。



```bash
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
}
```

或者将过滤器加到单个View或ViewSet中(**一般使用这种**)：



```python
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

class ArticleViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Article.objects.all()  # 查询结果集
    serializer_class = ArticleSerializer # 序列化类
    pagination_class = ArticlePagination   # 自定义分页会覆盖settings全局配置的
    # 过滤器
    filter_backends = (DjangoFilterBackend,)
    # 如果要允许对某些字段进行过滤，可以使用filter_fields属性。
    filter_fields = ('title', 'category')

    # def get_queryset(self):
    #     queryset = Article.objects.all()
    #     read_num = self.request.query_params.get('read_num', 0)
    #
    #     if read_num:
    #         queryset = queryset.filter(read_num__gt=int(read_num))
    #
    #     return queryset
```

###### 测试效果



![img](https://upload-images.jianshu.io/upload_images/9286065-f3fe3d0eea1218e5.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)


可以看出通过加过滤器和添加对应字段会过滤相关的，注意这里是精确匹配，字段间是且的关系，若一个为空，则按照其他的匹配，比如`title=测试&category=`则按照`title`来精确查找。



#### 自定义过滤类

默认是按照精准匹配，若想达到模糊搜索，可以自定义过滤类，再用filter_class指定过滤集合类。
新建过滤文件`filters.py`



```python
from django_filters import rest_framework
from article.models import Article

class AriticleFilter(rest_framework.FilterSet):
    min_read = rest_framework.NumberFilter(field_name='read_num', lookup_expr='gte')
    max_read = rest_framework.NumberFilter(field_name='read_num', lookup_expr='lte')
    title = rest_framework.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Article
        fields = ['title', 'category', 'min_read', 'max_read']
        # 或者这么写 他的判断条件和model的判断条件一样
        fields = {'title':['icontains'], 
                  'category':['lt','gt'], 
                  'min_read':['lte','gte','in'], 
                  'max_read':['exact','gt','year__lt','year__gt']
                 }
        'http://:9000/gettest/?title__icontains=百'
        '上面的意思是title 字段是否包含百'
        '如果fields = ['title', 'category', 'min_read', 'max_read']这么写只包含等于判定，exact就是等于判定默认就会给'
```

将视图类修改



```python
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .filters import AriticleFilter

class ArticleViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Article.objects.all()  # 查询结果集
    serializer_class = ArticleSerializer # 序列化类
    pagination_class = ArticlePagination   # 自定义分页会覆盖settings全局配置的
    # 过滤器
    filter_backends = (DjangoFilterBackend,)
    # 如果要允许对某些字段进行过滤，可以使用filter_fields属性。
    #filter_fields = ('title', 'category')
    # 使用自定义过滤器
    filter_class = AriticleFilter

    # def get_queryset(self):
    #     queryset = Article.objects.all()
    #     read_num = self.request.query_params.get('read_num', 0)
    #
    #     if read_num:
    #         queryset = queryset.filter(read_num__gt=int(read_num))
    #
    #     return queryset
```

测试效果：



![img](https://upload-images.jianshu.io/upload_images/9286065-8f3b41c5851b014e.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

image.png

## 搜索 SearchFilter

如果要明确指定可以对哪些字段进行搜索，可以使用search_fields属性，默认为可以对`serializer_class`属性指定的串行器上的任何可读字段进行搜索：



```python
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .filters import AriticleFilter

class ArticleViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Article.objects.all()  # 查询结果集
    serializer_class = ArticleSerializer # 序列化类
    pagination_class = ArticlePagination   # 自定义分页会覆盖settings全局配置的
    # 过滤器
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,)
    # 如果要允许对某些字段进行过滤，可以使用filter_fields属性。
    #filter_fields = ('title', 'category')
    # 使用自定义过滤器
    filter_class = AriticleFilter
    search_fields = ('title', 'description', 'content')
```

可以看出多了个搜索框



![img](https://upload-images.jianshu.io/upload_images/9286065-90ec367f96a35b54.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

image.png

默认情况下，搜索将使用不区分大小写的部分匹配。 搜索参数可以包含多个搜索项，它们应该是空格和/或逗号分隔。 如果使用多个搜索项，则仅当所有提供的条款匹配时，才会在列表中返回对象。默认情况下，搜索参数被命名为“search”，但这可能会被SEARCH_PARAM设置覆盖。
The search behavior may be restricted by prepending various characters to the search_fields.
可以通过在search_fields中加入一些字符来限制搜索行为，如下：
'^' ：以xx字符串开始搜索
'=' ：完全匹配
'@' ：全文搜索（目前只支持Django的MySQL后端）
'$' ：正则表达式搜索
如：search_fields = ('@username', '=email')

## 排序 OrderingFilter

OrderingFilter 类支持对单个查询字段结果集进行排序。
默认情况下，查询参数被命名为“ordering”，但这可能会被ORDERING_PARAM设置覆盖。
可以使用ordering_fields属性明确指定可以对哪些字段执行排序，这有助于防止意外的数据泄露，例如允许用户对密码散列字段或其他敏感数据进行排序。
如果不指定ordering_fields属性，则默认为可以对serializer_class属性指定的串行器上的任何可读字段进行过滤。



```python
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .filters import AriticleFilter

class ArticleViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Article.objects.all()  # 查询结果集
    serializer_class = ArticleSerializer # 序列化类
    pagination_class = ArticlePagination   # 自定义分页会覆盖settings全局配置的
    # 过滤器 过滤，搜索，排序
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    # 如果要允许对某些字段进行过滤，可以使用filter_fields属性。
    #filter_fields = ('title', 'category')
    # 使用自定义过滤器
    filter_class = AriticleFilter
    # 搜索
    search_fields = ('title', 'description', 'content')
    # 排序
    ordering_fields = ('id', 'read_num')
```

# django-filter 过滤 一

在DRF框架的使用中，一个比较让人头疼的问题是，怎么满足前端那变态的数据过滤需求，特别当前端提供所谓的灵活查询，过滤条件更是五花八门，比如一般前端查询都简单判等查询：

```text
path('book/<int:id>',views.BooksView.as_view(),name='book')
它对应的请求：
http://127.0.0.1:9000/book/1/
```

怎么查询书名中包含“英”字，日期大于“2019-3-14”等等诸如此类的请求。Django-filter这个组件就是要解决这样的问题。

## 1. 安装配置

Django-filter支持的Python版本和Django版本、DRF版本如下：

- **Python**: 3.5, 3.6, 3.7, 3.8
- **Django**: 1.11, 2.0, 2.1, 2.2, 3.0
- **DRF**: 3.10+

在虚拟开发环境中安装：

```text
pip install django-filter
```

在Django的项目配置文件中安装并配置django_filters应用：

```text
INSTALLED_APPS = [
    ...
    'django_filters',
]

REST_FRAMEWORK = {
   # 过滤器默认后端
    'DEFAULT_FILTER_BACKENDS': (
           'django_filters.rest_framework.DjangoFilterBackend',),
}
```

## 2.使用流程

我们通过一个简单的图书查询来说明如果在DRF中使用Django-filter过滤器。图书模型如下：

```text
# models.py
class Bookinfo(models.Model):
    btitle = models.CharField(max_length=200,verbose_name='标题')
    bpub_date = models.DateField(blank=True, null=True,verbose_name='出版日期')
    bread = models.IntegerField(null=True,verbose_name='阅读数量')
    bcomment = models.IntegerField(null=True,verbose_name='评论数量')
    bimage = models.CharField(max_length=200, blank=True, null=True,verbose_name='图片')

    class Meta:
        db_table = 'bookinfo'
        verbose_name = "图书"
```

序列化类：

```text
#serializers.py
class BookInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookinfo
        fields = "__all__"
```

我们需要自定义过滤器类：

```text
#filters.py
from django_filters import rest_framework as filters

from App.models import Bookinfo


class BookFilter(filters.FilterSet):
    class Meta:
        min_read = filters.NumberFilter(field_name="bread", lookup_expr='gte')
        max_read = filters.NumberFilter(field_name="bread", lookup_expr='lte')
        model = Bookinfo  # 模型名
        fields = {
            'btitle':['icontains'],  
            'bcomment':['gte','lte'],
        }
```

在视图中

```python3
# views.py
class BooksView(ListAPIView):
    """
    图书查询
    """
    queryset = Bookinfo.objects.all()
    serializer_class = BookInfoSerializer
    filter_class = BookFilter # 过滤类

#urls.py
app_name = 'App'
urlpatterns = [
    path('book/',views.BooksView.as_view(),name='book'),
    ....
]
```

在浏览器中测试

![img](https://pic4.zhimg.com/80/v2-c525b0666c1d919fdce7d5c25def621f_720w.jpg)图1 过滤器的使用

## 3.详解过滤器类

过滤器类和Django中表单类极其类似，写法基本一样，目的是指明过滤的时候使用哪些字段进行过滤，每个字段可以使用哪些运算。运算符的写法基本参照Django的ORM中查询的写法，比如：大于等于，小于等于用"gte"，“lte”等等

可以通过模型快速构建过滤器类

```text
class BookFilter(filters.FilterSet):
    class Meta:
        model = Bookinfo   # 模型名
        fields = ['btitle','bcomment']  # 可以使用的过滤字段
```

Meta中出现的fields是指过滤条件中可以出现的字段，默认是精确判等，查询的时候可以这样用：

```text
# bcomment=80
http://127.0.0.1:8000/book/?btitle=&bcomment=80
```

如果不是判等，可以自定义过滤字段进行过滤:

- 过滤器中常用的[字段类型](https://link.zhihu.com/?target=https%3A//django-filter.readthedocs.io/en/master/ref/filters.html%23core-arguments)，这些类型要输模型中对应字段类型兼容

```html
CharFilter         字符串类型
BooleanFilter      布尔类型
DateTimeFilter     日期时间类型
DateFilter         日期类型
DateRangeFilter    日期范围
TimeFilter         时间类型
NumberFilter       数值类型，对应模型中IntegerField, FloatField, DecimalField
```

- 参数说明：

```text
field_name: 过滤字段名，一般应该对应模型中字段名
lookup_expr: 查询时所要进行的操作，和ORM中运算符一致
```

- Meta字段说明

```text
model： 引用的模型，不是字符串
fields：指明过滤字段，可以是列表，列表中字典可以过滤，默认是判等；也可以字典，字典可以自定义操作
exclude = ['password'] 排除字段，不允许使用列表中字典进行过滤
```

自定义过滤字段：

```text
class BookFilter(filters.FilterSet):
    btitle = filters.CharFilter(field_name='title',lookup_expr='icontains')
    pub_year = filters.CharFilter(field_name='bpub_date',lookup_expr='year')
    pub_year__gt = filters.CharFilter(field_name='bpub_date',lookup_expr='year__gt')
    bread__gt = filters.NumberFilter(field_name='bread',lookup_expr="gt")
    bread__lt = filters.NumberFilter(field_name='bread',lookup_expr="lt")

    class Meta:
        model = Bookinfo
        fields = ['title','bread','bcomment']
```

自定义字段名可以和模型中不一致，但一定要用参数field_name指明对应模型中的字段名

日期查询

```text
#定义按年查询，
pub_year = filters.CharFilter(field_name='bpub_date',lookup_expr='year')
# 年份应该大于某值
pub_year__gt = filters.CharFilter(field_name='bpub_date',lookup_expr='year__gt')
#年份应该小于某值
bread__lt = filters.NumberFilter(field_name='bread',lookup_expr="lt")
示例：
http://127.0.0.1:8000/book/?title=&bread=&bcomment=&btitle=&pub_year=&pub_year__gt=2014&bread__gt=&bread__lt=
查询结果：
[
    {
        "id": 1,
        "title": "射雕英雄传",
        "bpub_date": "2020-02-18",
        "bread": 30,
        "bcomment": 80,
        "bimage": null
    }
]
```

标题查询

```text
# btitle查询的时候可以进行包含查询，icontains在ORM中表示不区分大小的包含
btitle = filters.CharFilter(field_name='btitle',lookup_expr='icontains')
示例：
http://127.0.0.1:8000/book/?title=&bread=&bcomment=&btitle=%E5%B0%84%E9%9B%95&pub_year=&pub_year__gt=&bread__gt=&bread__lt=
结果：
[
    {
        "id": 1,
        "title": "射雕英雄传",
        "bpub_date": "2020-02-18",
        "bread": 30,
        "bcomment": 80,
        "bimage": null
    }
]
```

阅读数查询

```text
# 阅读数大于
bread__gt = filters.NumberFilter(field_name='bread',lookup_expr="gt")
# 阅读数小于
bread__lt = filters.NumberFilter(field_name='bread',lookup_expr="lt")

示例：
http://127.0.0.1:8000/book/?title=&bread=&bcomment=&btitle=&pub_year=&pub_year__gt=&bread__gt=20&bread__lt=100
结果：
[
    {
        "id": 1,
        "title": "射雕英雄传",
        "bpub_date": "2020-02-18",
        "bread": 30,
        "bcomment": 80,
        "bimage": null
    },
    {
        "id": 6,
        "title": "连城诀",
        "bpub_date": "2009-10-23",
        "bread": 30,
        "bcomment": 90,
        "bimage": null
    }
]
```



# django-filter 过滤 二

在上一篇中介绍了Django-filter初步用法，接下来咱们看看字段条件字典的写法。

### **1.条件字典**

```text
class BookFilter(filters.FilterSet):
    class Meta:
        model = Bookinfo
        fields = {
            'title':['icontains'],
            'bcomment':['lt','gt'],
            'bread':['lte','gte','in'],
            'bpub_date':['exact','gt','year__lt','year__gt'],
            'bimage':['isnull']
        }
```

在这里，fields不再是列表，而是字典，键就是模型中字段名，值是一个列表，列表中，是可以进行的运算，运算符参照Django中ORM模型中filter里的写法，可以有多中运算。

- bcomment可以进行大于和小于运算：

```text
？bcomment__lt=20&bcomment__gt=50
```

- bread可以进行小于等于、大于等于、in运算

```text
http://127.0.0.1:9000/book/?bread__in=20,30
```

- bpub_date可以进行精确判等，大于，以及年份的小于和大于

```text
?bpub_date__gt=2014-02-18
?bpub_date__year__lt=2015&bpub_date__year__gt=2010
```

- bimage可以进行判空isnull

```text
？bimage__isnull=true
```



### **2.字符串判空**

如果条件字段是字符串类型，要判断name=''这种情况，可以使用同其他类型字段判空类似的方式

```text
from django.core.validators import EMPTY_VALUES  # 空值

#自定义空字符串类型
class EmptyStringFilter(filters.BooleanFilter):
    def filter(self, qs, value):  # 重载filter方法
        if value in EMPTY_VALUES:
            return qs

        exclude = self.exclude ^ (value is False)
        method = qs.exclude if exclude else qs.filter

        return method(**{self.field_name: ""})

class BookFilter(filters.FilterSet):
    bimage_isempty = EmptyStringFilter(field_name='bimage')
    class Meta:
        model = Bookinfo
        fields = {
            'title':['icontains'],
            'bcomment':['lt','gt'],
            'bread':['lte','gte','in'],
            'bpub_date':['exact','gt','year__lt','year__gt'],
            'bimage':['isnull']
        }
        
请求方式： http://localhost/api/my-model?myfield__isempty=false
```

查询结果如图1所示：

![img](https://pic2.zhimg.com/80/v2-e2bbda6e73a638457fa4753a83fb3ec1_720w.jpg)



### **3.自定义查询方法**

如果某个字段查询比较复杂，使用现有运算符不能满足要求，我们也可以自定义方法来进行查询

```text
class BookFilter(filters.FilterSet):
    path = filters.CharFilter('bimage',method='filter_empty_string')
    class Meta:
        model = Bookinfo
        fields = {
            'title':['icontains'],
            'bcomment':['lt','gt'],
            'bread':['lte','gte','in'],
            'bpub_date':['exact','gt','year__lt','year__gt'],
            'bimage':['isnull']
        }
    # 自定义方法判空字符串
    def filter_empty_string(self,queryset,name,value):
        return queryset.filter(bimage='')
```

method可以指定要进行的运算，在这里method的值可以是一个回调函数或是方法名。查询结果如图2所示：

![img](https://pic1.zhimg.com/80/v2-4a09500fac41ad3325467123e01978c4_720w.jpg)

到现在为止，我们已经可以解决大部分的复杂查询问题，但还有一些问题没有得到解决，比如如何进行条件或的表示，现在已有的都是逻辑与。

# [drf框架 - 过滤组件 | 分页组件 | 过滤器插件](https://www.cnblogs.com/waller/p/11734430.html)

# drf框架 接口过滤条件

## 群查接口各种筛选组件数据准备

##### models.py

```python
class Car(models.Model):
    name = models.CharField(max_length=16, unique=True, verbose_name='车名')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='价格')
    brand = models.CharField(max_length=16, verbose_name='品牌')

    class Meta:
        db_table = 'api_car'
        verbose_name = '汽车表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
```

##### admin.py

```python
admin.site.register(models.Car)
```

 

##### serializers.py

```python
class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Car
        # 参与序列化的字段
        fields = ['name', 'price', 'brand']
```

 

##### views.py

```python
# Car的群查接口
from rest_framework.generics import ListAPIView

class CarListAPIView(ListAPIView):
    queryset = models.Car.objects.all()
    serializer_class = serializers.CarModelSerializer
```

 

##### urls.py

```python
url(r'^cars/$', views.CarListAPIView.as_view()),
```

 

# drf过滤组件

## 搜索过滤组件 | SearchFilter

```python
使用步骤:
1.导入搜索过滤器 SearchFilter
2.局部配置 filter_backends = [SearchFilter]
3.局部配置过滤类依赖的过滤条件(字段) search_fields = ['name', 'price'] 注意:依赖的过滤字段只能配置序列化类中fields里配置的字段
接口使用样式:
/cars/?search=...
# eg：/cars/?search=1，name和price中包含1的数据都会被查询出
```

 

### 案例:

##### views.py

```python
from rest_framework.generics import ListAPIView

# 第一步：drf的SearchFilter - 搜索过滤
from rest_framework.filters import SearchFilter

class CarListAPIView(ListAPIView):
    queryset = models.Car.objects.all()
    serializer_class = serializers.CarModelSerializer

    # 第二步：局部配置 过滤类 们（全局配置用DEFAULT_FILTER_BACKENDS）
    filter_backends = [SearchFilter]

    # 第三步：SearchFilter过滤类依赖的过滤条件 => 接口：/cars/?search=...
    search_fields = ['name', 'price']
    # eg：/cars/?search=1，name和price中包含1的数据都会被查询出
```

 

## 排序过滤组件 | OrderingFilter

```python
使用步骤:
1.导入搜索过滤 OrderingFilter
2.局部配置 filter_backends = [OrderingFilter]
3.局部配置过滤类依赖的过滤条件(字段) ordering_fields = ['pk', 'price']
接口使用样式:
/cars/?ordering=...
# eg：/cars/?ordering=-price,pk，先按price降序，如果出现price相同，再按pk升序
```

 

### 案例:

##### views.py

```python
from rest_framework.generics import ListAPIView

# 第一步：drf的OrderingFilter - 排序过滤
from rest_framework.filters import OrderingFilter

class CarListAPIView(ListAPIView):
    queryset = models.Car.objects.all()
    serializer_class = serializers.CarModelSerializer

    # 第二步：局部配置 过滤类 们（全局配置用DEFAULT_FILTER_BACKENDS）
    filter_backends = [OrderingFilter]

    # 第三步：OrderingFilter过滤类依赖的过滤条件 => 接口：/cars/?ordering=...
    ordering_fields = ['pk', 'price']
    # eg：/cars/?ordering=-price,pk，先按price降序，如果出现price相同，再按pk升序
```

# drf分页组件

### 自定义分页组件:

```python
1.pahenations.py中自定义分页类(基础分页类/偏移分页类/游标分页类)
2.视图类中配置自定义的分页类: pagination_class = 自定义分页类
```

 

## 基础分页组件

##### pahenations.py

```python
from rest_framework.pagination import PageNumberPagination

class MyPageNumberPagination(PageNumberPagination):
    # ?page=页码
    page_query_param = 'page'
    # ?page=页面 下默认一页显示的条数
    page_size = 3
    # ?page=页面&page_size=条数 用户自定义一页显示的条数
    page_size_query_param = 'page_size'
    # 用户自定义一页显示的条数最大限制：数值超过5也只显示5条
    max_page_size = 5
```

##### views.py

```python
from rest_framework.generics import ListAPIView

class CarListAPIView(ListAPIView):
    # 如果queryset没有过滤条件，就必须 .all()，不然分页会出问题
    queryset = models.Car.objects.all()
    serializer_class = serializers.CarModelSerializer
    
    # 分页组件 - 给视图类配置分页类即可 - 分页类需要自定义，继承drf提供的分页类即可
    pagination_class = pagenations.MyPageNumberPagination
```

## 偏移分页组件

##### pahenations.py

```python
from rest_framework.pagination import LimitOffsetPagination
class MyLimitOffsetPagination(LimitOffsetPagination):
    # ?offset=从头偏移的条数&limit=要显示的条数
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    
    # ?不传offset和limit默认显示前3条，只设置offset就是从偏移位往后再显示3条
    default_limit = 3
    
    # ?limit可以自定义一页显示的最大条数
    max_limit = 5

    # 只使用limit结合ordering可以实现排行前几或后几
    # eg: ?ordering=-price&limit=2  => 价格前2
```

##### views.py

```python
from rest_framework.generics import ListAPIView

class CarListAPIView(ListAPIView):
    # 如果queryset没有过滤条件，就必须 .all()，不然分页会出问题
    queryset = models.Car.objects.all()
    serializer_class = serializers.CarModelSerializer
    
    # 分页组件 - 给视图类配置分页类即可 - 分页类需要自定义，继承drf提供的分页类即可
    pagination_class = pagenations.MyLimitOffsetPagination
```

## 游标分页组件

##### pahenations.py

```python
# 注：必须基于排序规则下进行分页
# 1）如果接口配置了OrderingFilter过滤器，那么url中必须传ordering
# 1）如果接口没有配置OrderingFilter过滤器，一定要在分页类中声明ordering按某个字段进行默认排序
from rest_framework.pagination import CursorPagination
class MyCursorPagination(CursorPagination):
    cursor_query_param = 'cursor'
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 5
    ordering = '-pk'
```

##### views.py

```python
pythonfrom rest_framework.generics import ListAPIView

class CarListAPIView(ListAPIView):
    # 如果queryset没有过滤条件，就必须 .all()，不然分页会出问题
    queryset = models.Car.objects.all()
    serializer_class = serializers.CarModelSerializer
    
    # 分页组件 - 给视图类配置分页类即可 - 分页类需要自定义，继承drf提供的分页类即可
    pagination_class = pagenations.MyCursorPagination
```

# 自定义过滤类

## 源码:

```python
class GenericAPIView(views.APIView):
    ...
    # 配置过滤器路径
    filter_backends = api_settings.DEFAULT_FILTER_BACKENDS
    ...
    
    def filter_queryset(self, queryset):
        # 若自己的视图列中配置了filter_backends=[过滤类] 就走视图类中的
        for backend in list(self.filter_backends):
            # 当时视图类中配置了filter_backends=[过滤类]
            # 下面这步会调用我们自己定义的过滤类的filter_queryset方法
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset
```

## 使用:

```
# 1.自定义过滤类,重写filter_queryset方法
# 2.在视图类中配置filter_backends = [自定义过滤类]补充: 自定义过滤类不需要继承GenericAPIView,因为视图类继承了ListAPIView, ListAPIView本来就继承GenericAPIView我们自定义的过滤类要在视图类中配置,当源码中的GenericAPIView要调用过滤类时就会调用我们在视图类中配置的自定义过滤类,从而调用filter_query方法
```

### filters.py

```python
class LimitFilter:
    # 重写filter_queryset方法
    def filter_queryset(self, request, queryset, view):
        # 从get请求中获取limit的值
        limit_mun = request.query_params.get('limit')
        if limit_mun:
            limit_mun = int(limit_mun)
            # 将queryset列表按limit_num切分
            return queryset[:limit_mun]
        return queryset
```

### views.py

```python
from rest_framework.generics import ListAPIView

class CarListAPIView(ListAPIView):
    # 如果queryset没有过滤条件，就必须 .all()，不然分页会出问题
    queryset = models.Car.objects.all()
    serializer_class = serializers.CarModelSerializer
    
    # 局部配置 过滤类 们（全局配置用DEFAULT_FILTER_BACKENDS）
    filter_backends = [LimitFilter]
```

# 过滤器插件：django-filter

##### 安装

```python
>: pip3 install django-filter
```

 

##### 过滤条件层：自定义api/filters.py

```python
from django_filters.rest_framework.filterset import FilterSet
from . import models
from django_filters import filters

class CarFilterSet(FilterSet):
    # 自定义过滤字段
    max_price = filters.NumberFilter(
        field_name='price',  # 该自定义字段关联的model类表中的字段
        lookup_expr='gte',  # 查找的条件  'gte':大于等于
    )
    min_price = filters.NumberFilter(
        field_name='price',  # 该自定义字段关联的model类表中的字段
        lookup_expr='lte',  # 查找的条件  'lte':小于等于
    )
    class Meta:
        model = models.Car
        fields = ['brand', 'min_price', 'max_price']
        # brand是model中存在的字段，一般都是可以用于分组的字段
        # min_price、max_price是自定义字段，需要自己自定义过滤条件
```

### 视图层：views.py

```python
# django-filter插件过滤器
from django_filters.rest_framework import DjangoFilterBackend
from .filters import CarFilterSet

class CarListAPIView(ListAPIView):
    queryset = models.Car.objects.all()
    serializer_class = serializers.CarModelSerializer
    
    # 局部配置 过滤类 们（全局配置用DEFAULT_FILTER_BACKENDS）
    filter_backends = [DjangoFilterBackend]
    
    # django-filter过滤器插件使用
    filter_class = CarFilterSet
    # 接口：?brand=...&min_price=...&max_price=...
    # eg:?brand=宝马&min_price=5&max_price=10 => 5~10间的宝马牌汽车
    
```



# 接口文档

```python
pip install coreapi

# settings.py
REST_FRAMEWORK = {
'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'
}

# urls.py 总
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('', include('App.urls')),
    path('docs/', include_docs_urls('xADM api docs'))
]

# 查看在 127.0.0.1:9000/docs
# 这个东西里面有英文不友好，对自己写的的分页没有支持，有挺多问题
# 下面是分页的帮助提示，其他的提示在models.py 和 serializer.py 加'help_text'字段 前面有写自己看
from django.utils.translation import gettext_lazy as _
page_query_description = _('页码')
page_size_query_description = _('每页现实的数量')
```

# 跨域解决

```python
最近在接一个前后端分离的项目，后端使用的django-restframework，前端使用的Vue。后端跑起来后，发现前端在访问后端API时出了了跨域的问题。

类似如下报错：



关于跨域问题，之前这篇文章也提到过一、前后端交互之Ajax及跨域问题，当时里面是使用的jsonp方式，但是jsonp只支持GET方法，不能全面支持跨域。

这里主要学习一下通过后端解决跨域问题的方法，其实前端也有解决跨域的方法，后面学习到了再写一个文章记录。

 

django后端解决跨域方式一Middleware
中间介实现跨域过程

1、新建中间介包



#mkidr middleware

#touch middleware/__init.py__

#vim middleware/crossdomainxhr.py

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
from django import http
                                                                                                                                                                  
try:
    from django.conf import settings
    XS_SHARING_ALLOWED_ORIGINS = settings.XS_SHARING_ALLOWED_ORIGINS
    XS_SHARING_ALLOWED_METHODS = settings.XS_SHARING_ALLOWED_METHODS
    XS_SHARING_ALLOWED_HEADERS = settings.XS_SHARING_ALLOWED_HEADERS
    XS_SHARING_ALLOWED_CREDENTIALS = settings.XS_SHARING_ALLOWED_CREDENTIALS
except AttributeError:
    XS_SHARING_ALLOWED_ORIGINS = '*'
    #XS_SHARING_ALLOWED_METHODS = ['POST', 'GET', 'OPTIONS', 'PUT', 'DELETE']
    XS_SHARING_ALLOWED_METHODS = ['POST', 'GET']
    XS_SHARING_ALLOWED_HEADERS = ['Content-Type', '*']
    XS_SHARING_ALLOWED_CREDENTIALS = 'true'
                                                                                                                                                                  
                                                                                                                                                                  
class XsSharing(object):
    """
    This middleware allows cross-domain XHR using the html5 postMessage API.
                                                                                                                                                                      
    Access-Control-Allow-Origin: http://foo.example
    Access-Control-Allow-Methods: POST, GET, OPTIONS, PUT, DELETE
                                                                                                                                                                  
    Based off https://gist.github.com/426829
    """
    def process_request(self, request):
        if 'HTTP_ACCESS_CONTROL_REQUEST_METHOD' in request.META:
            response = http.HttpResponse()
            response['Access-Control-Allow-Origin']  = XS_SHARING_ALLOWED_ORIGINS
            response['Access-Control-Allow-Methods'] = ",".join( XS_SHARING_ALLOWED_METHODS )
            response['Access-Control-Allow-Headers'] = ",".join( XS_SHARING_ALLOWED_HEADERS )
            response['Access-Control-Allow-Credentials'] = XS_SHARING_ALLOWED_CREDENTIALS
            return response
                                                                                                                                                                  
        return None
                                                                                                                                                                  
    def process_response(self, request, response):
        response['Access-Control-Allow-Origin']  = XS_SHARING_ALLOWED_ORIGINS
        response['Access-Control-Allow-Methods'] = ",".join( XS_SHARING_ALLOWED_METHODS )
        response['Access-Control-Allow-Headers'] = ",".join( XS_SHARING_ALLOWED_HEADERS )
        response['Access-Control-Allow-Credentials'] = XS_SHARING_ALLOWED_CREDENTIALS
                                                                                                                                                                  
        return response
　　

settings文件配置：

 在中间介新增配置

1
'finance.middleware.crossdomainxhr.XsSharing',
　

跨域配置：

我这里前端使用的是源是http://127.0.0.1:8081

1
2
3
4
5
6
# crossdomain
#XS_SHARING_ALLOWED_ORIGINS ='*'
XS_SHARING_ALLOWED_ORIGINS = 'http://127.0.0.1:8081'
XS_SHARING_ALLOWED_METHODS = ['POST', 'GET']
XS_SHARING_ALLOWED_HEADERS = ['Content-Type', '*']
XS_SHARING_ALLOWED_CREDENTIALS = 'true'
　　

 

 

django后端解决跨域方式二django-cors-headers
 通过第三方包方式：https://github.com/ottoyiu/django-cors-headers

注意：既然有第三方包，name为什么还要用第一种方式，自己写呢？原因是第三方包对Django的版本有要求：



 

有些Django版本比较老的话 就只能用第一种方式咯。

具体实现如下：

1、安装django-cors-headers

pip install django-cors-headers
　　

2、配置settings.py文件

# a.在INSTALLED_APPS里添加“corsheaders”

INSTALLED_APPS = [
    ...
    'corsheaders'，
    ...
 ]
　　

# b.在MIDDLEWARE_CLASSES添加配置：

MIDDLEWARE_CLASSES = (
    ...
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...
)
　　

# c.在sitting.py底部添加

CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = ('localhost','127.0.0.1') # 白名单
  
CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)
  
CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
)
```



# 上线部署

```python
# apt-get install python3-dev python3-setuptools libtiff5-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev libharfbuzz-dev libfribidi-dev  tcl8.6-dev tk8.6-dev python3-tk

#　安装不成功有可能缺插件 安装上面的插件就可成功

# 新建虚拟环境
pip install django
pip install mysqlclient
pip install pillow
pip install uwsgi

```

## 安装psycopg2报错

```python
# 安装psycopg2报错 centos
    yum install postgresql-devel*  
	pip install psycopg2-binary
# ubuntu
	sudo apt-get install postgresql
	sudo apt-get install python-psycopg2
	sudo apt-get install libpq-dev
	pip3 install psycopg2==2.8.4
    # 中间报 "下列软件包有未满足的依赖关系，依赖: libxxx(= 2.2.10) 但是 2.3.0正要被安装" 的错误
    # 报什么安装什么 如
    下列软件包有未满足的依赖关系：
 	libcups2-dev : 依赖: libcupsimage2-dev (= 2.2.10-6+deb10u1) 但是它将不会被安装
                依赖: libcups2 (= 2.2.10-6+deb10u1) 但是 2.3.0+deepin2-1+deepin 正要被安装
	apt install libcupsimage2-dev=2.2.10-6+deb10u1
    # 一直安到没报错
```

## 安装mysqlclient 报错

```python
apt-get search mysqlclient 
从中选一个安装，缺少依赖

# 安装常见的依赖
linmysqlclient-dev python3-dev
libpcre3-dev libreadline-dev libsqlite3-dev

# 常见的库
man gcc make lsof ssh openssh tree vim dnsutils
psmisc sysstat curl telnet traceroutr wget iputils-ping
net-tools libbz2-dev libpcre3 build-essential
linssl-dev llvm zliblg-dev git zip p7zip

```

# 宝塔配置反向代理

```python
https://www.cnblogs.com/bigyoung/p/12789955.html

# 注意
目标URL 必须是 你域名解析所在服务器的IP地址+端口号 必须加 http/https 前缀
发送域名 你想要把这个请求转接给谁 就填谁的域名（没试过IP地址好不好使，大概率好使）,如果没有转发的服务器，默认本机

# 反向代理静态资源
location /static/ {
alias /www/wwwroot/myblog/static/;
}

location /media/ {
alias /www/wwwroot/myblog/media/;
}
```

# uwsgi.ini 配置

```
[uwsgi]

# 外部访问地址 可以指定多种协议，现在用http 便于调试，之后用socket
socket = 0.0.0.0:8000

# 指向项目目录
chdir = /home/yby/data/www/django_rest_framework

# 文件所在地 所以是路径形式
wsgi-file = django_rest_framework/wsgi.py

# 可以不写 模块所以是 . 形式 这个和上面的意思是一样的
# module = django_rest_framework.wsgi

# 可以不写 找虚拟环境python
virtualenv = /home/yby/.env/pa/bin/python

# 可以不写
plugins = python

master = true

# 处理器数
processes = 1

# 线程数
threads = 2
```

```python
# 启动
uwsgi uwsgi.ini
uwsgi -d uwsgi.ini # -d 守护进程 Daemons
# 关闭
uwsgi --stop uwsgi.ini
ps -ef | grep uwsgi
sudo kill 进程号

```

# 安装nginx

```
# 当你卸载nginx 的时候 没卸载干净就会出现充装不了的麻烦

1.sudo apt-get --purge remove nginx
2.sudo apt-get autoremove
3.sudo apt-get --purge remove nginx-common
4.sudo apt-get --purge remove nginx-core

# 按顺序执行就卸载干净了

```

# nginx 和 uwsgi

```python
# 在/etc/nginx/sites-available 目录下创建文件 随便取名
# 在/etc/nginx/sites-enabled 目录下创建链接 指向sites-available目录下你创建的这个文件
# sites-available 里面的文件代表的是建站文件但不一定启用
# sites-enabled 里面代表的是启用的站点
# 看nginx 文件应该也可以放到conf.d 文件夹下 但文件名称必须是.conf 后缀

server {
	listen 80;

	root /home/yby/data/www/django_rest_framework;

	index index.html index.htm index.nginx-debian.html;

	server_name www.ybybbb.com;

	location / {
		# 转发端口必须和uwsgi.ini中的socket端口一致
		uwsgi_pass  0.0.0.0:8000;
		include uwsgi_params;
		uwsgi_param UWSGI_SCRIPT django_rest_framework.wsgi;
		# 项目的根目录
		uwsgi_param UWSGI_CHDIR /home/yby/data/www/django_rest_framework;
	}
	
	location /static {

		alias /home/yby/data/www/django_rest_framework/static;

	}
}

```

# 静态资源404

```python
# 收集静态资源 你安装的插件什么的用的静态资源就会调用这个文件夹下的资源
# 在settings.py 里加下面一段
# 运行 python manage.py collectstatic
# 只有在上线时候采用
STATIC_ROOT = os.path.join('BASE_DIR', 'collectstatic') 

```

# 开机自动重启uwsgi

背景生产环境中采用[nginx](https://www.centos.bz/category/web-server/nginx/) + [uwsgi](https://www.centos.bz/tag/uwsgi/) + [django](https://www.centos.bz/tag/django/) 来部署web服务，这里需要实现uwsgi的启动和停止，简单的处理方式可以直接在命令行中启动和kill掉uwsgi服务，但为了更安全、方便的管理uwsgi服务，配置uwsgi到[systemd](https://www.centos.bz/tag/systemd/)服务中，同时实现开启自启的功能；
另，鉴于[supervisor](https://www.centos.bz/tag/supervisor/)不支持[python3](https://www.centos.bz/tag/python3/),没采用supervisor来管理uwsgi服务；

具体配置方法如下：

step1. 创建配置文件

```
/etc/systemd/system/server_uwsgi.service
```

step2. 填入以下内容

```shell
[Unit]
Description=HTTP Interface Server
After=syslog.target 

[Service]
KillSignal=SIGQUITExecStart=/usr/bin/uwsgi --ini /path/uwsgi.ini
Restart=always
Type=notify
NotifyAccess=all
StandardError=syslog 

[Install]
WantedBy=multi-user.target
```

step3. 将该服务加入到systemd中

```
systemctl enable /etc/systemd/system/server_uwsgi.service
```

然后就可以通过systemctl来控制服务的启停

```shell
systemctl stop server_uwsgi.service 关闭uwsgi服务
systemctl start server_uwsgi.service 开启uwsgi服务
systemctl restart server_uwsgi.service 重启uwsgi服务
```

注意事项：

```
如果uwsgi配置文件中配置了 daemonize=/path/uwsgi.log (uwsgi服务以守护进程运行)会导致sytemctl启动时多次重启而导致启动失败需改为 logto=/path/uwsgi.log
```
