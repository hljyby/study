## apt update

从软件源服务器获取最新的软件信息并缓存到本地。
因为很多apt的其他命令都是要通过比对版本信息来进行操作的，如果每次都去对比线上的版本信息效率肯定不理想，也没必要，所以做了一个缓存的机制。

## apt upgrade

从本地仓库中对比系统中所有已安装的软件，如果有新版本的话则进行升级

## apt list

列出本地仓库中所有的软件包名

## apt list [package]

从本地仓库中查找指定的包名，支持通配符，比如"apt list zlib*"就能列出以zlib开头的所有包名

## apt list --installed

列出系统中所有已安装的包名

## apt search [key]

与list类似，通过给出的关键字进行搜索，列出所有的包和其描述

## apt show [package]

列出指定包的详细情况，包名要填写完整。

## apt install [package]

安装指定的包，并同时安装其依赖的其他包。

## apt remove [package]

卸载包，但不删除相关配置文件。包名支持通配符

## apt autoremove

卸载因安装软件自动安装的依赖，而现在又不需要的依赖包 

## apt purge [package]

卸载包，同时删除相关配置文件。包名支持通配符

## apt clean

删除所有已下载的软件包

## apt autoclean

类似clean，但删除的是过期的包（即已不能下载或者是无用的包）

```shell
选项： 

-h 本帮助文件。 

-q 输出到日志 - 无进展指示 

-qq 不输出信息，错误除外 

-d 仅下载 - 不安装或解压归档文件 

-s 不实际安装。模拟执行命令

-y 假定对所有的询问选是，不提示 

-f 尝试修正系统依赖损坏处 

-m 如果归档无法定位，尝试继续

-u 同时显示更新软件包的列表 

-b 获取源码包后编译 -V 显示详细的版本号

-c=? 阅读此配置文件

-o=? 设置自定的配置选项，如 -o dir::cache=/tmp
```

## apt-get 常用实例

```shell
apt-cache search packagename 搜索包
apt-cache show packagename 获取包的相关信息，如说明、大小、版本等
apt-get install packagename 安装包
apt-get install packagename --reinstall 重新安装包
apt-get -f install 修复安装”-f = –fix-missing”
apt-get remove packagename 删除包
apt-get remove packagename --purge 删除包，包括删除配置文件等
apt-get update 更新源
apt-get upgrade 更新已安装的包
apt-get dist-upgrade 升级系统
apt-get dselect-upgrade 使用 dselect 升级
apt-cache depends packagename 了解使用依赖
apt-cache rdepends packagename 是查看该包被哪些包依赖
apt-get build-dep packagename 安装相关的编译环境
apt-get source packagename 下载该包的源代码
apt-get clean 清理无用的包
apt-get autoclean 清理无用的包
apt-get check 检查是否有损坏的依赖
```

