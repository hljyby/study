# [DRF框架基础四之二次封装Response，数据库关系分析，ORM操作关系，序列化和十大接口](https://www.cnblogs.com/jiangxianseng/p/12883142.html)

# 一.二次封装Response

之前我们在视图类中返回响应结果是下面这种形式

```python
from rest_framework.views import APIViewfrom rest_framework.response import Responsefrom rest_framework import statusfrom . import models, serializersclass 
CarAPIView(APIView):    
    def get(self, request, *args, **kwargs):        
        pk = kwargs.get('pk')        
        if pk:            
            try:                
                car_obj = models.Car.objects.get(pk=pk)                
                car_serializer = serializers.CarModelSerializer(car_obj, many=False)                return Response({                    
                    'status': 0,                    
                    'msg': 'ok',                    
                    'result': car_serializer.data                
                })            
            except:                
                return Response(                    
                    data={                        
                        'status': 1,                        
                        'msg': 'pk error'                    
                    },                    
                    status=status.HTTP_400_BAD_REQUEST,                    
                    exception=True                
                )        
            else:            
                car_queryset = models.Car.objects.all()            
                car_serializer = serializers.CarModelSerializer(car_queryset, many=True)            return Response({                    
                    'status': 0,                    
                    'msg': 'ok',                    
                    'results': car_serializer.data                
                })
```

可以看到每一次return Response都是类似重服的，那能否将其封装一下，即面向对象封装,新建一个Response.py文件，里面设计封装方法

```python
from rest_framework.response import Response
# 是Response里面的init方法，我们二次封装Response就是重写init方法
'''  
def __init__(self, data=None, status=None,                 
             template_name=None, headers=None,                 
             exception=False, content_type=None):
'''
    class APIResponse(Response):    
        def __init__(self, status=0, msg='ok', http_status=None, headers=None, exception=False,                 **kwargs):  
            # 将外界传入的数据状态码、状态信息以及其他所有额外存储在kwargs中的信息，都格式化成data数据
            data = {'status': status,                
            'msg': msg}       
            # 在外界数据可以用result和results来存储        
            if kwargs:            
                data.update(kwargs) 
                # kwargs未打散是一个字典，对data进行跟新覆盖        
                super().__init__(data=data, status=http_status,headers=headers,exception=exception)
```

然后对一开始的Response进行修改

```python
from rest_framework.views import APIViewfrom rest_framework.response import Responsefrom rest_framework import statusfrom . import models, serializers
# 将封装好的APIResponse导入过来
from .response import APIResponseclass 
CarAPIView(APIView):    
    def get(self, request, *args, **kwargs):        
        pk = kwargs.get('pk')        
        if pk:            
            try:                
                car_obj = models.Car.objects.get(pk=pk)                
                car_serializer = serializers.CarModelSerializer(car_obj, many=False)                
                # return Response({                
                #     'status': 0,                
                #     'msg': 'ok',               
                #     'result': car_serializer.data               
                # })                return APIResponse(result = car_serializer.data)            except:                
                # return Response(                
                #     data={                
                #         'status': 1,               
                #         'msg': 'pk error'               
                #     },               
                #     status=status.HTTP_400_BAD_REQUEST,              
                #     exception=True             
                # )                
                return APIResponse(status=1,msg='ok',http_status=400,exception=True)        
            else:            
                car_queryset = models.Car.objects.all()            
                car_serializer = serializers.CarModelSerializer(car_queryset, many=True)         
                # return Response({           
                #         'status': 0,            
                #         'msg': 'ok',           
                #         'results': car_serializer.data           
                #     })            return APIResponse(result=car_serializer.data)     
'''        
总结：        
	•使用：# APIResponse() 代表就返回 {"status": 0, "msg": "ok"}                
	•APIResponse(result="结果") 代表返回 {"status": 0, "msg": "ok", "result": "结果"}       	 		•APIResponse(status=1, msg='error', http_status=400, exception=True) 异常返回 {"status": 1, "msg": "error"}        
'''
```

# 二.数据库关系分析

```
"""
1）之间有关系的两个表，增删改操作会相互影响(效率低)，查询操作就是正常的连表操作
2）之间有关系的两个表，断开关联，但所有数据保持与原来一致    每个表都可以单独操作，增删改操作效率极高，但是容易出现脏数据(开发中完全可以避免)    由于数据没有任何变化，所以查询的连表操作不会受到任何影响    
3）Django的ORM支持断关联操作关系表，且所有的操作方式和没有断关联操作一致"""
```

## ORM操作关系

