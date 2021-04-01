# Virtualenv虚拟环境的创建、激活、及退出

若没有安装，请先安装
1、shell下运行：

```shell
pip3 install virtualenv
```

2、使用方法

```shell
virtualenv [虚拟环境名称-也是目录名称] 
```

3、启动环境

```shell
source [创建的目录]/bin/activate
```

默认情况下，虚拟环境会依赖系统环境中的site packages，如果不想依赖这些package，那么可以加上参数 --no-site-packages建立虚拟环境：

```shell
virtualenv --no-site-packages [虚拟环境名称]
```

4、退出

```shell
deactivate
```

如果没有启动虚拟环境，系统也安装了pip工具，那么套件将被安装在系统环境中，为了避免发生此事，可以在~/.bashrc文件中加上：

```shell
export PIP_REQUIRE_VIRTUALENV=true
```

或者让在执行pip的时候让系统自动开启虚拟环境：

```shell
export PIP_RESPECT_VIRTUALENV=true
```

# Virtualenvwrapper

Virtaulenvwrapper是virtualenv的扩展包，用于更方便管理虚拟环境，它可以做：

将所有虚拟环境整合在一个目录下

管理（新增，删除，复制）虚拟环境

快速切换虚拟环境

安装方法
1、运行

```shell
pip install virtualenvwrapper  
```

2、创建目录用来存放虚拟环境

```shell
mkdir ~/.virtualenvs # 默认存放在这个文件夹
```

3、在.bashrc中添加

```shell
export WORKON_HOME=~/.virtualenvs # 可以修改默认文件夹

if [ `id -u` != '0' ]; then

  export VIRTUALENV_USE_DISTRIBUTE=1        # <-- Always use pip/distribute
  export WORKON_HOME=$HOME/.virtualenvs       # <-- Where all virtualenvs will be stored
  source /usr/local/bin/virtualenvwrapper.sh
  export PIP_VIRTUALENV_BASE=$WORKON_HOME
  export PIP_RESPECT_VIRTUALENV=true

fi
```

4、运行：` source ~/.bashrc`

此时virtualenvwrapper就可以使用了。

命令列表

```shell
workon:列出虚拟环境列表

lsvirtualenv:同上

mkvirtualenv :新建虚拟环境

workon [虚拟环境名称]:切换虚拟环境

rmvirtualenv :删除虚拟环境

deactivate: 离开虚拟环境
```

# Anaconda+用conda创建python虚拟环境

**Anaconda与conda区别** 

conda可以理解为一个工具，也是一个可执行命令，其核心功能是包管理与环境管理。包管理与pip的使用类似，环境管理则允许用户方便地安装不同版本的python并可以快速切换。 conda的设计理念——conda将几乎所有的工具、第三方包都当做package对待，甚至包括python和conda自身 Anaconda则是一个打包的集合，里面预装好了conda、某个版本的python、众多packages、科学计算工具等等。

- 首先在所在系统中安装Anaconda。可以打开命令行输入conda -V检验是否安装以及当前conda的版本。
- conda常用的命令。
  - **conda list** 查看安装了哪些包。
  - **conda env list** 或 **conda info -e** 查看当前存在哪些虚拟环境
  - **conda update conda** 检查更新当前conda
- 创建Python虚拟环境。
  - 使用 **conda create -n your_env_name python=X.X**（2.7、3.6等） anaconda 命令创建python版本为X.X、名字为your_env_name的虚拟环境。**your_env_name文件可以在Anaconda安装目录envs文件下找到**。

```python
# 指定python版本为2.7，注意至少需要指定python版本或者要安装的包

# 后一种情况下，自动安装最新python版本

conda create -n env_name python=2.7

# 同时安装必要的包
conda create -n env_name numpy matplotlib python=2.7
```

- 使用激活(或切换不同python版本)的虚拟环境。

  

  - 打开命令行输入python --version可以检查当前python的版本。

  

  - 使用如下命令即可 激活你的虚拟环境(即将python的版本改变)。


  ```shell
  Linux: source activate your_env_name(虚拟环境名称)
  
  Windows: activate your_env_name(虚拟环境名称)
  
  这是再使用python --version可以检查当前python版本是否为想要的。
  ```

- 对虚拟环境中安装额外的包。
  - 使用命令**conda install -n your_env_name [package]即可安装package到your_env_name中**

- 关闭虚拟环境(即从当前环境退出返回使用PATH环境中的默认python版本)。

```shell
使用如下命令即可。

deactivate env_name，也可以使用activate root切回root环境
Linux下使用 source deactivate 
```

- 删除虚拟环境。

```shell
移除环境
  使用命令conda remove -n your_env_name(虚拟环境名称) --all， 即可删除。


删除环境中的某个包。
  使用命令conda remove --name your_env_name package_name 即可。

```

- 设置国内镜像

```shell
# 如果需要安装很多packages，你会发现conda下载的速度经常很慢，因为Anaconda.org的服务器在国外。所幸的是，清华TUNA镜像源有Anaconda仓库的镜像，我们将其加入conda的配置即可：

# 添加Anaconda的TUNA镜像
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
# TUNA的help中镜像地址加有引号，需要去掉

# 设置搜索时显示通道地址
conda config --set show_channel_urls yes
```

