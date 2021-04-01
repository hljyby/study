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
# 进入画面后,选择第5项 Interfacing Options 接口设置
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

默认 用户 pi
默认 密码 raspberry

1、sudo raspi-config
2、advanced-options -> Expand Filesystem # 扩展文件系统
3、本地化配置 -> Localisation Options -> Locale -> 选择 zh utf-8 取消选择已选中的 # 改变本地语言
4、sudo passwd pi # 修改密码
5、sudo passwd -u root # 解除root锁定
6、sudo reboot # 重启 shutdown -r 
7、sudo poweroff # 关机 shutdown -h
8、sudo apt update # 更新软件源
9、sudo apt list --upgradable # 更新软件
```

# 更新软件源（中科大）

```shell
1、sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak
2、sudo cp /etc/apt/sources.list.d/raspi.list /etc/apt/sources.list.d/raspi.list.bak

3、sudo nano /etc/apt/sources.list
4、第一行替换为：deb http://mirrors.ustc.edu.cn/raspbian/raspbian/ stretch main contrib non-free rpi

5、sudo nano /etc/apt/sources.list.d/raspi.list
6、第一行替换为：deb http://mirrors.ustc.edu.cn/archive.raspberrypi.org/debian/ stretch main ui

7、sudo apt-get update
8、sudo apt-get upgrade


```

```shell
# 这两个随便，反正我没感受到有什么区别
查看系统版本
lsb_release  -a

sudo nano /etc/apt/sources.list
deb http://mirrors.ustc.edu.cn/raspbian/raspbian/ buster main contrib non-free rpi
deb http://mirrors.tuna.tsinghua.edu.cn/raspbian/raspbian/ buster main contrib non-free rpi
deb-src http://mirrors.tuna.tsinghua.edu.cn/raspbian/raspbian/ buster main contrib non-free rpi

sudo nano /etc/apt/sources.list.d/raspi.list
deb http://mirrors.ustc.edu.cn/archive.raspberrypi.org/debian/ buster main ui
deb http://mirrors.tuna.tsinghua.edu.cn/raspberrypi/ buster main ui
deb-src http://mirrors.tuna.tsinghua.edu.cn/raspberrypi/ buster main ui
```



# 代理

```shell
export http_proxy="http://192.168.0.104:1080"
export https_proxy="http://192.168.0.104:1080"

sudo visudo
Defaults        env_keep+="http_proxy https_proxy"

```

# 安装OMV

```shell
sudo nano /etc/hosts
# 用于访问Github加速
151.101.72.249 github.global.ssl.fastly.net
192.30.255.112 github.com
```

```shell
sudo nano /etc/apt/sources.list

deb http://mirrors.tuna.tsinghua.edu.cn/raspbian/raspbian/ buster main non-free contrib rpi
deb-src http://mirrors.tuna.tsinghua.edu.cn/raspbian/raspbian/ buster main non-free contrib rpi

```

```shell
sudo nano /etc/apt/sources.list.d/raspi.list

deb http://mirrors.tuna.tsinghua.edu.cn/raspberrypi/ buster main ui
```

```shell
# 更新系统
sudo apt-get update
sudo apt-get upgrade -y

```

```shell
wget -O - https://github.com/OpenMediaVault-Plugin-Developers/installScript/raw/master/install | sudo bash
```

或者

```shell
# 进入用户目录
cd ~
# 创建脚本文件
nano install.sh

```

```shell
#!/bin/bash
#
# shellcheck disable=SC1090,SC1091,SC1117,SC2016,SC2046,SC2086,SC2174
#
# Copyright (c) 2015-2020 OpenMediaVault Plugin Developers
# Copyright (c) 2017-2020 Armbian Developers
#
# This file is licensed under the terms of the GNU General Public
# License version 2. This program is licensed "as is" without any
# warranty of any kind, whether express or implied.
#
# Ideas/code used from:
# https://github.com/armbian/config/blob/master/debian-software
# https://forum.openmediavault.org/index.php/Thread/25062-Install-OMV5-on-Debian-10-Buster/
#
# version: 1.2.8
#

if [[ $(id -u) -ne 0 ]]; then
  echo "This script must be executed as root or using sudo."
  exit 99
fi

systemd="$(ps --no-headers -o comm 1)"
if [ ! "${systemd}" = "systemd" ]; then
  echo "This system is not running systemd.  Exiting..."
  exit 100
