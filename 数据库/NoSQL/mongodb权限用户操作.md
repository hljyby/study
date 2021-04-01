## 1. 创建用户

- 启动mongo shell
   我们先创建个管理员账号（该账号可以对所有数据库进行用户管理）



```python
C:\Users\xxx>mongo
> use admin
switched to db admin
> db.createUser(
... {
...   user: "admin",
...   pwd: "123456",
...   roles: [ { role: "userAdminAnyDatabase", db: "admin"} ]
... }
... )
Successfully added user: {
        "user" : "admin",
        "roles" : [
                {
                        "role" : "userAdminAnyDatabase",
                        "db" : "admin"
                }
        ]
}
>
```

## 2. 开启权限认证

如果是命令模式启动的话，就在原来的启动参数上，在加上 --auth 即可



```swift
c:\> mongod --auth --dbpath "D:\Program Files\MongoDB\Server\4.0\data"
```

如果是windows service方式运行的话，打开 mongo配置文件mongod.cfg, 在security项下，将authorization设置为enabled, 默认是disabled



```undefined
security:
  authorization: enabled
```

然后重启service就可以了

## 3. 以认证的方式连接mongo

- 连接的时候认证



```php
C:\Users\xxx>mongo -port 27017 -u "admin"  -p "123456" --authenticationDatabas
e "admin"
MongoDB shell version v4.0.1
connecting to: mongodb://127.0.0.1:27017/
MongoDB server version: 4.0.1
> use admin
switched to db admin
> show users;
{
        "_id" : "admin.admin",
        "user" : "admin",
        "db" : "admin",
        "roles" : [
                {
                        "role" : "userAdminAnyDatabase",
                        "db" : "admin"
                }
        ],
        "mechanisms" : [
                "SCRAM-SHA-1",
                "SCRAM-SHA-256"
        ]
}
>
```

- 连接好了之后，再认证



```dart
C:\Users\xxx>mongo
MongoDB shell version v4.0.1
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 4.0.1
> use admin
switched to db admin
> db.auth("admin", "123456")
1
> show users;
{
        "_id" : "admin.admin",
        "user" : "admin",
        "db" : "admin",
        "roles" : [
                {
                        "role" : "userAdminAnyDatabase",
                        "db" : "admin"
                }
        ],
        "mechanisms" : [
                "SCRAM-SHA-1",
                "SCRAM-SHA-256"
        ]
}
>
```

## 4. 根据需要创建其他的账号

- 比如我有一个test库，我需要读写权限，然后有个game_report库，我需要只读权限, 然后我们就可以如下创建一个账号:



```python
> use admin
switched to db admin
> db.createUser(
... {
...  user : "my_tester",
...  pwd : "123456",
...  roles: [ { role : "readWrite", db : "test" } ,
...           { role : "read", db : "game_report" } ]
... }
... )
Successfully added user: {
        "user" : "my_tester",
        "roles" : [
                {
                        "role" : "readWrite",
                        "db" : "test"
                },
                {
                        "role" : "read",
                        "db" : "game_report"
                }
        ]
}
```

- 以认证方式连接test库



```rust
C:\Users\xxx>mongo
MongoDB shell version v4.0.1
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 4.0.1
> use admin
switched to db admin
> db.auth("my_tester", "123456")
1
> use test
switched to db test
> db.foo.insert( { x : 1, y : 2 } )
WriteResult({ "nInserted" : 1 })
> db.foo.find()
{ "_id" : ObjectId("5b67fc008bd89ebd4abc54aa"), "x" : 1, "y" : 2 }
>
```

## 5. 权限说明（基于角色的权限控制）

#### 5.1 内置角色

###### 数据库用户角色

- read: 只读数据权限
- readWrite:读写数据权限

###### 数据库管理角色

- dbAdmin: 在当前db中执行管理操作的权限
- dbOwner: 在当前db中执行任意操作
- userADmin: 在当前db中管理user的权限

###### 备份和还原角色

- backup
- restore

###### 夸库角色

- readAnyDatabase: 在所有数据库上都有读取数据的权限
- readWriteAnyDatabase: 在所有数据库上都有读写数据的权限
- userAdminAnyDatabase: 在所有数据库上都有管理user的权限
- dbAdminAnyDatabase: 管理所有数据库的权限

###### 集群管理

