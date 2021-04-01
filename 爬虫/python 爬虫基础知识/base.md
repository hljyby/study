# python 爬虫基础库

- 网路请求

- urllib
- requests / urllib3
- selenium ( UI自动化测试，js动态渲染)
- appium (手机app 的自动化测试)

- 数据解析
- 正则 re
- xpath
- bs4
- json

- 数据存储
- pymsql
- mongodb
- elasticsearch  

- 多任务库
- 多线程 （threading），线程队列queue
- 协程   （asyncio，genent/eventlet）

- 爬虫框架
- scrapy
- scrapy-redis (分布式)（多机爬虫）

```
- urllib
	- request
		- urlopen()
		- urlretrieve(fullurl,filename)
		- Request(url,data=None,headers)
		- build_opener(handlers)
		- HTTPhandler
		- HTTPCookieProcess(http.cookiejar.CookieJar())
		- ProxyHandler(proxies={})
	- parse
		- quote()
		- urlencode()
- http.client.HTTPResponse
	- code
	- getheaders()
	- getheader(name,default)
	- read()

- requests
	- request(method,url,params,data,json,files,headers,cookies,proxies,auth)
	- get(url,params,**keargs)
	- post(url,params,**keargs)	
	- put(url,params,**keargs)	
	- delete(url,params,**keargs)	
	- Response
    	- status_code
    	- encoding
    	- headers
    	- content
    	- text
    	- json
    	
```

```
- re
- xpath
	- from lxml import etree
	  root = etree.HTML(html)
	  root.xpath('')
- bs4 (pip install bs4)
	- from bs4 import BeautifulSoup
	  root = BeautifulSoup(html,'lxml')
	
```



# 常见的反爬虫手段

- UA (User-Agent)
- 登陆限制 （cookie）
- 请求频次 （ip代理）
- 验证码 （图片- 云打码，滑块）
- 动态js (selenium/splash) 

# 一 上下文

## 1.1什么是上下文

- 任意python对象都可以使用上下文环境，使用with关键字，上下文是代码片段的区域，当对象进入上下文环境时解释器会调用对象的`__enter__()`,当对象退出上下文环境时，会调用对象`__exit__()`

## 1.2为什么使用

对象在使用上下文环境时，为确保对象正确的**释放资源**，避免出现**内存遗漏**。存在以下对象经常使用上下文**with**

- 文件操作对象**open**
- 数据库的连接 connnet
- 线程锁 Lock

## 1.3 如何使用

### 1.3.1 重写类的方法

上下文的两个核心方法

```python
class A:
    def __enter__(self):
        # 进入时调用
        # 必须返回一个相关对象
        return "enter"
    def __exit__(self,except_type,val,tb):
        # 退出上下文时被调用
        # except_type 如果存在异常，表示为异常的实例对象
        # val 异常消息的message
        # tb 异常的跟踪栈
        
        # 返回True 表示存在异常，不向外抛出
        # 返回False 表示存在异常，向外抛出 （默认False)
```

### 1.3.2 with中的使用

```python
a = A()
with a as ret:
	print(ret) # enter
```

# 二 Dao 设计



DAO(Data Access Object) 数据访问对象只是一种设计思想，目的是简化对数据库的操作，针对实体类对象（数据模型类），封装一套与数据库操作的SDK(Software Develope Kit) 软件开发环境

```python
- dao (基础数据库操作模块)
	|- __init__.py
	|- base.py
- entity (实体类的模块)
	|- user
	|- order
- db (具体的数据操作)
	|- user_db.py
    |- order_db.py
```

# 三 Requests 库

## 3.1 核心函数

- request.request() 所有请求方法的基本方法
  -  method 指定请求方法
  - url
  - params: **get请求**
  - data: **post** **请求**
  - json: **post 请求**
- requests.get()
- requests.post()
- requests.put()
- requests.patch() # 不建议使用 幂等性的问题
- requests.delete()

函数后面 -> 表示返回结果的类型

参数后面 **:str** 表示参数类型

定义变量 **: Response** 表示变量的类型

- Requests.Response
  - status_code 响应状态码
  - url
  - headers:dict
  - cookies:可迭代对象（name,value,path）
  - text:相应的文本信息
  - content:响应字节数据
  - encoding:相应的字符编码集
  - json:如果响应数据类型为application/json 将响应数据反序列化为python的list 或dict

# 四 XPath 解析

> xpath 属性xml/html 解析数据的一种方式，基于元素的树形结构，选择莫伊元素时，根据元素的路径选择，如
>
> `/html/head/title`获取title 标签 
>
> 安装包 pip install lxml 

## 4.1绝对路径

- 从根标签开始，把tree的解构依次向下查找

## 4.2 相对路径

相对路径可以有一下写法

- 相对于整个文档

  ```html
  //img
  ```

  查找出文档中所有的img 标签

- 相对于当前节点

  ```
  //table
  ```

  加入当前节点是`<table>`,查找他的`<img>`的路径的写法

  ```
  .//img
  ```

## 4.3 数据提取

- 提取文本

  ``````xpath
  //title/text() 提取文本
  ``````

- 提取属性

  ```xpath
  //img/@href
  ```

- 提取指定位置的元素

  获取网页中的数据类型与字符集

  ```xpath
  //meta[1]//@content # 从一开始
  //meta[first()]//@content
  ```

  获取最后一个`<meta>`content属性

  ```xpath
  //meta[last()]//@content
  ```

  获取倒数第二个`<meta>`content属性

  ```xpath
  //meta[position()-2]//@content
  ```

  获取前三个`<meta>`

  ```xpath
  //meta[position()<3]//@content
  ```

- 指定属性条件

  查找class为`circle-img`的`<img>`标签

  ```xpath
  //img[@class="circle-img"]
  ```

  ```
  //img[@class="circle-img" and @class="circle-img"]
  ```
  
  ```
  //img[@class] 所有带类属性的img元素
  ```
  
  ```
  //@class  所有带类属性的元素
  ```
  
- 模糊查询

  ```
  //[contains(@id,"he")] 类似sql 的like 关键字
  //[starts-with(@id,"he")] 
  //[ends-with(@id,"he")] 
  
  ```

  

## 4.4 XPath 术语



\1. 在 XPath 中，有七种类型的节点：元素、属性、文本、命名空间、处理指令、注释以及文档节点（或称为根节点）。XML 文档是被作为节点树来对待的。树的根被称为文档节点或者根节点。

\2. 基本值（或称原子值，Atomic value）是无父或无子的节点。

\3. 项目（Item）是基本值或者节点。

***\*XPath 语法\****

XPath 使用路径表达式来选取 XML 文档中的节点或节点集。节点是通过沿着路径 (path) 或者步 (steps) 来选取的。

