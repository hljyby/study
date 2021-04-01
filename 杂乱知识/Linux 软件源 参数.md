# ubuntu /etc/apt/sources.list软件源格式说明



每次修改源都是网上复制下来，粘贴进/etc/apt/sources.list里面，里面每一个代表说明含义，参考别人的文章并再次记录一下，以待后续记忆学习。

`/etc/apt/sources.list` 文件是包管理工具 `apt` 所用的记录软件包仓库位置的配置文件，同样的还有位于 `/etc/apt/sources.list.d/*.list` 的各文件。

阿里源格式如下：

```
deb http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiversedeb http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiversedeb http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiversedeb http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiversedeb http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiversedeb-src http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiversedeb-src http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiversedeb-src http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiversedeb-src http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiversedeb-src http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse
```

每一行分为四部分：

```
档案类型 镜像url                           版本代号 软件包分类 
deb http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse 
```

### 档案类型 (Archive type)

```Delphi
deb:档案类型为二进制预编译软件包，一般我们所用的档案类型。deb-src:软件包的源代码。
```

### 地址url

ftp镜像的url，以我的阿里镜像为例，在浏览器打开出现以如下内容：

![img](https://img-blog.csdnimg.cn/20190506164335977.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3VuaWNvcm5fbWl0bmljaw==,size_16,color_FFFFFF,t_70)

每一个源目录下都应该至少包含dists和pool两个目录，否则就是无效的源

/dists/ 目录包含"发行版"(distributions), 此处是获得 Debian 发布版本(releases)和已发布版本(pre-releases)的软件包的正规途径. 有些旧软件包及 packages.gz 文件仍在里面.

/pool/ 目录为软件包的物理地址. 软件包均放进一个巨大的 "池子(pool)", 按照源码包名称分类存放. 为了方便管理, pool 目录下按属性再分类("main", "contrib" 和 "non-free"), 分类下面再按源码包名称的首字母归档. 这些目录包含的文件有: 运行于各种系统架构的二进制软件包, 生成这些二进制软件包的源码包.你可以执行命令 apt-cache showsrc mypackagename, 查看 'Directory:' 行获知每个软件包的存放位置. 例如: apache 软件包存放在 pool/main/a/apache/ 目录中.另外, 由于lib*软件包数量巨大, 它们以特殊的方式归档: 例如, libpaper 软件包存放在 pool/main/libp/libpaper/.

**还有一些目录:**

*/tools/*:用于创建启动盘, 磁盘分区, 压缩/解压文件, 启动 Linux 的 DOS 下的小工.

*/doc/*:基本的 Debian 文档, 如 FAQ, 错误报告系统指导等..

*/indices/*:维护人员文件和重载文件.

*/project/*:大部分为开发人员的资源, 如:*project/experimental/*，本目录包含了处于开发中的软件包和工具, 它们均处于 alpha 测试阶段. 用户不应使用这些软件, 因为即使是经验丰富的用户也会被搞得一团糟.）

###  版本号

发行版有两种分类方法，一类是发行版的具体代号，如Ubuntu18.04是bionic 16.04是Xenial，`trusty`, `precise` 等；还有一类则是发行版的发行类型，如`oldstable`, `stable`, `testing` 和 `unstable`。

另外，在发行版后还可能有进一步的指定，如 `xenial-updates`, `trusty-security`, `stable-backports` 等

### 软件包分类 

main/restricted/multiverse/universe是ubuntu对软件的分类。

```
ubuntu:main:官方支持的自由软件。
restricted:官方支持的非完全自由的软件。
universe:社区维护的自由软件。
multiverse:非自由软件。
```