- clusterAdmin: 管理机器的最高权限
- clusterManager: 管理和监控集群的权限
- clusterMonitor: 监控集群的权限
- hostManager: 管理Server

##### 超级权限

- root: 超级用户

#### 5.2 自定义角色

内置角色只能控制User在DB级别上执行的操作，管理员可以创建自定义角色，控制用户在集合级别（Collection-Level）上执行的操作，即，控制User在当前DB的特定集合上执行特定的操作

## 6. 参考连接

- https://docs.mongodb.com/manual/tutorial/enable-authentication/
- http://www.runoob.com/mongodb/mongodb-window-install.html
- https://www.cnblogs.com/zxtceq/p/7690977.html

#  给mongoDb设置权限

## 1、创建角色

 连接数据库，在admin集合中新增一个用户



```css
db.createUser({
  user: 'admin',
  pwd: 'admin',
  roles: [{role: 'root', db: 'admin'}]
})
```

user是用户名，pwd是密码， roles是角色。
 role: 'root'表示超级管理员，
 db表示可以操作的数据库

2、修改配置文件：开启权限验证
 找到安装目录
 找到配置文件 mongodb.cfg
 增加一句



```bash
#security:
security:
  authorization: enabled
```

3、重启mongoDb服务
 我的电脑 >> 管理 >> 服务和应用程序 >> 服务 >> 找到mongoDb(键盘直接输入mong就能直接指向它)
 右击重启服务，等待重启完成即可

4、重新连接mongoDb
 此时连接输入用户名和密码



```undefined
mongo -u username -p password
```

远程数据库连接



```bash
mongo 192.168.1.1:12702/test -u username -p password
```

# MongoDB 内置角色

#### (1).数据库用户角色

针对每一个数据库进行控制。
 **read **:提供了读取所有非系统集合，以及系统集合中的system.indexes, system.js, system.namespaces **readWrite**: 包含了所有read权限，以及修改所有非系统集合的和系统集合中的system.js的权限.

#### (2).数据库管理角色

每一个数据库包含了下面的数据库管理角色。
 **dbOwner**：该数据库的所有者，具有该数据库的全部权限。
 **dbAdmin**：一些数据库对象的管理操作，但是没有数据库的读写权限。（参考：[http://docs.mongodb.org/manual/reference/built-in-roles/#dbAdmin](https://links.jianshu.com/go?to=http%3A%2F%2Fdocs.mongodb.org%2Fmanual%2Freference%2Fbuilt-in-roles%2F%23dbAdmin)）
 **userAdmin**：为当前用户创建、修改用户和角色。拥有userAdmin权限的用户可以将该数据库的任意权限赋予任意的用户。

#### (3).集群管理权限

admin数据库包含了下面的角色，用户管理整个系统，而非单个数据库。这些权限包含了复制集和共享集群的管理函数。
 **clusterAdmin**：提供了最大的集群管理功能。相当于clusterManager, clusterMonitor, and hostManager和dropDatabase的权限组合。
 **clusterManager**：提供了集群和复制集管理和监控操作。拥有该权限的用户可以操作config和local数据库（即分片和复制功能）
 **clusterMonitor**：仅仅监控集群和复制集。
 **hostManager**：提供了监控和管理服务器的权限，包括shutdown节点，logrotate, repairDatabase等。
 备份恢复权限：admin数据库中包含了备份恢复数据的角色。包括backup、restore等等。

#### (4).所有数据库角色

admin数据库提供了一个mongod实例中所有数据库的权限角色：
 **readAnyDatabase**：具有read每一个数据库权限。但是不包括应用到集群中的数据库。
 **readWriteAnyDatabase**：具有readWrite每一个数据库权限。但是不包括应用到集群中的数据库。
 **userAdminAnyDatabase**：具有userAdmin每一个数据库权限，但是不包括应用到集群中的数据库。
 **dbAdminAnyDatabase**：提供了dbAdmin每一个数据库权限，但是不包括应用到集群中的数据库。

#### (5). 超级管理员权限

root: dbadmin到admin数据库、useradmin到admin数据库以及UserAdminAnyDatabase。但它不具有备份恢复、直接操作system.*集合的权限，但是拥有root权限的超级用户可以自己给自己赋予这些权限。

#### (6). 备份恢复角色：backup、restore；

#### (7). 内部角色：__system