fi

declare -i cfg=0
declare -l codename
declare -l omvCodename
declare -l omvInstall=""
declare -l omvextrasInstall=""
declare -i skipFlash=0
declare -i skipNet=0
declare -i version

cpuFreqDef="/etc/default/cpufrequtils"
crda="/etc/default/crda"
defaultGovSearch="^CONFIG_CPU_FREQ_DEFAULT_GOV_"
ioniceCron="/etc/cron.d/make_nas_processes_faster"
ioniceScript="/usr/sbin/omv-ionice"
keyserver="hkp://keyserver.ubuntu.com:80"
omvKey="/etc/apt/trusted.gpg.d/openmediavault-archive-keyring.asc"
omvRepo="https://mirrors.tuna.tsinghua.edu.cn/OpenMediaVault/public"
omvSources="/etc/apt/sources.list.d/openmediavault.list"
rfkill="/usr/sbin/rfkill"
smbOptions="min receivefile size = 16384\nwrite cache size = 524288\ngetwd cache = yes\nsocket options = TCP_NODELAY IPTOS_LOWDELAY"
url="https://github.com/OpenMediaVault-Plugin-Developers/packages/raw/master/"
wpaConf="/etc/wpa_supplicant/wpa_supplicant.conf"

export DEBIAN_FRONTEND=noninteractive
export APT_LISTCHANGES_FRONTEND=none
export LANG=C.UTF-8

if [ -f /etc/armbian-release ]; then
  . /etc/armbian-release
fi

while getopts "fhn" opt; do
  echo "option ${opt}"
  case "${opt}" in
    f)
      skipFlash=1
      ;;
    h)
      echo "Use the following flags:"
      echo "  -f"
      echo "    to skip the installation of the flashmemory plugin"
      echo "  -n"
      echo "    to skip the network setup"
      echo ""
      echo "Examples:"
      echo "  install"
      echo "  install -f"
      echo "  install -n"
      exit 100
      ;;
    n)
      skipNet=1
      ;;
    \?)
      echo "Invalid option: -${OPTARG}"
      ;;
  esac
done

# Fix permissions on / if wrong
echo "Current / permissions = $(stat -c %a /)"
chmod g-w,o-w /
echo "New / permissions = $(stat -c %a /)"

echo "Updating repos before installing..."
apt-get update

echo "Installing lsb_release..."
apt-get --yes --no-install-recommends --reinstall install lsb-release

arch="$(dpkg --print-architecture)"
codename="$(lsb_release --codename --short)"

case ${codename} in
  stretch)
    confCmd="omv-mkconf"
    network="interfaces"
    ntp="ntp"
    omvCodename="arrakis"
    phpfpm="php-fpm"
    version=4
    ;;
  buster)
    confCmd="omv-salt deploy run"
    network="systemd-networkd"
    ntp="chrony"
    omvCodename="usul"
    phpfpm="phpfpm"
    version=5
    ;;
  *)
    echo "Unsupported version.  Exiting..."
    exit 1
  ;;
esac
echo "${omvCodename} :: ${version}"

hostname=$(</etc/hostname)
tz=$(</etc/timezone)

