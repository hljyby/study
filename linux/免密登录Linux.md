# 生成公钥

```shell
ssh-keygen

# C:\Users\Administrator\.ssh
```

# 查看公钥

```shell
cd C:\Users\Administrator\.ssh

# 打开
id_rsa.pub
```

# 发送公钥到Linux

```shell
scp ./id_rsa.pub root@192.168.xxx.xxx:~/.ssh/windows_ras.pub
```

# 配置Linux

```shell
cd ~/.ssh #进入到ssh目录.这个目录注意.我们是链接root所以这个家目录应该是root
touch authorized_keys	# 新建文件用来存放公钥,如果你已经有这个文件了.继续往下追加即可
# 然后将你的windows公钥追加到这个文件中即可
```

