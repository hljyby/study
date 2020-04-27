1数据库图形化软件 Navicat

https://dev.mysql.com/downloads/mysql/

https://www.navicat.com.cn/download/navicat-premium

2有安装包，和压缩包两种

3教程：

https://www.jianshu.com/p/c89bace95cfa

https://blog.csdn.net/qq_37350706/article/details/81707862



字符集[utf-8,ASSCII,unicode,gbk(汉字字符集，gb开头),UTF16]

# 4 sql数据库简介基础知识

##sql语言

## 1:功能分类

ddl:数据定义语言（创建库，表，列，定义数据库对象）

dml:数据操作语言（操作数据库表中的记录）

dql:数据查询语言（查询数据）

dcl:数据控制语言（定义访问权限和安全级别）



## 2：基本操作

增：

INSERT INTO [TABLE_NAME] (column1, column2, column3,...columnN)  VALUES (value1, value2, value3,...valueN)， (value1, value2, value3,...valueN);

删：

DELETE FROM [table_name] WHERE [condition];

改：

UPDATE [table_name] SET column1 = value1, column2 = value2...., columnN = valueN

查：

### 1：SELECT column1, column2, columnN FROM table_name;

### 2：SELECT * FROM person;//查这个表里的全部



### 3：select * from person where name='yang'&& age=22; 

//and也可以（&&）

### 4：like（模糊查询）

- 百分号 %：匹配任意多个字符
- 下划线 _：匹配固定一个字符

**select * from person where name like '%ang';**

### 5：in 

in 关键字也是使用在 where 子句的条件表达式中，它限制的是一个集合，只要字段的值在集合中即符合条件，例如：

**select * from person where age in (22,30,23);**

你也可以使用 not in 反向限制，例如：

***select * from person where age not in (22,30,23);***

### **6、ORDER BY 子句**

ORDER BY 子句根据一列或者多列的值，按照升序或者降序排列数据。某些数据库就默认以升序排列查询结果。

基本的 SQL 语法为：

```
SELECT column
FROM table_name 
[WHERE condition] 
[ORDER BY column1, column2, .. columnN] [ASC | DESC];
```

ASC 表示数据结果集按升序排序，DESC 表示数据结果集按降序排序。

一般来说，我们按某一列进行排序即可，当然，有时候一列排序并不能完全解决问题，如果按多列排序，那么当遇到某一列值相同的时候，就会参照第二个列参数将这些重复列值得数据记录再一次排序。

举个例子：

**我们将 person 表中的数据参照 id 列，倒序排序：**

```
select * from person
order by id desc;
```

**7、GROUP BY 子句**

GROUP BY 子句用于将查询返回的结果集进行一个分组，并展示各个分组中排在第一个的记录，将分组中其余成员隐藏。

我们为 person 表添加几条数据，用于演示：

```
+----+-------+------+------------+----------+
| id | name  | age  | phone      | address  |
+----+-------+------+------------+----------+
|  1 | yang  |   22 | 231232132  | 中国上海 |
|  2 | cao   |   30 | 456789     | 浙江杭州 |
|  3 | li    |   23 | 34567894   | 江苏南京 |
|  4 | huang |   33 | 34567894   | 湖北武汉 |
|  5 | zhang |   30 | 4567890    | 中国北京 |
|  6 | yang  |   24 | 2343435353 | 山东青岛 |
|  7 | cao   |   44 | 12312312   | 河南郑州 |
|  8 | huang |   45 | 5677675    | 安徽合肥 |
|  9 | yang  |   80 | 3343738    | 江苏南通 |
+----+-------+------+------------+----------+
```

*注意观察姓名列，有几组重复的姓名。*

我们按照姓名对结果集进行分组，SQL 如下：

```
select * from person
group by name;
```

执行 SQL，得到结果：

```
+----+-------+------+-----------+----------+
| id | name  | age  | phone     | address  |
+----+-------+------+-----------+----------+
|  2 | cao   |   30 | 456789    | 浙江杭州 |
|  4 | huang |   33 | 34567894  | 湖北武汉 |
|  3 | li    |   23 | 34567894  | 江苏南京 |
|  1 | yang  |   22 | 231232132 | 中国上海 |
|  5 | zhang |   30 | 4567890   | 中国北京 |
+----+-------+------+-----------+----------+
```

你看，分组之后，只展示每个分组下排序第一的记录，其余成员隐藏。

细心的同学可能发现了，分组后的数据记录排序怎么乱了，怎么不是默认的 id 升序排列了？

对，如果你没有显式执行排序方式的话，将默认以你用于分组参照的那个字段进行排序。

当然，我们是可以执行排序方式的，使用 order by 子句：

```
select * from person
group by name
order by id;
```

效果是这样：

```
+----+-------+------+-----------+----------+
| id | name  | age  | phone     | address  |
+----+-------+------+-----------+----------+
|  1 | yang  |   22 | 231232132 | 中国上海 |
|  2 | cao   |   30 | 456789    | 浙江杭州 |
|  3 | li    |   23 | 34567894  | 江苏南京 |
|  4 | huang |   33 | 34567894  | 湖北武汉 |
|  5 | zhang |   30 | 4567890   | 中国北京 |
+----+-------+------+-----------+----------+
```

这就是分组，可能会有同学疑问，这样的分组有什么意义，分组是分完了，给我返回每个分组的第一行记录有什么用？

其实是这样的，我们之所以进行分组，就是为了统计和估量每个分组下的指标情况，比如这组数据的平均年龄、最高薪水等等等等。

而当我们只是 「select *」的时候，数据库根本不知道你要干什么，换句话说就是你并没有对每一个分组中的数据进行任何的分析统计，于是给你返回该分组的第一行数据。

你要记住的是，每个分组只能出来一个数据行，究竟让什么样的数据出来取决于你。

**比如我们计算每个分组下的平均年龄：**

```
select avg(age) as '平均年龄' from person
group by name;
```

查询结果：

```
+----------+
| 平均年龄 |
+----------+
|  37.0000 |
|  39.0000 |
|  23.0000 |
|  42.0000 |
|  30.0000 |
+----------+
```

**8、HAVING 子句**

HAVING 子句在我看来就是一个高配版的 where 子句，无论是我们的分组或是排序，都是基于以返回的结果集，也就是说 where 子句的筛选已经结束。

那么如果我们对排序、分组后的数据集依然有筛选需求，就用到我们的 HAVING 子句了。

例如：

```
select avg(age) as vage from person
group by name
having vage>23;
```

分组之后，我们得到每个分组中数据的平均年龄，再者我们通过 having 语句筛选出平均年龄大于 23 的数据记录。

以上我们介绍了六个子句的应用场景及其使用语法，但是如果需要同时用到这些子句，语法格式是什么样的？作用优先级是什么样的？

```
SELECT column1, column2
FROM table
WHERE [ conditions ]
GROUP BY column1, column2
HAVING [ conditions ]
ORDER BY column1, column2
```

大家一定要记住这个模板，各个子句在 SQL 语句中的位置，可以不出现，但不得越位，否则就会报语法错误。

首先是 from 语句，查出表的所有数据，接着是 select 取指定字段的数据列，然后是 where 进行条件筛选，得到一个结果集。

接着 group by 分组该结果集并得到分组后的数据集，having 再一次条件筛选，最后才轮到 order by 排序。

# 3聚合函数

count(DISTINCT)  //distinct 去重

sum,svg,max,min