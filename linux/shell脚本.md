# shell 编程

- 运行脚本文件的方式
  - bash test.sh
  - source test.sh
  - ./test.sh
    - 如果要以此种方式执行脚本，该脚本必须要有可执行权限
    - chmod a+x add.sh

- Shell 脚本首行通过注释的方式表示执行脚本的程序

- 常见方式有

  - \#!/bin/sh

  - \#!/bin/bash
  - \#!/usr/bin/env bash
  - python脚本的第一句一般是   #!/usr/bin/env python

- 字符串可以有引号也可以没引号
  - 单引号双引号，以及反引号都可以，
  - 反引号里面的内容会解释成，Linux命令  ``
- echo 代表输出
- a=10 shell里定义了一个变量，**等号两端不能有空格**
- $a 获取变量值 不能写在单引号中
- **单引号的内容会原样输出**
- ${a}也可以用来取值 {}一般情况下可以省略
- $ 符的作用
  - $(cmd)命令
  - $((1+1))
  - 特殊的值 $0 表示的是脚本文件的名字
  - 特殊的值 $1~n 表示的是脚本文件参数的名字 
  - 特殊的值 $* 表示的是脚本文件参数的所有名字 
  - 特殊的值 $@ 表示的是脚本文件参数的个数
  - 特殊的值 $# 表示的是脚本文件参数的所有名字 
  - 特殊的值 $? 表示的是脚本文件的执行结果
    - 0表示执行执行完成，正常退出
    - 不是0表示执行异常

- export x=abc export 代表环境变量
- \$PWD \$USER  \$HOME

- export PATH=$PATH:自己的环境变量

- read -p '请输入您的年龄' age

- echo $age

- ```- 
  if ls /;then
  	echo '命令执行成功了'
  else 
  	echo '命令执行失败了'
  fi
  ```

- ```el
  // shell 编程 判断语句不能用><号
  // 他有三种比较方式
  // 数字比较，字符串比较，文件比较
  // 比较的时候要加[]
  // 条件测试命令 
  // -eq 等于 equal
  // -ge 大于等于 greater equal
  // -gt 大于 greater than
  // -le 小于等于 less equal
  // -lt 小于 less than
  // -ne 不等于  not equal
  if [ 3 -gt 2 ];then
  	echo 3>2
  else
  	echo 3<2
  fi
  ```

- 字符串比较

  ```
  if [ str1 = str2 ]
  if [[ str1 > str2 ]]  #字符串比较必须再加一个[] 
  ```

- -d 判断是不是一个文件夹 还有其他的上网上搜去吧

  ```
  if [ -d  $path ];then
  	echo $path是一个文件夹
  else
  	echo $path不是一个文件夹
  fi
  
  ```

  

- case 语句

  ```
  read -p 请输入命令 po
  case $op in
  	1)
  		echo 添加用户
  		;;
  	2)
  		echo 删除用户
  		;;
  	3）
  		echo 查询用户
  		;;
  	*)
  		echo 输入的操作不正确
  		;;
  esac
  ```

  

- for 变量名 in 列表;do
  循环体
  done

- ```
  for i in`seq 1 10
  do
  	if [ $[ $i % 2 ] == 0 ]
  	then
  		echo 偶数$i
  	else
  		echo 奇数$i
  	fi
  done
  ```

  \$[ $i % 2 ] 进行基本的数学运算

  seq satrt end 产生一个数字序列

  {1..100..2} 从一到100间隔2位数和python 的 [1\:100\:2]

  ```
  for((j=0;j<10;j++))
  do
  	echo $i
  done 
  ```

  

- while CONDITION; do
  循环体
  done

- ```shell
  while [ $# -gt 0 ]
  do
      id $1 &>/dev/null
      if [ $? -eq 0 ];then
          echo $1 is already exsit.
          shift
          continue
      fi
      useradd $1
      echo "$1 用户创建成功"
      shift
   
  done
  ```

- 函数

  - ```shell
    function foo(){
    	echo app
    	echo good
    }
    foo
    
    foo(){
    	echo $0
    	echo $1
    	echo $#
    	...
    	echo app
    	echo good
    }
    foo 1 2 3 4
    ```

    

- 数组

  - names=(1 2 3 hellow)

  - 拿的话需要 ${names[0]}

  - ${} 中的{} 一般情况下可以省略，但是在数组里不行

  - 如果省略会出现 1[3] 的情况 $直接输出names[0]然后再加上[3]

  - ${names[*]}

  - ${names[@]} 都可以拿到所有数据

  - ￥{#names[*]} 获取长度

  - ```
    for i in ${names[*]}
    do
    	echo $i
    done
    for((i=0;i<${#names[*]};i++))
    do
    	echo ${names[i]}
    done 
    ```

    