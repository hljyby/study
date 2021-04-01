# [利用yum下载软件包的三种方法](https://www.cnblogs.com/djoker/p/6380680.html)

## 方法一:downloadonly插件

### 1.安装插件

```
yum -y install yum-download
```



### 2.下载httpd软件包到当前文件夹内

```
yum -y install httpd -downloadonly -downloaddir=./
```

## 方法二:yum-utils中的yumdownloader

### 1.安装yum-utils

```
yum -y install yum-utils
```

### 2.使用yumdownloader下载软件包httpd

```
yumdownloader httpd
```

## 方法三:利用yum的缓存功能

```shell
# 默认情况下,yum在安装软件包后会自动清理软件包,修改配置,使yum不再清理软件包
vim /etc/yum.conf中修改keepcache = 0 改为keepcache = 1
/etc/init.d/yum-updatesd restart
yum -y install httpd
# 这时软件包已经安装下载,目录为/var/cache/yum
```