```python
"""
外键位置：
1）一对多：ForeignKey必须放在多的一方，书与出版社，外键应该放在书表
2）多对多：ManyToManyField放在任何一方都可以，因为会创建关系表，在关系表中用两个外键分别关联两个表
3）一对一：OneToOneField放在依赖的表，作者与作者详情，放在详情表，OneToOneField会被转换为 外键 + 唯一约束
"""
"""
ORM关系Field：
ForeignKey可以设置related_name(表的反向外键关系), db_constraint（关联关系）, on_delete OneToOneField可以设置related_name, db_constraint, on_delete
ManyToManyField只能设置related_name, db_constraint    
不能设置on_delete的原因：不管是关联的A表，还是B表，数据修改，都会影响到关系表（默认级联），    如果想控制，只能自定义关系表，在关系表的两个外键分别设置on_delete
"""
"""
参数含义related_name：
表之间反向访问的名字，默认是 表名小写|表名小写_setdb_constraint：表之间的关联关系，默认为True，代表关联，设置False，可以提高增删改的效率，且不影响查等其他操作
on_delete：在django 1.x下默认是CASCADE，在django 2.x下必须手动明确
"""
"""
表关系：作者没，作者详情一定没(级联删除）：models.CASCADE  
*****作者没，书还是该作者出的：DO_NOTHING部门们，部门内的员工全部进入未分组部门：SET_DEFAULT (需要配合default属性使用)  部门们，部门内的员工部门外键字段设置为空：SET_NULL (需要配合null=True属性使用)  *****
"""
```

##### 案例

```python
class Author(models.Model):    
    name = models.CharField(max_length=64)
class AuthorDetail(models.Model):    
    phone = models.CharField(max_length=11)    
    author = models.OneToOneField(        
        to=Author,        
        related_name='detail',        
        db_constraint=False,        
        on_delete=models.SET_NULL,        
        null=True    
    )
```

##### 测试

```python
# 测试数据库需要建立的Django的环境
import os, djangoos.environ.setdefault("DJANGO_SETTINGS_MODULE", "d_proj.settings")
django.setup()
from api.models import Author, AuthorDetail
# 测试正向反向查询
# a1 = Author.objects.first()
# print(a1.name)
# print(a1.detail.phone)
# ad2 = AuthorDetail.objects.last()
# print(ad2.phone)
# print(ad2.author.name)
# 级联关系测试
# ad2 = AuthorDetail.objects.last()
# type: AuthorDetail
# ad2.delete()
# Author.objects.first().delete()
```

 

## 基表

```python
# 基类：是抽象的(不会完成数据库迁移)，目的是提供共有字段的
class BaseModel(models.Model):    
    is_delete = models.BooleanField(default=False)    
    updated_time = models.DateTimeField(auto_now_add=True)    
    class Meta:        
        abstract = True  # 必须完成该配置
```

##### 应用

```python
class Book(BaseModel):    
    name = models.CharField(max_length=64)    
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True)    
    image = models.ImageField(upload_to='img', default='img/default.png')    
    publish = models.ForeignKey(to='Publish', related_name='books', db_constraint=False, 
                                on_delete=models.DO_NOTHING)    
    authors = models.ManyToManyField(to='Author', related_name='books', db_constraint=False)
class Publish(BaseModel):    
    name = models.CharField(max_length=64)
class Author(BaseModel):    
    name = models.CharField(max_length=64)
class AuthorDetail(BaseModel):    
    phone = models.CharField(max_length=11)    
    author = models.OneToOneField(        
        to=Author,        
        related_name='detail',        
        db_constraint=False,        
        on_delete=models.SET_NULL,        
        null=True    
    )
```

## 序列化类其他配置（了解）

```python
class AuthorModelSerializer(serializers.ModelSerializer):    
    class Meta:        
        model = models.Author        
        # 不常用，将全部字段提供给外界，因为有些字段比如密码等是不能轻易序列化出去的        
        fields = '__all__'         
# ------------------------------------------------------------------
class AuthorModelSerializer(serializers.ModelSerializer):    
    class Meta:        model = models.Author        
        # 不常用，排除指定字段的其他所有字段，不能自动包含 外键反向 字段        
        exclude = ['is_delete', 'updated_time']          
# ------------------------------------------------------------------
class AuthorModelSerializer(serializers.ModelSerializer):    
    class Meta:        
        model = models.Author        
        # 'detail', 'books' 是 外键(正向|反向) 字段        
        fields = ['name', 'detail', 'books']        
        # 不常用，自动深度，自动深度会显示外键关联表的所有字段        
        depth = 2  # 正向外键字段：就是外键的属性名# 反向外键字段：就是外键属性设置的related_name
```

 

 

