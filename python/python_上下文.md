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

# 