**![img](https://img-blog.csdn.net/20170920201210050)
**

**![img](https://img-blog.csdn.net/20170920201538575)
**



### 谓语（Predicates）



谓语用来查找某个特定的节点或者包含某个指定的值的节点。

谓语被嵌在方括号中。

**![img](https://img-blog.csdn.net/20170920201931075)
**

**![img](https://img-blog.csdn.net/20170920202011726)
**

## 4.5 在python 中使用

> pip install lxml

```python
    root = etree.HTML(html)
    divs = root.xpath('//div[@class="left"]/div[@class="sons"]')
    for div in divs:
        item['id'] = uuid.uuid4().hex
        item['title'] = div.xpath('./div[@class="cont"]/p/a/b/text()')[0]
        item['author'] = "-".join(div.xpath('./div[@class="cont"]/p/a/text()'))
        item['content'] = "<br>".join(
            div.xpath('./div[@class="cont"]/div[@class="contson"]//text()'))
```

# Python 中使用socks 代理

> **{'http':'http://username:password@IP:port'}**

```python
from urllib import request
#网上很多说的urllib2,在python3中其实就是urllib.request
proxy_support = request.ProxyHandler({'http':'http://username:password@IP:port'})
auth = request.HTTPBasicAuthHandler()
opener = request.build_opener(proxy_support, auth, request.HTTPHandler)
request.install_opener(opener)
response = request.urlopen("你访问的rul")
html = response.read()
```

```python
pip3 install Pysocks


import socket
import socks
socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 10808)
socket.socket = socks.socksocket
```

```python
# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:   test_socks
# Date:   2020/4/14
__Author__ = 'Negoo_wen'
#-------------------------------------------------------------------------------
import requests

import socket
import socks
socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 10808)
socket.socket = socks.socksocket

def main():
  url = 'https://www.google.com'
  html = requests.get(url).text
  print(html)


if __name__ == '__main__':
  main()
```

- urllib 默认会使用环境变量 http_proxy 来设置 HTTP Proxy。假如一个网站它会检测某一段时间某个IP 的访问次数，如果访问次数过多，它会禁止你的访问。所以你可以设置一些代理服务器来帮助你做工作，每隔一段时间换一个代理，网站君都不知道是谁在捣鬼了！

- 下面一段代码说明了代理的设置用法

```python
import urllib.request  
enable_proxy = True
proxy_support = urllib.request.ProxyHandler({'sock5': 'localhost:1080'})  
null_proxy_handler = urllib.request.ProxyHandler({})
if enable_proxy:
    opener = urllib.request.build_opener(proxy_support)  
else:
  opener = urllib.request.build_opener(null_proxy_handler)
urllib.request.install_opener(opener)  
a = urllib.request.urlopen("").read().decode("utf8")  
print(a)  
```

# [requests支持socks5代理了](https://www.cnblogs.com/c-x-a/p/10193004.html)

记录下
以前：

```python
import socket
import socks
from requests_html import HTMLSession
session=HTMLSession()
socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 1080)
socket.socket = socks.socksocket
url = "https://www.google.co.jp"
print(session.get(url).text)
```

现在：

```python
from requests_html import HTMLSession

session = HTMLSession()
proxy = {"http": "socks5://127.0.0.1:1080","https": "socks5://127.0.0.1:1080"}
url = "https://www.google.co.jp"
req = session.get(url, proxies=proxy)
print(req.text)
```

# 代理总结

- 以前requests不支持socks5 现在支持了
- 对于urllib 来说 可以使用安装 pysocks 方法 也可以自己试
- 上面的方法都是没经过实验的，使用时自己试着使

# 正则 python

```python
#  字符的表示
. 任意字符
[a-f] 范围内的任意字符
\w 字母数字下划线组成的任意字符
\W 与小写\w 取反
\d 数字
\D 非数字
\s 空白
\S 非空白
# 量词
* 0 或多个
+ 1 或多个
? 0 或1个
{n} n个 除了这个都是贪婪的
{n,} n个或大于n个
{n,m} n~m个

# 分组
() 普通分组，多个正则分组时，search(),group() 返回的是元祖

(?P<name>字符+数量) 带有名称的分组 groupdict返回的是字典

import re
text = "123abc90ccc"
res.search(r'(?P<n1>\d+?)[a-z]+?(?P<n2>\d+)',text).groupdict()
```

## python 的正则模块

```python
re.compile() 一次生成正则对象，可以多次匹配查询
re.match(正则对象,字符串) 只搜索一次
re.search()
re.findall()
re.sub()
re.split()

text = "123abc444"
re.sub('\d+','120',text)

str.replace(正则表达式,要替换的数)
```



## [python中，有关正则表达式re函数：compile、match、search、findall](https://www.cnblogs.com/xiaomingzaixian/p/7223651.html)

**1、全局匹配函数 re.compile(pattern=pattern,re.S).findall(text)函数：**

compile 函数根据一个模式字符串和可选的标志参数生成一个正则表达式对象。该对象拥有一系列方法用于正则表达式匹配和替换。

```
import re
string = 'dsfdspythondsfdsjpythonfds'
pattern = '.python'
s = re.compile(pattern=pattern).findall(string)
print(s)
```

![img](https://images2015.cnblogs.com/blog/801822/201707/801822-20170723085843934-117878653.png)

**2、re.match函数：（从第一字符开始匹配，不匹配则不成功，这也是match和search的区别）**

match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。

函数语法： re.match(pattern, string, flags=0)

匹配结果：re.match匹配成功会返回一个对象，否则返回None。

用group（num=0）或groups（）来获取匹配的结果

```
import re
string = '刘德华 Andy Lau'
pattern = '.*?\s'
s = re.match(pattern=pattern,string=string)
print(s.group())
```

![img](https://images2015.cnblogs.com/blog/801822/201707/801822-20170723090509262-728511208.png)

**3、re.search函数：**

扫描整个字符串并返回第一个成功的匹配。

函数语法：re.search(pattern, string, flags=0)

参数如上

匹配结果：如果匹配成功则返回一个匹配的对象，否则返回None。

用group（num=0）或groups（）来获取匹配的结果。

# BeatifulSoup 解析工具

```
pip install bs4
from bs4 import BeautifulSoup
```

> 使用

```python
# 网上文件生成对象 soup = BeautifulSoup('网上下载的字符串','lxml')
# 本地文件生成对象 soup = BeautifulSoup(open('1.html'),'lxml')

# 根据标签名查找
soup.a # 只找第一个a 标签

# 函数
find('a') # 只找到第一个a标签
find('a',title='名字')
find('a',class_='名字') # 通过class属性查找第一a

find_all('a') # 查找所有的a标签 返回list 列表
find_all(['a','span']) # 查找返回所有a和span 标签 
# 每一项标签类型可以定义为文本或者bs 对象（标签对象）如果是标签对象可依据需使用.h3或get()或find()等相关命令
find_all('a',limit=2) # 只找前两个

# select
	# element
	select('p') # 选择所有p 元素
   	# .class
    select('.firstname') # 选择所有class 为firstname 的标签
    # #id
    select('#firstname') # 选择所有id 为firstname 的标签
    # 属性选择器
    	# [attribute] 
        sleect('li[class]') # 选择所有带有类属性的li
        # [attribute=value]
        select('li[class=app]')
    # 层级选择器
    	# element element div p
        # element>element div>p
        # element,element div,p
# 获取子孙节点
contents # 返回一个列表
descendants # 返回的是一个生成器

# 节点信息
bs4.element.Tag
	# 获取节点内容
    obj.string
    obj.text
    obj.get_text()
    # 节点属性
    tag.name # 获取标签名
    tag.attrs # 将属性值作为一个字典返回
	# 获取节点属性
    obj.sttrs.get('title')
    obj.get('title')
    obj['title']
# 节点类型
bs4.BeautifulSoup # 根节点类型
bs4.element.NavigableString # 连接类型
bs4.element.Tag # 节点类型
bs4.element.Comment # 注释类型

```

# 协程 asyncio

```python
loop = asyncio.get_event_loop()
# 运行起来直到所有协程全都执行完毕才结束
# loop.run_until_complete() # 起始协程是一个 
loop.run_until_complete(asyncio.wait(
    (get(''),post(''))
)) # 起始协程是多个
    
asyncio.run(fun1()) # 代替上面那几行


```

## Task对象

```python
# Task对象
# asyncio.create_task() 推荐
# loop.create_task()
# asyncio.ensure_future()

tasks = [asyncio.create_task(fun1(i),name="n1") for i in range(10)] # create_task 函数是添加函数到事件循环里面
asyncio.run(asyncio.wait(tasks)) # wait() 的意思是等待这几个任务完成
# 这么写会报错，报错原因是你还没创建事件循环 无法将fun1() 函数添加到循环里面
# 可以这么写
tasks = [fun1(i) for i in range(10)]
done,pending = asyncio.run(asyncio.wait(tasks，timeout=None)) # 这么写可以是因为 你在创建事件循环的时候，他会封装tasks列表成为task类型
# done 是正常情况下程序的结果，pending 是程序的状态
# task 对象就是将任务放到事件循环
```

## Await

```python
await + 可等待对象（协程对象，Future,Task,IO等待）
异步函数直接调用不会执行 只会返回一个协程对象 无法直接执行
```

## Future 

```python
# Task 继承于Future Task对象内部结果的处理

async def set_future(fut):
    await asyncio.sleep(3)
    fut.set_result("666")

async def main():
    # 获取当前事件循环
    loop = asyncio.get_rrunning_loop()
    # 创建一个任务，这个任务什么都不干
    fut = loop.create_future()
    # 等待任务最终结果（Future对象），没有结果则会一直等下去吗
    await loop.create_task(set_future(fut))
    await fut
    
asyncio.run( main() )
    
```

## concurrent.futures.Future 对象

```python
使用线程池，进程池才使用的对象
# 在以后代码可能会存在交叉使用
import time
import asyncio
import concurrent.futures
def func1():
    time.sleep(2)
    return "aaa"
async def main():
    loop = asyncio.get_running_loop()
    # run in the default loop's executor (默认的ThreadPoolExecutor)
    # 第一步调用ThreadPoolExecutor 的 submit方法去线程池中申请一个线程去执行func1函数，并返回一个concurrent.futures.Future对象
    # 第二步 调用asyncio.wrap_future 将concurrent.futures.Futures包装成	async.Future 对象
    # 因为concurrent.futures.Futures对象不支持await语法，所以需要包含asyncio.Future对象，才能使用
    fut = loop.run_in_executor(None,func1)
    result = await fut
   	print ("chenggong ")
    
asyncio.run(main())
```

## 异步迭代器

```python
async def main():
	async for i in iter:
    	...
# 一步迭代期循环只能在一个异步函数里，不在会报错
```

## 异步上下文管理器

```python
# 有__aenter__() 和 __aexit__() 来对async with 语句中的环境进行控制
import asyncio

class AsyncContent:
    def __init__(self):
        pass
    async def do_soming(self):
        return 666
    async def __aenter__(self):
        # 异步链接数据库
        self.conn = await asyncio.sleep(1)
        return self
    async def __aexit__(self,exc_type,exc,tb):
        # 异步关闭数据库
        await asyncio.sleep(1)
async def main():
	async with AsyncContent() as f:
    result = await f.do_soming()
    print(result)    
# 必须放到异步函数里
async.run(main())
        
```

## uvloop

> **是asyncio的事件循环的替代方案，事件循环>默认的asyyncio 的事件循环**

``` python
pip install uvloop
# 和go 语言差不多了
```

```python
import asyncio
import uvloop
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
# 编写async 代码和之前一样
# 内部的事件循环会自动变化为ucloop
asyncio.run(main())

django->asgi->uvicorn->uvloop
```

## 异步操作redis

```python
pip install aioredis
```

```python
import asyncio
import aioredis

async def execute(address,password):
    print("开始执行"，address)
    # 网络IO操作：创建redis链接
    redis = await aioredis.create_redis(address,password=password)
    
    # 网络IO操作：在redis中设置哈希值car,内部在设置三个键值对
    await redis.hmset_dict("car",key1=1,key2=2,key3=3)
    
	# 网络IO操作：创建redis链接
    result = await redis.hgetall("car",encoding="utf-8")
    print(result)
    result.close()
    # 网络IO操作：关闭redis链接
    await redis.wait_closed()
    print("结束",address)
asyncio.run(execute("http://....:6379","root!1234"))

```

## 异步操作MySql

```python
pip install aiomysql
```

```python
import asyncio
import aiomysql

async def execute(address,password):
    print("开始执行"，address)
    # 网络IO操作：链接mysql
    conn = await aiomysql.connect(host,port,user,password,db)
    
    # 网络IO操作：创建cursor
    cur = await conn.cursor()
    
	# 网络IO操作：执行SQL
    await cur.execute("select host.user from user")
    
    # 网络IO操作：获取SQL结果
    result = await cur.fetchall()
    print(result)
    
    # 网络IO操作：关闭连接
    await cur.close()
    conn.close
    
    print("结束",address)
asyncio.run(execute("http://....:6379","root!1234"))
```

## FastAPI框架

```python
pip install fastapi
```

```python
pip install uvicorn
```

```python
# main.py

from fastapi import FastAPI

app = FastAPI()

async def authenticate_user(
        username: str, password: str) -> schemas.User:
    user = await User.async_first(name=username)
    user = schemas.UserAuth(**user)
    if not user: return False
    if not verify_password(password, user.password): return False
    return user
if __name__ == "__main__":
    uvicorn.run("luffy:app", )
```

sys.argv[1] 是命令行参数列表

# Selenium

> 驱动浏览器 进行浏览器相关操作

### Selenium是什么:

ason Huggins在2004年发起了Selenium项目，当时身处ThoughtWorks的他，为了不想让自己的时间浪费在无聊的重复性工作中，幸运的是，所有被测试的浏览器都支持Javascript。Jason和他所在的团队采用Javascript编写一种测试工具来验证浏览器页面的行为；这个JavaScript类库就是Selenium core，同时也是seleniumRC、Selenium IDE的核心组件。Selenium由此诞生。

关于Selenium的命名比较有意思，当时QTP mercury是主流的商业自化工具，是化学元素汞（俗称水银），而Selenium是开源自动化工具，是化学元素硒，硒可以对抗汞。

因为Selenium和Webdriver的合并，所以，Selenium 2.0由此诞生。简单用公式表示为：Selenium 2.0 = Selenium 1.0 + WebDriver

### Selenium 使用

```python
pip install selenium

from selenium.webdriver import Chrome

chrome = Chrome(executable_path="chromedriver.exe") # 谷歌浏览器的可执行驱动程序
# window 把驱动程序放到项目目录下
# linux mac 放到/usr/local/bin 下 之后直接指定驱动程序名称
chrome.get(url)

# 定位元素
find_element_by_id
find_elements_by_name
find_elements_by_xpath
find_elements_by_tag_name
find_elements_by_class_name
find_elements_by_css_selector
find_elements_by_link_text

# 访问元素信息
.get_attribute('class') # 获取元素属性
.text # 获取元素文本
.id # 获取id
.tag_name # 获取标签名

# 交互
# 点击click()
# 输入send_keys()
# 清除 .clear()
# 退出浏览器 chrome.quit() 
# 窗口最大化 driver.maximize_window()
# 页面返回 driver.back()
# 页面前进 driver.forward()
# 模拟JS滚动
	# var  q = document.documentElement.scrollTop = 10000
    # execute_script() 执行 js代码
# 获取网页代码 page_source

# 页面ajax的解决办法
# 导包
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
# 解决
# 等待某一个Element出现为止，否则一直阻塞下去，不过可以设置一个超时时间
ui.WebDriverWait(driver,60).until(EC.visibility_of_all_elements_located((By.CLASS_NAME,'soupager')))

# switch
# 原因
	# 当页面中出现对话框alert或内嵌窗口iframe
	# 如果查找的元素节点在alert或iframe中的话则需要
# 解决
	# 查找iframe标签对象 iframe = driver.find_element_by_id('login_frame')
    # 切换到iframe中 driver.switch_to.frame(iframe)
# 获取浏览器页签
	# driver.window_handlers[0] 第一个页签
    # w2 = driver.window_handlers[1] 第二个页签
    # driver.switch_to.window(w2)
```

```python
chrome.find_element(By.XPATH,"//div/@class") 根据by 查找一个元素
chrome.find_elements(BY.CSS_SELECTOR,".app .huya span") 根据by 查找多个元素
By.CLASS_NAME
BY.CSS_SELECTOR
By.ID
By.NAME
By.TAG_NAME
By.XPATH
By.LINK_TEXT

chrome.close() # 关闭窗口
chrome.save_screenshot("a.png") # 截屏
chrome.get_cookies()
chrome.get_window_rect() # 元素在屏幕的位置
chrome.get_window_size() # 窗口的大小
chrome.set_window_size(1920,1080)
```



```python
2.  键盘常用操作方法：

send_keys() # Keys 模拟键盘输入；模拟键盘按键、组合键等

部分key 列举如下：

ALT= u'\ue00a'

ARROW_DOWN= u'\ue015'

ARROW_LEFT= u'\ue012'

ARROW_RIGHT= u'\ue014'

ARROW_UP= u'\ue013'

BACKSPACE= u'\ue003'

BACK_SPACE= u'\ue003'

CANCEL= u'\ue001'

CLEAR= u'\ue005'

COMMAND= u'\ue03d'

CONTROL= u'\ue009'

3.  鼠标常用操作方法：

click() # ActionChains 模拟鼠标操作，除了最常用的点击，还有右击、双击等

方法

描述

click(on_element=None)

单击鼠标左键

click_and_hold(on_element=None)

点击鼠标左键，不松开

context_click(on_element=None)

点击鼠标右键

double_click(on_element=None)

双击鼠标左键

drag_and_drop(source,   target)

拖拽到某个元素然后松开

drag_and_drop_by_offset(source,xoffset,yoffset)

拖拽到某个坐标然后松开

key_down(value,   element=None)

按下某个键盘上的键

key_up(value,   element=None)

松开某个键

move_by_offset(xoffset,   yoffset)

鼠标从当前位置移动到某个坐标

move_to_element(to_element)

鼠标移动到某个元素

move_to_element_with_offset(to_element,   xoffset, yoffset)

移动到距某个元素（左上角坐标）多少距离的位置

perform()

执行链中的所有动作

release(on_element=None)

在某个元素位置松开鼠标左键

send_keys(*keys_to_send)

发送某个键到当前焦点的元素

send_keys_to_element(element,   *keys_to_send)

发送某个键到指定元素

 

4.  调用js脚本：

execute_script  #执行js脚本完成特定操作
```



# Splash

> 是web 服务，基于webkit技术框架，可以动态加载网页

### 什么是Splash

Splash是一个Javascript渲染服务。它是一个实现了HTTP API的轻量级浏览器，Splash是用Python实现的，同时使用Twisted和QT。Twisted（QT）用来让服务具有异步处理能力，以发挥webkit的并发能力。

### 为什么要有Splash：

为了更加有效的制作网页爬虫，由于目前很多的网页通过javascript模式进行交互，简单的爬取网页模式无法胜任javascript页面的生成和ajax网页的爬取，同时通过分析连接请求的方式来落实局部连接数据请求，相对比较复杂，尤其是对带有特定时间戳算法的页面，分析难度较大，效率不高。而通过调用浏览器模拟页面动作模式，需要使用浏览器，无法实现异步和大规模爬取需求。鉴于上述理由Splash也就有了用武之地。一个页面渲染服务器，返回渲染后的页面，便于爬取，便于规模应用

### Splash和selenium两者的区别：

selenium是浏览器测试自动化工具，很容易完成鼠标点击，翻页等动作，确定是一次只能加载一个页面，无法异步渲染页面，也就限制了selenium爬虫的抓取效率

splash可以实现异步渲染页面，可以同时渲染几个页面。缺点是在页面点击，模拟登陆方面没有selenium灵活。

### Splash使用

#### docker部署Splash

```shell
docker pull scrapinghub/splash

sudo docker run -dit --name splash-server -p 5023:5023 -p 9099:8050 -p 8051:8051 scrapinghub/splash

curl http://localhost:9099/render.html?url=http://jd.com
```

启动splash服务，并通过http，https，telnet提供服务

通常一般使用http模式，可以只启用一个8050（http）就好，也可以指定8051（https）和5023（telnet）

# 自动化测试

## 1、单元测试

### python单元测试模块 unittest

## 2、集成测试

### 单元测试套件 unittest.TestSuit

## 3、系统测试

### 3.1、UI自动化测试

### 3.2、性能测试

### 3.3、安全测试

### 

# Scrapy

## Scrapy安装

```python
pip install scrapy

# 如果出错需要安装依赖 如果出错可以安装 anconda 之后在安装
twisted 包 # 去pypi 下载twisted
```

## 文档

> https://www.osgeo.cn/scrapy/intro/tutorial.html
>
> https://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html

- Scrapy是一个应用程序框架，用于对网站进行爬行和提取结构化数据，这些结构化数据可用于各种有用的应用程序，如数据挖掘、信息处理或历史存档。
- 提供两种爬虫方式
  - scrapy.Spider 普通爬虫类
  - scrapy.CrawSpider 规则的爬虫类

## 架构图

```python
# 五大核心
- 引擎（engine）
	- 自动运行无需关注，会自动组织所有的请求对象，分发给下载器
    - 协调其他四个组件之间的联系，即与其他四个组件之间通信，也是scrapy 框架的核心
- 下载器（downloader）
	- 从引擎处获取到请求对象后，请求数据
    - 实现请求任务的执行，从网络上请求数据
    - 将请求的数据封装成响应对象，并将响应对象返回给engine
    - engine将相应对象（以回调方式）回传给他的爬虫对象进行解析
- 爬虫 （spiders）
	- scrapy.Spider 普通爬虫
	- scrapy.CrawSpider
		- 可设置规则的爬虫类
		- Rule 规则类
	- 开始的函数 start_requests()
    - 爬虫程序的编写代码所在，也是发起请求开始的位置
    - spider 发起请求，经过engine转入到scheduler中
- 调度器（scheduler）
	- 调度所有请求（优先级越高则会优先执行）
    - 当执行某一请求是，由engine转入到downloader中
- 管道（item pipeline）
	- 1、清理HTML数据
	- 2、验证爬取的数据（检查item包含某些字段）
	- 3、查重（并丢弃）
	- 4、将爬取的结果保存的数据库中
	- 5、对图片数据进行下载

# 两大中间件
- 爬虫中间件
	- 介于Spider和Engine之间的，可以拦截Spider发起的请求及数据
- 下载中间件
	- 介于Engine和Downloader之间的，可以拦截下载和响应的对象，可以在下载之前，设置代理，请求头，Cookie等操作
    - 还可以基于 Splash或者Selenium实现特定的操作
```



## 工作原理

### 示意图

![](https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg.mp.itc.cn%2Fupload%2F20170513%2F9d06590fed5d4646a25fe14da87d6612_th.jpg&refer=http%3A%2F%2Fimg.mp.itc.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1617171736&t=0d824d690d20cc5d7aeac414ab3a4380)

## scrapy指令

- 创建项目的命令
  
  - `scrapy startproject 项目名称`
  
- 创建爬虫的命令

  - scrapy genspider 爬虫名 域名

- 启动爬虫的命令

  - scrapy crawl 爬虫名

- 调试爬虫的命令

  - `scrapy shell [url]`

  - ```shell
    # 没有url可以去里面请求
    scrapy shell
    fetch('http://qidian.com/finish')
    response
    # 有url不用去里面请求 
    scrapy shell http://qidian.com/finish
    response
    
    # 退出
    exit()
    ```

```shell
Usage:
  scrapy <command> [options] [args]

Available commands:
  bench         Run quick benchmark test
  check         Check spider contracts
  commands
  crawl         Run a spider
  edit          Edit spider
  fetch         Fetch a URL using the Scrapy downloader
  genspider     Generate new spider using pre-defined templates
  list          List available spiders
  parse         Parse URL (using its spider) and print the results
  runspider     Run a self-contained spider (without creating a project)
  settings      Get settings values
  shell         Interactive scraping console
  startproject  Create new project
  version       Print Scrapy version
  view          Open URL in browser, as seen by Scrapy
```

```python
http://www.baidu.com/robots.txt
# 这个文件代表此网站可不可以被爬虫爬取
```

## 爬虫停止条件

- **可用选项**
  -  **CLOSESPIDER_TIMEOUT** （秒）指定时间过后
  -  **CLOSESPIDER_ITEMCOUNT**  抓取了指定数目的item后
  -  **CLOSESPIDER_PAGECOUNT**  收到了指定数目的响应后
  -  **CLOSESPIDER_ERRPRCOUNT** 发生了指定数目的错误之后
- **案例**
  - **scrapy crawl fast -s CLOSESPIDER_ITEMCOUNT=10**
  - **scrapy crawl fast -s CLOSESPIDER_PAGECOUNT=10**
  - **scrapy crawl fast -s CLOSESPIDER_TIMEOUT=10**

## 自定义爬虫文件的参数

-  scrapy.genspider 爬虫的名字 网页的域名

- 继承scrapy.Spider类

  - name='qidian'
  - allowed_domains
  - start_urls
  - parse(self,response)

- 解析数据返回给engine

  - yield item

- 向engine发起新请求

  - yield scrapy.Request(url,callback=,meta=,dont_filter=True)

- 运行程序

  - scrapy carwl 爬虫名称

  - 导出文件
    - -o name.json
    - -o name.xml
    - -o name.csv
    - eg：scrapy crawl dy -o vides.json

## scrapy 配置文件

```python
# Scrapy settings for qidian project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'qidian'

SPIDER_MODULES = ['qidian.spiders']
NEWSPIDER_MODULE = 'qidian.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'

# Obey robots.txt rules
# 判断是否可以爬取该网站
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# 同时最大请求数（默认16）
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# 每一次请求延时多长时间
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# 是否开启Cookie
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# 是否可以远程连接
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# 默认的请求头
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# 爬虫中间件
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'qidian.middlewares.QidianSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# 下载中间件
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'qidian.middlewares.QidianDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# 扩展
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# 管道
#ITEM_PIPELINES = {
#    'qidian.pipelines.QidianPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# http缓存
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

```

## Response类

- 属性相关
  - **body** 响应的字节数据
  - **encoding** 字符编码
  - **text** 响应的编码之后文本数据
  - **headers** 响应头信息，是字节数据
  - **status** 响应的状态码
  - **url** 请求的url
  - **request** 请求对象
  - **meta** 用于request和 callback回调函数之间传值
  - **urljoin** 用于拼接url 继承自**urllib.urljoin**,直接使用只需添加要拼接的url

- **解析相关**【重点】

  - selector()

  - **css()** 样式选择器 返回Selector选择器的可迭代对象

    - scrapy.selector.SelectorList 选择器列表

    - scrapy.selector.Selector 选择器

    - ```python
      response.css('title::text')
      # text 代表标签内的文字
      
      response.css('title::attr("href")')
      # attr 代表标签的属性
      
      response.css('title:last-child')
      response.css('title[class="app"]')
      
      ```

  - **xpath()** xpath路径 

    - 该xpath 使用方法和正常的xpath一样

  - **获取字符串对象**

    - ```python
      # get() 获取第一个元素 变成str 字符串对象
      response.css('div').get()
      
      # getall() 提取全部 变成str 字符串对象
      response.css('div').getall()
      
      # extracy() 提取全部 变成str 字符串对象
      response.css('div').extracy()
      
      # extracy_first() 提取第一个 变成str 字符串对象
      response.css('div').extracy_first()
      
      # re() 按照正则匹配返回全部 字符
      response.css('div').re(regex)
      
      # re_first() 按照正则匹配返回第一个 字符
      response.css('div').re_first(regex)
      ```


- **使用 yield** 

- ```python
  import uuid
  
  import scrapy
  from scrapy.http import Response, HtmlResponse, Request
  from scrapy.selector import Selector, SelectorList
  
  from qidian.items import *
  
  class FinishSpider(scrapy.Spider):
      name = 'finish'
      allowed_domains = ['qidian.com',"book.qidian.com"] # 允许的域名
      start_urls = ['https://www.qidian.com/finish'] # 开始的url
  
      def parse(self, response: Response):
          if response.status == 200:
              liList = response.css(".all-img-list.cf li")
              for i in liList:
                  item = BookItem()
                  item["book_id"] = uuid.uuid4().hex
                  item["url"] = i.css('.book-mid-info h4 a::attr("href")').get()
                  item["cover"] = i.css('.book-img-box a img::attr("src")').get()
                  item["name"] = i.css('.book-mid-info h4 a::text').get()
                  item["summary"] = i.css(
                      '.book-mid-info .intro::text').get().replace(" ", "").replace("\r", "")
                  item["author"], * \
                      item["tags"] = i.css(
                          '.book-mid-info .author a::text').getall()
                  yield Request(response.urljoin(item["url"]),callback=self.parse_info,priority=1,meta={'book_id':item['book_id']})
                  yield item
  
                  # 请求小说详情页
              next_url = response.css(
                  ".lbf-pagination li:last-child a::attr('href')").get()
              if next_url.find("javascript") == -1:
                  yield Request(response.urljoin(next_url),callback=self.parse,priority=100)
  
      def parse_info(self,response:Response):
          if response.status == 200: 
              print("解析小说详情---",response.meta['book_id'])
  ```

## Request类

- **参数**
  - **url** 请求的url
  - **callback** 请求回调，请求完了执行哪个函数 如果请求回来的数据和当前解析的一样，callback 可以不写，就比如上面的例子，就可以不写
  - **method** 请求方法 默认get
  - **headers** 请求头，默认没有
  - **body** 请求体，默认没有
  - **cookies** cookie，默认没有
  - **meta** 元数据，默认没有，方便与response 之间进行传值
  - **encoding** 编码方式，默认‘utf-8’
  - **priority** 请求优先级，默认0 数越大优先级越高
  - **dont_filter** 过滤重复的url True为不过滤，False过滤

## scrapy 的数据管道

### 指令方式存储数据

```shell
scrapy crawl finish -o qidian.json
```

- 只适合单页数据 的爬取，如果我们多页多层次爬取时，不适合此方式。

### Item类

作用：用于区别那一页（类型）的数据

用法：类似于 dict用法，在数据管道类的process_item() 方法中，通过isinstance() 方法来判断item是哪一类型的。

```python
# items.py
import scrapy

class BookItem(scrapy.Item):
    book_id = scrapy.Field() # 书的id
    url = scrapy.Field()     # 书的url
    cover = scrapy.Field()   # 书封面url
    name = scrapy.Field()    # 书名
    summary = scrapy.Field() # 简介
    author = scrapy.Field()  # 作者
    tags = scrapy.Field()    # 标签


class JuanItem(scrapy.Item):
    juan_id = scrapy.Field()  # 卷的id
    book_id = scrapy.Field()  # 数的id
    title = scrapy.Field()    # 卷名

class SegItem(scrapy.Item):
    seg_id = scrapy.Field()  # 章节id
    title = scrapy.Field()   # 章节标题
    juan_id = scrapy.Field() # 卷id

class SegDetail(scrapy.Item):
    seg_id = scrapy.Field() # 章节id
    text = scrapy.Field()   # 内容
```

```python
# pipelines.py
    # 通过isinstance() 方法来判断item是哪一类型的
    def process_item(self, item, spider):
        # print(item)
        if isinstance(item, BookItem):
            self.save_csv(item,self.book_csv)
        elif isinstance(item, JuanItem):
            self.save_csv(item,self.juan_csv)
        elif isinstance(item, SegItem):
            self.save_csv(item,self.seg_csv)
        return item
```

```python
 # spiders/finish.py
    def parse(self, response: Response):
        if response.status == 200:
            liList = response.css(".all-img-list.cf li")
            for i in liList:
                item = BookItem()
                item["book_id"] = uuid.uuid4().hex
                item["url"] = i.css('.book-mid-info h4 a::attr("href")').get()
                item["cover"] = i.css('.book-img-box a img::attr("src")').get()
                item["name"] = i.css('.book-mid-info h4 a::text').get()
                item["summary"] = i.css(
                    '.book-mid-info .intro::text').get().replace(" ", "").replace("\r", "")
                item["author"], * \
                    item["tags"] = i.css(
                        '.book-mid-info .author a::text').getall()
                yield Request(response.urljoin(item["url"]),callback=self.parse_info,priority=1,meta={'book_id':item['book_id']})
                yield item
```

### Pipeline

- 处理数据的方法

  ```python
  def process_item(self, item, spider):
      return item
  ```
  - item 参数表示爬虫类中解释到的数据（yield item）
  - spider 参数 表示爬虫类对象
  - 如果item被返回，则表示可以被优先级低的pipleline处理，代表可以被多个管道处理。

- 初始化方法

  属于定制方法，可以初始化一些参数或者对象，文件名，数据库链接等

  ```python
      def __init__(self):
          self.book_csv = 'book.csv'
          self.seg_csv = 'seg.csv'
          self.seg_detail_csv = 'seg_detail.csv'
  ```

- `process_item`和`init`调用次数

  - `process_item`方法 会被engine 多次调用
  - `init` 方法随着爬虫程序的启动时创建pipleline类时调用，只会调用一次

- 新建管道

  - 300 是管道优先级，越大优先级越低，数字相同，按顺序，与Request优先级顺序相反

  ```python
  # settings.py
  ITEM_PIPELINES = {
     'qidian.pipelines.QidianPipeline': 300,
     'qidian.pipelines.DBpipeline': 300,
  }
  ```

  - Dao 数据库设计（储存到数据库）

    ```python
    import pymysql
    from pymysql.cursors import DictCursor
    class Database():
        def __init__(self):
            self.conn = pymysql.Connection(
                host='localhost',
                port=3306,
                user='root',
                password='1234',
                db='qidian'
            )
    
        def __enter__(self):
            return self.conn.cursor(cursor=DictCursor)
    
        def __exit__(self,exc_type,exc_val,exc_tb):
            if exc_type:
                self.conn.rollback()
            else:
                self.conn.commit()
            
            return True
    
        def close(self):
            self.conn.close()
    
    
    class BaseDao():
        def __init__(self):
            self.db = Database()
    
        def save(self,table_name,**item):
            sql = 'insert into %s(%s) values(%s)'
            fields = ",".join(item.keys())
            field_placeholds = ",".join(['%%(%s)s' % key for key in item])
    
            with self.db as cursor:
                cursor.execute(sql % (table_name,fields,field_placeholds),item)
    
                # 判断执行是否成功
                if cursor.rowcount > 0:
                    return True
                
            return False
    ```

    ```python
    class DBpipeline:
        def __init__(self):
            self.dao = BaseDao()
            self.book_table = "t_book"
            self.seg_table = "t_seg"
            self.seg_detail_table = "t_detail_seg"
    
        def process_item(self, item, spider):
            if isinstance(item, BookItem):
                item["tags"] = "-".join(item["tags"])
                self.dao.save(self.book_table,**item)
            
            elif isinstance(item, SegItem):
                self.dao.save(self.seg_table,**item)
    
            elif isinstance(item, SegDetail):
                self.dao.save(self.seg_detail_table,**item)
        
            return item
    ```


## 定量爬虫

### 基于信号的方式【推荐】

```shell
scrapy crawl -s 信号
```

常用的scrapy 信号

-  **CLOSESPIDER_TIMEOUT** （秒）指定时间过后
-  **CLOSESPIDER_ITEMCOUNT**  抓取了指定数目的item后
-  **CLOSESPIDER_PAGECOUNT**  收到了指定数目的响应后
-  **CLOSESPIDER_ERRPRCOUNT** 发生了指定数目的错误之后

```shell
scrapy crawl finish -s CLOSESPIDER_ITEMCOUNT=10
```

### 异常方式 **Raise**【不一定好使】

- `raise Exception('停止爬虫')`

```python
class CSVPipeline:
    def __init__(self):
        self.book_csv = 'book.csv'
        self.seg_csv = 'seg.csv'
        self.seg_detail_csv = 'seg_detail.csv'
        self.num = 0
        
    def process_item(self, item, spider):
		if num == 10:
            raise Exception('停止爬虫')
```

### telnet 远程连接 关掉

## 中间件

> 在setting.py 中越小权重越高

###  爬虫中间件

```python
监测爬虫类语音情之间的交互数据（请求 Request，响应 Response，数据item）及异常 Exception
```

```python
@classmethod
def from_crawler(cls,crawler):pass # 启动爬虫时用于创建爬虫中间件类的实例对象

def process_spider_input(self, response, spider): pass # engine 将我们请求响应的数据传给spider时调用

def process_spider_output(self, response, result, spider):pass # spider 将解析之后产生的数据，返回给engine是调用此方法

def process_spider_exception(self, response, exception, spider):pass # 解析数据时发生异常

def process_start_requests(self, start_requests, spider):pass # 第一次爬虫发起请求时调用该方法

```



### 下载中间件【重点】

```python
下载中间件是engine和downloader之间的中间件，可以拦截请求和响应以及请求异常的处理
```

```python
@classmethod
def from_crawler(cls, crawler):

def process_request(self, request, spider):pass

def process_response(self, request, response, spider):pass

def process_exception(self, request, exception, spider):pass
```

- **process_request()** 方法可返回的对象 （四种可能）【**优先级越高的中间件，越先调用；**】

  - scrapy.http.Request
  - scrapy.http.HtmlResponse/Response
  - None 表示不拦截
  - raise IgnoreRequest 不下载这个请求

  ```python
  1、返回None：scrapy会继续执行其他中间件相应的方法；
  2、返回Response对象：scrapy不会再调用其他中间件的process_request方法，也不会去发起下载，而是直接返回该Response对象；
  3、返回Request对象：scrapy不会再调用其他中间件的process_request()方法，而是将其放置调度器待调度下载；
  4、抛出IgnoreRequest异常：已安装中间件的process_exception()会被调用，如果它们没有捕获该异常，则Request.errback会被调用；如果再没被处理，它会被忽略，且不会写进日志。
  ```

  

- **process_response()** 方法可返回的对象 【**优先级越高的中间件，越晚被调用；**】

  - scrapy.http.Request 未下载成功的请求
  - scrapy.http.Response 进一步封装之后的Response
  - raise IgnoreRequest 不下载这个请求

  ```python
  1、返回Response对象：scrapy会继续调用其他中间件的process_response方法；
  2、返回Request对象：停止中间器调用，将其放置到调度器待调度下载；
  3、抛出IgnoreRequest异常：Request.errback会被调用来处理函数，如果没有处理，它将会被忽略且不会写进日志。
  ```

- #### **process_exception(request, exception, spider)**
  - scrapy.http.Request
  - scrapy.http.Response
  - None 表示不拦截

  ```python
  1、如果返回None：scrapy会继续调用其他中间件的process_exception()；
  2、如果返回Response对象：中间件链的process_response()开始启动，不会继续调用其他中间件的process_exception()；
  3、如果返回Request对象：停止中间器的process_exception()方法调用，将其放置到调度器待调度下载。
  ```

- **from_crawler(cls, crawler)**

  ```python
  1、如果存在该函数，from_crawler会被调用使用crawler来创建中间器对象，必须返回一个中间器对象，通过这种方式，可以访问到crawler的所有核心部件，如settings、signals等。
  ```


#### 作用

> 在下载中间件中，可以设置代理，设置cookie，设置请求头以及基于Selenium实现动态js渲染和用户登录

#### 设置代理

```python
request.meta['proxy'] = 'http://60.174.189.42:9999'
```

## 规则爬虫

> 不用再做分页了，他自己把符合规则的所有链接访问一遍，返回给callback


```bash
scrapy genspider -t crawl qy qcc.com # 新建qy 规则爬虫
scrapy genspider -t crawl 爬虫名 域名
```

- 作用：提取感兴趣a标签中的href属性，因此在指定正则表达式，参考某些a标签href属性写法。如果正则提取困难，则支持css，xpath两个方式来指定a标签所在父级标签

```python
# 提取链接
# rapy shell 链接

from scrapy.linkextractors import LinkExtractor

links =  extractor.extract_links(response)
for link in links:
    print(link.url,link.text) # 获取链接的路径和文本名称
```

- scrapy.spiders.CrawSpider 规则类爬虫

  - 重写了parse()解析函数，在此函数中通过指定规则中的LinkExtractor对象来提取当前相应数据中的链接，并向engine发起新的请求。新的请求中包含我们提取的链接url，和规则中的回调函数

  ```python
  class CrawlSpider(Spider):
  
      rules: Sequence[Rule] = ()
  
      def __init__(self, *a, **kw):
          super().__init__(*a, **kw)
          self._compile_rules()
  
      def _parse(self, response, **kwargs):
          return self._parse_response(
              response=response,
              callback=self.parse_start_url,
              cb_kwargs=kwargs,
              follow=True,
          )
  
      def parse_start_url(self, response, **kwargs):
          return []
  
      def process_results(self, response, results):
          return results
  
      def _build_request(self, rule_index, link):
          return Request(
              url=link.url,
              callback=self._callback,
              errback=self._errback,
              meta=dict(rule=rule_index, link_text=link.text),
          )
  
      def _requests_to_follow(self, response):
          if not isinstance(response, HtmlResponse):
              return
          seen = set()
          for rule_index, rule in enumerate(self._rules):
              links = [lnk for lnk in rule.link_extractor.extract_links(response)
                       if lnk not in seen]
              for link in rule.process_links(links):
                  seen.add(link)
                  request = self._build_request(rule_index, link)
                  yield rule.process_request(request, response)
  
      def _callback(self, response):
          rule = self._rules[response.meta['rule']]
          return self._parse_response(response, rule.callback, rule.cb_kwargs, rule.follow)
  
      def _errback(self, failure):
          rule = self._rules[failure.request.meta['rule']]
          return self._handle_failure(failure, rule.errback)
  
      def _parse_response(self, response, callback, cb_kwargs, follow=True):
          if callback:
              cb_res = callback(response, **cb_kwargs) or ()
              cb_res = self.process_results(response, cb_res)
              for request_or_item in iterate_spider_output(cb_res):
                  yield request_or_item
  
          if follow and self._follow_links:
              for request_or_item in self._requests_to_follow(response):
                  yield request_or_item
  
      def _handle_failure(self, failure, errback):
          if errback:
              results = errback(failure) or ()
              for request_or_item in iterate_spider_output(results):
                  yield request_or_item
  
      def _compile_rules(self):
          self._rules = []
          for rule in self.rules:
              self._rules.append(copy.copy(rule))
              self._rules[-1]._compile(self)
  
      @classmethod
      def from_crawler(cls, crawler, *args, **kwargs):
          spider = super().from_crawler(crawler, *args, **kwargs)
          spider._follow_links = crawler.settings.getbool('CRAWLSPIDER_FOLLOW_LINKS', True)
          return spider
  
  ```

- scrapy.spiders.Rule 规则类

  - extractor:LinkExtractor
  - callback:str
  - follow:bool

- scrapy.linkextractors.LinkExtractor 链接提取器类

  - allow
  - deny
  - restrict_xpaths
  - restrict_css

- 创建规则爬虫是使用-t crawl模板

  ```shell
  scrapy genspider -t crawl 爬虫名 域名
  ```

```python
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class QySpider(CrawlSpider):
    name = 'qy'
    allowed_domains = ['qcc.com']
    start_urls = ['http://qcc.com/']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )
    # allow 允许提取链接的方式
    # deny 不允许提取链接的方式
	# follow 是响应按不按照上一个内容继续提取
    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
    
    
```

### 1.爬虫文件中导入的Link Extractors：

```python
class scrapy.linkextractors.LinkExtractor
作用是：

# 每个LinkExtractor有唯一的公共方法是 extract_links()，它接收一个 Response 对象，类中定义了Response中的链接的提取规则，并返回一个 scrapy.link.Link 对象，返回的是符合链接匹配对象的列表。

# Link Extractors要实例化一次，并且extract_links 方法会根据不同的 response 调用多次提取链接｡
```

### 2.Link Extractors 中的主要参数：

```python
# allow：满足括号中“正则表达式”的值会被提取，如果为空，则全部匹配。（使用最多）

# deny：与这个正则表达式(或正则表达式列表)不匹配的URL一定不提取。

# allow_domains：会被提取的链接的domains。

# deny_domains：一定不会被提取链接的domains。

# restrict_xpaths：使用xpath表达式，和allow共同作用过滤链接。指定a标签所在父级标签（间接）

# restrict_css：使用css表达式，和allow共同作用过滤链接。指定a标签所在父级标签（间接）

```

### rules

在rules中包含一个或多个Rule对象，每个Rule对爬取网站的动作定义了特定操作。如果多个rule匹配了相同的链接，则根据规则在本集合中被定义的顺序，第一个会被使用

```python
class scrapy.spiders.Rule(
        link_extractor, 
        callback = None, 
        cb_kwargs = None, 
        follow = None, 
        process_links = None, 
        process_request = None
解释一下以上参数：
    
# link_extractor：是一个Link Extractor对象，用于定义需要提取的链接。

# callback： 从link_extractor中每获取到链接时，参数所指定的值作为回调函数，该回调函数接受一个response作为其第一个参数。

# 注意：当编写爬虫规则时，避免使用parse作为回调函数。由于CrawlSpider使用parse方法来实现其逻辑，如果覆盖了 parse方法，crawl spider将会运行失败。

# follow：是一个布尔(boolean)值，指定了根据该规则从response提取的链接是否需要跟进。 如果callback为None，follow 默认设置为True ，否则默认为False。
# 一句话解释:follow可以理解为回调自己的回调函数

# 举个例子,如百度百科,从任意一个词条入手,抓取词条中的超链接来跳转,rule会对超链接发起requests请求,如follow为True,scrapy会在返回的response中验证是否还有符合规则的条目,继续跳转发起请求抓取,周而复始,如下图

# process_links：指定该spider中哪个的函数将会被调用，从link_extractor中获取到链接列表时将会调用该函数。该方法主要用来过滤。

# process_request：指定该spider中哪个的函数将会被调用， 该规则提取到每个request时都会调用该函数。 (用来过滤request)
```



## 图片管道 ImagePipeline

> 参考文档:https://docs.scrapy.org/en/latest/topics/media-pipeline.html

### 核心类和方法

- from scrapy.pipelines.images import ImagesPipeline
- def get_media_requests(self,item,info) 获取下载图片信息，并发起yield Request()
- def item_completed(self,results,item,info)
  - item处理完毕
  - results的样本
- def file_path(self,request,response=None,info=None) 获取图片下载文件后保存的路径

### settings.py 里面的设置

- ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline':1}
- IMAGES_STORE = '/path/to/valid/dir'
- IMAGES_EXPIRES = 30 图片的有效时间，单位是天
- IMAGES_THUMBS = {'small':(50,50),'big':(270,270)}
- 设置缩略图存储路径是<IMAGES_STORE>/thumbs/<size_name>/<img_id>.jpg

### 使用

- 使用ImagesPipeline 下载图片时，需要imag_urls 字段，时刻迭代的列表或元组类型

```python
import scrapy

class MyItem(scrapy.Item):
    # ... other item fields ...
    image_urls = scrapy.Field()
    images = scrapy.Field() # 下载图片之后本地的存放位置
```

### 自定义ImagesPipeline

> 实现ImagesPipeline的子类，重写三个核心方法

三个核心的方法

- get_media_requests(self,item,info)

  - 从item中取到图片下载的任务，返回图片下载的请求
  - 可以返回一个request也可以返回多个request

- file_path(self,request,response=None,info=None)

  - 根据请求和响应返回图片保存的位置
  - 相对于images_store
  - 如果返回路径中包含子路径，系统还自动创建子目录 os.makedirs()

- item_completed(self,results,item,info)

  - 图片下载完成后，从results的结果获取图片保存路径，并设置到item中，最后返回这个item
  - results格式

  ```python
  [
      (True,{'path':'','url':'',"chucksum":''}),
      (True,{'path':'','url':'',"chucksum":''}),	
  ]
  ```

  

## 构建器设计模式

> 流式编程

```python
car:Car = CarBuilder().step1().step2().step3().step4().build()
```

```python
text:str =  response.xpath().css().xpath().css().get()
```

## 全局异常处理

如果python 程序中发生了某些异常，且没有try except处理时，则会调用解释器处理，解释器会调用sys.excepthook函数处理

- sys.excepthook
  - 如果我们指定excepthook执行的函数，我们必须指定此函数的三个必要参数
    - except_type 异常类
    - except_value 异常信息
    - traceback
      - 异常跟踪栈的对象
      - tb_frame
        - 异常栈的信息
        - f_code
        - f_lineno
        - f_locals
      - tb_next 下一个traceback对象
      - tb_lineno 跟踪行号
      - tb_lasti

```python
import sys
def global_excepthook(except_type,except_value,traceback):
    pass
	print_except(traceback)
    
def print_except(tb):
    if tb.tb_next:
        print(tb.tb_next) # 找到最后一个记录到logger 里

if __name__ == "__main__":
    sys.excepthook = global_excepthook
```

## 分布式爬虫

### 什么是分布式

- Hadoop 分布式计算框架（大数据处理）HDFS（分布式文件系统）
  - MapReduce
  - Hbase 数据库
  - Hive 实时数据库
  - Spark 大数据平台（MYSql，Hbase）

- 由多个服务器（操作系统） 组成，在调度器调度的情况下，完成不同的任务，这种架构称之为分布式。常见的调度器是消息中间件，服务注册中心，负载均衡等组成
- 通俗意义来说就是一个任务由几个服务共同完成

- 区块链就是去中心化

### 常见的消息队列

- Redis订阅与发布-实现消息队列
-  RabbitMQ 基于Channel实现消息队列
- Kafka 消息队列

### scrapy-redis

> 案例：https://github.com/rmax/scrapy-redis

#### 组成

-  Scheduler
  - SCHEDULER = "scrapy_redis.scheduler.Scheduler"
  - SCHEDULER_PERSIST = True
    - 调度用户的持久性
    - True 之前未完成的任务
- Duplication Filter
  - DUPERFILTER_CLASS="scrapy_redis.dupefilter.RFPDupeFilter"
  - 去重的过滤器
- Item Pipeline
- Base Spider
  - scrapy_redis.spiders.RedisSpider
  - scrapy_redis.spiders.RedisCrawlSpider
  - redis_key 从redis中读取任务的key

#### 安装scrapy-redis

- `pip install scrapy-redis`
- redis命令文档 `http://redisdoc.com/`

```python
# settings.py
# 配置调度器

SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

# 配置去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# 配置Redis消息队列服务器
REDIS_URL = 'redis://192.168.0.200:6378/0'

在redis-cli 里面
select 0 
lpush 你在spider里面建的redis_key 你的开始网址

# 其他配置按照这个来看
https://github.com/rmax/scrapy-redis/tree/master/example-project/example
```

#### 修改爬虫类

- 父类 scrapy_redis.spiders.RedisSpider | RedisCrawlSpider
- 去掉start_urls列表
- 增加redis_key字符串变量，指定redis服务中存储的key

#### 按正常启动爬虫程序命令启动爬虫

```python
scrapy crawl 爬虫名
```

#### 链接redis服务，向redis_key的列表list中推送请求任务

```sql
lpush redis_key 链接地址
lpush redis_key_urls https://www.dushu.com/guoxue/
-- 爬虫开始
```

### 部署到服务器

```python
which virtualenv

pip install virtualenv
pip install python3

virtualenv /root/.env/spider -p python3 # 创建虚拟环境 -p python3 代表版本

source /root/.env/spider/bin/activate # 激活虚拟环境

# cd 到项目目录
pip install -r requirements.txt -i https://mirrors.aliyun.com/pipy/simple # -i 指定镜像源
    
scrapy crawl 爬虫名 # 开启项目
```

### scrapyd 部署

```python
# 进入到虚拟环境
pip install scrapyd
pip install scrapy-client

# 创建配置文件
sudo mkdir /etc/scrapyd
sudo vim /etc/scrapyd/scrapyd.conf

# 进入到下面的页面吧配置复制进去 并把bind_address = 127.0.0.1 改为 bind_address = 0.0.0.0
# https://scrapyd.readthedocs.io/en/stable/config.html#example-configuration-file

# 修改scrapy.cfg 文件
[settings]
default = dushu_redis.settings

[deploy:100] # :100 是版本号
url = http://192.168.0.200:6800/ # 发布服务的地址
project = dushu_redis # 工程的名字


# 发布
scrapyd-deploy <target> -p <project_name> # target 是版本号 project_name 是工程的名字
# 开启爬虫
curl http://localhost:6800/schedule.json -d project=default -d spider=somespide

```

### docker 部署

```python
# Dockerfile
FROM python:3.6
MAINTAINER yby xxxxxxx@qq.com
ADD . /usr/src
WORKDIR /usr/src
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
RUN chmod +x run.sh
CMD /usr/src/run.sh
```

```shell
# run.sh
#!/bin/bash
cd /usr/src
scrapy crawl dushu
```

```shell
# 构建镜像
docker build -t spider:1.0 .
```

### 定时爬虫

`/root/runspider.sh`

- 第一种

```shell
#!/bin/bash
cd /root/dushu_spider/dushu_redis_分布式
source /root/.env/dushu_spider/bin/activate
scrapy crawl dushu
```

- 第二种

```shell
#!/bin/bash
docker start dushu_spider
```

```shell
chmod +x runspider.sh
```

```shell
ln -s /root/runspider.sh /usr/bin/run_dushu
```

- 编辑定时任务 vim /root/dushu.cron

```shell
30 * * * * run_dushu
```

格式：分 时 天 月 周

```shell
crontab dushu.cron # 添加定时任务
crontab -l # 查看全部定时任务
```

