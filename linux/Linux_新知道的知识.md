# 为什么配置文件后缀都有d

```js
 // 守护进程，也就是通常说的Daemon进程
 // 一般配置文件后面都加d 代表守护进程
```

# 查看是否加入开机启动systemctl list-unit-files

```shell
systemctl list-unit-files |grep xxx
```