# Add Debian signing keys to raspbian to prevent apt-get update failures
# when OMV adds security and/or backports repos
if grep -q raspberrypi.org /etc/apt/sources.list.d/*; then
  echo "Adding Debian signing keys..."
  for key in AA8E81B4331F7F50 112695A0E562B32A 04EE7237B7D453EC 648ACFD622F3D138; do
    apt-key adv --no-tty --keyserver ${keyserver} --recv-keys "${key}"
  done
  echo "Installing monit from raspberrypi repo..."
  apt-get --yes --no-install-recommends install -t ${codename} monit
fi

echo "Install prerequisites..."
apt-get --yes --no-install-recommends install dirmngr gnupg

# install openmediavault if not installed already
omvInstall=$(dpkg -l | awk '$2 == "openmediavault" { print $1 }')
if [[ ! "${omvInstall}" == "ii" ]]; then
  echo "Installing openmediavault required packages..."
  if ! apt-get --yes --no-install-recommends install postfix; then
    echo "failed installing postfix"
    exit 2
  fi

  echo "Adding openmediavault repo and key..."
  echo "deb ${omvRepo} ${omvCodename} main" > ${omvSources}
  wget -O "${omvKey}" ${omvRepo}/archive.key
  apt-key add "${omvKey}"

  echo "Updating repos..."
  if ! apt-get update; then
    echo "failed to update apt repos."
    exit 2
  fi

  echo "Install openmediavault-keyring..."
  if ! apt-get --yes install openmediavault-keyring; then
    echo "failed to install openmediavault-keyring package."
    exit 2
  fi

  monitInstall=$(dpkg -l | awk '$2 == "monit" { print $1 }')
  if [[ ! "${monitInstall}" == "ii" ]]; then
    if ! apt-get --yes --no-install-recommends install monit; then
      echo "failed installing monit"
      exit 2
    fi
  fi

  echo "Installing openmediavault..."
  aptFlags="--yes --auto-remove --show-upgraded --allow-downgrades --allow-change-held-packages --no-install-recommends"
  cmd="apt-get ${aptFlags} install openmediavault"
  if ! ${cmd}; then
    echo "failed to install openmediavault package."
    exit 2
  fi

  if [ ${version} -gt 4 ]; then
    omv-confdbadm populate
  else
    omv-initsystem
    omv-mkconf interfaces
    omv-mkconf issue
  fi
fi

# check if openmediavault is install properly
omvInstall=$(dpkg -l | awk '$2 == "openmediavault" { print $1 }')
if [[ ! "${omvInstall}" == "ii" ]]; then
  echo "openmediavault package failed to install or is in a bad state."
  exit 3
fi

. /etc/default/openmediavault
. /usr/share/openmediavault/scripts/helper-functions

# remove backports from sources.list to avoid duplicate sources warning
sed -i "/\(stretch\|buster\)-backports/d" /etc/apt/sources.list

if [ "${codename}" = "eoan" ]; then
  omv_set_default "OMV_APT_USE_KERNEL_BACKPORTS" false true
fi

# install omv-extras
echo "Downloading omv-extras.org plugin for openmediavault ${version}.x ..."
file="openmediavault-omvextrasorg_latest_all${version}.deb"

if [ -f "${file}" ]; then
  rm ${file}
fi
wget ${url}/${file}
if [ -f "${file}" ]; then
  if ! dpkg --install ${file}; then
    echo "Installing other dependencies ..."
    apt-get --yes --fix-broken install
    omvextrasInstall=$(dpkg -l | awk '$2 == "openmediavault-omvextrasorg" { print $1 }')
    if [[ ! "${omvextrasInstall}" == "ii" ]]; then
      echo "omv-extras failed to install correctly.  Trying to fix with ${confCmd} ..."
      if ${confCmd} omvextras; then
        echo "Trying to fix apt ..."
        apt-get --yes --fix-broken install
      else
        echo "${confCmd} failed and openmediavault-omvextrasorg is in a bad state."
        exit 3
      fi
    fi
    omvextrasInstall=$(dpkg -l | awk '$2 == "openmediavault-omvextrasorg" { print $1 }')
    if [[ ! "${omvextrasInstall}" == "ii" ]]; then
      echo "openmediavault-omvextrasorg package failed to install or is in a bad state."
      exit 3
    fi
  fi

  echo "Updating repos ..."
  apt-get update
else
  echo "There was a problem downloading the package."
fi

# disable armbian log services if found
for service in log2ram armbian-ramlog armbian-zram-config; do
  if systemctl list-units --full -all | grep ${service}; then
    systemctl stop ${service}
    systemctl disable ${service}
  fi
done
rm -f /etc/cron.daily/armbian-ram-logging
if [ -f "/etc/default/armbian-ramlog" ]; then
  sed -i "s/ENABLED=.*/ENABLED=false/g" /etc/default/armbian-ramlog
fi
if [ -f "/etc/default/armbian-zram-config" ]; then
  sed -i "s/ENABLED=.*/ENABLED=false/g" /etc/default/armbian-zram-config
fi
if [ -f "/etc/systemd/system/logrotate.service" ]; then
  rm -f /etc/systemd/system/logrotate.service
  systemctl daemon-reload
fi

# install flashmemory plugin unless disabled
if [ ${skipFlash} -eq 1 ]; then
  echo "Skipping installation of the flashmemory plugin."
