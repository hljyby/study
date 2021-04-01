# %用法

## 1、整数的输出

%o —— oct 八进制
%d —— dec 十进制
%x —— hex 十六进制

```python
1 >>> print('%o' % 20)
2 24
3 >>> print('%d' % 20)
4 20
5 >>> print('%x' % 20)
6 14
```

### （1）格式化输出

%f ——保留小数点后面六位有效数字
　　%.3f，保留3位小数位
%e ——保留小数点后面六位有效数字，指数形式输出
　　%.3e，保留3位小数位，使用科学计数法
%g ——在保证六位有效数字的前提下，使用小数方式，否则使用科学计数法
　　%.3g，保留3位有效数字，使用小数或科学计数法


```python
 1 >>> print('%f' % 1.11)  # 默认保留6位小数
 2 1.110000
 3 >>> print('%.1f' % 1.11)  # 取1位小数
 4 1.1
 5 >>> print('%e' % 1.11)  # 默认6位小数，用科学计数法
 6 1.110000e+00
 7 >>> print('%.3e' % 1.11)  # 取3位小数，用科学计数法
 8 1.110e+00
 9 >>> print('%g' % 1111.1111)  # 默认6位有效数字
10 1111.11
11 >>> print('%.7g' % 1111.1111)  # 取7位有效数字
12 1111.111
13 >>> print('%.2g' % 1111.1111)  # 取2位有效数字，自动转换为科学计数法
14 1.1e+03
```


### （2）内置round()

round(number[, ndigits])
参数：
number - 这是一个数字表达式。
ndigits - 表示从小数点到最后四舍五入的位数。默认值为0。
返回值
该方法返回x的小数点舍入为n位数后的值。


round()函数只有一个参数，不指定位数的时候，返回一个整数，而且是最靠近的整数，类似于四舍五入，当指定取舍的小数点位数的时候，一般情况也是使用四舍五入的规则，但是碰到.5的情况时，如果要取舍的位数前的小数是奇数，则直接舍弃，如果是偶数则向上取舍。

注：“.5”这个是一个“坑”，且python2和python3出来的接口有时候是不一样的，尽量避免使用round()函数吧


```python
 1 >>> round(1.1125)  # 四舍五入，不指定位数，取整
 2 1
 3 >>> round(1.1135,3)  # 取3位小数，由于3为奇数，则向下“舍”
 4 1.113
 5 >>> round(1.1125,3)  # 取3位小数，由于2为偶数，则向上“入”
 6 1.113
 7 >>> round(1.5)  # 无法理解，查阅一些资料是说python会对数据进行截断，没有深究
 8 2
 9 >>> round(2.5)  # 无法理解
10 2
11 >>> round(1.675,2)  # 无法理解
12 1.68
13 >>> round(2.675,2)  # 无法理解
14 2.67
15 >>> 
```




## 3、字符串输出

%s
%10s——右对齐，占位符10位
%-10s——左对齐，占位符10位
%.2s——截取2位字符串
%10.2s——10位占位符，截取两位字符串

```python
 1 >>> print('%s' % 'hello world')  # 字符串输出
 2 hello world
 3 >>> print('%20s' % 'hello world')  # 右对齐，取20位，不够则补位
 4          hello world
 5 >>> print('%-20s' % 'hello world')  # 左对齐，取20位，不够则补位
 6 hello world         
 7 >>> print('%.2s' % 'hello world')  # 取2位
 8 he
 9 >>> print('%10.2s' % 'hello world')  # 右对齐，取2位
10         he
11 >>> print('%-10.2s' % 'hello world')  # 左对齐，取2位
12 he        
```




## 4、 其他

### （1）字符串格式代码

