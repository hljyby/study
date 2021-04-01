Web应用程序安全性的黄金法则是永远不要信任来自不受信任来源的数据。有时，通过不受信任的介质传递数据会很有用。加密签名的值可以在不检测任何篡改的情况下安全地通过不受信任的通道传递。

在开发中比较常见的应用场景是：

- 账号激活
- 密码找回
- 生成token

## 1. ItsDangerous概述

在Django框架中提供了签名加密模块Cryptographic signing，但提供的签名算法比较简单，安全性不高，Flask的ItsDangerous模块借鉴了Django的签名加密模块，提供了更安全易用的签名加密算法。

ItsDangerous是一个独立的模块，可以在其他框架中使用。在虚拟环境用pip安装：

```text
pip install -U itsdangerous
```

ItsDangerous主要包括签名和序列化两部分，签名主要是为了检测数据是否被篡改，签名只针对字符串，**对于其他类型数据可以使用序列化进行序列化后再签名**。

## 2. 签名算法

签名只针对字符串，Signer能把签名附加的字符串后面。

```text
from itsdangerous.signer import Signer
Signer(secret_key, salt=None, sep='.', key_derivation=None, digest_method=None, algorithm=None)
参数：
    secret_key：秘钥串；
    salt: 盐值，区分不同签名，相当于命名空间
    sep: 签名字符串和签名之间的分隔符
    key_derivation: 用于签名的key，有三种类型：concat、django-concat、hmac
    digest_method: 摘要算法，缺省是sha1,可以是hashlib中任何合法摘要算法
    algorithm：MAC算法，带签名的hash函数

Signer的方法：
- sign(value) 签名
- unsign(singed_value) #反签名 从签名串返回源串
-verify_signature(value, sig) # 验证字符串的签名和指定的签名是否相等
-validate(signed_value) # 验证一个签名串是否存在且有效
-get_signature(value)  # 得到指定字符串的签名部分
```

示例：

```text
s = Signer("hello")
s1 = s.sign("123")  # b'123.Uig89caNdNoeJnT4YEjyutchQFk'
s2 = s.unsign(s1)   #b'123'
tmp = s.get_signature('123')  #b'Uig89caNdNoeJnT4YEjyutchQFk'
print(s.validate(s1)) # True

# 验证签名，参数类型必须是bytes
print(s.verify_signature('123'.encode('utf8'),tmp)) # True
```

## 3.序列化

对于非字符串类型的签名，可以通过序列化进行。序列化类的用法和内置Json类差不多，提供了`dumps`/`loads`方法。

```text
from Itsdangerous.serializer import Serializer
Serializer(secret_key, salt=b'itsdangerous', serializer=None, serializer_kwargs=None, signer=None, signer_kwargs=None, fallback_signers=None)
参数：
    secret_key： 秘钥串
    salt： 盐值，命名空间，区分不同签名
    serializer： 序列化器，默认是json
    serializer_kwargs: 序列化器参数字典
    signer： 签名类，默认是Signer
    signer_kwargs： 实例化签名类的参数字典
    fallback_signers：反签名，可以是一个类，字典，元组
```

示例：

```text
# 生成序列化对象
sig = Serializer("oododod23998")

# 序列化
#{"name": "admin", "password": "123"}.UVbGG9PpgIrGsQp8FinoznP1Ztw
res = sig.dumps({'name':'admin','password':"123"})
    
# 反序列化
data = sig.loads(res) # {'name': 'admin', 'password': '123'}
    
#10.XYPflLg1Dq0sWm49A293Vna55DA
res = sig.dumps(10)
data = sig.loads(res) # 10
```

不同的盐值生成的序列化器是不能相互通用的：

```text
# 盐值用于区分不同签名
ser1 = Serializer('dhfie83',salt='hello')
s1 = ser1.dumps(30)

ser2 = Serializer('dhfie83',salt='world')
s2 = ser2.dumps(30)

#ser2和ser1是用不同盐值生成的，即便签名数据相同，也是不同的
res = ser2.loads(s1)  # 抛出异常
print(res)
```