## 子序列化

```python
"""
1）子序列化的字段，必须是 外键(正向|反向) 字段
2）子序列化对应的数据是单个many=False，数据对应是多个many=True
3）子序列化其实就是自定义序列化字段，覆盖了原有 外键(正向|反向)字段 的规则，所以不能进行反序列化
"""
```

### 案例

##### urls.py

```python
url(r'^authors/$', views.AuthorAPIView.as_view()),
url(r'^authors/(?P<pk>\d+)/$', views.AuthorAPIView.as_view()),
```

##### serializers.py

```python
from rest_framework import serializersfrom . 
import models
class AuthorDetailModelSerializer(serializers.ModelSerializer):    
    class Meta:       
        model = models.AuthorDetail        
        fields = ['phone']
class BookModelSerializer(serializers.ModelSerializer):    
    class Meta:        
        model = models.Book        
        fields = ['name', 'price']
class AuthorModelSerializer(serializers.ModelSerializer):    
    # 子序列化：子序列化类必须写在上方，且只能对 外键(正向反向)字段 进行覆盖    
    # 注：运用了子序列化的外键字段，就不能进行数据库的反序列化过程    
    detail = AuthorDetailModelSerializer(many=False, read_only=True)    
    books = BookModelSerializer(many=True, read_only=True)    
    # 问题：    
    # 1）不设置read_only时，就相当于允许反序列化，反序列化是就会报错    
    # 2）设置read_only时，可以完成反序列化，但是新增的数据再序列化了，就没有外键关联的数据，与原来数据格式就不一致了    
    class Meta:        
        model = models.Author        
        fields = ['name', 'detail', 'books']
```

##### views.py

```python
# 实际开发，资源的大量操作都是查询操作，只有查需求的资源，可以采用子序列化
class AuthorAPIView(APIView):    
    def get(self, request, *args, **kwargs):        
        pk = kwargs.get('pk')        
        if pk:            
            obj = models.Author.objects.filter(is_delete=False, pk=pk).first()            
            serializer = serializers.AuthorModelSerializer(instance=obj)            
            return APIResponse(result=serializer.data)        
        else:            
            queryset = models.Author.objects.filter(is_delete=False).all()            
            serializer = serializers.AuthorModelSerializer(instance=queryset, many=True)            return APIResponse(results=serializer.data)   
        # 测试子序列化外键字段，不能参与反序列化，因为    
        def post(self, request, *args, **kwargs):        
            serializer = serializers.AuthorModelSerializer(data=request.data)        
            if serializer.is_valid():            
                obj = serializer.save()            
                return APIResponse(result=serializers.AuthorModelSerializer(instance=obj).data, http_status=201)        
            else:            
                # 校验失败 => 异常响应            
                return APIResponse(1, serializer.errors, http_status=400)
```

 

 

## 多表序列化与反序列化

```python
"""
1）外键字段要参与反序列化，所以外键字段设置为write_only
2）外键关系需要连表序列化结果给前台，可以用@property来自定义连表序列化
"""
```

### 案例

##### urls.py

```python
url(r'^books/$', views.BookAPIView.as_view()),
url(r'^books/(?P<pk>\d+)/$', views.BookAPIView.as_view()),
```

##### models.py

```python
class Book(BaseModel):    
    # ...        @property  
    # @property字段默认就是read_only，且不允许修改    
    def publish_name(self):        
        return self.publish.name    
    @property  # 自定义序列化过程    
    def author_list(self):        
        temp_author_list = []        
        for author in self.authors.all():            
            author_dic = {                
                "name": author.name            
            }            
            try:                
                author_dic['phone'] = author.detail.phone            
            except:                
                author_dic['phone'] = ''            
            temp_author_list.append(author_dic)        
         return temp_author_list    
    @property  # 借助序列化类完成序列化过程    
    def read_author_list(self):        
        from .serializers import AuthorModelSerializer        
        return AuthorModelSerializer(self.authors.all(), many=True).data
```

##### serializers.py

