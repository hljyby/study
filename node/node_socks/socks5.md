# 使用nodejs实现socks5协议

> 本文出处[shenyifengtk.github.io/](https://shenyifengtk.github.io/2019/07/14/Nodejs实现socks5协议/) 如有转载，请说明出处

## socks5 介绍

socks5s是一种网络传输协议，主要用于客户端与外网服务器之间通讯的中间传递。当防火墙后的客户端要访问外部的服务器时，就跟SOCKS代理服务器连接。这个代理服务器控制客户端访问外网的资格，允许的话，就将客户端的请求发往外部的服务器。

![参考图](G:\新知识\node\images\1)

根据OSI模型，SOCKS是会话层的协议，位于表示层与传输层之间，也就是说socks是在TCP 之上的协议。



### 和HTTP代理相比

HTTP代理只能代理http请求，像TCP、HTTPS这些协议显得很无力，有一定的局限性。 SOCKS工作在比HTTP代理更低的层次：SOCKS使用握手协议来通知代理软件其客户端试图进行的连接SOCKS，然后尽可能透明地进行操作，而常规代理可能会解释和>重写报头（例如，使用另一种底层协议，例如FTP；然而，HTTP代理只是将HTTP请求转发到所需的HTTP服务器）。虽然HTTP代理有不同的使用模式，CONNECT方法允 许转发TCP连接；然而，SOCKS代理还可以转发UDP流量和反向代理，而HTTP代理不能。HTTP代理通常更了解HTTP协议，执行更高层次的过滤（虽然通常只用于GET和 POST方法，而不用于CONNECT方法）。

> [官方协议RFC](https://www.ietf.org/rfc/rfc1928.txt)

### 选择认证方法

大体说下socks连接过程，首先客户端发送一个数据包到socks代理

| Var  | NMETHODS | METHODS |
| :--: | :------: | :-----: |
|  1   |    1     |  0-255  |

表格里面的单位表示位数

- **Var** 表示是SOCK版本，应该是５;

- **NMETHODS** 表示 **METHODS**部分的长度

- METHODS

   

  表示支持客户端支持的认证方式列表，每个方法占1字节。当前的定义是

  - 0x00 不需要认证
  - 0x01 GSSAPI
  - 0x02 用户名、密码认证
  - 0x03 - 0x7F由IANA分配（保留）
  - 0x80 - 0xFE为私人方法保留
  - 0xFF 无可接受的方法

服务器会响应给客户端

| VER  | METHOD |
| :--: | :----: |
|  1   |   1    |

- **Var** 表示是SOCK版本，应该是５;
- **METHOD**是服务端选中方法，这个的值为上面**METHODS** 列表中一个。如果客户端支持0x00，0x01，0x02，这三个方法。服务器只会选中一个认证方法返回给客户端，如果返回0xFF表示没有一个认证方法被选中，客户端需要关闭连接。 我们先用一个简单Nodejs在实现sock连接握手.查看客户端发送数据报

```
const net = require('net');
let server = net.createServer(sock =>{
sock.once('data', (data)=>{
console.log(data);
});
});
server.listen(8888,'localhost');
复制代码
```

使用curl工具连接nodejs

```
curl -x socks5://localhost:8888 https://www.baidu.com
复制代码
```

console输出

> <Buffer 05 02 00 01>

### 使用账号密码认证

当服务器选择0x02 账号密码方式认证后，客户端开始发送账号 、密码，数据包格式如下: (以字节为单位)

| VER  | ULEN |  UNAME   | PLEN |  PASSWD  |
| :--: | :--: | :------: | :--: | :------: |
|  1   |  1   | 1 to 255 |  1   | 1 to 255 |

- VER是SOCKS版本
- ULEN 用户名长度
- UNAME 账号string
- PLEN 密码长度
- PASSWD 密码string

可以看出账号密码都是**明文传输**，非常地不安全。 服务器端校验完成后，会响应以下数据():

| VER  | STATUS |
| :--: | :----: |
|  1   |   1    |

- STATUS 0x00 表示成功，0x01 表示失败

### 封装请求

认证结束后客户端就可以发送请求信息。客户端开始封装请求信息 SOCKS5请求格式（以字节为单位）：

| VER  | CMD  | RSV  | ATYP | DST.ADDR | DST.PORT |
| :--: | :--: | :--: | :--: | :------: | :------: |
|  1   |  1   | 0x00 |  1   |   动态   |    2     |

- VER是SOCKS版本，这里应该是0x05；

- CMD是SOCK的命令码

  - 0x01表示CONNECT请求

    - CONNECT请求可以开启一个客户端与所请求资源之间的双向沟通的通道。它可以用来创建隧道（tunnel）。例如，**`CONNECT` **可以用来访问采用了 [SSL](https://developer.mozilla.org/en-US/docs/Glossary/SSL) ([HTTPS](https://developer.mozilla.org/en-US/docs/Glossary/HTTPS)) 协议的站点。客户端要求代理服务器将 TCP 连接作为通往目的主机隧道。之后该服务器会代替客户端与目的主机建立连接。连接建立好之后，代理服务器会面向客户端发送或接收 TCP 消息流。

  - 0x02表示BIND请求

    > Bind方法使用于目标主机需要主动连接客户机的情况(ftp协议)

    当服务端接收到的数据包中CMD为X'02'时，服务器使用Bind方法进行代理。使用Bind方法代理时服务端需要回复客户端至多两次数据包。

    服务端使用TCP协议连接对应的(DST.ADDR, DST.PORT)，如果失败则返回失败状态的数据包并且关闭此次会话。如果成功，则监听(BND.ADDR, BND.PORT)来接受请求的主机的请求，然后返回第一次数据包，该数据包用以让客户机发送指定目标主机连接客户机地址和端口的数据包。

    在目标主机连接服务端指定的地址和端口成功或失败之后，回复第二次数据包。此时的(BND.ADDR, BND.PORT)应该为目标主机与服务端建立的连接的地址和端口。

  - 0x03表示UDP转发

- RSV 0x00，保留

- ATYP 类型

  - 0x01 IPv4地址，DST.ADDR部分4字节长度
  - 0x03 域名，DST.ADDR部分第一个字节为域名长度，DST.ADDR剩余的内容为域名，没有\0结尾。
  - 0x04 IPv6地址，16个字节长度。

- DST.ADDR 目的地址

- DST.PORT 网络字节序表示的目的端口 示例数据

> <Buffer 05 01 00 01 0e d7 b1 26 01 bb>

服务器根据客户端封装数据，请求远端服务器，将下面固定格式响应给客户端。

| VER  | REP  | RSV  | ATYP | BND.ADDR | BND.PORT |
| :--: | :--: | :--: | :--: | :------: | :------: |
|  1   |  1   | 0x00 |  1   |   动态   |    2     |

- VER是SOCKS版本，这里应该是0x05；
- REP应答字段
  - 0x00表示成功
  - 0x01普通SOCKS服务器连接失败
  - 0x02现有规则不允许连接
  - 0x03网络不可达
  - 0x04主机不可达
  - 0x05连接被拒
  - 0x06 TTL超时
  - 0x07不支持的命令
  - 0x08不支持的地址类型
  - 0x09 - 0xFF未定义
- RSV 0x00，保留
- ATYP
  - 0x01 IPv4地址，DST.ADDR部分4字节长度
  - 0x03域名，DST.ADDR部分第一个字节为域名长度，DST.ADDR剩余的内容为域名，没有\0结尾。
  - 0x04 IPv6地址，16个字节长度。
- BND.ADDR 服务器绑定的地址
- BND.PORT 网络字节序表示的服务器绑定的端口

### 使用nodejs 实现CONNECT请求

```
const net = require('net');
const dns = require('dns');
const AUTHMETHODS = { //只支持这两种方法认证
	NOAUTH: 0,
	USERPASS: 2
}

//创建socks5监听

let socket = net.createServer(sock => {

		//监听错误
		sock.on('error', (err) => {
			console.error('error code %s',err.code);
                        console.error(err);
		});

                sock.on('close', () => {
			sock.destroyed || sock.destroy();
		});

		sock.once('data', autherHandler.bind(sock)); //处理认证方式
	});

let autherHandler = function (data) {
	let sock = this;
	console.log('autherHandler ', data);
	const VERSION = parseInt(data[0], 10);
	if (VERSION != 5) { //不支持其他版本socks协议
		sock.destoryed || sock.destory();
		return false;
	}
	const methodBuf = data.slice(2); //方法列表

	let methods = [];
	for (let i = 0; i < methodBuf.length; i++)
		methods.push(methodBuf[i]);
	//先判断账号密码方式
	let kind = methods.find(method => method === AUTHMETHODS.USERPASS);
	if (kind) {
		let buf = Buffer.from([VERSION, AUTHMETHODS.USERPASS]);
		sock.write(buf);
		sock.once('data', passwdHandler.bind(sock));
	} else {
		kind = methods.find(method => method === AUTHMETHODS.NOAUTH);
		if (kind === 0) {
			let buf = Buffer.from([VERSION, AUTHMETHODS.NOAUTH]);
			sock.write(buf);
			sock.once('data', requestHandler.bind(sock));
		} else {
			let buf = Buffer.from([VERSION, 0xff]);
			sock.write(buf);
			return false;
		}
	}

}

/**
 * 认证账号密码
 */
let passwdHandler = function (data) {
	let sock = this;
	console.log('data ', data);
	let ulen = parseInt(data[1], 10);
	let username = data.slice(2, 2 + ulen).toString('utf8');
	let password = data.slice(3 + ulen).toString('utf8');
	if (username === 'admin' && password === '123456') {
		sock.write(Buffer.from([5, 0]));
	} else {
		sock.write(Buffer.from([5, 1]));
		return false;
	}
	sock.once('data', requestHandler.bind(sock));
}

/**
 * 处理客户端请求
 */
let requestHandler = function (data) {
	let sock = this;
	const VERSION = data[0];
	let cmd = data[1]; // 0x01 先支持 CONNECT连接
        if(cmd !== 1)
          console.error('不支持其他连接 %d',cmd);
        let flag = VERSION === 5 && cmd < 4 && data[2] === 0;
	if (! flag)
		return false;
	let atyp = data[3];
	let host,
	port = data.slice(data.length - 2).readInt16BE(0);
	let copyBuf = Buffer.allocUnsafe(data.length);
	data.copy(copyBuf);
	if (atyp === 1) { //使用ip 连接
		host = hostname(data.slice(4, 8));
		//开始连接主机！
	        connect(host, port, copyBuf, sock);

	} else if (atyp === 3) { //使用域名
		let len = parseInt(data[4], 10);
		host = data.slice(5, 5 + len).toString('utf8');
		if (!domainVerify(host)){
			console.log('domain is fialure %s ', host);
                        return false;
                }
		console.log('host %s', host);
		dns.lookup(host, (err, ip, version) => {
			if(err){
				console.log(err)
				return;
			}			
			connect(ip, port, copyBuf, sock);
		});

	}
}

let connect = function (host, port, data, sock) {
        if(port < 0 || host === '127.0.0.1')
           return;
	console.log('host %s port %d', host, port);
	let socket = new net.Socket();
	socket.connect(port, host, () => {
		data[1] = 0x00;
                if(sock.writable){
			sock.write(data);
			sock.pipe(socket);
			socket.pipe(sock);
		}
	});
 
        socket.on('close', () => {
		socket.destroyed || socket.destroy();
        });
        
	socket.on('error', err => {
		if (err) {
                        console.error('connect %s:%d err',host,port);
			data[1] = 0x03;
                        if(sock.writable)
			sock.end(data);
			console.error(err);
			socket.end();
		}
	})
}

let hostname = function (buf) {
	let hostName = '';
	if (buf.length === 4) {
		for (let i = 0; i < buf.length; i++) {
			hostName += parseInt(buf[i], 10);
			if (i !== 3)
				hostName += '.';
		}
	} else if (buf.length == 16) {
		for (let i = 0; i < 16; i += 2) {
			let part = buf.slice(i, i + 2).readUInt16BE(0).toString(16);
			hostName += part;
			if (i != 14)
				hostName += ':';
		}
	}
	return hostName;
}

/**
 * 校验域名是否合法
 */
let domainVerify = function (host) {
	let regex = new RegExp(/^([a-zA-Z0-9|\-|_]+\.)?[a-zA-Z0-9|\-|_]+\.[a-zA-Z0-9|\-|_]+(\.[a-zA-Z0-9|\-|_]+)*$/); 
	return regex.test(host);
}


socket.listen(8888,() => console.log('socks5 proxy running ...')).on('error', err => console.error(err));
                                                                                                                        
复制代码
```

### end

和浏览器结合使用的，发现没办法加载斗鱼的视频，不知什么原理，优酷都没有什么问题的． 刚刚学习NodeJs一些知识点，写得一般般，有哪里写得不好的，请大家指出来，大家一起讨论。一开始在看协议的时候，以为客户端（浏览器）和服务器在认证请求完后，双方会保持一个TCP长连接，客户端直接发送封装请求数据包．实际上客户端每一个请求都是从认证开始的，每一个请求都是相互独立的，所以`once`这个方法特别适合这里

# socks5 第二个人的讲解

# Socks5代理协议

或许你没听说过socks5，但你一定听说过SS，SS内部使用的正是socks5协议。

socks5是一种网络传输协议，主要用于客户端与目标服务器之间通讯的透明传递。

该协议设计之初是为了让有权限的用户可以穿过防火墙的限制，访问外部资源。

## 1. RFC地址

1. [socks5协议规范rfc1928](https://www.ietf.org/rfc/rfc1928.txt)
2. [socks5账号密码鉴权规范rfc1929](https://www.ietf.org/rfc/rfc1929.txt)

## 2. 协议过程



![image.png](https://user-gold-cdn.xitu.io/2019/8/24/16cc2db73edb7200?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)



1. 客户端连接上代理服务器之后需要发送请求告知服务器目前的socks协议版本以及支持的认证方式
2. 代理服务器收到请求后根据其设定的认证方式返回给客户端
3. 如果代理服务器不需要认证，客户端将直接向代理服务器发起真实请求
4. 代理服务器收到该请求之后连接客户端请求的目标服务器
5. 代理服务器开始转发客户端与目标服务器之间的流量

## 3. 认证过程

### 3.1 客户端发出请求

> 客户端连接服务器之后将直接发出该数据包给代理服务器

| VERSION | METHODS_COUNT | METHODS...                            |
| ------- | ------------- | :------------------------------------ |
| 1字节   | 1字节         | 1到255字节，长度由METHODS_COUNT值决定 |
| 0x05    | 0x03          | 0x00 0x01 0x02                        |

- VERSION SOCKS协议版本，目前固定0x05
- METHODS_COUNT 客户端支持的认证方法数量
- METHODS... 客户端支持的认证方法，每个方法占用1个字节

METHOD定义

- 0x00 不需要认证（常用）
- 0x01 GSSAPI认证
- 0x02 账号密码认证（常用）
- 0x03 - 0x7F IANA分配
- 0x80 - 0xFE 私有方法保留
- 0xFF 无支持的认证方法

### 3.2 服务端返回选择的认证方法

> 接收完客户端支持的认证方法列表后，代理服务器从中选择一个受支持的方法返回给客户端

#### 3.2.1 无需认证

| VERSION | METHOD |
| ------- | ------ |
| 1字节   | 1字节  |
| 0x05    | 0x00   |

- VERSION SOCKS协议版本，目前固定0x05
- METHOD 本次连接所用的认证方法，上例中为无需认证

#### 3.2.2 账号密码认证

| VERSION | METHOD |
| ------- | ------ |
| 1字节   | 1字节  |
| 0x05    | 0x02   |

#### 3.2.3 客户端发送账号密码

> 服务端返回的认证方法为0x02(账号密码认证)时，客户端会发送账号密码数据给代理服务器

| VERSION | USERNAME_LENGTH | USERNAME  | PASSWORD_LENGTH | PASSWORD  |
| ------- | --------------- | --------- | --------------- | --------- |
| 1字节   | 1字节           | 1-255字节 | 1字节           | 1-255字节 |
| 0x01    | 0x01            | 0x0a      | 0x01            | 0x0a      |

- VERSION 认证子协商版本（与SOCKS协议版本的0x05无关系）
- USERNAME_LENGTH 用户名长度
- USERNAME 用户名字节数组，长度为USERNAME_LENGTH
- PASSWORD_LENGTH 密码长度
- PASSWORD 密码字节数组，长度为PASSWORD_LENGTH

#### 3.2.4 服务端响应账号密码认证结果

> 收到客户端发来的账号密码后，代理服务器加以校验，并返回校验结果

| VERSION | STATUS |
| ------- | ------ |
| 1字节   | 1字节  |

- VERSION 认证子协商版本，与客户端VERSION字段一致
- STATUS 认证结果
  - 0x00 认证成功
  - 大于0x00 认证失败

## 4. 命令过程

> 认证成功后，客户端会发送连接命令给代理服务器，代理服务器会连接目标服务器，并返回连接结果

#### 4.1 客户端请求

| VERSION | COMMAND | RSV   | ADDRESS_TYPE | DST.ADDR  | DST.PORT |
| ------- | ------- | ----- | ------------ | --------- | -------- |
| 1字节   | 1字节   | 1字节 | 1字节        | 1-255字节 | 2字节    |

- VERSION SOCKS协议版本，固定0x05
- COMMAND 命令
  - 0x01 CONNECT 连接上游服务器
  - 0x02 BIND 绑定，客户端会接收来自代理服务器的链接，著名的FTP被动模式
  - 0x03 UDP ASSOCIATE UDP中继
- RSV 保留字段
- ADDRESS_TYPE 目标服务器地址类型
  - 0x01 IP V4地址
  - 0x03 域名地址(没有打错，就是没有0x02)，域名地址的第1个字节为域名长度，剩下字节为域名名称字节数组
  - 0x04 IP V6地址
- DST.ADDR 目标服务器地址
- DST.PORT 目标服务器端口

#### 4.2 代理服务器响应

| VERSION | RESPONSE | RSV   | ADDRESS_TYPE | BND.ADDR  | BND.PORT |
| ------- | -------- | ----- | ------------ | --------- | -------- |
| 1字节   | 1字节    | 1字节 | 1字节        | 1-255字节 | 2字节    |

- VERSION SOCKS协议版本，固定0x05
- RESPONSE 响应命令
  - 0x00 代理服务器连接目标服务器成功
  - 0x01 代理服务器故障
  - 0x02 代理服务器规则集不允许连接
  - 0x03 网络无法访问
  - 0x04 目标服务器无法访问（主机名无效）
  - 0x05 连接目标服务器被拒绝
  - 0x06 TTL已过期
  - 0x07 不支持的命令
  - 0x08 不支持的目标服务器地址类型
  - 0x09 - 0xFF 未分配
- RSV 保留字段
- BND.ADDR 代理服务器连接目标服务器成功后的代理服务器IP
- BND.PORT 代理服务器连接目标服务器成功后的代理服务器端口

## 5. 通信过程

>  经过认证与命令过程后，客户端与代理服务器进入正常通信，客户端发送需要请求到目标服务器的数据给代理服务器，代理服务器转发这些数据，并把目标服务器的响应转发给客户端，起到一个“透明代理”的功能。

## 6. 实际例子

上文详细讲解了协议规范，下面来一个实例的通信过程范例。

*6.2中无需认证和需要账号密码认证是互斥的*，同一请求只会采取一种，本文都列在下面。

### 6.1 客户端发送受支持的认证方法

```
0x05 0x02 0x00 0x02
复制代码
```

- 0x05 SOCKS5协议版本
- 0x02 支持的认证方法数量
- 0x00 免认证
- 0x02 账号密码认证

### 6.2 服务端响应选择的认证方法

#### 6.2.1 无需认证

> 以下是无需认证，客户端收到该响应后直接发送需要发送给目标服务器的数据给到代理服务器，此时进入通信错过程

```
0x05 0x00
复制代码
```

- 0x05 SOCKS5协议版本
- 0x00 免认证

#### 6.2.2 需要账号密码认证

```
0x05 0x02
复制代码
```

- 0x05 SOCKS5协议版本
- 0x02 账号密码认证

#### 6.2.3 客户端发送账号密码

```
0x01 0x04 0x61 0x61 0x61 0x61 0x04 0x61 0x61 0x61 0x61
复制代码
```

- 0x01 子协商版本
- 0x04 用户名长度
- 0x61 0x61 0x61 0x61 转换为ascii字符之后为"aaaa"
- 0x04 密码长度
- 0x61 0x61 0x61 0x61 转换为ascii字符之后"aaaa"

#### 6.2.4 代理服务器响应认证结果

```
0x01 0x00
复制代码
```

- 0x01 子协商版本
- 0x00 认证成功（也就是代理服务器允许aaaa账号以aaaa密码登录）

### 6.3 客户端请求代理服务器连接目标服务器

以127.0.0.1和80端口为例

```
0x05 0x01 0x01 0x01 0x7f 0x00 0x00 0x01 0x00 0x50
复制代码
```

- 0x05 SOCKS协议版本
- 0x01 CONNECT命令
- 0x01 RSV保留字段
- 0x01 地址类型为IPV4
- 0x7f 0x00 0x00 0x01 目标服务器IP为127.0.0.1
- 0x00 0x50 目标服务器端口为80

### 6.4 代理服务器连接目标主机，并返回结果给客户端

```
0x05 0x00 0x01 0x01 0x7f 0x00 0x00 0x01 0x00 0xaa 0xaa
复制代码
```

- 0x05 SOCKS5协议版本
- 0x00 连接成功
- 0x01 RSV保留字段
- 0x01 地址类型为IPV4
- 0x7f 0x00 0x00 0x01 代理服务器连接目标服务器成功后的代理服务器IP, 127.0.0.1
- 0xaa 0xaa 代理服务器连接目标服务器成功后的代理服务器端口（代理服务器使用该端口与目标服务器通信），本例端口号为43690

### 6.5 客户端发送请求数据给代理服务器

如果客户端需要请求目标服务器的HTTP服务,就会发送HTTP协议报文给代理服务器,代理服务器将这些报文原样转发给目标服务器,并将目标服务器的响应发送给客户端,代理服务器不会对客户端或者目标服务器的报文做任何解析。