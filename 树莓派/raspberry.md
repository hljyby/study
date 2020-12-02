# 树莓派设置

```python
ssh pi@raspberrypi.local

# wifi链接设置
# /boot分区下创建一个文件 wpa_supplicant.conf
country=CN
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
network={
ssid="MERCURY_2246"
psk="12345678"
key_mgmt=WPA-PSK
priority=1
}
# priority 链接优先级 越大优先级越高 不能为负
# 如果你的 WiFi 没有密码

network={
ssid="你的无线网络名称(ssid)"
key_mgmt=NONE
}

# 如果你的 WiFi 使用 WEP 加密

network={
ssid="你的无线网络名称(ssid)"
key_mgmt=NONE
wep_key0="你的 wifi 密码"
}

# 如果你的 WiFi 使用 WPA/WPA2 加密

network={
ssid="你的无线网络名称(ssid)"
key_mgmt=WPA-PSK
psk="你的 wifi 密码"
}

# sudo nano /etc/dhcpcd.conf 修改ip 地址

interface eth0
static ip_address=192.168.0.155/24
static routers=192.168.0.1
static domain_name_servers=192.168.0.1 114.114.114.114
 
interface wlan0
static ip_address=192.168.0.166/24
static routers=192.168.0.1
static domain_name_servers=192.168.0.1 114.114.114.114

# 如何显示树莓派的系统桌面  https://www.realvnc.com/en/connect/download/viewer/
# sudo raspi-config
# 进入画面后,选择第5项Interfacing Options 接口设置
# 选择第3项VNC 选择开启

# 修改屏幕分辨率
# sudo raspi-config
# 选择 Advanced opations 高级设置
# 选择  Resolution 
# 选择 分辨率


# curl https://download.argon40.com/argon1.sh | bash
# Argon ONE 外壳 脚本命令
# argonone-config 运行 配置文件在/etc/argononed.conf 55:70 ==> 55摄氏度：风扇速度70 （0-100）
# argonone-uninstall 卸载
```

# 树莓派 vim 上下左右 退格不好使

```

#卸载vim
sudo apt-get remove vim-common
#安装vim
sudo apt-get install vim
```

# 树莓派系统安装 MYSQL 

```python
# 通过apt直接安装mysql数据库，说明：树莓派提供了一个数据库(MriaDB)，相当于mysql使用，具体命令如下
sudo apt-get update
sudo apt-get install mariadb-server

# 修改数据库密码
sudo mysql -u root
use mysql;
update user set plugin='mysql_native_password' where user='root';
UPDATE user SET password=PASSWORD('root的密码') WHERE user='root';
flush privileges;
exit;

# 修改完成后重启服务
sudo /etc/init.d/mysql restart
# mysql的其他操作 status、start、stop、restart

# 允许远程登录
sudo vi /etc/mysql/mariadb.conf.d/50-server.cnf
# 将bind-address这行注释掉
# 或者将127.0.0.1 这个值改为  0.0.0.0
# 然后重启
sudo /etc/init.d/mysql restart

# 设置账号权限
mysql -u root -p
use mysql;
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'root的密码' WITH GRANT OPTION;
flush privileges;
```

# 树莓派换源（也可以看做其他Linux 系统换源）

## 前言

树莓派系统安装后默认使用国外的镜像源来更新软件，由于不可描述原因，国内访问速度非常慢，而且会遇到各种各样连接错误的蛋疼问题，因此需要换成国内源。树莓派官方提供了一个更新源列表，在这里我们使用中科大的软件源和系统源。

## 正文

```python

# 登陆到树莓派。你可以通过屏幕键鼠直接打开终端或者通过putty SSH登陆到树莓派。
# 备份源文件。执行如下命令：

sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak
sudo cp /etc/apt/sources.list.d/raspi.list /etc/apt/sources.list.d/raspi.list.bak

# 修改软件更新源，执行如下命令：（其他的linux 系统也有这个文件）

sudo vim /etc/apt/sources.list

# 将第一行修改成中科大的软件源地址

deb http://mirrors.ustc.edu.cn/raspbian/raspbian/ stretch main contrib non-free rpi

# 修改系统更新源，执行如下命令：

sudo nano /etc/apt/sources.list.d/raspi.list

# 将第一行修改成中科大的系统源地址

deb http://mirrors.ustc.edu.cn/archive.raspberrypi.org/debian/ stretch main ui

# 同步更新源，执行如下命令：

sudo apt-get update （获取可更新的软件列表）

# 更新升级以安装软件包，这个过程耗时较长。（慎用，会把所软件升级到最新的状态）

sudo apt-get upgrade

```

# KDE（桌面版）  Gnome（桌面版）  Minimal（最小系统） Linux三种不同的系统

# 树莓派摄像头

```shell
$ sudo apt-get install vlc

# 开启视频流 通过网络传输
$ sudo raspivid -o - -t 0 -w 640 -h 360 -fps 25|cvlc -vvv stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:8090}' :demux=h264 

# sudo raspistill -o yby.jpg
```

# motion

```shell
sudo apt-get install motion

sudo vim /etc/default/motion
# 把no 变成yes 开启开机自启
start_motion_deamon=yes

sudo vim /etc/motion/motion.conf
deamon on # 开启后台运行模式
stream_port 8081 # 摄像头端口

# web浏览器相关配置
webcontrol_port 8080
webcontrol_localhost off
wencontrol_html_output on

# 摄像头成像相关设置
width 320
height 240
framerate 50 # 帧
stream_maxrate 50 # 最大帧
stream_localhost off # 只允许本地访问设为 off
```

- **motion基本操作命令** 

  启动摄像头 :            

```ruby
$sudo motion
```

 	关闭摄像头（root用户）:

```markdown
#service motion stop
```

在浏览器中键入树莓派ip和端口号，就可以看到摄像头拍到的图像了。

## 问题

### 视频卡顿
motion的配置文件中关于framerate，由两个参数控制：framerate & stream_maxrate。maxrate决定了上限。起初只设置了framerate为100,但maxrate仍然是1,因此会出现卡顿。

### 重影

