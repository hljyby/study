Mongodb

## Docker 部署mongodb

```shell
docker pull mongo
```

```shell
docker run -d --name mongodb -p 27017:27017 mongo
```

# 安装

[mongoDB官网](https://www.mongodb.org/)下载安装（[Windows安装方法](http://docs.mongodb.org/manual/tutorial/install-mongodb-on-windows/)）

# 基础知识

集合——对应关系数据库中的表

文档——对应关系数据库中的行

# 启动数据库服务

定位到安装目录下的bin文件夹里后

```shell
> mongod --dbpath ../data/db
```

如没有`data/db`文件夹，需先创建，`dbpath`用于指定数据存放位置

# 开启一个客户端访问数据库

同样的bin文件夹下执行

```shell
> mongo
```

默认连接至`test`数据库

# 显示帮助

```shell
> help
```

# 显示所有数据库名称

```shell
> show dbs
```

# 切换数据库

```shell
> use test
```

# 显示当前连接的数据库名称

```shell
> db
```

# 显示当前数据库所有集合

```shell
> show collections
```

# 显示数据库支持的方法

```shell
> db.help()
```

# 显示集合支持的方法

```shell
> db.users.help()
```

# 创建collection

```shell
> db.createCollection("users")
```

# 删除数据库

```javascript
> db.dropDatabase()
```

# 删除collection

```javascript
> db.users.drop()
```

# 重命名collection

```shell
db.hello.renameCollection("HELLO")
```

# 插入操作insert

```shell
> db.users.insert({"name":"kiinlam","age":28})
```

# 加载js文件

```shell
# index.js
db.user.insert({_id:1,name:"yby",age:18})

mongo
>load('index.js')
```

# 查询操作find

#### 查找所有文档

```shell
> db.users.find()
```

#### 查找指定文档

```shell
> db.users.find({"name":"kiinlam"})
```

#### 查询一条

```shell
> db.users.findOne({"name":"kiinlam"})
```

#### 查看名称中包含‘a’的数据

```shell
> db.user.find({name:/a/})
```

#### 查询name以W打头的数据

```shell
> db.user.find({name:/^W/})
```

#### 多条件“与”

查询age小于30，salary大于6000的数据

```shell
> db.user.find({age:{$lt:30},salary:{$gt:6000}})
```

#### 多条件“或”

查询age小于25，或者salary大于10000的记录

```shell
> db.user.find({$or:[{salary:{$gt:10000}},{age:{$lt:25}}]})
```

#### 查询指定字段的数据，并去重

```shell
> db.user.distinct('gender')
[ "female", "male" ]
```



#### 大于$gt

```shell
> db.users.find({"age":{$gt:22}})
```

#### 大于等于$gte

```shell
> db.users.find({"age":{$gte:22}})
```

#### 小于$lt

```shell
> db.users.find({"age":{$lt:22}})
```

#### 小于等于$gte

```shell
> db.users.find({"age":{$lte:22}})
```

#### 不等于$ne

```shell
> db.users.find("age":{$ne:22})
```

#### 或$or

```shell
> db.users.find({$or:[{"name":"kiinlam"},{"name":"cheungkiinlam"}]})
```

#### 在集合中$in

```shell
> db.users.find("name":{$in:["kiinlam","cheungkiinlam"]})
```

#### 不在集合中$nin

```shell
> db.users.find("name":{$nin:["kiinlam","cheungkiinlam"]})
```

#### 正则查询

```shell
> db.users.find({"name":/^k/,"name":/m$/})
```

#### 筛选查询$where

```shell
// 使用js function作为筛选条件 
> db.users.find({$where: function(){return this.name=='kiinlam'}})
```

#### 限制查询数量limit

```shell
> db.users.find({"age":22}).limit(10)
```

# 对查询结果集的操作

```
mongo`也提供了`pretty print`工具，`db.collection.pretty()`或者是`db.collection.forEach(printjson)
```

#### Pretty Print

```swift
> db.user.find().pretty()
{
        "_id" : ObjectId("5ce4f4c33e7e1703c34ec0d1"),
        "name" : "Gal Gadot",
        "gender" : "female",
        "age" : 28,
        "salary" : 11000
}
{
        "_id" : ObjectId("5ce4f4d03e7e1703c34ec0d2"),
        "name" : "Mikie Hara",
        "gender" : "female",
        "age" : 26,
        "salary" : 7000
}
{
        "_id" : ObjectId("5ce4f4dc3e7e1703c34ec0d3"),
        "name" : "Wentworth Earl Miller",
        "gender" : "male",
        "age" : 41,
        "salary" : 33000
}
```

#### 指定结果集返回条目

```bash
> db.user.find().limit(2)
{ "_id" : ObjectId("5ce4f4c33e7e1703c34ec0d1"), "name" : "Gal Gadot", "gender" : "female", "age" : 28, "salary" : 11000 }
{ "_id" : ObjectId("5ce4f4d03e7e1703c34ec0d2"), "name" : "Mikie Hara", "gender" : "female", "age" : 26, "salary" : 7000 }
```

#### 查询第一条以外的数据

```swift
> db.user.find().skip(1)
{ "_id" : ObjectId("5ce4f4d03e7e1703c34ec0d2"), "name" : "Mikie Hara", "gender" : "female", "age" : 26, "salary" : 7000 }
{ "_id" : ObjectId("5ce4f4dc3e7e1703c34ec0d3"), "name" : "Wentworth Earl Miller", "gender" : "male","age" : 41, "salary" : 33000 }
```

#### 对结果集排序

 升序

```swift
> db.user.find().sort({salary:1})
{ "_id" : ObjectId("5ce4f4d03e7e1703c34ec0d2"), "name" : "Mikie Hara", "gender" : "female", "age" : 26, "salary" : 7000 }
{ "_id" : ObjectId("5ce4f4c33e7e1703c34ec0d1"), "name" : "Gal Gadot", "gender" : "female", "age" : 28, "salary" : 11000 }
{ "_id" : ObjectId("5ce4f4dc3e7e1703c34ec0d3"), "name" : "Wentworth Earl Miller", "gender" : "male","age" : 41, "salary" : 33000 }
```

降序

```swift
> db.user.find().sort({salary:-1})
{ "_id" : ObjectId("5ce4f4dc3e7e1703c34ec0d3"), "name" : "Wentworth Earl Miller", "gender" : "male","age" : 41, "salary" : 33000 }
{ "_id" : ObjectId("5ce4f4c33e7e1703c34ec0d1"), "name" : "Gal Gadot", "gender" : "female", "age" : 28, "salary" : 11000 }
{ "_id" : ObjectId("5ce4f4d03e7e1703c34ec0d2"), "name" : "Mikie Hara", "gender" : "female", "age" : 26, "salary" : 7000 }
```

#### 统计结果集中的记录数量

```css
> db.user.find().count()
```

# 更新操作update

#### 更新

```shell
db.集合名.update(条件{},更新的数据{},upsert,multi)
upsert（updateinsert）为真时，当条件没有匹配数据时，将跟更新的数据插入集合中，反之为假时，则什么也不做。
multi为真时，当条件匹配多条数据时，将会更新所有的数据，反之则更新第一条数据。
```



#### 指定文档全部更新，等于覆盖

```shell
> db.users.update({"name":"kiinlam"}, {"name":"cheungkiinlam","age":27})
```

#### 局部更新一：增量更新$inc

```javascript
// age增加2，其他不变 
> db.users.update({"name":"kiinlam"}, {$inc:{"age":2}})
```

#### 局部更新二：字段修改$set

```javascript
// age改为20 
> db.users.update({"name":"kiinlam"}, {$set:{"age":20}})
```

#### 新增更新：如果不存在，就新增一条

```javascript
// 第三个参数为true 
> db.users.update({"name":"kiinlam"}, {$set:{"age":18}}, true)
```

#### 批量更新

```javascript
// 如果匹配多条，默认只改第一条，将第四个参数设为true可全部更新 
> db.users.update({"name":"kiinlam"}, {$set:{"age":18}}, true, true)
```

# 保存操作save

```javascript
// 插入新文档，如果不提供"_id"字段 
> db.users.save({"name":"kiinlam", "age":28}) 

// 更新已存在的文档 
> db.users.save({"_id":"xxx","name":"kiinlam", "age":28})
```

# 删除操作remove

删除操作不可恢复

#### 删除所有，但不删除索引

```javascript
> db.users.remove({})
```

#### 删除指定文档

```javascript
> db.users.remove({"name":"kiinlam"})
```

#### 删除一条指定文档，如果有多条结果

```javascript
> db.users.remove({"name":"kiinlam"}, true)
```

完全删除集合，包括索引，应当使用`drop`

大量删除时，采用复制需要保留的文档到新集合，再用`drop`删除集合。

# 计数操作count

```javascript
> db.users.count() 
> db.users.count({"age":29})
```

# 唯一值查询distinct

#### 指定字段有多个相同时，只取一个，返回指定字段的值组合成的数组

```javascript
> db.users.distinct("age")
```

# 分组操作group

按照`age`进行分组操作，分组结果存放在`user`中，值为对应`age`的name值的数组

`key`：分组依据

`initial`：初始化函数，每个不同的age组共享同一个函数

`$reduce`： 第一个参数为当前文档，第二参数为前一次函数操作的累计对象，第一次为`initial`对应的对象

```javascript
db.users.group({
    "key": {
        "age": true
    },
    "initial": {
        "user": []
    },
    "$reduce": function(cur, prev) {
        prev.user.push(cur.name);
    }
})
```

假设有数据如下：

```javascript
{
    "_id": ObjectId("55910457607379845607d9e2"),
    "name": "kiinlam",
    "age": 29
} {
    "_id": ObjectId("55910468607379845607d9e3"),
    "name": "shadow",
    "age": 26
} {
    "_id": ObjectId("55910992607379845607d9e5"),
    "name": "foo",
    "age": 29
} {
    "_id": ObjectId("55911fca607379845607d9e6"),
    "name": "dd",
    "age": 22
} {
    "_id": ObjectId("55911fd3607379845607d9e7"),
    "name": "mm",
    "age": 22
} {
    "_id": ObjectId("55911fdf607379845607d9e8"),
    "name": "gg",
    "age": 22
} {
    "_id": ObjectId("55911feb607379845607d9e9"),
    "name": "jj",
    "age": 22
} {
    "_id": ObjectId("55920545ff40738c1fd0a839"),
    "name": "zz",
    "age": 1
}
```

分组结果为：

```javascript
[{
    "age": 29,
    "user": ["kiinlam", "foo"]
},
{
    "age": 26,
    "user": ["shadow"]
},
{
    "age": 22,
    "user": ["dd", "mm", "gg", "jj"]
},
{
    "age": 1,
    "user": ["zz"]
}]
```

#### 更多分组功能

可选参数: `condition` 和 `finalize`。

```javascript
`condition` —— 过滤条件 
`finalize` —— 函数，分组完成后执行
```

过滤掉`age`大于22的文档，增加属性标明分组中文档的数量

```javascript
db.users.group({
    "key": {
        "age": true
    },
    "initial": {
        "user": []
    },
    "$reduce": function(cur, prev) {
        prev.user.push(cur.name);
    },
    "condition": {
        "age": {
            $lte: 22
        }
    },
    "finalize": function(out) {
        out.count = out.user.length;
    }
})
```

分组结果为：

```javascript
[{
    "age": 22,
    "user": ["dd", "mm", "gg", "jj"],
    "count": 4
},
{
    "age": 1,
    "user": ["zz"],
    "count": 1
}]
```

# mapReduce

`map`：映射函数，内部调用`emit(key,value)`，集合按照`key`进行映射分组。

`reduce`：简化函数，对`map`分组后的数据进行分组简化，`reduce(key,value)`中的`key`是`emit`中的`key`，而`value`则是`emit`分组结果的集合。

`mapReduce`：最后执行的函数，参数为`map`、`reduce`和一些可选参数。

```javascript
db.users.mapReduce
function(map, reduce, optionsOrOutString) {
    var c = {
        mapreduce: this._shortName,
        map: map,
        reduce: reduce
    };
    assert(optionsOrOutString, "need to supply an optionsOrOutString") if (typeof(optionsOrOutString) == "string") c["out"] = optionsOrOutString;
    else Object.extend(c, optionsOrOutString);
    var raw = this._db.runCommand(c);
    if (!raw.ok) {
        __mrerror__ = raw;
        throw Error("map reduce failed:" + tojson(raw));
    }
    return new MapReduceResult(this._db, raw);
}
```

创建`map`函数

```javascript
function() {
    emit(this.name, {
        count: 1
    });
}
```

创建`reduce`函数

```javascript
function(key, value) {
    var result = {
        count: 0
    };
    for (var i = 0; i < value.length; i++) {
        result.count += value[i].count;
    }
    return result;
}
```

执行`mapReduce`操作

```javascript
db.users.mapReduce(map, reduce, {
    "out": "collection"
})
```

假设有数据如下

```javascript
{
    "_id": ObjectId("55910457607379845607d9e2"),
    "name": "kiinlam",
    "age": 29
} {
    "_id": ObjectId("55910468607379845607d9e3"),
    "name": "shadow",
    "age": 26
} {
    "_id": ObjectId("55910992607379845607d9e5"),
    "name": "foo",
    "age": 29
} {
    "_id": ObjectId("55920545ff40738c1fd0a839"),
    "name": "zz",
    "age": 1
} {
    "_id": ObjectId("55911fca607379845607d9e6"),
    "name": "foo",
    "age": 22
} {
    "_id": ObjectId("55911fd3607379845607d9e7"),
    "name": "foo",
    "age": 22
} {
    "_id": ObjectId("55911fdf607379845607d9e8"),
    "name": "foo",
    "age": 22
} {
    "_id": ObjectId("55911feb607379845607d9e9"),
    "name": "foo",
    "age": 22
}
```

输出结果

```javascript
{
    "result": "collection",// 存放最终结果的集合名
    "timeMillis" : 28, 
    "counts" : { 
    	"input" : 8, // 传入文档的次数 
    	"emit" : 8, // emit函数被调用次数 
    	"reduce" : 1, // reduce函数被调用次数 
    	"output" : 4 // 最后返回文档的个数 
    }, 
    "ok" : 1 
}
    
```

查看集合`collection`中的结果

```javascript
> db.collection.find()
```

输出结果

```javascript
{
    "_id": "foo",
    "value": {
        "count": 5
    }
} {
    "_id": "kiinlam",
    "value": {
        "count": 1
    }
} {
    "_id": "shadow",
    "value": {
        "count": 1
    }
} {
    "_id": "zz",
    "value": {
        "count": 1
    }
}
```

# 游标

游标只表示一个引用，并不是真正的执行，在需要的时候，通过for循环或`next()`方法进行遍历读取，枚举结束后，游标销毁，不再返回数据。

申明一个游标

```javascript
> var list = db.collection.find()
```

通过`forEach`遍历游标

```javascript
> list.forEach(function(i){ print(i._id); })
```

输出结果

```javascript
foo kiinlam shadow zz
```

或者通过`next`遍历集合

```javascript
> var list = db.collection.find() 
> list.next() { "_id" : "foo", "value" : { "count" : 5 } } 
> list.next() { "_id" : "kiinlam", "value" : { "count" : 1 } } 
> list.next() { "_id" : "shadow", "value" : { "count" : 1 } } 
> list.next() { "_id" : "zz", "value" : { "count" : 1 } } 
> list.next() 
2015-07-01T11:27:38.186+0800 E QUERY Error: error hasNext: false at Error (<anonymous>) at DBQuery.next (src/mongo/shell/query.js:255:15) at (shell):1:6 at src/mongo/shell/query.js:255 
> list >
```

# 索引ensureIndex

#### 建立索引

```javascript
// 1为升序，-1为降序 
> db.users.ensureIndex({"name":1})
```

#### 唯一索引

```javascript
> db.users.ensureIndex({"name":1},{"unique":true})
```

#### 组合索引

```javascript
> db.users.ensureIndex({"name":1, "age":-1})
```

#### 查看索引

```javascript
> db.users.getIndexes()
```

#### 按指定索引查询

```javascript
> db.users.find({"name":"kiinlam"}).hint({"name":1,"age":1})
```

#### 删除索引

```javascript
// 删除所有自定义索引 
> db.users.dropIndexes() 

// 删除指定索引 
> db.users.dropIndex("name_1")
```

# 性能分析函数explain

```javascript
> db.users.find().explain("executionStats")
```

# 主从数据库部署

#### 创建主数据库master

```javascript
> mongod --dbpath=XXX --master
```

#### 创建从数据库slave

```javascript
// 指定从数据库端口
--port 

// 指定主数据库源
--source 

> mongod --dbpath=XXX --port=8888 --slave --source=127.0.0.1:27017
```

#### 后期指定主数据库源

```javascript
> mongod --dbpath=XXX --port=8888 --slave 
// 后期添加源 
// 切换到local数据库 
> use local 

// 在sources中加入源地址 
> db.sources.insert({"host":"127.0.0.1:27017"})
```

# 副本集replSet

该架构没有特定的主数据库，一个数据库宕机了，另一个数据库会顶上

#### 创建第一个数据库服务器

```javascript
// 需要指定集群名及下一个数据库地址 
> mongod --dbpath=XXX --port 2222 --replSet mySet/127.0.0.1:3333
```

#### 创建第二个数据库服务器

```javascript
> mongod --dbpath=XXX --port 3333 --replSet mySet/127.0.0.1:2222
```

#### 初始化副本集

```javascript
// 进入任一数据库的admin集合 
> mongo 127.0.0.1:2222/admin 

// 执行初始化操作 
> db.runCommand({ "replSetInitiate":{ "_id":"mySet", "members":[ { "_id":1, "host":"127.0.0.1:2222" }, { "_id":2, "host":"127.0.0.1:3333" } ] } })
```

#### 仲裁服务器

```javascript
// 启动仲裁服务器 
> mongod --dbpath=XXX --port 4444 --replSet mySet/127.0.0.1:2222 

// 回到admin集合中添加仲裁服务器 
> mongo 127.0.0.1:2222/admin 
> rs.addArb("127.0.0.1:4444") 

// 查看服务器集群状态 
> rs.status()
```

# 分片技术

将集合进行拆分，将拆分的数据均摊到几个分片上。

主要参与者：

- 客户端
- 路由服务器mongos
- 配置服务器
- 分片数据库实例

#### 开启配置服务器config

```javascript
> mongod --dbpath=XXX --port 2222
```

#### 开启路由服务器mongos

```javascript
// 指定配置服务器 
> mongos --port 3333 --configdb=127.0.0.1:2222
```

#### 开启分片数据库服务器mongod

```javascript
> mongod --dbpath=XXX --port 4444 
> mongod --dbpath=XXX --port 5555
```

#### 服务配置

```javascript
// 进入mongos数据库admin集合 
> mongo 127.0.0.1:3333/admin 

// 添加分片服务器addshard 
> db.runCommand({ "addshard":"127.0.0.1:4444", "allowLocal":true }) 
> db.runCommand({ "addshard":"127.0.0.1:5555", "allowLocal":true }) 

// 开启数据库test的分片功能enablesharding 
> db.runCommand({"enablesharding":"test"}) 

// 指定集合中分片的片键users.name 
> db.runCommand({"shardcollection":"test.users","key":{"name":1}}) 

// 在mongos中查看数据分片情况 
> use test 
> db.printShardingStatus()
```

# 运维

运维通常会涉及到以下4个方面

- 安装部署
- 状态监控
- 安全认证
- 备份和恢复

#### 安装部署为windows服务

```javascript
// 指定日志路径，添加install参数 
> mongod --dbpath=XXX --logpath=XXX --port=2222 --install 

// 启动服务 > net start MongoDB
```

#### 状态监控

###### 静态统计

*db.stats()*

```javascript
// 查看单个数据库状态 
> db.stats()
```

`stats`比较简单，可以参考[db.stats()](http://www.cnblogs.com/xuegang/archive/2011/10/13/2209965.html)一文

*db.serverStatus()*

```javascript
// 查看整个mongodb的状态 
// 进入admin集合 
> mongo 127.0.0.1:2222/admin 

// 查看状态 > db.serverStatus()
```

`serverStatus`的参数很多，可以参考[db.serverStatus()](http://www.cnblogs.com/xuegang/archive/2011/10/13/2210339.html)一文

###### 实时统计

```javascript
> mongostat --port 2222
```

#### 安全认证

*TODO*

有点复杂，偷懒了，参考[安全认证](http://docs.mongodb.org/manual/security/)

#### 备份和恢复

```javascript
// 备份test数据库到D:\mongodb\backup 
> mongodump --port 2222 -d test -c jobs -o D:\mongodb\backup 

-o 备份数据存储位置(目录)
-d 数据库名
-c 集合collection

> mongodump -d zhaopin
// 将招聘库的所有集合备份到当前目录的 *.bson 文件中（此文件用于回复置顶集合的数据）

> mongorestore -d zhaopin -c job dump/zhaopin/jobs.bson // 恢复job集合的数据
> mongorestore -d zhaopin dump/zhaopin // 恢复dump/zhaopin 数据库的全部数据
```



# MongoDB 建立集群的三种方式

​    今天主要来说说Mongodb的三种集群方式的搭建：Replica Set / Sharding / Master-Slaver。这里只说明最简单的集群搭建方式（生产环境），如果有多个节点可以此类推或者查看官方文档。OS是Ubuntu_x64系统，客户端用的是[Java](http://lib.csdn.net/base/javase)客户端。Mongodb版本是mongodb-[Linux](http://lib.csdn.net/base/linux)-x86_64-2.2.2.tgz



## **Replica Set**

​    中文翻译叫做副本集，不过我并不喜欢把英文翻译成中文，总是感觉怪怪的。其实简单来说就是集群当中包含了多份数据，保证主节点挂掉了，备节点能继续提供数据服务，提供的前提就是数据需要和主节点一致。如下图：

![img](G:\新知识\数据库\NoSQL\images\u=2789613013,962414579&fm=26&gp=0.jpg)

​    Mongodb(M)表示主节点，Mongodb(S)表示备节点，Mongodb(A)表示仲裁节点。主备节点存储数据，仲裁节点不存储数据。客户端同时连接主节点与备节点，不连接仲裁节点。

​    默认设置下，主节点提供所有增删查改服务，备节点不提供任何服务。但是可以通过设置使备节点提供查询服务，这样就可以减少主节点的压力，当客户端进行数据查询时，请求自动转到备节点上。这个设置叫做[Read Preference Modes](http://docs.mongodb.org/manual/applications/replication/#read-preference-modes)，同时Java客户端提供了简单的配置方式，可以不必直接对数据库进行操作。

​    仲裁节点是一种特殊的节点，它本身并不存储数据，主要的作用是决定哪一个备节点在主节点挂掉之后提升为主节点，所以客户端不需要连接此节点。这里虽然只有一个备节点，但是仍然需要一个仲裁节点来提升备节点级别。我开始也不相信必须要有仲裁节点，但是自己也试过没仲裁节点的话，主节点挂了备节点还是备节点，所以咱们还是需要它的。

介绍完了集群方案，那么现在就开始搭建了。



### 1.建立数据文件夹

一般情况下不会把数据目录建立在mongodb的解压目录下，不过这里方便起见，就建在mongodb解压目录下吧。

```shell
mkdir -p /mongodb/data/master 
mkdir -p /mongodb/data/slaver 
mkdir -p /mongodb/data/arbiter  
#三个目录分别对应主，备，仲裁节点
```

### 2.建立配置文件

由于配置比较多，所以我们将配置写到文件里。

```shell
#master.conf
dbpath=/data/db/master
logpath=/var/log/mongodb/master.log
pidfilepath=/var/run/mongodb.pid
directoryperdb=true
logappend=true
replSet=testrs
bind_ip=10.10.148.130
port=27017
oplogSize=100
fork=true
noprealloc=true
```

```shell
#slaver.conf
dbpath=/data/db/slaver
logpath=/var/log/mongodb/slaver.log
pidfilepath=/var/run/mongodb.pid
directoryperdb=true
logappend=true
replSet=testrs
bind_ip=10.10.148.131
port=27017
oplogSize=100
fork=true
noprealloc=true
```

```shell
#arbiter.conf
dbpath=/data/db/arbiter
logpath=/var/log/mongodb/arbiter.log
pidfilepath=/var/run/mongodb.pid
directoryperdb=true
logappend=true
replSet=testrs
bind_ip=10.10.148.132
port=27017
oplogSize=100
fork=true
noprealloc=true
```

进程号在/data/db/mongod.lock 里

### 参数解释：

- dbpath：数据存放目录

- logpath：日志存放路径

- pidfilepath：进程文件，方便停止mongodb

- directoryperdb：为每一个数据库按照数据库名建立文件夹存放

- logappend：以追加的方式记录日志

- replSet：replica set的名字

- bind_ip：mongodb所绑定的ip地址

- port：mongodb进程所使用的端口号，默认为27017

- oplogSize：mongodb操作日志文件的最大大小。单位为Mb，默认为硬盘剩余空间的5%

- fork：以后台方式运行进程

- noprealloc：不预先分配存储

### 3.启动mongodb

进入每个mongodb节点的bin目录下

```shell
./mongod -f master.conf
./mongod -f slaver.conf
./mongod -f arbiter.conf
```

注意配置文件的路径一定要保证正确，可以是相对路径也可以是绝对路径。

### 4.配置主，备，仲裁节点

可以通过客户端连接mongodb，也可以直接在三个节点中选择一个连接mongodb。

```shell
./mongo 10.10.148.130:27017   #ip和port是某个节点的地址
> use admin
> cfg={ 
	_id:"testrs", members:[ 
		{_id:0,host:'10.10.148.130:27017',priority:2},
		{_id:1,host:'10.10.148.131:27017',priority:1}, 
		{_id:2,host:'10.10.148.132:27017',arbiterOnly:true}
	] 
};
> rs.initiate(cfg)             #使配置生效
```

cfg是可以任意的名字，当然最好不要是mongodb的关键字，conf，config都可以。最外层的_id表示replica set的名字，members里包含的是所有节点的地址以及优先级。优先级最高的即成为主节点，即这里的10.10.148.130:27017。特别注意的是，对于仲裁节点，需要有个特别的配置——arbiterOnly:true。这个千万不能少了，不然主备模式就不能生效。

配置的生效时间根据不同的机器配置会有长有短，配置不错的话基本上十几秒内就能生效，有的配置需要一两分钟。如果生效了，执行rs.status()命令会看到如下信息：


```shell
{
        "set" : "testrs",
        "date" : ISODate("2013-01-05T02:44:43Z"),
        "myState" : 1,
        "members" : [
                {
                        "_id" : 0,
                        "name" : "10.10.148.130:27017",
                        "health" : 1,
                        "state" : 1,
                        "stateStr" : "PRIMARY",
                        "uptime" : 200,
                        "optime" : Timestamp(1357285565000, 1),
                        "optimeDate" : ISODate("2013-01-04T07:46:05Z"),
                        "self" : true
                },
                {
                        "_id" : 1,
                        "name" : "10.10.148.131:27017",
                        "health" : 1,
                        "state" : 2,
                        "stateStr" : "SECONDARY",
                        "uptime" : 200,
                        "optime" : Timestamp(1357285565000, 1),
                        "optimeDate" : ISODate("2013-01-04T07:46:05Z"),
                        "lastHeartbeat" : ISODate("2013-01-05T02:44:42Z"),
                        "pingMs" : 0
                },
                {
                        "_id" : 2,
                        "name" : "10.10.148.132:27017",
                        "health" : 1,
                        "state" : 7,
                        "stateStr" : "ARBITER",
                        "uptime" : 200,
                        "lastHeartbeat" : ISODate("2013-01-05T02:44:42Z"),
                        "pingMs" : 0
                }
        ],
        "ok" : 1
}
```

如果配置正在生效，其中会包含如下信息：

```shell
"stateStr" : "RECOVERING"
```

同时可以查看对应节点的日志，发现正在等待别的节点生效或者正在分配数据文件。
       现在基本上已经完成了集群的所有搭建工作。至于测试工作，可以留给大家自己试试。一个是往主节点插入数据，能从备节点查到之前插入的数据（查询备节点可能会遇到某个问题，可以自己去网上查查看）。二是停掉主节点，备节点能变成主节点提供服务。三是恢复主节点，备节点也能恢复其备的角色，而不是继续充当主的角色。二和三都可以通过rs.status()命令实时查看集群的变化。

## Sharding

和Replica Set类似，都需要一个仲裁节点，但是Sharding还需要配置节点和路由节点。就三种集群搭建方式来说，这种是最复杂的。部署图如下：

![img](G:\新知识\数据库\NoSQL\images\sharding.jpg)

### 1.启动数据节点

```shell
./mongod --fork --dbpath ../data/set1/ --logpath ../log/set1.log --replSet test #192.168.4.43
./mongod --fork --dbpath ../data/set2/ --logpath ../log/set2.log --replSet test #192.168.4.44
./mongod --fork --dbpath ../data/set3/ --logpath ../log/set3.log --replSet test #192.168.4.45 决策 不存储数据
```

### 2.启动配置节点

```shell
./mongod --configsvr --dbpath ../config/set1/ --port 20001 --fork --logpath ../log/conf1.log #192.168.4.30
./mongod --configsvr --dbpath ../config/set2/ --port 20002 --fork --logpath ../log/conf2.log #192.168.4.31
```

### 3.启动路由节点

```shell
./mongos --configdb 192.168.4.30:20001,192.168.4.31:20002 --port 27017 --fork --logpath ../log/root.log #192.168.4.29
```

这里我们没有用配置文件的方式启动，其中的参数意义大家应该都明白。一般来说一个数据节点对应一个配置节点，仲裁节点则不需要对应的配置节点。注意在启动路由节点时，要将配置节点地址写入到启动命令里。

### 4.配置Replica Set

这里可能会有点奇怪为什么Sharding会需要配置Replica Set。其实想想也能明白，多个节点的数据肯定是相关联的，如果不配一个Replica Set，怎么标识是同一个集群的呢。这也是人家mongodb的规定，咱们还是遵守吧。配置方式和之前所说的一样，定一个cfg，然后初始化配置。

```shell
./mongo 192.168.4.43:27017   #ip和port是某个节点的地址
>use admin
>cfg={ 
	_id:"testrs", 
	members:[ 
		{_id:0,host:'192.168.4.43:27017',priority:2}, 
		{_id:1,host:'192.168.4.44:27017',priority:1}, 
		{_id:2,host:'192.168.4.45:27017',arbiterOnly:true}
	] 
};
>rs.initiate(cfg)             #使配置生效
```

### 5.配置Sharding

```shell
./mongo 192.168.4.29:27017   #这里必须连接路由节点
>sh.addShard("test/192.168.4.43:27017") #test表示replica set的名字 当把主节点添加到shard以后，会自动找到set里的主，备，决策节点
>db.runCommand({enableSharding:"diameter_test"})    #diameter_test is database name
>db.runCommand( { shardCollection: "diameter_test.dcca_dccr_test",key:{"__avpSessionId":1}}) 
```

第一个命令很容易理解，第二个命令是对需要进行Sharding的数据库进行配置，第三个命令是对需要进行Sharding的Collection进行配置，这里的dcca_dccr_test即为Collection的名字。另外还有个key，这个是比较关键的东西，对于查询效率会有很大的影响，具体可以查看 Shard Key Overview

到这里Sharding也已经搭建完成了，以上只是最简单的搭建方式，其中某些配置仍然使用的是默认配置。如果设置不当，会导致效率异常低下，所以建议大家多看看官方文档再进行默认配置的修改。


## Master-Slaver

这个是最简答的集群搭建，不过准确说也不能算是集群，只能说是主备。并且官方已经不推荐这种方式，所以在这里只是简单的介绍下吧，搭建方式也相对简单。

```shell
./mongod --master --dbpath /data/masterdb/      #主节点
./mongod --slave --source masterip:masterport --dbpath /data/slavedb/     备节点
```

基本上只要在主节点和备节点上分别执行这两条命令，Master-Slaver就算搭建完成了。我没有试过主节点挂掉后备节点是否能变成主节点，不过既然已经不推荐了，大家就没必要去使用了。

以上三种集群搭建方式首选Replica Set，只有真的是大数据，Sharding才能显现威力，毕竟备节点同步数据是需要时间的。Sharding可以将多片数据集中到路由节点上进行一些对比，然后将数据返回给客户端，但是效率还是比较低的说。

我自己有测试过，不过具体的机器配置已经不记得了。Replica Set的ips在数据达到1400w条时基本能达到1000左右，而Sharding在300w时已经下降到500ips了，两者的单位数据大小大概是10kb。大家在应用的时候还是多多做下性能测试，毕竟不像Redis有benchmark。

Mongodb现在用的还是比较多的，但是个人觉得配置太多了。。。。我看官网都看了好多天，才把集群搭建的配置和注意要点弄明白。而且用过的人应该知道mongodb吃内存的问题，解决办法只能通过ulimit来控制内存使用量，但是如果控制不好的话，mongodb会挂掉。。。