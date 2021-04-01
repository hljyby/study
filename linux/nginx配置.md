#  Nginx 文件配置解构

```python
main 全局配置
events{
	# 工作模式 ，连接配置
}
http{
	# http配置
	upstream xxx{
		# 负载均衡
	}
	server {
		# 主机设置
		location xxx {
			# url 匹配
		}
	}
}
```

## events

```python
# 指定工作模式以及连接上限

events{
	use epoll;
	worker_connections 1024;
	
}
use 指定Nginx 工作模式
	epoll 高效工作模式， linux
	kqueue 高效工作模式，bsd
	poll 标准模式
	select 标准模式
	
work_connections 定义nginx每个进程的最大连接数
	正向代理     连接数*进程数	
	反向代理     连接数*进程数/4
	linux 系统限制最多能同时打开65535个文件，默认上线就是65535，可解除 ulimit -n 65535
```

## http

```python
# 最核心的模块，主要负责http服务器相关的配置，包含server ，upstream子模块
include mime.types;# 设置文件的mime类型
include xxxconfig; # 包含其他配置文件，分开规划解耦
default_type xxx; # 设置默认类型为二进制流，文件类型未知是就会默认使用
log_format # 设置日志格式
sendfile # 设置搞笑文件传输模式
keepalive_timeout # 设置客户端连接活跃超时
gzip # gzip压缩
```

## server

```python
# 用来指定虚拟主机
listen 80; # 制定虚拟主机监听的端口
server_name localhost; #指丁ip地址和域名，多个域名使用空格隔开
charset utf-8; # 指定网页的默认编码模式
error_page 500 502 /50x.html # 指定错误页面
access_log xxx main # 指定虚拟主机的访问日志存放路径
error_log xxx mian # 指定虚拟主机的错误日志存放路径
root xxx # 制定这个虚拟主机的根目录
index xxx # 制定默认首页
```

## location

```python
# 核心中的核心 ，以后主要的配置都在这了
# 主要功能：定位url 解析url,支持正则匹配， 还能支持条件，实现动态分离
#语法
	lcoal [modifier] uri{
		...
	}
modifier 修饰符
	= 	# 使用精确匹配，并且终止搜索
	~ 	# 区分大小洗的正则表达式
	~* 	# 不区分大小写的正则表达式
	^~ 	# 最佳配置，不是正则匹配，通常用来匹配目录

# 常用指令
	 alias 别名，定义location的其他名字，在文件系统中能够找到，如果location制定了正则表达式，alias将会引用正则表达式中的捕获，alias 将会代替location中匹配的部分，没有匹配的部分将会在文件系统中搜索。
		
```

## upstream

```python
# 负载均衡模块 ，通过简单的调度算法来实现客户ip到后吨服务器的负载均衡
写法
	upstream myproject{
		ip_hash;
		server 127.0.0.1:8100;
         server 127.0.0.1:8200 down;
		server 127.0.0.1:8300 weight=3;
		server 127.0.0.1:8400 backup;
		fair;
	}
负载均衡算法
	weight 	负载权重
	down 	当前服务不参与负载均衡
	backup	其他机器全down掉后满载使用此服务
	ip_hash	那每个请求的hash结果分配
	fair	庵后端详用的时间来分配（第三方的）
```

## 反向代理

```python
proxy_pass URL	# 反向代理转发地址，默认不转发header,需要转发header则设置 proxy_set_header HOST $host
proxy_method POST	# 装发的方法名
peoxy_hide_header Cache-Control;	# 指定头部不被转发
peoxy_pass_header Cache-Control;	# 设置哪些头部转发
peoxy_pass_request_header on;	# 设置转发http请求头
peoxy_pass_request_body on;	# 设置转发请求提

```