![img](https://pic3.zhimg.com/80/v2-08bb51e9102c6c9521506bc8a73b79b2_720w.jpg)图1 不同盐值生成的序列化器不能通用

除了前面讲的两种基本前面和序列化算法，itsdangerous还提供了带时间戳的签名和序列化算法。

这些方法签名后信息带了当前的时间戳，可以在unsign的时候验证签名是否过期。

![img](https://pic4.zhimg.com/80/v2-62f7b6c1a88417dd39d8b487547f6eab_720w.jpg)图1 带时间戳的签名算法

## 1. 带时间戳的签名

从类图上看，带时间戳的签名TimestampSigner继承自基本签名类Siger,重写了sign、unsign和validate方法，因为签名字符串中包含了时间戳。TimestampSigner继承了Signer，没有重写构造方法，所以构造方式同Signer。

```text
TimestampSigner(secret_key, salt=None, sep='.', key_derivation=None, digest_method=None, algorithm=None)
```

图2的代码是TimestampSigner签名的结果，咱们可以和Signer签名的结果比较一下，看看差别在什么地方。

![img](https://pic2.zhimg.com/80/v2-7125e7629c2504aff88ed8add0e74c31_720w.jpg)图2 TimeStampSigner的签名

签名后的字符串是Bytes类型，所以转换成了python的字符串输出：

![img](https://pic4.zhimg.com/80/v2-9d1b68d22ad46b34f94b70f941c4097b_720w.jpg)图3 签名结果对比

对比后，会发现TimeStampSigner签名的结果被分为三部分：要签名的串.时间戳.签名串

比Signer签名结果多出一个时间戳。这个 时间戳是把当前时间转换为整数再做base64编码得到的。其签名的源代码如图4所示：

![img](https://pic3.zhimg.com/80/v2-41dff9f07a595e99b00ef38a069004be_720w.jpg)图4. TimeStampSigner签名的源码

明白了其签名的原理，那用法就比较简单了，因为签名后的串包含了时间戳，所以unsign时，可以指定max_age，也就是过期时间，超出规定的过期时间，unsign的方法会直接抛出SignatureExpired异常。

![img](https://pic3.zhimg.com/80/v2-68c851334e2f6c9c840362d6dbf0ff32_720w.jpg)图5 TimeStampSigner签名过期

## 2.带时间戳的序列化

```python3
TimedSerializer(secret_key,salt=b"itsdangerous",serializer=None,serializer_kwargs=None,signer=None,signer_kwargs=None,fallback_signers=None)
```

![img](https://pic3.zhimg.com/80/v2-7962d47231043eec81aa6ff9752d3492_720w.jpg)图6 TimedSerializer继承层次

从继承上看，TimedSerializer类直接继承了Serializer，没有重写构造方法，所以其构造方式和Serializer雷同，可以对内置非字符串类型序列化然后签名，当然签名的时候会带时间戳，就像TimedStampSigner一样；所以TimedSerializer重写了父类的loads和loads_unsafe方法，以便判断签名是否过期。

![img](https://pic3.zhimg.com/80/v2-b6bf02abfa71a73c4ac5408aa50ac9aa_720w.jpg)图7 TimedStampSigner基本使用

TimedSerializer基本使用方式和其父类大体相同，但反序列化的时候可以通过max_age参数指定过期时间，以秒为单位，逾期将会抛出SignatureExpired异常，如图8所示。

![img](https://pic4.zhimg.com/80/v2-fe5371a561e882137ef6e3fda2c9094f_720w.jpg)图8 逾期抛出SignatureExpired异常

在网络上进行数据传输是不安全的，必须的防止数据的伪造和篡改，特别是在web开发中使用GET传参的时候就更加要考虑这种需求，但GET传参是通过URL传参的，只能使用ASCII码，Itsdangerous模块中的URL安全序列化正好满足这种字符受限的情况。

URL安全序列化包括以下两个类：

- URLSafeSerializer
- URLSafeTimedSerializer

## 1.URLSafeSerializer

这个类的用法同Serializer差不多，但可以序列化和反序列化url安全的字符串，包括大小写英文字母和'_'、'-'、'.'

![img](https://pic3.zhimg.com/80/v2-e968c2508937b801fb977de2a786a92a_720w.jpg)图1 URLSafeSerializer继承层次

从继承的层次看URLSafeSerializer多了一个父类URLSafeSerializerMixin，这类功能是什么呢？下面是它的源码

```text
class URLSafeSerializerMixin(object):
    default_serializer = _CompactJSON

    def load_payload(self, payload, *args, **kwargs):  # 反序列化预处理
        decompress = False
        if payload.startswith(b"."):
            payload = payload[1:]
            decompress = True
        try:
            json = base64_decode(payload)  # base64解码
        except Exception as e:
            raise BadPayload(
                "Could not base64 decode the payload because of an exception",
                original_error=e,
            )
        if decompress:
            try:
                json = zlib.decompress(json)   # 解压缩
            except Exception as e:
                raise BadPayload(
                    "Could not zlib decompress the payload before decoding the payload",
                    original_error=e,
                )
        return super(URLSafeSerializerMixin, self).load_payload(json, *args, **kwargs)

    def dump_payload(self, obj):  # 序列化预处理
        json = super(URLSafeSerializerMixin, self).dump_payload(obj)
        is_compressed = False
        compressed = zlib.compress(json)    # 关键，压缩字符串
        if len(compressed) < (len(json) - 1):
            json = compressed
            is_compressed = True
        base64d = base64_encode(json)  # 对字符串做base64编码
        if is_compressed:
            base64d = b"." + base64d
        return base64d
```

从源代码看，这个类主要完成序列化和反序列化的预处理，在序列化预处理中，对要序列化的字符串进行压缩，然后再进行base64编码。所以它的子类URLSafeSerializer可以对特殊字符（_-.）进行处理。URLSafeSerializer用法和Serializer相同，如图2所示

![img](https://pic3.zhimg.com/80/v2-e1fceb8bbf26ca3445e966231df45726_720w.jpg)图2 URLSafeSerializer用法

2.URLSafeTimedSerializer

这个类和*TimedSerializer用法差不多，但序列化（dumps)和反序列化(loads)*url安全的字符串，包括大小写英文字母和'_'、'-'、'.'

![img](https://pic3.zhimg.com/80/v2-aec997a5227b67cabf3b5bd0120abc82_720w.jpg)图3 URLSafeTimedSerializer继承层次

URLSafeTimedSerializer也继承了URLSafeSerializerMixin，它会对字符串进行base64编码，所以也可以处理特殊字符。下面是它的用法：

```text
import time

from itsdangerous.url_safe import URLSafeTimedSerializer

url_time_serializer = URLSafeTimedSerializer('ksdfkls903')

# 序列化
res = url_time_serializer.dumps([1,2,3])
# WzEsMiwzXQ.XoBQLA.0fRHds5_DwWfVqeorMSOU4ohz0U
print(res)

# 反序列化
# 没有时间限制
res = url_time_serializer.loads(res)
# [1, 2, 3]
print(res)

time.sleep(5) # 等等5秒

# 有时间限制
res = url_time_serializer.loads(res,max_age=3)
print(res)
```

其执行结果如图4所示。

![img](https://pic2.zhimg.com/80/v2-07709bca34beeaed0c5024381b185869_720w.jpg)图4 执行结果

URLSafeTimedSerializer可以对各种内置类型进行序列化，生成URL安全的字符串，并且可以限制过期时间，是非常理想的生成token的算法，所以在前后端分离的项目总可以使用URLSafeTimedSerializer生成token

Token 是在服务端产生的。如果前端使用用户名/密码向服务端请求认证，服务端认证成功，那么在服务端会返回 Token 给前端。前端以后再次请求的时候带上 Token 证明自己的合法地位，无需再次带上用户名和密码。其流程如图1所示。

![img](https://pic2.zhimg.com/80/v2-cee416fce6c3f3f72b0a21858a69490d_720w.jpg)图1 token认证过程

基本流程是这样的：

1. 客户端使用用户名跟密码请求登录
2. 服务端收到请求，去验证用户名与密码
3. 验证成功后，服务端会签发一个 Token，再把这个 Token 发送给客户端
4. 客户端收到Token 以后可以把它存储起来，比如放在 Cookie 里或者 Local Storage 里
5. 客户端每次向服务端请求资源的时候需要带着服务端签发的Token
6. 服务端收到请求，然后去验证客户端请求里面带着的 Token，如果验证成功，就向客户端返回请求的数据

## **一、token的优势**

**1.无状态**

Token机制在服务端不需要存储session信息，因为Token 自身包含了所有登录用户的信息，只需要在客户端的cookie或本地介质存储状态信息。

**2.安全性**

　　请求中发送token而不再是发送cookie能够防止CSRF(跨站请求伪造)。即使在客户端使用cookie存储token，cookie也仅仅是一个存储机制而不是用于认证。

**3.更适用于移动应用**

当你的客户端是一个原生平台（iOS, Android，Windows 8等）时，Cookie是不被支持的（你需要通过Cookie容器进行处理），这时采用Token认证机制就会简单得多。

**4.多平台跨域**

　　我们提前先来谈论一下CORS(跨域资源共享)，对应用程序和服务进行扩展的时候，需要介入各种各种的设备和应用程序。只要用户有一个通过了验证的token，数据和资源就能够在任何域上被请求到。

**5.基于标准**
　　你的API可以采用标准化的 JSON Web Token (JWT). 这个标准已经存在多个后端库（.NET, Ruby, Java,Python, PHP）和多家公司的支持（如：Firebase,Google, Microsoft）。

## 二、token生成

在python中，我们可以使用itsdangerous模块生成token，并且可以设置时限，不用在服务器端保存用户登录数据。

```text
from itsdangerous import SignatureExpired,  BadData, BadSignature
from itsdangerous.url_safe import URLSafeTimedSerializer


class TokenException(Exception):
    def __init__(self,obj):
        super().__init__()
        self.status = {}
        if isinstance(obj,SignatureExpired):
            self.status['code'] = -1
            self.status['msg'] = "签名过期"
        elif isinstance(obj,BadSignature):
            self.status['code'] = -2
            self.status['msg'] = "签名失效"
        elif isinstance(obj,BadData):
            self.status['code'] = -3
            self.status['msg'] = "数据异常"

    @property
    def code(self):
        return self.status['code']
    @property
    def message(self):
        return self.status['msg']

    def __str__(self):
        return self.status['msg']

class TokenManager:
    def __init__(self,secret_key,salt='hello world'):
        """secret_key 加密密钥"""
        self.secret_key = secret_key
        self.salt = salt

    def generate_token(self,playload):
        """
        :param playload: 负载，也就是你要序列化的数据，不要用关键数据（如密码等）做playload
        :return: token字符串
        """
        serializer = URLSafeTimedSerializer(self.secret_key, self.salt)
        return serializer.dumps(playload)

    def confirm_token(self,token,expired=3600):
        """
        验证token
        :param token: generate_validate_token产生的字符串
        :param expired: 过期时间，以秒为单位
        :return: 成功返回负载数据，失败返回错误码
        """
        serializer = URLSafeTimedSerializer(self.secret_key, self.salt)
        try:
            data = serializer.loads(token,max_age=expired)
        except BadData as e:
           return TokenException(e)
        # 签名验证通过，返回原始数据
        return data


if __name__ == '__main__':
    tm = TokenManager('kdkdk',salt="hello")
    # 获取签名数据
    uid = 10
    token = tm.generate_token(uid)
    print(token)

    # 验证,默认是1个小时
    # data = tm.confirm_token(token)
    # print(data)

    # 签名失效
    token = token + 'dd'
    data = tm.confirm_token(token)
    print(data,type(data))
```