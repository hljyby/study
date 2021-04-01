### 1：strip()方法，去除字符串开头或者结尾的空格

> \>>> a = " a b c "
>
> \>>> a.strip()
>
> 'a b c'

### 2：lstrip()方法，去除字符串开头的空格

> \>>> a = " a b c "
>
> \>>> a.lstrip()
>
> 'a b c '

### 3：rstrip()方法，去除字符串结尾的空格

> \>>> a = " a b c "
>
> \>>> a.rstrip()
>
> ' a b c'

### 4：replace()方法，可以去除全部空格

\# replace主要用于字符串的替换replace(old, new, count)

> \>>> a = " a b c "
>
> \>>> a.replace(" ", "")
>
> 'abc'

### 5: join()方法+split()方法，可以去除全部空格

\# join为字符字符串合成传入一个字符串列表，split用于字符串分割可以按规则进行分割

> \>>> a = " a b c "
>
> \>>> b = a.split() # 字符串按空格分割成列表
>
> \>>> b ['a', 'b', 'c']
>
> \>>> c = "".join(b) # 使用一个空字符串合成列表内容生成新的字符串
>
> \>>> c 'abc'
>
>  
>
> \# 快捷用法
>
> \>>> a = " a b c "
>
> \>>> "".join(a.split())
>
> 'abc'

​     