![img](https://images2015.cnblogs.com/blog/1099650/201707/1099650-20170713135059962-1387501593.png)

### （2）常用转义字符

![img](https://images2015.cnblogs.com/blog/1099650/201707/1099650-20170713135229556-190015564.png)

 

# format用法

 相对基本格式化输出采用‘%’的方法，format()功能更强大，该函数把字符串当成一个模板，通过传入的参数进行格式化，并且使用大括号‘{}’作为特殊字符代替‘%’

## 位置匹配

　　（1）不带编号，即“{}”

　　（2）带数字编号，可调换顺序，即“{1}”、“{2}”

　　（3）带关键字，即“{a}”、“{tom}”


```python
 1 >>> print('{} {}'.format('hello','world'))  # 不带字段
 2 hello world
 3 >>> print('{0} {1}'.format('hello','world'))  # 带数字编号
 4 hello world
 5 >>> print('{0} {1} {0}'.format('hello','world'))  # 打乱顺序
 6 hello world hello
 7 >>> print('{1} {1} {0}'.format('hello','world'))
 8 world world hello
 9 >>> print('{a} {tom} {a}'.format(tom='hello',a='world'))  # 带关键字
10 world hello world
```


![img](https://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif)![img](https://images.cnblogs.com/OutliningIndicators/ExpandedBlockStart.gif) 通过位置匹配

![img](https://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif)![img](https://images.cnblogs.com/OutliningIndicators/ExpandedBlockStart.gif) 通过名字匹配

![img](https://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif)![img](https://images.cnblogs.com/OutliningIndicators/ExpandedBlockStart.gif) 通过对象属性匹配

![img](https://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif)![img](https://images.cnblogs.com/OutliningIndicators/ExpandedBlockStart.gif) 通过下标或key匹配参数

 

## 格式转换

'b' - 二进制。将数字以2为基数进行输出。

'c' - 字符。在打印之前将整数转换成对应的Unicode字符串。

'd' - 十进制整数。将数字以10为基数进行输出。

'o' - 八进制。将数字以8为基数进行输出。

'x' - 十六进制。将数字以16为基数进行输出，9以上的位数用小写字母。

'e' - 幂符号。用科学计数法打印数字。用'e'表示幂。

'g' - 一般格式。将数值以fixed-point格式输出。当数值特别大的时候，用幂形式打印。

'n' - 数字。当值为整数时和'd'相同，值为浮点数时和'g'相同。不同的是它会根据区域设置插入数字分隔符。

'%' - 百分数。将数值乘以100然后以fixed-point('f')格式打印，值后面会有一个百分号。


```python
 1 >>> print('{0:b}'.format(3))
 2 11
 3 >>> print('{:c}'.format(20))
 4 
 5 >>> print('{:d}'.format(20))
 6 20
 7 >>> print('{:o}'.format(20))
 8 24
 9 >>> print('{:x}'.format(20))
10 14
11 >>> print('{:e}'.format(20))
12 2.000000e+01
13 >>> print('{:g}'.format(20.1))
14 20.1
15 >>> print('{:f}'.format(20))
16 20.000000
17 >>> print('{:n}'.format(20))
18 20
19 >>> print('{:%}'.format(20))
20 2000.000000%
21 >>> 
```




## 进阶用法

### 进制转换

![img](https://images.cnblogs.com/OutliningIndicators/ExpandedBlockStart.gif)


```python
>>> # format also supports binary numbers
>>> "int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42)
'int: 42;  hex: 2a;  oct: 52;  bin: 101010'
>>> # with 0x, 0o, or 0b as prefix:
>>> "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42)  # 在前面加“#”，则带进制前缀
'int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010'
```


### 左中右对齐及位数补全

（1）< （默认）左对齐、> 右对齐、^ 中间对齐、= （只用于数字）在小数点后进行补齐

（2）取位数“{:4s}”、"{:.2f}"等

![img](https://images.cnblogs.com/OutliningIndicators/ExpandedBlockStart.gif)


```python
>>> print('{} and {}'.format('hello','world'))  # 默认左对齐
hello and world
>>> print('{:10s} and {:>10s}'.format('hello','world'))  # 取10位左对齐，取10位右对齐
hello      and      world
>>> print('{:^10s} and {:^10s}'.format('hello','world'))  # 取10位中间对齐
  hello    and   world   
>>> print('{} is {:.2f}'.format(1.123,1.123))  # 取2位小数
1.123 is 1.12
>>> print('{0} is {0:>10.2f}'.format(1.123))  # 取2位小数，右对齐，取10位
1.123 is       1.12

>>> '{:<30}'.format('left aligned')  # 左对齐
'left aligned                  '
>>> '{:>30}'.format('right aligned')  # 右对齐
'                 right aligned'
>>> '{:^30}'.format('centered')  # 中间对齐
'           centered           '
>>> '{:*^30}'.format('centered')  # 使用“*”填充
'***********centered***********'
>>>'{:0=30}'.format(11)  # 还有“=”只能应用于数字，这种方法可用“>”代替
'000000000000000000000000000011'
```


### 正负符号显示

![img](https://images.cnblogs.com/OutliningIndicators/ExpandedBlockStart.gif)


```python
>>> '{:+f}; {:+f}'.format(3.14, -3.14)  # 总是显示符号
'+3.140000; -3.140000'
>>> '{: f}; {: f}'.format(3.14, -3.14)  # 若是+数，则在前面留空格
' 3.140000; -3.140000'
>>> '{:-f}; {:-f}'.format(3.14, -3.14)  # -数时显示-，与'{:f}; {:f}'一致
'3.140000; -3.140000'
```


### 百分数%

![img](https://images.cnblogs.com/OutliningIndicators/ExpandedBlockStart.gif)

```python
>>> points = 19
>>> total = 22
>>> 'Correct answers: {:.2%}'.format(points/total)
'Correct answers: 86.36%'
```

### 时间

![img](https://images.cnblogs.com/OutliningIndicators/ExpandedBlockStart.gif)

```python
>>> import datetime
>>> d = datetime.datetime(2010, 7, 4, 12, 15, 58)
>>> '{:%Y-%m-%d %H:%M:%S}'.format(d)
'2010-07-04 12:15:58'
```

### 逗号","分隔金钱，没以前进位

![img](https://images.cnblogs.com/OutliningIndicators/ExpandedBlockStart.gif)

```python
>>> '{:,}'.format(1234567890)
'1,234,567,890'
```

### 占位符嵌套

![img](https://images.cnblogs.com/OutliningIndicators/ExpandedBlockStart.gif)


```python
>>> for align, text in zip('<^>', ['left', 'center', 'right']):
...     '{0:{fill}{align}16}'.format(text, fill=align, align=align)
...
'left<<<<<<<<<<<<'
'^^^^^center^^^^^'
'>>>>>>>>>>>right'
>>>
>>> octets = [192, 168, 0, 1]
>>> '{:02X}{:02X}{:02X}{:02X}'.format(*octets)
'C0A80001'
>>> int(_, 16)  # 官方文档给出来的，无法在IDLE复现
3232235521
>>>
>>> width = 5
>>> for num in range(5,12):
...     for base in 'dXob':
...         print('{0:{width}{base}}'.format(num, base=base, width=width), end=' ')
...     print()
...
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8     8    10  1000
    9     9    11  1001
   10     A    12  1010
   11     B    13  1011
```


### 占位符%s和%r

![img](https://images.cnblogs.com/OutliningIndicators/ExpandedBlockStart.gif)


```python
"""
replacement_field ::= "{" [field_name] ["!" conversion] [":" format_spec] "}"
conversion ::= "r" | "s" | "a"
这里只有三个转换符号，用"!"开头。
"!r"对应 repr()；"!s"对应 str(); "!a"对应ascii()。
"""

>>> "repr() shows quotes: {!r}; str() doesn't: {!s}".format('test1', 'test2')
"repr() shows quotes: 'test1'; str() doesn't: test2"  # 输出结果是一个带引号，一个不带
```


# format的用法变形


```python
# a.format(b)
>>> "{0} {1}".format("hello","world")
'hello world'


# f"xxxx"# 可在字符串前加f以达到格式化的目的，在{}里加入对象，此为format的另一种形式：
>>> a = "hello"
>>> b = "world"
>>> f"{a} {b}"
'hello world'



name = 'jack'
age = 18
sex = 'man'
job = "IT"
salary = 9999.99

print(f'my name is {name.capitalize()}.')
print(f'I am {age:*^10} years old.')
print(f'I am a {sex}')
print(f'My salary is {salary:10.3f}')

# 结果
my name is Jack.
I am ****18**** years old.
I am a man
My salary is   9999.990
```