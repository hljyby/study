Vultr 配置 SSR 保持正确的冲浪姿势

发表于 2018-03-29 22:19

|

分类于 [印象笔记](https://www.lcgod.com/menu_22)

|

评论次数 3

|

阅读次数 6683

![https://img.lcgod.com/2019/04/14/1555247113.gif](https://img.lcgod.com/2019/04/14/1555247113.gif)



身为一名程序猿，拥有一身高明的轻功是非常有必要的，毕竟中国没有 msdn、stack overflow 那么好的技术论坛，更没有发明过任何优秀的语言等等，那么当我们遇到各种棘手的技术问题或者 BUG 时，google 等工具的使用就显得非常重要了.

并且很多公司在招聘信息上都有一点额外备注，例如美团：**如果技术问题你是选择百度而不是谷歌，我想你们不适合我。** 当然，我们科学上网肯定不只这一个原因，我就不多说了，懂的人自然懂，hiahiahia~

![20180329221755_32141.gif](https://img.lcgod.com/2019/04/14/1555247113.gif)

## 购买Vultr服务器

Vultr 是美国知名云服务提供商 Choopa 旗下的 VPS 服务，Choopa 一直在为游戏公司提供全球支撑服务，因此该公司在全球 14 个国家及地区部署数据中心，包括日本东京、新加坡、美国洛杉矶、西雅图、英国伦敦、德国等地。可谓公司资金雄厚，体验和服务一流，最重要的是价格亲民。当前最低仅需 $2.5 / 月，在这个价位的 VPS，单论性价比来说，基本没有对手。唯一能抗衡的也就只有搬瓦工了。

### Vultr的优势

机房众多 ：拥有日本、美国、欧洲等 14 个机房

架构优秀 ：全部采用 KVM 架构、SSD 固态硬盘、500G/月流量起步

镜像强大 ：常见的 Linux 之外还可以自定义安装 ISO 系统，还可以安装 Windows 系统，这在其他 VPS 商是不可能遇到的

后台强大 ：拥有系统快照、一键装机部署脚本、备份、防火墙等强大功能，从 VPS 这点丝毫不输给阿里云。

促销活动 : 不定期有新用户注册奖励，有时赠送金额高达 $100

计费灵活 : 采用小时计费模式，可以任意的添加和删除机器 , 并且是单向流量收费 , 也就是只计算下载的的流量

### 注册账号

现在 Vultr 的注册活动 , 注册即送 25 刀 , 需要充值 10 刀即可使用 , 实测 18 年 3 月 30 日之前都是有效的,来晚了可能就没咯

注册地址: [曲境折跃](https://www.vultr.com/promo25b/?service=promo25b)

![20180330091135_61703.png](https://img.lcgod.com/2019/04/14/1555247270.png)

如上图所示 , 进入注册页面输入你的邮箱地址和密码 , 密码必须包含以下规则 :

- 10位字符
- 大写字母
- 小写字母与数字

#### 选购服务器

注册成功后会调转至用户中心 , 点击Servers选项 , 进行选购服务器

![20180330092144_97715.png](https://img.lcgod.com/2019/04/14/1555247333.png)

#### 选择服务器地区

实测截止18年3月30日最低价位2.5刀每月的服务器只有纽约地区有货, 如上图, 我选择了纽约地区, 当然 , 如果你是个土豪可以无视这些东西

![20180330092348_84022.png](https://img.lcgod.com/2019/04/14/1555247434.png)

### 选择操作系统

如下图 , 网页默认选择了64位的CentOS 7系统 , 可以不用进行其他操作

![20180330092820_28927 1.png](https://img.lcgod.com/2019/04/14/1555247492.png)

#### 选择服务器配置

如下图 , 当前纽约地区有最低价位 2.5 刀每月的服务器 , 相应的配置是 1 核 CPU 500 MB 内存 20 GB 硬盘 500 GB 流量/每月 , 还是那句话如果你是个土豪 , 可以无视这些东西 , 随意选择就好 , 一般人 500GB 流量就够用

![20180330093105_51983.png](https://img.lcgod.com/2019/04/14/1555247514.png)

呜呜呜, 真羡慕你们这些有钱人的生活!

![20180330093725_24596.jpg](https://img.lcgod.com/2019/04/14/1555247572.jpeg)

### 选择附加功能

如下图, 勾选 Enable IPv6 选项, 开启 IPv6

![20180330094157_66105.png](https://img.lcgod.com/2019/04/14/1555247614.png)

#### 自定义设置主机名称与标签

如下图 , 我设置为leo

![20180330121221_45748.png](https://img.lcgod.com/2019/04/14/1555247672.png)

最后 点击网页底部的 Deploy Now 按钮 , 进入支付界面

![20180330121515_13733.png](https://img.lcgod.com/2019/04/14/1555247702.png)

### 订单支付

如下图, 第一次并不能使用支付宝进行支付 , 所以你必须选择 PayPal 或者信用卡进行支付 , PayPal 和支付宝一样 , 也是一个国际知名的第三方支付公司

![20180330130338_42284.png](https://img.lcgod.com/2019/04/14/1555247749.png)

这里我选择PayPal支付方式 , 可以看到右侧显示了注册后赠送的25刀余额 , 当然 , 需要充值之后才能使用 , 勾选卖身契 , 进入PayPal页面

![20180330121845_81350.png](https://img.lcgod.com/2019/04/14/1555247775.png)

注册并绑定银行卡手机号之类的东西后登录 , 完成支付后页面会跳转回控制台

![20180330131110_30496.png](https://img.lcgod.com/2019/04/14/1555247790.png)

## 配置服务器环境

### 查看主机状态

如下图 , 购买完成后 , 在控制台点击主机名leo , 查看主机密码 , 状态等相关信息

![20180330131329_47605.png](https://img.lcgod.com/2019/04/14/1555247827.png)

如下图 , 分别点击copy按钮可以将IP地址和密码复制

![20180330131557_28679.png](https://img.lcgod.com/2019/04/14/1555247865.png)

#### 下载 sh 工具

使用 Xshell 工具连接服务器 , 没有此工具的话 , 可以去官网下载 , 或者从我的百度云备份地址下载

[Xshell官网](https://www.netsarang.com/zh/xshell/)

[百度云](https://baidu.com/)

提取密码:

### 连接服务器

如下图, 打开Xshell, 点击上方工具栏中的文件->新建 , 弹出此对话框 , 输入自定义名称 , 选择协议为SSH , 输入主机的IP地址 , 输入端口号 22

![20180330133006_13844.png](https://img.lcgod.com/2019/04/14/1555248144.png)

如下图, 弹出对话框后, 点击确定按钮后再次点击连接按钮 , 接着会弹出此对话框 , 选择接受并保存

![20180330133431_95570.png](https://img.lcgod.com/2019/04/14/1555248159.png)

如下图, 勾选记住用户名 , 方便下次登录 , 用户名为 root

![20180330133527_58989.png](https://img.lcgod.com/2019/04/14/1555248257.png)

最后, 从Vultr的控制台复制服务器的密码 , 然后粘贴进来 , 点击确定按钮

![20180330133844_20710.png](https://img.lcgod.com/2019/04/14/1555248199.png)

如下图, 成功连接服务器, 接下来就该使用命令来操作了 , 因为是米国的服务器 , 所以输入命令时会有延迟 , 并没有国内主机那么快。

![20180330133912_73319.png](https://img.lcgod.com/2019/04/14/1555248342.png)

### 安装yum-axelget插件

yum-axelget是EPEL提供的一个yum插件。默认的yum是单线程下载的，使用该插件后用yum安装软件时可以并行下载。yum-axelget插件原理是调用系统中的axel下载软件，然后根据软件包的大小自动设定线程数。在多线程操作时，还能避免因为线程数过多而导致服务器拒绝下载的问题，大大提高了软件的下载速度，减少了下载的等待时间。注意：通过下面这条安装命令，会同时安装axel下载软件。

```bash
yum -y install yum-axelget
```

### 关闭防火墙

```bash
#查看防火墙状态
service firewalld status

#关闭防火墙
service firewalld stop

#禁止防火墙开机启动
systemctl disable firewalld.service    
```

如下图, 操作完成后显示防火墙已经被关闭且禁止开机启动了

![20180330151127_47207.png](https://img.lcgod.com/2019/04/14/1555248461.png)

### 下载ssr脚本, 并启动

```bash
### 获取脚本
wget --no-check-certificate https://raw.githubusercontent.com/teddysun/shadowsocks_install/master/shadowsocksR.sh

#添加可执行权限
chmod +x shadowsocksR.sh
    
#执行sh脚本 并将执行后的标准错误与标准输出写入log文件
./shadowsocksR.sh 2>&1 | tee shadowsocksR.log    
```

### 设置ssr配置信息

如下图, 输入密码与端口号 , 如上图所示 , 端口号为3-4位数字 , 不要使用80 , 443 , 3306之类的系统软件所用端口号 , 我设置为7751

![20180330153622_34428.png](https://img.lcgod.com/2019/04/14/1555248556.png)

### 选择加密方式

如下图, 输入2, 选择aes-256-cfb加密方式

![20180330155732_39670.png](https://img.lcgod.com/2019/04/14/1555248646.png)

### 选择协议插件

如下图, 输入3, 选择auth_sha1_v4协议插件

![20180330160027_68598.png](https://img.lcgod.com/2019/04/14/1555248689.png)

### 选择混淆插件

如下图, 输入6, 选择tls1.2_ticket_auth混淆插件

![20180330160508_34753.png](https://img.lcgod.com/2019/04/14/1555248718.png)

### 安装环境

如下图, 任意键开始安装环境

![20180330160741_44736.png](https://img.lcgod.com/2019/04/14/1555248772.png)

安装完成后会出现如下界面

![20180330161008_28838.png](https://img.lcgod.com/2019/04/14/1555248787.png)

### 重启系统

安装完成 , 接着输入以下命令重启系统 , 并点击Xshell工具栏中的文件->重新连接, 重连服务器

```bash
reboot
```

## 安装TCP BBR拥塞控制算法脚本

TCP BBR 是谷歌在 2016 年 9 月开源的一个优化 TCP 拥塞的算法，并且 Linux 内核从 4.9 版本开始集成该算法，据多方网友反馈，网速甚至可以提升好几个数量级，比锐速还快！

依次输入如下命令：

```bash
# 下载脚本
wget --no-check-certificate https://github.com/teddysun/across/raw/master/bbr.sh

# 添加可执行权限
chmod +x bbr.sh

# 运行bbr脚本
./bbr.sh
```

如下图, 输入完毕后, 任意键开始安装脚本

![20180330163549_39925.png](https://img.lcgod.com/2019/04/14/1555248952.png)

此过程大约5-10分钟 , 安装完成后出现如下提示 :

![20180330163903_68938.png](https://img.lcgod.com/2019/04/14/1555248974.png)

输入 y，重启系统，这代表着科学上网的服务器环境已配置完毕啦!

## 下载 SSR 客户端

### 说到这里，很多人可能会疑惑 Shadowsocks 原版和 ShadowsocksR 的区别是什么?

Shadowsocks 原版本身，是具有协议和混淆功能的，也就是原版协议/混淆，只是只有一个不能自行选择，并且全靠作者维护，作者被约谈喝茶之后，现在已经 GG 了。

其他的接手者只是继续完善其他的功能，那么 ShadowsocksR 就是原版的另一个分支，由另外一位作者维护，并且增加了很多人性化的功能，并且增加了更多的协议和混淆插件，来避免被墙流量匹配和 QOS 限速，所以这就是我们选择 SSR 的目的。

那么解释清楚后接下来的事情就是使用 ShadowsocksR 客户端连接VPS服务端

[Windows客户端](https://github.com/shadowsocksr-backup/shadowsocksr-csharp/releases/download/4.7.0/ShadowsocksR-4.7.0-win.7z)

[Mac客户端](https://github.com/shadowsocksr-backup/ShadowsocksX-NG/releases/download/1.4.2-R8-subscribe-alpha-3/ShadowsocksX-NG-R8.dmg)

[Android客户端](https://github.com/shadowsocksr-backup/shadowsocksr-android/releases/download/3.4.0.8/shadowsocksr-release.apk)

如果你嫌gayhub下载速度慢 , 也可以来我的[百度云](https://pan.baidu.com/s/1cVXoLTZdMX6vexQIT01r0g)备份地址下载

提取密码: y9ma

### 填写配置信息

如下图, 下载安装客户端, 完成后打开, 将相关的配置信息一一对应地填写, 点击确定按钮

![20180330174741_73691.png](https://img.lcgod.com/2019/04/14/1555249260.png)

接下来就真正地可以做爱做的事啦! hia hia hia~

最后补充一点, 鼠标右键点击任务栏中的图标 , 可以选择几种代理模式 , 默认是全局模式, 也就是说, 系统中所有的网络连接, 都会先经过你的 Vultr 服务器代理

![20180330175212_71946.png](https://img.lcgod.com/2019/04/14/1555249540.png)

然后可以打开 Chrome 测试测试

![20180330175457_26466.png](https://img.lcgod.com/2019/04/14/1555249451.png)

秒进谷歌，兄弟萌，我好了，你萌呢?

## 其他配置

网上还有一种常见的 SSR 安装与配置，可以自行参考

一键安装：

```bash
wget -N --no-check-certificate https://raw.githubusercontent.com/ToyoDAdoubi/doubi/master/ssr.sh && chmod +x ssr.sh && bash ssr.sh
```

如果 `wget` 命令不存在，则先安装 `wget` 命令：

```bash
apt-get install wget
wget --version
```

ssr 协议选择：

| 配置 | 值           |
| :--- | :----------- |
| 端口 | 2333         |
| 加密 | none         |
| 协议 | auth_chain_a |
| 混淆 | plain        |