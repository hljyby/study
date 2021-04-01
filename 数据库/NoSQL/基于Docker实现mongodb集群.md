# 基于Docker方式搭建MongoDB集群

# 1.简介

MongoDB目前是最流行的非关系型数据库，他的数据存储并不是key-value形式，而是BSON格式。具体用法，可以参考菜鸟教程《[MongDB教程](https://links.jianshu.com/go?to=https%3A%2F%2Fwww.runoob.com%2Fmongodb%2Fmongodb-tutorial.html)》,这里就不做详细描述

在这里我们主要是讲述基于Docker的Mongo集群搭建。

在早期的项目开发中，一般都是采用单个数据库去存储数据，这是一种很危险的举动。一旦数据库挂了，也就意味着数据库里面存储的所有数据都挂了。

基于这个原因，所以一个优秀的项目就应该采用Mongo的集群环境。

MongoDB集群搭建方式一共有三种：

- Master-Slave

  主从模式，这种模式没有什么意义，官方也不推荐使用这种方式搭建集群。

- Replica-Set

  副本集方式，集群中包含多份数据，假如主节点挂了，备份节点就会变成主节点，继续提供数据服务。一旦主节点修复，那么备份节点就不再充当主节点的角色，把提供数据的服务交给主节点。这样就保证了MongoDB的高可用性。

  不过这种方式需要一个仲裁节点，这个节点本身不存储任何数据，其主要作用就是当主节点挂掉以后，把那个备份节点提升为一个主节点。

  这次讲述，我们就着重讲述这种方式

- Sharding

  分片方式，与副本集方式类似，都需要仲裁节点，除了这个以外还需要配置节点和路由。这种方式相对复杂，这种方式不是今天重点，就不着重介绍了。

# 2.副本集方式

- 简介

  集群中包含多份数据，假如主节点挂了，备份节点就会变成主节点，继续提供数据服务。前提是备份节点要和主节点保持一致。

一旦主节点修复，那么备份节点就不再充当主节点的角色，把提供数据的服务交给主节点。这样就保证了MongoDB的高可用性。

不过这种方式需要一个仲裁节点，这个节点本身不存储任何数据，其主要作用就是当主节点挂掉以后，把那个备份节点提升为一个主节点。

原理图如下：

![img](G:\新知识\数据库\NoSQL\images\webp)

如上图所示：

Master:代表主节点，主节点提供所有数据的CRUD服务

Backup:代表从节点，从节点不提供任何服务

Arbitration:代表仲裁节点，仲裁节点不存储任何数据，客户点可以同时连接主节点和备份节点，但是不连接仲裁节点。

当然我们在进行数据操作的时候，我们可以将增删改请求交给主节点，查询交给备份节点，这样减少主节点压力。

# 3.搭建方式

- 原理

  这次我们就搭建一个主，一个备份，一个仲裁，原理图如下：

  ![img](G:\新知识\数据库\NoSQL\images\webp02)

  

  虽然简单，但对于简单的项目来说已经足够使用了。

- 准备工作

  - 准备一台虚拟机

    镜像：ubuntu,当然你也可以选择换其他的镜像

    ip地址：192.168.80.128(安装好后，系统的ip地址)

  - 安装docker

    具体参考《[docker系列教程](https://www.jianshu.com/p/ecd272f82325)》

- 拉取Mongo镜像

  

  ```shell
  docker pull mongo
  ```

  ![img](G:\新知识\数据库\NoSQL\images\webp03)

  

- 创建容器

  

  ```shell
  docker run -d --name master_mongo -p 27016:27017 mongo --replSet "mongo_clus"
  
  docker run -d --name backup_mongo -p 27018:27017 mongo  --replSet "mongo_clus"
  
  docker run -d --name arbi_mongo -p 27019:27017 mongo  --replSet "mongo_clus"
  ```

  解释：`--replSet` 设置副本集名称，也就是设置集群名称，必须要设置，否则没法构建集群

  ![img](G:\新知识\数据库\NoSQL\images\webp04)

  

- 通过客户端连接

  通过客户端连接，确保服务端容器创建成功

  客户端地址：[https://nosqlbooster.com/downloads](https://links.jianshu.com/go?to=https%3A%2F%2Fnosqlbooster.com%2Fdownloads)

  下载安装即可。

  ![img](G:\新知识\数据库\NoSQL\images\webp05)

  三个全部连接成功 现在还不行得配置之后才能连接成功

# 4.配置

- 进入`Master_Mongo`容器中

  

  ```shell
  docker exec  -it master_mongo /bin/bash
  ```

  ![img](G:\新知识\数据库\NoSQL\images\webp06)

  登录Mongo

  

  ```shell
  mongo --host 192.168.80.128 --port 27017
  ```

  ![img](G:\新知识\数据库\NoSQL\images\webp07)

  创建集群

  

  ```sql
  cfg={
    "_id":"mongo_clus",
    members:[{
        _id:0,
        host:"192.168.0.200:27016",
        priority:2
    },{
        _id:1,
        host:"192.168.0.200:27018",
        priority:1
    },{
        _id:2,
        host:"192.168.0.200:27019",
        arbiterOnly:true
    }]
  }
  rs.initiate(cfg)
  ```

  ![img](G:\新知识\数据库\NoSQL\images\webp08)

  

  配置信息解释如下：

  `cfg` 为任意名字，可以随意写

  `_id` 最外面的，其值为副本集名字，必须与创建容器时指定的副本集名字保持一致

  `members` 代表这个集群里面的节点

  `_id`里面的 节点编号，必须唯一

  `host` 节点的地址

  `priority` 优先级，优先级最高的为主节点，其他为备份节点

  `arbiterOnly` 如果想把某一个节点声明为仲裁节点，就必须配置该属性，将值设置为 true

- 查看集群状态

  

  ```sql
  rs.status()
  ```

  ![img](G:\新知识\数据库\NoSQL\images\webp09)

  

  整个集群状态信息如下：

  

  ```json
  {
          "set" : "mongo_clus",
          "date" : ISODate("2020-07-09T08:43:19.469Z"),
          "myState" : 1,
          "term" : NumberLong(1),
          "syncingTo" : "",
          "syncSourceHost" : "",
          "syncSourceId" : -1,
          "heartbeatIntervalMillis" : NumberLong(2000),
          "majorityVoteCount" : 2,
          "writeMajorityCount" : 2,
          "optimes" : {
                  "lastCommittedOpTime" : {
                          "ts" : Timestamp(1594284193, 1),
                          "t" : NumberLong(1)
                  },
                  "lastCommittedWallTime" : ISODate("2020-07-09T08:43:13.164Z"),
                  "readConcernMajorityOpTime" : {
                          "ts" : Timestamp(1594284193, 1),
                          "t" : NumberLong(1)
                  },
                  "readConcernMajorityWallTime" : ISODate("2020-07-09T08:43:13.164Z"),
                  "appliedOpTime" : {
                          "ts" : Timestamp(1594284193, 1),
                          "t" : NumberLong(1)
                  },
                  "durableOpTime" : {
                          "ts" : Timestamp(1594284193, 1),
                          "t" : NumberLong(1)
                  },
                  "lastAppliedWallTime" : ISODate("2020-07-09T08:43:13.164Z"),
                  "lastDurableWallTime" : ISODate("2020-07-09T08:43:13.164Z")
          },
          "lastStableRecoveryTimestamp" : Timestamp(1594284173, 1),
          "lastStableCheckpointTimestamp" : Timestamp(1594284173, 1),
          "electionCandidateMetrics" : {
                  "lastElectionReason" : "electionTimeout",
                  "lastElectionDate" : ISODate("2020-07-09T08:38:52.977Z"),
                  "electionTerm" : NumberLong(1),
                  "lastCommittedOpTimeAtElection" : {
                          "ts" : Timestamp(0, 0),
                          "t" : NumberLong(-1)
                  },
                  "lastSeenOpTimeAtElection" : {
                          "ts" : Timestamp(1594283921, 1),
                          "t" : NumberLong(-1)
                  },
                  "numVotesNeeded" : 2,
                  "priorityAtElection" : 2,
                  "electionTimeoutMillis" : NumberLong(10000),
                  "numCatchUpOps" : NumberLong(0),
                  "newTermStartDate" : ISODate("2020-07-09T08:38:53.035Z"),
                  "wMajorityWriteAvailabilityDate" : ISODate("2020-07-09T08:38:53.594Z")
          },
          "members" : [
                  {
                          "_id" : 0,
                          "name" : "192.168.80.128:27017",
                          "health" : 1,
                          "state" : 1,
                          "stateStr" : "PRIMARY",
                          "uptime" : 386,
                          "optime" : {
                                  "ts" : Timestamp(1594284193, 1),
                                  "t" : NumberLong(1)
                          },
                          "optimeDate" : ISODate("2020-07-09T08:43:13Z"),
                          "syncingTo" : "",
                          "syncSourceHost" : "",
                          "syncSourceId" : -1,
                          "infoMessage" : "",
                          "electionTime" : Timestamp(1594283932, 1),
                          "electionDate" : ISODate("2020-07-09T08:38:52Z"),
                          "configVersion" : 1,
                          "self" : true,
                          "lastHeartbeatMessage" : ""
                  },
                  {
                          "_id" : 1,
                          "name" : "192.168.80.128:27018",
                          "health" : 1,
                          "state" : 2,
                          "stateStr" : "SECONDARY",
                          "uptime" : 277,
                          "optime" : {
                                  "ts" : Timestamp(1594284193, 1),
                                  "t" : NumberLong(1)
                          },
                          "optimeDurable" : {
                                  "ts" : Timestamp(1594284193, 1),
                                  "t" : NumberLong(1)
                          },
                          "optimeDate" : ISODate("2020-07-09T08:43:13Z"),
                          "optimeDurableDate" : ISODate("2020-07-09T08:43:13Z"),
                          "lastHeartbeat" : ISODate("2020-07-09T08:43:19.126Z"),
                          "lastHeartbeatRecv" : ISODate("2020-07-09T08:43:17.663Z"),
                          "pingMs" : NumberLong(0),
                          "lastHeartbeatMessage" : "",
                          "syncingTo" : "192.168.80.128:27017",
                          "syncSourceHost" : "192.168.80.128:27017",
                          "syncSourceId" : 0,
                          "infoMessage" : "",
                          "configVersion" : 1
                  },
                  {
                          "_id" : 2,
                          "name" : "192.168.80.128:27019",
                          "health" : 1,
                          "state" : 7,
                          "stateStr" : "ARBITER",
                          "uptime" : 277,
                          "lastHeartbeat" : ISODate("2020-07-09T08:43:19.126Z"),
                          "lastHeartbeatRecv" : ISODate("2020-07-09T08:43:18.219Z"),
                          "pingMs" : NumberLong(0),
                          "lastHeartbeatMessage" : "",
                          "syncingTo" : "",
                          "syncSourceHost" : "",
                          "syncSourceId" : -1,
                          "infoMessage" : "",
                          "configVersion" : 1
                  }
          ],
          "ok" : 1,
          "$clusterTime" : {
                  "clusterTime" : Timestamp(1594284193, 1),
                  "signature" : {
                          "hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
                          "keyId" : NumberLong(0)
                  }
          },
          "operationTime" : Timestamp(1594284193, 1)
  }
  ```

  这样我们就搭建成功了一个集群。接下来我们就是测试测试

# 5.测试

- 使用客户端连接主节点

  ![img](G:\新知识\数据库\NoSQL\images\webp10)

  

  我们明显可以看到集群配置

  PAIRMAY代表主节点

  ARBITER 代表仲裁节点

  其他代表备份节点

接下来我们在主节点创建数据库和集合，并插入文档



```css
use studies
db.createCollection("person", { capped : true, size : 50 * 1024 * 1024, max : 100 * 1000 } )

db.person.insertOne({name:"lisi",age:15})
```

![img](G:\新知识\数据库\NoSQL\images\webp11)



- 使用客户端连接备份节点

  ![img](G:\新知识\数据库\NoSQL\images\webp12)

  

  备份节点上数据也是存在的

  ![img](G:\新知识\数据库\NoSQL\images\webp13)

  

- 测试主节点挂掉，备份节点自动转换成主节点

  关闭主节点容器

  

  ```sql
  docker stop master_mongo
  ```

  ![img](G:\新知识\数据库\NoSQL\images\webp14)

  

  再次去连接Mongo

  ![img](G:\新知识\数据库\NoSQL\images\webp15)

  

  发现`27018`自动转换成主节点，而原来的主节点已经挂掉

  接下来我们启动一下刚刚关闭的主节点

  

  ```sql
  docker start master_mongo
  ```

  ![img](G:\新知识\数据库\NoSQL\images\webp16)

  

  刷新客户端连接

  ![img](G:\新知识\数据库\NoSQL\images\webp17)

  

  主节点恢复，先前转换成主节点的备份节点，已经恢复成了备份节点。

  到这我们就完成来了MongoDB的集群搭建方式的副本集搭建。