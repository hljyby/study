### **yum命令的用法：**

　　yum [options] [command] [package ...]

### **显示仓库列表：**

　　yum repolist [all | enabled | disabled]

### **显示程序包：**

　　yum list

　　yum list [all | glob_exp1] [glob_exp2] [...]

　　yum list {available | installed | updates} [glob_exp1] [...]

### **安装程序包：**

　　yum install package1 [package2] [...]

　　yum reinstall package1 [package2] [...] (重新安装)yum命令

### **升级/降级程序包：**

　　yum update [package1] [package2] [...]

　　yum downgrade package1 [package2] [...] (降级)

### **检查可用升级：**

　　yum check-update

### **卸载程序包：**

　　yum remove | erase package1 [package2] [...]yum命令

### **查看程序包**information(**详细信息**)：

　　yum info [...]

### **查看指定的特性(可以是某文件)是由哪个程序包所提供：**

　　yum provides | whatprovides feature1 [feature2] [...]

### **清理本地缓存：**

　　清除/var/cache/yum/$basearch/$releasever缓存

　　　　yum clean [ packages | metadata | expire-cache | rpmdb | plugins |all ]

### **构建缓存：**

　　yum makecache yum命令

### **搜索**：

　　yum search string1 [string2] [...]

　　以指定的关键字搜索程序包名及summary信息

### **查看指定包所依赖的capabilities：**

　　yum deplist package1 [package2] [...]

### **查看yum事务历史**：

　　yum history [info|list|packages-list|packages-info|summary|addon-info|redo|undo|rollback|new|sync|stats]

　　yum history

　　yum history info 6

　　yum history undo 6

### **查看yum日志** 

　　cat /var/log/yum.log

### **安装及升级本地程序包：**

　　yum localinstall rpmfile1 [rpmfile2] [...](用install替代)

　　yum localupdate rpmfile1 [rpmfile2] [...] (用update替代)

### **包组管理的相关命令：**

　　yum groupinstall group1 [group2] [...]

　　yum groupupdate group1 [group2] [...]

　　yum grouplist [hidden] [groupwildcard] [...]

　　yum groupremove group1 [group2] [...]

　　yum groupinfo group1 [...]yum命令

### **yum的命令行选项：**

　　--nogpgcheck：禁止进行gpg check

　　-y: 自动回答为“yes”

　　-q：静默模式

　　--disablerepo=repoidglob：临时禁用此处指定的repo

　　--enablerepo=repoidglob：临时启用此处指定的repo

　　--noplugins：禁用所有插件