```python
# 辅助序列化类
class AuthorDetailModelSerializer(serializers.ModelSerializer):    
    class Meta:       
        model = models.AuthorDetail     
        fields = ['phone']
# 辅助序列化类
class AuthorModelSerializer(serializers.ModelSerializer):    
    detail = AuthorDetailModelSerializer(many=False, read_only=True)   
    class Meta:       
        model = models.Author      
        fields = ['name', 'detail']
# 主序列化类
class BookModelSerializer(serializers.ModelSerializer):   
    class Meta:    
        model = models.Book     
        fields = ('name', 'price', 'image', 'publish', 'authors', 'publish_name', 'author_list', 'read_author_list')      
        extra_kwargs = {         
            'image': {            
                'read_only': True,        
            },          
            'publish': {  
                # 系统原有的外键字段，要留给反序列化过程使用，序列化外键内容，用@property自定义               
                'write_only': True,        
            },          
            'authors': {         
                'write_only': True,     
            }     
        }
```

##### views.py

```python
# 六个必备接口：单查、群查、单增、单删、单整体改(了解)、单局部改
# 四个额外接口：群增、群删、群整体改、群局部改
class BookAPIView(APIView):    
    # 单查群查    
    def get(self, request, *args, **kwargs):        
        pk = kwargs.get('pk')        
        if pk:            
            obj = models.Book.objects.filter(is_delete=False, pk=pk).first()      
            serializer = serializers.BookModelSerializer(instance=obj)    
            return APIResponse(result=serializer.data)     
        else:          
            queryset = models.Book.objects.filter(is_delete=False).all()  
            serializer = serializers.BookModelSerializer(instance=queryset, many=True)            return APIResponse(results=serializer.data) 
        # 单增群增  
        def post(self, request, *args, **kwargs):    
            # 如何区别单增群增：request.data是{}还是[]   
            if not isinstance(request.data, list):      
                # 单增         
                serializer = serializers.BookModelSerializer(data=request.data)       
                serializer.is_valid(raise_exception=True) 
                # 如果校验失败，会直接抛异常，返回给前台      
                obj = serializer.save()       
                # 为什么要将新增的对象重新序列化给前台：序列化与反序列化数据不对等     
                return APIResponse(result=serializers.BookModelSerializer(obj).data, http_status=201) 
            else:        
                # 群增     
                serializer = serializers.BookModelSerializer(data=request.data, many=True)          
                serializer.is_valid(raise_exception=True) 
                # 如果校验失败，会直接抛异常，返回给前台       
                objs = serializer.save()         
                # 为什么要将新增的对象重新序列化给前台：序列化与反序列化数据不对等    
                return APIResponse(result=serializers.BookModelSerializer(objs, many=True).data, 
                                   http_status=201)
            # 友情注释：群增其实是借助了ListSerializer来的create方法完成的
```

 

 

 

## 小结

```python
"""
1）二次封装Response：   
自定义类继承Response，重写init方法，在内部格式化data  
2）表关系分析：   
断关联：     
优点：提示增删改操作效率，不允许查效率    
缺点：增删改操作可能会导致脏数据，所以需要通过逻辑或是事务来保证     
3）ORM表关系处理语法：   
	1）外键所在位置   
	2）如何断关联db_constraint  
	3）正向方向自定义名字：related_name  
	4）表关系：on_delete四种  
4）基表：Meta中配置abstract=True，来被继承，提供共有字段
5）多表连表Meta中的了解配置  
	fields = '__all__'  
	# 不常用，将全部字段提供给外键  
	exclude = ['is_delete', 'updated_time'] 
	# 不常用，排除指定字段的其他所有字段   
	depth = 2  
	# 不常用，主动深度，自动深度会显示关联表的所有字段  
6）子序列化   
	i）通常只用于序列化过程，对外键字段进行了覆盖，影响外键字段的反序列化过程  
class SubSerializer:      
	pass    
class SupSerializer:   
	外键 = SubSerializer(many=True|False)  
7）多表的序列化与反序列化 
	1）连表序列化用自定义@property完成：内部实现可以自定义逻辑，也可以走序列化类  
	2）外键字段留给反序列化来使用 
8）单查、群查、单增、群增接口
"""
```

```python
read_only
read_only表示只能读，不能进行修改。例如定义序列化器时，id字段通常指定read_only=True。在序列化时，即对象转为字典、JSON字符串时，字典、JSON字符串包含着id字段。但是反序列化时，即JSON字符串、字典转换为对象时，在参数校验的时候，即使字典有id的键值对，校验不会出错，但是校验后的数据不会有id这个字段，所以id也不会存进数据库。

write_only
write_only表示只能写，不能读。例如定义序列化器时，password字段（还有短信验证码等）通常指定write_only=True。在序列化时，即对象转为字典、JSON字符串时，字典、JSON字符串不会包含着字段。但是反序列化时，即JSON字符串、字典转换为对象时，在参数校验的时候，校验通过，而且校验后的数据有password这个字段，并且能存进数据库。
```