else
  echo "Install folder2ram..."
  if apt-get --yes --fix-missing --no-install-recommends install folder2ram; then
    echo "Installed folder2ram."
  else
    echo "Failed to install folder2ram."
  fi
  echo "Install flashmemory plugin..."
  if apt-get --yes install openmediavault-flashmemory; then
    echo "Installed flashmemory plugin."
  else
    echo "Failed to install flashmemory plugin."
    ${confCmd} flashmemory
    apt-get --yes --fix-broken install
  fi
fi

# change default OMV settings
omv_config_update "/config/services/smb/extraoptions" "$(echo -e "${smbOptions}")"
omv_config_update "/config/services/ssh/enable" "1"
omv_config_update "/config/services/ssh/permitrootlogin" "1"
omv_config_update "/config/system/time/ntp/enable" "1"
omv_config_update "/config/system/time/timezone" "${tz}"
omv_config_update "/config/system/network/dns/hostname" "${hostname}"

# disable monitoring and apply changes
echo "Disabling data collection ..."
/usr/sbin/omv-rpc -u admin "perfstats" "set" '{"enable":false}'
/usr/sbin/omv-rpc -u admin "config" "applyChanges" '{ "modules": ["monit","rrdcached","collectd"],"force": true }'

# set min/max frequency and watchdog for RPi boards
if [[ $(awk '$1 == "Model" { print $3 }' /proc/cpuinfo) = "Raspberry" ]]; then
  omv_set_default "OMV_WATCHDOG_DEFAULT_MODULE" "bcm2835_wdt"
  omv_set_default "OMV_WATCHDOG_CONF_WATCHDOG_TIMEOUT" "14"

  MIN_SPEED="$(</sys/devices/system/cpu/cpufreq/policy0/cpuinfo_min_freq)"
  MAX_SPEED="$(</sys/devices/system/cpu/cpufreq/policy0/cpuinfo_max_freq)"
  # Determine if RPi4 (for future use)
  if [[ $(awk '$1 == "Revision" { print $3 }' /proc/cpuinfo) =~ [a-c]03111 ]]; then
    BOARD="rpi4"
  fi
  cat << EOF > ${cpuFreqDef}
GOVERNOR="ondemand"
MIN_SPEED="${MIN_SPEED}"
MAX_SPEED="${MAX_SPEED}"
EOF
fi

if [ -f "${cpuFreqDef}" ]; then
  . ${cpuFreqDef}
else
  # set cpufreq settings if no defaults
  if [ -f "/proc/config.gz" ]; then
    defaultGov="$(zgrep "${defaultGovSearch}" /proc/config.gz | sed -e "s/${defaultGovSearch}\(.*\)=y/\1/")"
  elif [ -f "/boot/config-$(uname -r)" ]; then
    defaultGov="$(grep "${defaultGovSearch}" /boot/config-$(uname -r) | sed -e "s/${defaultGovSearch}\(.*\)=y/\1/")"
  fi
  if [ -z "${DEFAULT_GOV}" ]; then
    defaultGov="ondemand"
  fi
  GOVERNOR=${defaultGov,,}
  MIN_SPEED="0"
  MAX_SPEED="0"
fi

# set defaults in /etc/default/openmediavault
omv_set_default "OMV_CPUFREQUTILS_GOVERNOR" "${GOVERNOR}"
omv_set_default "OMV_CPUFREQUTILS_MINSPEED" "${MIN_SPEED}"
omv_set_default "OMV_CPUFREQUTILS_MAXSPEED" "${MAX_SPEED}"

if [ ${version} -gt 4 ]; then
  # update pillar default list - /srv/pillar/omv/default.sls
  omv-salt stage run prepare
fi

# update config files
for service in nginx ${phpfpm} samba flashmemory ssh ${ntp} timezone monit rrdcached collectd cpufrequtils apt watchdog; do
  ${confCmd} ${service}
done

# create php directories if they don't exist
modDir="/var/lib/php/modules"
if [ ! -d "${modDir}" ]; then
  mkdir --parents --mode=0755 ${modDir}
fi
sessDir="/var/lib/php/sessions"
if [ ! -d "${sessDir}" ]; then
  mkdir --parents --mode=1733 ${sessDir}
fi

if [[ "${arch}" == "amd64" ]] || [[ "${arch}" == "i386" ]]; then
  # skip ionice on x86 boards
  echo "Done."
  exit 0
fi

