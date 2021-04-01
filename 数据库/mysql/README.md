- 1数据库图形化软件 Navicat

  ​	https://dev.mysql.com/downloads/mysql/

  ​	https://www.navicat.com.cn/download/navicat-premium

- 2有安装包，和压缩包两种

- 3教程：

  ​	https://www.jianshu.com/p/c89bace95cfa

  ​	https://blog.csdn.net/qq_37350706/article/details/81707862



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



insert into 表名 set 字段名=值;

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



# mysql CentOS 安装

- yum repolist 查看yum 的库

- 1.使用 yum 查找软件包 
  命令：yum search 
  2.列出所有可安装的软件包 
  命令：yum list 
  3.列出所有可更新的软件包 
  命令：yum list updates 
  4.列出所有已安装的软件包 
  命令：yum list installed

- 在CentOS里 直接 yum install mysql 安装的不是 mysql

- 先去官网下载 [MySQL Yum Repository](https://dev.mysql.com/downloads/repo/yum/)

  - 这个是mysql 的社区版（community）

  - 然后用 wget https://dev.mysql.com/downloads/repo/yum/ 下载
  - 安装下载的这个mysql 库
  - vim /etc/yum/repos.d/mysql-community.repo
  - 修改里面 mysql 8.0文件 enabled 改为0（0为不安装，1位安装），添加5.7的安装目录，没有上网查。（把8.0复制一遍改为5.7）
  - yum install mysql-community-server 安装mysql数据库

- 忘记密码了
  - 找到etc里面的mysql 配置文件 在 【mysqld】 下面加一行skip-grant-tables
  - 不同的系统这个文件所在的不一样，有可能叫my.cnf 也有可能叫mysql.cnf

- 直接登录mysql数据库

  - ```
    mysql -uroot -hlocalhost -P3306 -p
    ```

- 添加用户

  - ```sql
     5.7
     
     GRANT ALL ON *.*(<database>.<table>) TO 'myuser'@'localhost' IDENTIFIED BY "123" WITH GRANT OPTION
     
     ALL 代表 所有权限 （privileges）
     
     GRANT 授予
     
     privileges 权限  包括 select insert update delete create drop index alter
     grant reference reload shutdown process file 14个权限 
     
     *.* 所有数据库所有的表
     
     WITH GRANT OPTION 权限可以向下传递
     
     
     8.0版本
     
     create user '用户名'@主机 indentified by '密码';
    grant all on *.* to 用户名@主机 with grant option
    ```
  ```
     
  - ```
    flush privilegs 刷新权限
  ```

- 查看权限

  - ```
    show grants;
    show grants for '用户名'@'localhost'; 
    ```

- 回收权限

  - ```sql
    revoke all privileges on *.* from 'abc'@'localhost';
    revoke grant option on *.* from 'abc'@'localhost'; #回收权限的传递
    ```

- 修改密码

  - ```sql
    update user set authentication_string=password('你的密码') where user="root" 
    or
    alter user '用户名'@'localhost' identified with mysql_native_password by '你的密码';
    -- mysql_native_password 代表密码加密规则 这个加密规则是5.x 的
    ```

- 删除用户

  - ```sql
    use mysql
    select host,user from user
    drop user 用户名@'%'
    ```

- 创建一个可以再任意mysql client 登录的账户

  - ``` sql
     GRANT ALL ON *.* TO myuser@'%' IDENTIFIED BY "123" WITH GRANT OPTION -- mysql5.x
    ```

  - 此用户可以在任意mysql 客户端登录

  - 如果在my.cnf里有

    ``` sql
    bind-address=127.0.0.1 把它注释掉，他阻止远端登录
    ```

- 创建一个数据库，表

  - ``` sql
    create database 数据库名
    drop database 数据库名
    alter database 数据库名 charset=utf8;
    use 数据库名
    create table 表名(
    	id int primary key auto_increment,
    	name varchar(128),
    	tel varchar(32) unique, #unique 唯一约束，如果这个手机重号就不可以在往里面写了
    )charset=utf8;
    describe 表名;
    show create table 表名; -- 查看建表语句
    alter table 表名 rename 新表名;
    alter 表名 rename to 数据库名.表名;-- 移动表
    alter table 表名 add 字段名 数据类型
    alter table 表名 add 字段名 数据类型 first ;# 添加到第一行
    alter table 表名 add 字段名 数据类型 after 字段名; 添加到某个字段之后
    alter table 表名 modify 字段名 数据类型; # 修改字段的属性
    alter table 表名 change 原字段名 新字段名 数据类型; # 修改字段名
    alter table 表名 change 原字段名 新字段名 数据类型 after 指定字段; # 修改字段位置
    alter table 表名 drop 字段名; # 删除字段
    drop table 表名;
    
    
    
    ```

- mysql 登入没有语法高亮，可以安装 mycli

  - ```sql
    pip3 install mycli
    
    mycli -u root #用mycli登录mysql
    ```

    

- 复制表

  - ```sql
    create table 表名 select * from 要复制的表名 #不建议使用
    
    
    create table 新表 like 旧表; # 只复制结构不复制数据
    insert into 新表 select * from 旧表; # 复制数据插入到新表
    ```

    

- 查看默认编码集 （utf8）

  - ```sql
    show variables like '%character%'
    
    show create table 表名
    
    show create database 数据库名
    ```

    

- 校对集 （_ci）

  - ```sql
    show character set #查看字符集和校对集
    
    show collection # 查看所有校对集
    
    collate=utf8mb4_general_ci #在创建的时候可以指定校对集（mysql 默认对大小写不敏感）
    ```

    后缀_ci 是对大小写不敏感

    后缀_cs 是对大小写敏感

    后缀_bin 是对大小写敏感

    在mysql 中字段名是忽略大小写的

- enum 枚举

  - 可以限定内容（enum('男','女','保密')）
  - 最好别用，好坑！！！！

- 集合（set）
  
- set('吃','喝')
  
- 时间类型

  - ```sql
    DateTime >> 1999-08-19 12:12:12
    Date >> 1999-08-19
    timestamp >> 15453134 # 时间戳 存的时候存 1999-08-19 12:12;12
    Time >> 12:12:12
    year >> 1901-2155
    
    now() # mysql内置函数 
    ```
    
    
  
- 布尔类型 （bool）

  - True （保存的是1）
  - False （保存的是 0）

- 列的属性

  - ``` sql
    null
    not null
    default
    auto_increment
    primary key
    unique
    coment 注释
    ```

- 运算符

  - ```sql
    + - * / = != <>
    123 between 100 and 200
    not between and
    in
    null <=> null -- >> 1
    12 is null -- >> 0
    23 = null -- >> null
    null is null -- >> 1
    32 is not null -- >> 1
    and
    like
    -- 注释
    /*
    多行注释
    */
    # mysql独有的注释
    rand() -- 随机数
    now() -- 时间
    -- 如果表名叫into 等关键字 可以加一个``
    decimal(7,2) -- 长度为7位，小数点后面保留两位
    ```

    

- 函数语法

  - ```sql
    distinct 去重 
    	select distinct from 表 where 条件 
    char_length 字符长度
    	select * from 表 where char_length(name) 
    length 字节长度
    	select length(name) from 表
    ___ 三个下划线 找字符长度为3的
    	select from 表 where name like '___'
    year 时间转化为年
    	select * from 表 where year(date)=2017
    	select * from 表 where date like '2017%'
    regexp 正则匹配
    	select * from 表 where date regexp '2017.*'
    count(); --算个数
    sum() --求和
    avg() --平均值
    max()
    min()
    abs()
    floor()
    ceil() --向上取整
    round(2.3423,2) -- 保留小数点后n位，四舍五入 2.34
    datediff('','') -- 两个时间相差的天数
    week() -- 返回一年中的第几周
    hour()
    minute()
    second()
    monthname -- 返回月份名
    date_formate -- 格式化
    lower() -- 变小写
    upper() -- 变大写
    left('hellow',3) -- 要左面三个 hel
    right('hellow',3) -- 要右面三个 low
    replace
    trim
    substring
    database() -- 返回当前数据库名
    version() -- 返回当前版本
    user() -- 返回登录用户
    password(str) -- 返回字符串的加密版本 mysql 8以后就没有了 
    MD5() -- 返回字符串的MD5 值
    ```

    

    

- having 和 where 的区别

  - where 可以通过所有的查

  - having 只能通过 你想要获取的查

  - 在使用别名查询的时候只能用having

  - ```
    select name as n age as a from 表 having n='XXX'
    -- 使用n（别名） 查询 就必须要用having
    -- having 是把表查回来再筛选
    -- where 是先筛选在查回来
    ```

  - having 后面能够使用聚合函数

- group  by 聚合函数

  - ```sql
    select group_concat(name) as 姓名，sun(money) as 总金额 from 表 group by city
    
    -- group_concat(name) 把城市一样的名字拼到一起
    
    select group_concat(name) as 姓名，sun(money) as 总金额 from 表 group by city having year(age)>1996
    ```

    

- order by 排序

  - ```sql
    esc
    desc
    order by age
    ```

- limit 

  - ``` sql
    limit 5 --取前五个
    offect 3 -- 忽略三个
    ```

- dual 虚拟表

  - ``` sql
    select 3+5 from dual
    -- 为了保证语句的完整性
    
    ```

-  union 列数得一样 
  - 上下合并到一起
  - select student.age,student.name,student.id from srtudent union select * from app

- inner join 

  - ```sql
    select student.age,student.name,student.id from srtudent inner join sorce 
    on student.id = sorce.id
    -- 两个表相交的地方
    ```

    

- left join 
  
  - 左边表里的都列出来
  
- right join
  
- 右边表里的都列出来
  
- 子查询

  - ```sql
    select * from student where id in (select min(id) from student group by city)
    ```

- 自动更新时间

  - ```sql
    DEFAULT CURRENT_TIMESTAMP 	-- 默认值为 CURRENT_TIMESTAMP
    ON UPDATE CURRENT_TIMESTAMP -- 用Navicat 设置根据当前时间戳更新
    -- 时间戳类型会根据服务器市区不通进行转化，并且不能存入Null，他会自动变成当前时间，datetime 类型存入什么就是什么。
    
    -- 创建测试表
    CREATE TABLE mytest (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `username` varchar(50) DEFAULT NULL,
        `password` varchar(50) DEFAULT NULL,
      createTime DATETIME DEFAULT CURRENT_TIMESTAMP ,
      updateTime DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        PRIMARY KEY (`id`)
    );
    
    -- 如果是添加新字段使用如下语句
    alter table tableName add column createTime DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间';
    alter table tableName add column updateTime DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间';
    
    --  如果是更新已有字段使用如下语句
    alter table tableName modify column createTime DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间';
    alter table tableName modify column updateTime DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间';
    ```

    

- 视图表

  - ```sql
    -- 把一条查询语句查到的数据存到视图表中，以后就不用每次都写一长串sql 语句了
    create view 视图名 as sql语句
    -- 视图表不会提升执行效率 视图表一般以v_为前缀，与一般的表进行区分，视图表不适合增删改
    drop view 视图表名
    -- 改变原表视图表会自动更新，改动视图表，原表也会改变
    -- 在5.7.xx 小版本以前不能修改视图表，5.7.29 版本可以改
    -- 视图表是否可以修改取决于，algorithm（算法） 的值
    -- algorithm有三个属性 nudefind merge temptable
    -- undefind merge 可以修改
    -- temptable 不可修改
    
    create algorithm=temptable view 视图名 as sql语句
    ```

    

- 存储引擎（storage engine）

  - ```sql
    show variables like '%engine%'
    show engines
    -- InnoDB 存储引擎
    -- MyISAM 存储引擎
    -- transactions 事务
    -- row-level locking 行级锁
    -- foreign key 外键
    -- innoDB 把文件存储为两个文件
    /*
    	.frm 存储的是表结构
        .idb 存储的是数据
    */
    -- MyISAM 把文件存储为三个文件
    /*
    	.frm 存储的是表结构
        .myd 存储的是数据
        .myi 存储的是表索引
    */
    
    -- 索引 是将要查的东西独立建一张表，查询速度会变快，不建索引查询是一行一行挨个查，建立索引会就查索引建的表。
    -- 索引 不要随便建，建立索引后查询的效率会很高，插入的效率会很低
    ```

- 外键

  - ```sql
    alter table userinfo add constraint fk_uid foreign key(id) references user(id)
    
    alter table userinfo drop foreign key fk_uid
    ```

    

- 事务

  - ```sql
    /*
    事务四大特性 (ACID)
    -- musql的隔离级别不会引起脏读
    	1:原子性 （Atomity）
    		事务中所有操作，要不就全部完成，要不就全部失败，不会结束在中间位置
    		事务在发生错误后会回滚
    	2:一致性 （Consistey）
    	3:隔离性 （Isolation）
    		脏读：一个事务读取了一个回滚了的数据
    		不可重复读：一个事务A用事务B修改了的数据查询，过后事务B回滚了
    		幻读：
    			查看事务的隔离级别 show variables like '%isolation%'
    			事务的隔离级别一般是出现在并发问题
    	4:持久性 （durability）
    */
    
    begin; -- 开启事务 或者 start transaction
    commit; -- 提交事务
    roolback; -- 事务回滚
    savepoint identifier; -- 创建保存点
    release savepoint identifier; -- 删除保存点
    rollback to identifier; -- 把事务回滚到保存点
    show variables like '%isolation%'; -- 查看事务的隔离级别
    set session|global transaction isolation level {read uncommitted | read committed | repeatable read | serializable(线性) } -- 设置隔离级别
    ```

- 存储过程 （stored procedure）【**IN** **OUT** **INOUT**】

  - ```sql
    -- 创建存储过程
    drop procedure if exists `foo`;
    delimiter $$ -- 改变sql 语句的结束符，写完这句换之后sql 语句的结束符就不是 ';' 了。
    create procedure foo()
    begin
    declare tmp varchar(10) -- 定义的变量， 仅在当前存储过程中生效
    set tmp = 'yby' 
    select * from persion
    select * from student
    select * from score
    end$$ 
    
    -- 调用
    delimiter ; --用完之后改回来
    call foo();
    
    
    -- 查看
    show procedure status like '%foo%';
    drop procedure foo;
    
    -- 带参数的存储过程
    /*
    	set @var=1 中的@是定义全局变量的
    	在存储过程中用declare 也可以定义变量，不过他是局部变量，只能在存储过程中使用。
    	如果不在全局使用变量可以不用加@符号
    	在存储过程中declare 定义的变量，在后续使用的时候，如果前面加了@也会变为全局变量
    */
    delimiter $$ -- 改变sql 语句的结束符，写完这句换之后sql 语句的结束符就不是 ';' 了。
    create procedure foo(in a int,in b varchar(32),out c int)
    begin
    declare num int;
    set @num=1;
    select count(*) into @num from persion;
    select * from student;
    select * from score;
    set c=@num;
    end$$ 
    
    
    -- mysql if 语句
    
    IF expression THEN
       statements;
    ELSE
       else-statements;
    END IF;
    
    -- mysql if else if语句
    IF expression THEN
       statements;
    ELSEIF elseif-expression THEN
       elseif-statements;
    ...
    ELSE
       else-statements;
    END IF;
    
    
    -- exists (存在)
    create table IF NOT EXISTS t1(id int not null);
    -- 如果不存在t1 就创建t1 表
    
    DROP PROCEDURE IF EXISTS p_alter_table;
    -- 如果存在p_alter_table存储过程就删除
    
    select * from 表名 where exists(select * from main)
    -- exists 另一种用法
    ```

- 主从复制（数据库）

- 数据库备份和恢复

  - ``` sql
    -- 备份
    mysqldump - h localhost -u root -p 数据库名 > dbname.sql
    -- 恢复
    mysql -h localhost -u root -p 数据库名 < ./dbname.sql
    ```

    

- 自动备份数据库

  - ```python
    
    #!/usr/bin env python3
    import os
    import time
    import datetime
    #定义服务器，用户名、密码、数据库名称（多个库分行放置）和备份的路径
    DB_HOST = 数据库地址
    DB_USER = 用户名
    DB_USER_PASSWD = 用户密码
    DB_NAME = 可配置的数据库名称文件
    BACKUP_PATH = 要保存到的路径名称
    print("checking for databases names file")
     
     
    #定义执行备份脚本，读取文件中的数据库名称，注意按行读写，不校验是否存在该库
    def run_backup():
    		while True:
    			DATETIME = time.strftime('%Y%m%d-%H%M%S')
    			TODAYBACKUPPATH = BACKUP_PATH + DATETIME
    			print("createing backup folder!")
    			#创建备份文件夹
    			if not os.path.exists(TODAYBACKUPPATH):
    					os.makedirs(TODAYBACKUPPATH)
    			in_file = open(DB_NAME,"r")
    			for dbname in in_file.readlines():
    					dbname = dbname.strip()
    					print("now starting backup database %s" %dbname)
    					dumpcmd = "mysqldump --single-transaction  --ignore-table=哪些表不需要备份 -h" +DB_HOST+" -u" +DB_USER + " -p"+DB_USER_PASSWD+" " +dbname+" > "+TODAYBACKUPPATH +"/"+dbname+".sql"
                        #针对mysqldump用法很多，大家可以自行查询，包括条件备份等
    					print(dumpcmd)
    					os.system(dumpcmd)
    			file1.close()
    			time.sleep(24*60*60)//每天备份
     
    if os.path.exists(DB_NAME):
            file1 = open(DB_NAME)
            print("starting backup of all db listed in file "+DB_NAME)
            run_backup()
            print("backup success!")
    else:
            print("database file not found..")
            exit()
            
    ```

    

    - DB_NAME 文件（里面装的数据库名）

  - ```txt
    ybytest
    main
    code
    ```

    

# mysql5.x mysql8.x 密码加密规则不一样 导致client 无法登陆

```sql
-- 出现这个原因是mysql8 之前的版本中加密规则是mysql_native_password,而在mysql8之后,加密规则是caching_sha2_password, 解决问题方法有两种,一种是升级navicat驱动,一种是把mysql用户登录密码加密规则还原成mysql_native_password. 

-- 修改账户密码加密规则并更新用户密码
ALTER USER 'root'@'localhost' IDENTIFIED BY 'password' PASSWORD EXPIRE NEVER;   -- 修改加密规则 
-- PASSWORD EXPIRE NEVER 永不过期
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';  -- 更新一下用户的密码

-- 上面两句合起来才能 修改加密规则 第一句用处就是永不过期，还可以这么写
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password' PASSWORD EXPIRE NEVER;
-- 效果是一样的

FLUSH PRIVILEGES;   -- 刷新权限 

-- 单独修改密码命令：
alter user 'root'@'localhost' identified by '111111';
 
```

# 新建数据库可以写成sql 文件

```sql
准备 sql 文件
user 数据库
source sql文件路径 -- 执行sql 语句
```

