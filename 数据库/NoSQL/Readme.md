# nosql 数据库

- qps
  - 数据库的查询速度
  - queries per sencod
  - mysql ====> 5000 -8000
  - redis =====> 11w

- redis 可以实现的功能
  - 高速缓存
  - 排行榜 （zset）
  - 商品秒杀、投票点赞
  - 分布式锁
  - 消息队列

- redis 配置文件

  - ```python
    sudo make && make install # 必须有makefile文件，没有运行 ./configure 获取文件
    # ./configure --prefix=/软件要安装的路径
    # 也可以这么指定文件 make PREFIX=/软件要安装的路径 install -------- PREFIX 必须要大写才好使，这么安完之后要配置环境变量,如果不用这个，那redis的命令在/usr/local/bin里
    redis-server /配置文件路径 # 想使用配置文件里的内容就必须带着配置文件运行命令
    
    redis-cli -h 地址 -p 端口 # redis-client 地址是本地可以不写，端口默认也可以
    
    redis-cli shutdown
    
    # 找redis-server命令可以
    find -name redis-server
    find -name redis-cli
    
    # 自己安装的配置文件在解压的安装包里，yum 安装上网查
    deamonize yes # 守护进程，虚拟光驱,作用是使 redis 在后台运行。
    
    port 6379 # 默认端口号
    
    bind 127.0.0.1 # 默认IP地址，设置为127.0.0.1可阻止远程登录。
    
    loglevel notice # log信息级别 notice 最低级别，所有信息都会打印到log文件里
    
    logfile "" #log信息打印到什么文件里里
    
    databases 16 # 默认16个数据库，redis 不用自己创建数据库。 
    
    dir ./ # dump.rdb文件默认保存的地方，可以改。
    
    dbfilename dump.rdb # 保存数据库文件名
    
    # dir ./ 表示你用那个账户启动dump.rdb 就存到那个‘账户’的根目录，比如root启动就存在/root里
    ```

    

- redis命令 

  [redis文档]: http://redisdoc.com/

  

  - **字符串命令**

    ```python
    # redis 命令
    
        set name zhangsan
        get name
        set age 18 ex 20 # ex 20s后失效
        get age
        # ex 是秒数 px 是毫秒数 
        ttl age # 查看有效时间 -1表示永不过期
        
        SETNX 是『SET if Not eXists』(如果不存在，则 SET)的简写。
        
        setex = set app 123 ex 20
        
        MSET date "2012.3.30" time "11:00 a.m." weather "sunny" # 同时存储多个值
        MGET date time weather # 同时取多个值
        
        MSETNX # 同时设置多个（不存在则 set ） multi set
        
        strlen # 获取key 的长度
        
        keys * #查看所有key值
        
        incr # 自增  incr ====> 增量
        
        incrby age 18 # age + 18 增加设置的数
        
        decr # 自减 decr===> 减量
        
        decrby #
    ```

  - **hash表**

    ```python
    hset dog name dahuang age 18
    hget dog name
    hexists dog age==> 1
    hdel dog age name
    hlebn dog  # 长度
    hstrlen dog name  # 长度
    hkeys dog # 拿到所有dog key
    hvals dog #dog的所有value
    hgetall dog
    ```

  - **列表**

    ```python
    lpush names lisi wangwu 
    rpush names jerry tony
    lrange names 0 -1
    lpop names 
    rpop names
    lset name 0 rous # 改值
    llen name # 长度
    lindex names 3 # 查下标 
    ```

  - **集合**

    ```python
    sadd names aaa bbb ccc
    sismember names aaa ==>1
    sismember names ddd ==>0
    
    srandmember names 3 # 随机取三个
    smembers names
    sdiff names 表  # 查出不同
    sunion name 表 # 合并两个表
    sinter name 表 # 交集
    
    ```

  - **有序集合**

    ```python
    zadd 表名 数据 名 数据 名
    zrange 表名 0 -1
    zrange 表名 名 withscored # 会打印名和数据
    zrevrange # 倒序
    zincrby names 5 名 加数
    ```

  - ipython ,client = redis.Redis(); client.get('name')

- redis 持久化

  - ```python
    RDB
    
    '''
    默认的持久化方式，会根据配置文件的时间节点来对文件进行持久化，对内存中的数据进行镜像，以二进制形式保存在dump.rdb文件中
    '''
    '''
    save 900 1 # 900秒修改过一个key 保存一次数据库
    save 300 10 # 300秒修改过10次key 保存一次数据库
    save 60 10000 # 60秒内修改了10000个key 保存一次数据库
    '''
    # 优点：速度快文件小
    # 缺点：数据有可能会丢失，有两次保存间隔内的数据，有可能会丢失
    	
    AFO
    
    '''
    append only file 将修改的每一条指令录进appendonly.aof，需要修改配置文件，来打开aof功能。
    
    appendfsync always # 每次有新命令追加到aof文件时 就执行一个持久化，非常慢但是安全
    appendfsync eversec # 每秒执行一次持久化，和rdb差不多，并在故障时只会丢失一秒的数据
    appendfsync no # 从不执行持久化，将数据交给操作系统，redis处理命令速度加快，不安全
    '''
    
    
    '''
    优点 适合保存增量数据，数据不丢失
    缺点 文件体积大恢复时间长
    
    '''
    	
    ```

    

# MongoDB 基本

- | mysql       | mongodb     | 解释            |
  | ----------- | ----------- | --------------- |
  | database    | database    | 数据库          |
  | table       | collection  | 二维表/集合     |
  | row         | document    | 行/文档         |
  | column      | field       | 列/域           |
  | index       | index       | 索引            |
  | table joins |             | 表连接/嵌套文档 |
  | primary key | primary key | 主键/主键 _id   |

  