# Add a cron job to make NAS processes more snappy and silence rsyslog
cat << EOF > /etc/rsyslog.d/omv-armbian.conf
:msg, contains, "omv-ionice" ~
:msg, contains, "action " ~
:msg, contains, "netsnmp_assert" ~
:msg, contains, "Failed to initiate sched scan" ~
EOF
systemctl restart rsyslog

# add taskset to ionice cronjob for biglittle boards
case ${BOARD} in
  odroidxu4|bananapim3|nanopifire3|nanopct3plus|nanopim3)
    taskset='; taskset -c -p 4-7 ${srv}'
    ;;
  *rk3399*|*edge*|nanopct4|nanopim4|nanopineo4|renegade-elite|rockpi-4*|rockpro64|helios64)
    taskset='; taskset -c -p 4-5 ${srv}'
    ;;
  odroidn2)
    taskset='; taskset -c -p 2-5 ${srv}'
    ;;
esac

# create ionice script
cat << EOF > ${ioniceScript}
#!/bin/sh

for srv in \$(pgrep "ftpd|nfsiod|smbd"); do
  ionice -c1 -p \${srv} ${taskset};
done
EOF
chmod 755 ${ioniceScript}

# create ionice cronjob
cat << EOF > ${ioniceCron}
* * * * * root ${ioniceScript} >/dev/null 2>&1
EOF
chmod 600 ${ioniceCron}

# add pi user to ssh group if it exists
if getent passwd pi > /dev/null; then
  echo "Adding pi user to ssh group ..."
  usermod -a -G ssh pi
fi

# add user running the script to ssh group if not pi or root
if [ -n "${USER}" ] && [ ! "${USER}" = "root" ] && [ ! "${USER}" = "pi" ]; then
  if getent passwd ${USER} > /dev/null; then
    echo "Adding ${USER} to the ssh group ..."
    usermod -a -G ssh ${USER}
  fi
fi

# remove networkmanager and dhcpcd5 then configure networkd
if [ ${version} -gt 4 ] && [ ${skipNet} -ne 1 ]; then

  defLink="/etc/systemd/network/99-default.link"
  if [ -e "${defLink}" ]; then
    rm -fv "${defLink}"
  fi

  echo "Removing network-manager and dhcpcd5 ..."
  apt-get -y --autoremove purge network-manager dhcpcd5

  echo "Enable and start systemd-resolved ..."
  systemctl enable systemd-resolved
  systemctl start systemd-resolved
  rm /etc/resolv.conf
  ln -s /run/systemd/resolve/resolv.conf /etc/resolv.conf

  if [ -f "${rfkill}" ]; then
    echo "Unblocking wifi with rfkill ..."
    ${rfkill} unblock all
  fi

  for nic in $(ls /sys/class/net | grep -vE "br-|docker|dummy|lo|tun|virbr"); do
    if grep -q "<devicename>${nic}</devicename>" ${OMV_CONFIG_FILE}; then
      echo "${nic} already found in database.  Skipping..."
      continue
    fi

    if udevadm info /sys/class/net/${nic} | grep -q wlan; then
      if [ -f "${wpaConf}" ]; then
        country=$(awk -F'=' '/country=/{gsub(/["\r]/,""); print $NF}' ${wpaConf})
        wifiName=$(awk -F'=' '/ssid="/{st=index($0,"="); ssid=substr($0,st+1); gsub(/["\r]/,"",ssid); print ssid; exit}' ${wpaConf})
        wifiPass=$(awk -F'=' '/psk="/{st=index($0,"="); pass=substr($0,st+1); gsub(/["\r]/,"",pass); print pass; exit}' ${wpaConf})

        if [ -n "${country}" ] && [ -n "${wifiName}" ] && [ -n "${wifiPass}" ]; then
          if [ -f "${crda}" ]; then
            awk -i inplace -F'=' -v country="$country" '/REGDOMAIN=/{$0=$1"="country} {print $0}' ${crda}
          fi
          echo "Adding ${nic} to openmedivault database ..."
          jq --null-input --compact-output \
            "{uuid: \"${OMV_CONFIGOBJECT_NEW_UUID}\", devicename: \"${nic}\", type: \"wifi\", method: \"dhcp\", method6: \"dhcp\", wpassid: \"${wifiName}\", wpapsk: \"${wifiPass}\"}" | \
            omv-confdbadm update "conf.system.network.interface" -
          if grep -q "<devicename>${nic}</devicename>" ${OMV_CONFIG_FILE}; then
            cfg=1
          fi
        fi
      fi
    else
      echo "Adding ${nic} to openmedivault database ..."
      jq --null-input --compact-output \
        "{uuid: \"${OMV_CONFIGOBJECT_NEW_UUID}\", devicename: \"${nic}\", method: \"dhcp\", method6: \"dhcp\"}" | \
        omv-confdbadm update "conf.system.network.interface" -
      if grep -q "<devicename>${nic}</devicename>" ${OMV_CONFIG_FILE}; then
        cfg=1
      fi
    fi
  done

  if [ ${cfg} -eq 1 ]; then
    echo "IP address may change and you could lose connection if running this script via ssh."

    # create config files
    ${confCmd} ${network}

    echo "Network setup for DHCP.  Rebooting..."
    reboot
  else
    echo "It is recommended to reboot and then setup the network adapter in the openmediavault web interface."
  fi

