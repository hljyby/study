**目录**

- [1、settings.py文件中：static相关内容](https://www.cnblogs.com/gengyufei/p/12632408.html#_label0)
- [2、模板文件的使用：](https://www.cnblogs.com/gengyufei/p/12632408.html#_label1)
- [3、各个文件夹的作用](https://www.cnblogs.com/gengyufei/p/12632408.html#_label2)
- [4、Django静态文件的引用](https://www.cnblogs.com/gengyufei/p/12632408.html#_label3)
- [5、static_url详解](https://www.cnblogs.com/gengyufei/p/12632408.html#_label4)
- [6、static静态文件->模板使用](https://www.cnblogs.com/gengyufei/p/12632408.html#_label5)

 

------

先上一个项目文件结构：

![img](https://img-blog.csdnimg.cn/20181207112719826.png)

[回到顶部](https://www.cnblogs.com/gengyufei/p/12632408.html#_labelTop)

## 1、settings.py文件中：static相关内容

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
# the settings above
# STATIC SETTINGS
STATIC_URL = '/static/'
# BASE_DIR 是项目的绝对地址
STATIC_ROOT = os.path.join(BASE_DIR, 'collect_static')
#以下不是必须的  各个app共用的文件可以放在这
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'common_static'),
) 
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

[回到顶部](https://www.cnblogs.com/gengyufei/p/12632408.html#_labelTop)

## 2、模板文件的使用：

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
# 这四个都可以定位到文件
{% load staticfiles %}  
    <img src="{% static 'img/1.png' %}" />
    <img src="{% static 'img/3.png' %}" />
 
    <img src="{{STATIC_URL}}img/1.png" />
    <img src="{{STATIC_URL}}img/3.png" />
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

[回到顶部](https://www.cnblogs.com/gengyufei/p/12632408.html#_labelTop)

## 3、各个文件夹的作用

- ### STATIC_ROOT

 

 

　　　　是在**部署**的时候才**发挥作用**,执行 **python managy.py collectstatic** ，会在工程文件下**生成(STATIC_ROOT )文件夹**，把各个app下的静态文件**收集到这个目录下**。当然，**需要配置Nginx**。

 

- ### STATICFILES_DIRS

　　　　静态文件的安放位置有两种:

- - #### app/static：

    - 在每个app里面新建一个static文件夹，将静态文件放到里面
    - 在加载静态文件时，比如要在**模板中用到静态文件**，django会**自动**在每个app里面**搜索static文件夹**
    - 所以，不要把文件夹的名字写错， 否则django就找不到你的文件夹
    - 因此，一般会这样设计：app01/static/app01_static/css

  - #### STATICFILES_DIRS

    - 在所有的app文件外面，建立一个**公共的文件夹**,，也就是我们的***\*STATICFILES_DIRS: common_static\****
    - 因为有些静态文件不是某个app独有的,那么就可以把它放到一个公共文件夹里面，方便管理
    - 注意，建立一个**公共的静态文件**的文件夹只是一种**易于管理的做法**，但是**不是必须的**，**app是可以跨app应用静态文件的**，因为最后所有的静态文件都会**在STATIC_ROOT里面存在**
    - 那现在的问题是：如何让django知道你把一些静态文件放到app以外的公共文件夹中呢，那就需要配置STATICFILES_DIRS了

  - #### STATIC_URL

    - 静态路由映射
    - django利用STATIC_URL来让浏览器可以直接访问静态文件

[回到顶部](https://www.cnblogs.com/gengyufei/p/12632408.html#_labelTop)

## 4、Django静态文件的引用

- ### 两个查找路径：

　　　　在static标签中引用文件时有两个查找路径：

　　　　　　1、app下的static

　　　　　　2、工程下的commen_static（STATICFILES_DIRS）

- ### 查找机制：

　　　　STATICFILES_DIRS告诉django：

　　　　**首先，到STATICFILES_DIRS里面寻找静态文件,**

　　　　**其次，再到各个app的static文件夹里面找**

　　　　ps：(注意，**django查找静态文件是惰性查找，查找到第一个，就停止查找了**)

**截止到目前为止，静态文件的机制已经可以运作了**。

但是，有一个疑问，如何通过url来访问项目中的静态文件呢？可能会这么做：直接访问项目的静态文件的绝对路径，eg：home/blogproject/common_static/img/[1.png](http://127.0.0.1:8000/static/img/3.png)，那么，在浏览器端需要这样：http://127.0.0.1:8000/home/blogproject/common_static/img/[1.png](http://127.0.0.1:8000/static/img/3.png)

但是，很抱歉，如果这样做的话，Django会报错，那么，该如何做呢？下面给出答案：

[回到顶部](https://www.cnblogs.com/gengyufei/p/12632408.html#_labelTop)

## 5、static_url详解

那么django是如何让浏览器也可以访问服务器上的静态文件呢，前面已经说了，直接访问服务器本地的地址是不行的，那就**需要一个映射**，django利用**STATIC_URL**来让**浏览器可以直接访问静态文件**，比如：

```
STATIC_URL = '/static/'
```

那么可以在浏览器上输入:

```
　　http://127.0.0.1:8000/static/img/1.png
　　http://127.0.0.1:8000/static/img/3.png
```

那么就相当与访问：

```
/home/blogproject/common_static/img/1.png

/home/blogproject/mytest/static/img/3.png
```

 

也就是说**STATIC_URL = '/static/'** 可以**定位到各个app下的staic/和工程下的commen_static/**。



所以在浏览器上，利用前缀 STATIC_URL的具体内容，来映射app下的static和STATICFILES_DIRS，
[http://127.0.0.1:8000/static/](http://127.0.0.1:8000/static/img/3.png) 相当于 本地地址的app/static 和 STATICFILES_DIRS

[回到顶部](https://www.cnblogs.com/gengyufei/p/12632408.html#_labelTop)

## 6、static静态文件->模板使用

```
{% load staticfiles %}
<img src="{% static 'img/1.png' %}" />
```

- 我们在模板中添加一行 **{% load staticfiles %}**，告诉django模板引擎我们要在模板中使用静态文件；
- 这样，便可以使用static模板标签引入静态目录中的文件；
- static 'img/1.png' 告诉django，我们要显示目录名中img/1.png 的文件；
- static标签会在img/1.png前加上STATIC_URL的指定URL，得到/static/img/1.png ；

django模板引擎生成如下html：

```
<img src="/static/img/1.png" />
```

**如果使用：**

```
<img src="{{STATIC_URL}}img/3.png" />
```

需要在setting.py中添加些设置：

\1. INSTALLED_APPS 中，加入 'django.contrib.staticfiles' ，这个一般都有。

\2. TEMPLATES 中，context_processors中，加入django.template.context_processors.static
![img](https://img2020.cnblogs.com/blog/1756501/202004/1756501-20200404163516250-1879761701.png)

 

 

![img](https://img2020.cnblogs.com/blog/1756501/202004/1756501-20200404163459717-453880727.png)