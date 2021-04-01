# Nginx 安装

- sudo yum install nginx
- whereis nginx 查找nginx所在地
- systemctl start(stop) nginx (.server)                      ------ systemctl (systemcontrol)
- ps aux|grep nginx 查看后台运行的程序
- 先运行 然后读取配置文件一般是在/etc/nginx/nginx.conf 
- 安装包编译安装
  - wget <下载链接> 命令下载安装包
  - 把安装包解压
  - 执行./configure --prefix=url进行配置
    - --prefix 指定安装目录
    - 目的是用来查看当前系统的环境能否安装软件，在此过程中可能会提示你安装第三方依赖包
    - 在此过程中会提示需要安装第三方依赖包需要手动运行命令安装
    - 依赖安装完成以后在执行一边命令

- - 生成MakeFIle
  - 执行命令进行编译安装 sudo make && sudo make install
  - 启动nginx  
  - - cd /usr/local/nginx/sbin 进入安装目录启动它
    - 执行nginx文件 或者 执行 systemctl start(stop) nginx (.server) （不一定好使，好像服务没有注册）

# 安装python3

- 标准的centOS yum 装不了python3 因为标准库不确定
- 但是阿里云，腾讯云可以，因为它使用了镜像。
- 标准的centOS 在安装一个库 就可以安装python3了
  - sudo yum install epel-release
  - sudo yum install python3 -y
    - -y代表着中间不提示是否继续安装提示
- yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc* make -y 

# python 虚拟环境

- sys.path 可以找到python包的site-packages 里面有各种安装的包插件

- pychrome 新进一个工程可以选择新建一个虚拟环境或者在大环境下写代码，最好用虚拟环境，并且虚拟环境和代码别放在一起，这么做找插件好找，不同项目不同虚拟环境。

- pip freeze > requirement.txt 把安装的插件写入这个文件，给别人发送

- 在Linux环境里site-packages 一般在/usr/local/bin/python/下

- Linux 1:安装虚拟环境 可以使用virtualenv

- pip3 install virualenv

- 2: virtualenvwrapper

- sudo pip3 install virtualenvwapper

- 3:编辑~/.bashrc 在文件的最后面添加下面三行

  - export VIRTUALENVWRAPPER_PYTsoucHON=/usr/bin/python3.6 指定新虚拟环境使用的解释器
  - export WORKON_HOME=~/.env 指定新的虚拟环境保存在那个文件夹里

- source /usr/local/bin/virtualenvwrapper.sh 指定virtualenvwrapper.sh 脚本

- 执行mkvirtualenv test 新建虚拟环境目录放在~/.env里

- mkvirtualenv -p python2 虚拟环境名 不写-p 默认python3.6

- 在虚拟环境里安装时不要用sudo 命令，会穿透虚拟环境

- 切换虚拟环境 **workon pa** 切换虚拟环境 

- 退出虚拟环境 **deactivate**

- 删除虚拟环境 **rmvirtualenv**

- ln -s python3.6 python  创建一个链接，把python指向python3.6

  # anaconda

- conda info -e 

- ```python
  conda create --name python34 python=3.4
  
  activate python34 # for Windows
  source activate python34 # for Linux & Mac
  
  
  # 此时，再次输入
  python --version
  
  # 如果想返回默认的python 2.7环境，运行
  deactivate python34 # for Windows
  source deactivate python34 # for Linux & Mac
  
  # 删除一个已有的环境
  conda remove --name python34 --all
  ```

# 