- sql 语句

  ```sql
  -- 创建collection的语句
  db.createCollections('student')  # 大小写分清
  show collections
  show databases
  db.student.insert({'name':'张三','age':'李四'})
  
  db.student.find()
  
  db.student.update({'name':'张三'},{'name':'王五'})
  
  db.student.find().pretty() -- 变漂亮
  
  db.student.findOne()
  
  ```

  ```sql
  db.user.find().limit(2)
  
    -- 条件符查询 mongodb支持<  <=  >  >= 四种运算符查询
  
    db.user.find({“age”:{$gt:30}})     age大于30
  
    db.user.find({“age”:{$lt:30}})      age小于30
  
    db.user.find({“age”:{$gte:30}})   age大于或等于30
  
    db.user.find({“age”:{$lte:30}})    age小于或等于30
  
    db.user.find({“age”:{$all:[6,8]}});
  
    -- 查询某一个字段是否存在：$exists
  
    db.user.find({age:{“in":[null],"
  
    db.user.find({“password”:{$exists:true}})；    password存在的记录
  
    db.user.find({“password”:{$exists:false}})；   password不存在的记录
  
    9，取模运算   $mod
  
    10,不等于   $ne       –> (not equals)
  
    11,包含   $in
  
    12,不包含  $nin
  
    13,数组元素的个数   $size
  
    14，正则表达式匹配查询
  
    name不以wpz开头的数据
  
    db.user.find({“name”:{$not:/^wpz.*/}});
  
    查询age数据元素个数为3的数据
  
    db.user.find({age:{$size:3}});
  
    查询所有age不等于10 或者20 的数据
  
    db.user.find({age:{$nin:[10,20]}});
  
    查询所有age等于10 或者20 的数据
  
    db.user.find({age:{$in:[10,20]}});
  
    查询所有age不等于10 的数据
  
    db.user.find({age:{$ne:10}});
  
    查询所有age取模10之后为0 的数据，即查询age为10的倍数的字段：
    db.user.find({age:{$mod:[10,0]}});
  
    exists”:true}});
  
    15,count查询条数
  
    db.user.find().count();
  
    16,skip  设置查询数据的起点
  
    查询从第三条数据之后的五条数据
  
    db.user.find().skip(3).limit(5);
  
    17 排序  sort
  
    db.user.find().sort({age:1});      按照age升序
    db.user.find().sort({age:-1});     按照age降序
  
    mongodb也支持存储过程的查询。
  
  ```

  

    7,数据修改更新

  ```sql
    mongodb的修改是比较烦的一种 ，要用到$set:
  
    例如，吧mongodb中,name为wpz,修改为  wpz_new
    db.user.update({“name”:”wpz”},{$set:”name”:”wpz_new”});
  ```

    8，数据删除

  ```
    mongodb的删除比较简单，格式如下：
    db.user.remove({“name”:”wpz”});             
                 
    db.user.find({“name”:”wpz”}).limit(2)
  
    db.student.drop() -- 删表
  
    db.dropDatabase() -- 删库 注意大小写 
    
  ```

- RoBo 3T

  想要外网链接数据库必须关闭防火墙

  ```sql
  systemctl stop firewalld.service -- 停止firewall
  
  systemctl disable firewalld.service -- 禁止firewall开机启动
  
  ```

firewall-cmd --zone=public --add-port=6379/tcp --permanent 
    -- 防火墙放开6379端口

    –zone #作用域
    –add-port=80/tcp #添加端口，格式为：端口/通讯协议
    –permanent #永久生效，没有此参数重启后失效
    
    -- centOS 
    
    1、开启防火墙 
        systemctl start firewalld
    
    2、开放指定端口
          firewall-cmd --zone=public --add-port=1935/tcp --permanent
     命令含义：
    --zone #作用域
    --add-port=1935/tcp  #添加端口，格式为：端口/通讯协议
    --permanent  #永久生效，没有此参数重启后失效
    
    3、重启防火墙
          firewall-cmd --reload
    
    4、查看端口号
    netstat -ntlp   //查看当前所有tcp端口·
    
    netstat -ntulp |grep 1935   //查看所有1935端口使用情况·
    
     方式二


    #开放端口:8080

    /sbin/iptables -I INPUT -p tcp --dport 8080 -j ACCEPT


​     
​    
​    方式三
​    
    -A INPUT -m state --state NEW -m tcp -p tcp --dport 8080 -j ACCEPT
    
    service iptables restart


​    
​    -- ubuntu 
​    
    一般情况下，ubuntu安装好的时候，iptables会被安装上，如果没有的话那就安装上吧
    
    安装
    在终端输入
    sudo apt-get install iptables
    添加规则
    在终端输入
    iptables -I INPUT -p tcp --dport 80 -j ACCEPT
    中间的80为所需要开放的端口
    
    保存规则
    在终端输入
    iptables-save
    完成上述命令我们就完成了开放指定的端口，但是如果此时服务器重启，上述规则就没有了，所以我们需要对规则进行一下持续化操作


​    
​    
​    持久化规则
​    这里我们需要在安装一下工具来帮我们实现，这里我们使用 iptables-persistent
​    
    安装iptables-persistent
    sudo apt-get install iptables-persistent
    持久化规则
    sudo netfilter-persistent save
    sudo netfilter-persistent reload
    完成上述操作就可以永久打开我们需要的端口了
    ```


​    