fi

exit 0
```

```shell
sudo chmod a+x install.sh
sudo bash install.sh
```

# Docker安装 Qbittorrentee

```shell
docker create  \
    --name=qbittorrentee  \
    -e WEBUIPORT=8080  \
    -e PUID=1026 \
    -e PGID=100 \
    -e TZ=Asia/Shanghai \
    -p 6881:6881  \
    -p 6881:6881/udp  \
    -p 8080:8080  \
    -v /home/docker/btee/config:/config  \
    -v /srv/dev-disk-by-uuid-3E387BD3387B88A3/BT:/downloads  \
    --restart unless-stopped  \
    
docker run -d \
  --name=qbittorrent \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -e WEBUI_PORT=8080 \
  -p 6881:6881 \
  -p 6881:6881/udp \
  -p 8080:8080 \
  -v /home/docker/bt/config:/config \
  -v /srv/dev-disk-by-uuid-3E387BD3387B88A3/BT:/downloads \
  -v /srv/dev-disk-by-uuid-B06CDF606CDF2040/BT:/downloadss \
  --restart unless-stopped \
  linuxserver/qbittorrent
```

# Docker 安装  Aria2

```shell
docker run -d \
  --name aria2-pro \
  --restart unless-stopped \
  --log-opt max-size=1m \
  -e PUID=$UID \
  -e PGID=$GID \
  -e UMASK_SET=022 \
  -e RPC_SECRET=970829 \
  -e RPC_PORT=6800 \
  -p 6800:6800 \
  -e LISTEN_PORT=6888 \
  -p 6888:6888 \
  -p 6888:6888/udp \
  -v /home/docker/aria2/config:/config \
  -v /srv/dev-disk-by-uuid-3E387BD3387B88A3/BT:/downloads \
  p3terx/aria2-pro

# 这个没有v7 架构不好使
docker run -d \
  --name ariang \
  --log-opt max-size=1m \
  --restart unless-stopped \
  -p 6880:6880 \
  p3terx/ariang

# v7 架构 树莓派可以用 	这个是ui和aria2 集成在一起的
docker run -d --name ariang -p 6880:80 -p 6800:6800 -p 443:443 -e ENABLE_AUTH=true -e RPC_SECRET=970829 -e ARIA2_USER=yby -e ARIA2_PWD=970829 -v /srv/dev-disk-by-uuid-3E387BD3387B88A3/BT:/data -v /home/docker/aria2/config:/root/conf/key huangzulin/aria2-ui-pi
# 加下面这个出错，没找到原因
 -v /home/docker/aria2/aria2.conf:/root/conf/aria2.conf
  
docker run -d \
  --name=transmission \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -e TRANSMISSION_WEB_HOME=/combustion-release/ `#optional` \
  -e USER=username `#optional` \
  -e PASS=password `#optional` \
  -e WHITELIST=iplist `#optional` \
  -p 9091:9091 \
  -p 51413:51413 \
  -p 51413:51413/udp \
  -v /home/docker/transmission/config:/config \
  -v /srv/dev-disk-by-uuid-3E387BD3387B88A3/BT:/downloads \
  -v /home/docker/transmission/watch:/watch \
  --restart unless-stopped \
  ghcr.io/linuxserver/transmission
  

```



# 开启root 登录

```shell
cd /etc/ssh/
vi sshd_config

permitRootLogin yes # prohibit-password # 将这一段改成这样

