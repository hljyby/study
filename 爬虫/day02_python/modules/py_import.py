# import oop.demo2 as od
# as 取别名
# （不支持模块里的对象（类，函数，变量））
# from oop.demo2 import Dog，Animal

# 支持模块里的对象
# dog = Dog('旺财', 1)
# dog.show()

# from oop import * 会加载oop下__init__.py文件声明的模块信息
# 如果__init__.py中声明了__all__那么就只会加载all中的白名单
from oop import *

print(locals())

dog = Dog('wangcaoo', 1)

dog.show()
