# guthub 最新地址

```
https://github.com/v2fly/fhs-install-v2ray
```

# json 配置

```
{
  "log": {
    "access": "/var/log/v2ray/access.log",
    "error": "/var/log/v2ray/error.log",
    "loglevel": "warning"
  },
  "inbound": {
    "port": 7751,
    "protocol": "vmess",
    "settings": {
      "clients": [
        {
          "id": "392029fa-a9e0-42e3-93cb-97a9281495ed",
          "level": 1,
          "alterId": 100
        }
      ]
    },
    "streamSettings": {
      "network": "tcp"
    },
    "detour": {
      "to": "vmess-detour-118345"
    }
  },
  "outbound": {
    "protocol": "freedom",
    "settings": {}
  },
  "inboundDetour": [
    {
      "protocol": "vmess",
      "port": "10000-10010",
      "tag": "vmess-detour-118345",
      "settings": {},
      "allocate": {
        "strategy": "random",
        "concurrency": 5,
        "refresh": 5
      },
      "streamSettings": {
        "network": "kcp"
      }
    }
  ],
  "outboundDetour": [
    {
      "protocol": "blackhole",
      "settings": {},
      "tag": "blocked"
    }
  ],
  "routing": {
    "strategy": "rules",
    "settings": {
      "rules": [
        {
          "type": "field",
          "ip": [
            "0.0.0.0/8",
            "10.0.0.0/8",
            "100.64.0.0/10",
            "127.0.0.0/8",
            "169.254.0.0/16",
            "172.16.0.0/12",
            "192.0.0.0/24",
            "192.0.2.0/24",
            "192.168.0.0/16",
            "198.18.0.0/15",
            "198.51.100.0/24",
            "203.0.113.0/24",
            "::1/128",
            "fc00::/7",
            "fe80::/10"
          ],
          "outboundTag": "blocked"
        }
      ]
    }
  }
}
```

# json 文件一般在

```
/usr/local/etc/v2ray/config.json
```

# 管理v2ray 的命令

```
# 查看 v2ray 进程状态
systemctl status v2ray

# 启动
systemctl start v2ray

# 重启
systemctl restart v2ray
```

# v2ray 客户端工具

```
https://github.com/2dust/v2rayN/releases # window
https://github.com/2dust/v2rayNG/releases/download/1.1.14/v2rayNG_1.1.14.apk # 安卓
```

# 配置客户端

```
服务器地址：你的主机 ip 地址

端口：config.json 文件中设置的端口（可以自定义填写，不一定需要使用我的配置）

用户ID：config.json 文件中设置的 clients.id（可以自己随机生成，不一定需要使用我的配置）

额外ID：config.json 文件中设置的 clients.alertId（可以自定义填写，不一定需要使用我的配置）

选择加密方式：auto

传输协议：tcp
```

# 放开安全组 出站规则

# 配置 BBR 加速以及 SSR

依次运行以下命令即可开启 BBR 加速：

```bash
echo net.core.default_qdisc=fq >> /etc/sysctl.conf
echo net.ipv4.tcp_congestion_control=bbr >> /etc/sysctl.conf
sysctl -p
```