service ssh restart # 重启ssh 服务

```

# 安装OMV

```shell

wget --no-check-certificate -O - https://github.com/OpenMediaVault-Plugin-Developers/installScript/raw/master/install | sudo bash

```

##  OMV 5 换源

注意

这部分内容适用于 OMV5

### 一、编辑 sources.list

#### 1. 备份配置文件

```shell
$ sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak
```

#### 2. 清空配置文件

```shell
$ sudo sh -c 'echo > /etc/apt/sources.list'
```

#### 3. 编辑配置文件

```shell
$ sudo nano /etc/apt/sources.list
```

**复制并粘贴以下内容：**

> 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释

```shell
deb http://mirrors.tuna.tsinghua.edu.cn/debian/ buster main
# deb-src http://mirrors.tuna.tsinghua.edu.cn/debian/ buster main

deb http://mirrors.tuna.tsinghua.edu.cn/debian-security buster/updates main contrib non-free
# deb-src http://mirrors.tuna.tsinghua.edu.cn/debian-security buster/updates main contrib non-free

deb http://mirrors.tuna.tsinghua.edu.cn/debian/ buster-updates main contrib non-free
# deb-src http://mirrors.tuna.tsinghua.edu.cn/debian/ buster-updates main contrib non-free
```

### 二、编辑 openmediavault-kernel-backports.list

#### 1. 备份配置文件

```shell
$ sudo cp /etc/apt/sources.list.d/openmediavault-kernel-backports.list /etc/apt/sources.list.d/openmediavault-kernel-backports.list.bak
```

#### 2. 清空配置文件

```shell
$ sudo sh -c 'echo > /etc/apt/sources.list.d/openmediavault-kernel-backports.list'
```

#### 3. 编辑配置文件

```shell
$ sudo nano /etc/apt/sources.list.d/openmediavault-kernel-backports.list
```

**复制并粘贴以下内容：**

```text
deb https://mirrors.tuna.tsinghua.edu.cn/debian buster-backports main contrib non-free
```

### 三、编辑 openmediavault.list

#### 1. 备份配置文件

```shell
$ sudo cp /etc/apt/sources.list.d/openmediavault.list /etc/apt/sources.list.d/openmediavault.list.bak
```

#### 2. 清空配置文件

```shell
$ sudo sh -c 'echo > /etc/apt/sources.list.d/openmediavault.list'
```

#### 3. 编辑配置文件

```shell
$ sudo nano /etc/apt/sources.list.d/openmediavault.list
```

**复制并粘贴以下内容：**

```text
deb https://mirrors.tuna.tsinghua.edu.cn/OpenMediaVault/public/ usul main
```

### 四、编辑 omvextras.list

#### 1. 备份配置文件

```shell
$ sudo cp /etc/apt/sources.list.d/omvextras.list /etc/apt/sources.list.d/omvextras.list.bak
```

#### 2. 清空配置文件

```shell
$ sudo sh -c 'echo > /etc/apt/sources.list.d/omvextras.list'
```

#### 3. 编辑配置文件

```shell
$ sudo nano /etc/apt/sources.list.d/omvextras.list
```

**复制并粘贴以下内容：**

```text
deb https://mirrors.tuna.tsinghua.edu.cn/OpenMediaVault/openmediavault-plugin-developers/usul buster main
deb [arch=armhf] https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/debian buster stable
deb http://linux.teamviewer.com/deb stable main
```

# 树莓派 vim 上下左右 退格不好使

```shell

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
framerate 80 # 帧
stream_maxrate 80 # 最大帧
stream_localhost off # 只允许本地访问设为 off
```

- **motion基本操作命令** 

  启动摄像头 :            

```ruby
$sudo motion
```

 	关闭摄像头（root用户）:

```markdown
# service motion stop
```

在浏览器中键入树莓派ip和端口号，就可以看到摄像头拍到的图像了。

## 问题

### 视频卡顿
motion的配置文件中关于framerate，由两个参数控制：framerate & stream_maxrate。maxrate决定了上限。起初只设置了framerate为100,但maxrate仍然是1,因此会出现卡顿。

### 重影

```shell
apt update：只检查，不更新（已安装的软件包是否有可用的更新，给出汇总报告）

用法：sudo apt update


apt upgrade：更新已安装的软件包

用法：sudo apt upgrade 软件包名
```

