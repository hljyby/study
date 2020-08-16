# win + R

- compmgmt.msc                                    打开计算机管理

- services.msc                                           打开服务

- gpedit.msc 										     打开组策略

- control                                                      打开控制面板

- certmgr.msc                                             证书管理实用程序

- calc														     启动计算器

- devmgmt.msc                                           设备管理器

- desk.cpl                                                      显示属性

- diskmgmt.msc                                           磁盘管理实用程序

- firewall.cpl                                                  WINDOWS防火墙

- mspaint                                                        画图板

- ncpa.cpl                                                       网络连接

- nslookup                                                     IP地址侦测器

- notepad                                                      打开记事本

- regedit                                                         注册表

- wordpad || write                                      写字板

- ### optionalfeatures             windows 功能（IIS.....）

# CMD



- netstat -an                                               查看网络链接
- 打开无线热点：netsh wlan start hostednetwork
- 关闭无线热点netsh wlan stop hostednetwork
- 查询无线热点状态：netsh wlan show hostednetwork
- 开启无线热点功能：netsh wlan set hostednetwork mode=allow
- 禁用无线热点功能：netsh wlan set hostednetwork mode=disallow
- netsh wlan set hostednetwork mode=allow ssid=mywifi key=12345678
  - mode：是否开启无线热点，disallow为禁用，allow为开启 
  - ssid = 后填无线热点名称
  - key = 后填无线热点密码（必须八位及以上）

- 没出现在适配器里没出现 新的wifi名 就是代表你的网卡不支持wifi共享 也就是虚拟wifi