Arduino 基础操作

## 一 Arduino 软件安装

> https://www.arduino.cc/en/software
>
> https://www.kancloud.cn/yundantiankong/arduino_examples/431713 **基础教程**

### 1.1 软件配置 

> 需要在安装完驱动之后或者是原厂开发板的情况下
>
> 也就是电脑能识别的情况下

- 工具 => 串口监视器 选择串口
- 工具 => 选择开发板

## 二 安装CH340 驱动

> http://www.wch.cn/products/CH340.html

### 2.1 为什么要安装驱动

- arduino 开发板分为 原厂版 和 开发板（副厂）

  - 因为arduino 是开源项目所以工厂可以获取全部数据（设计图）所以有副厂版本，但是结果是一样的

  - 他们两块板子的唯二区别是原厂板子可以使用arduino 的商标，以及他们用的usb转化 模块（处理电脑传过来的信息）不一样

  - 这也导致了副厂板子得使用CH340（便宜） 驱动，才能和电脑建立通信

  - 下面两张图片就是原厂和副厂的板子

    ![img](.\images\arduino原厂.jpeg)

    ![img](G:\新知识\树莓派\images\arduino副厂.jpeg)

## 三 实例

### 目录

```javascript
examples
├─01.Basics 较为基础的例程
│  ├─AnalogReadSerial 模拟输入和串口操作：通过模拟输入读取电位器的值，并把结果输出到Arduino串口监视器(Serial Monitor) 
│  ├─BareMinimum arduino程序最基本的结构
│  ├─Blink 让arduino板上的13引脚所连接的LED闪烁
│  ├─DigitalReadSerial 数字输入：读取按钮开关的值，并输出到串口监视器，
│  ├─Fade 模拟输出，呼吸灯：让一个LED的亮度渐弱
│  └─ReadAnalogVoltage 读取模拟电压：读取模拟输入的值，并换算成电压，显示到串口监视器，
├─02.Digital 数字引脚操作
│  ├─BlinkWithoutDelay  不用delay函数闪烁led，
│  ├─Button 按钮：使用按钮，控制LED，
│  ├─Debounce 按钮去抖动：读取一个按钮状态，并且滤去干扰
│  ├─DigitalInputPullup 数字引脚上的拉电阻：pinMode()函数INPUT_PULLUP参数的使用
│  ├─StateChangeDetection 探测按钮状的态改变：按钮按下次数计数
│  ├─toneKeyboard 三键电子琴：使用压力传感器和压电扬声器制作三键电子琴
│  ├─toneMelody 使用tone播放乐曲
│  ├─toneMultiple 多个扬声器播放乐曲：使用tone()函数操作多个扬声器播放曲调
│  └─tonePitchFollower 光感琴：根据外界光照的不同，播放不同的曲调，
├─03.Analog 模拟信号操作
│  ├─AnalogInOutSerial 模拟信号与串口：根据电位器读出的值来控制led的亮暗，
│  ├─AnalogInput 模拟信号输入：根据电位器的值来控制led闪烁的时间间隔，
│  ├─AnalogWriteMega 模拟信号输出：12个按照呼吸灯变化的led流水灯，
│  ├─Calibration 模拟信号的校准：根据光敏电阻的值来调节led的亮暗，
│  ├─Fading 呼吸灯：使用脉宽引脚（PWM pin）来让一个LED的亮度渐弱
│  └─Smoothing 输入信号平滑处理：多个模拟引脚的输入值变得更加均匀平滑
├─04.Communication 通信
│  ├─ASCIITable ASCIl表：通过串口输出ASCII码表，
│  ├─Dimmer 调光器：与processing通信，通过移动鼠标来改变led的亮度，
│  ├─Graph 数据图表：与processing通信，绘制电位器的数据图像，
│  ├─Midi MIDI音乐：串口发送MIDI音符
│  ├─MultiSerial 多串口：使用Arduino Mega上的两个串口
│  ├─PhysicalPixel 控制LED：与processing通信，控制led，
│  ├─ReadASCIIString 读取ASCII字符串：通过串口读的数值控制REG LED，
    │  ├─SerialCallResponse 串口双向调用 (握手连接)：使用握手方式发送多个变量，
│  ├─SerialCallResponseASCII 串口双向调用(使用ASCII字符串)：使用握手方式发送多个变量，并且在转发之前将这些变量的值通过ASCII解码为字符串。
│  ├─SerialEvent 串口事件：串口高级用法SerialEvent举例
│  ├─SerialPassthrough 一个板子上，同时用两个串口通信，
│  └─VirtualColorMixer  虚拟调色盘：与processing通信，通过串口发送多个数据，来控制电脑端的颜色，
├─05.Control 结构控制
│  ├─Arrays 数组举例：通过for循环来展示如何使用数组
│  ├─ForLoopIteration for循环示例：用for循环控制多个LED
│  ├─IfStatementConditional if判断语句：使用if语句根据输入的条件的变化改变输出条件
│  ├─switchCase switchCase语句：从一堆不连续的数字中找到需要的数字
│  ├─switchCase2 switchCase语句：根据串口的输入值来采取不同的动作
│  └─WhileStatementConditional While语句：使用while循环来在按钮被按下时校准传感器
├─06.Sensors 传感器
│  ├─ADXL3xx 加速度计：读取ADXL3xx加速度计
│  ├─Knock 检测碰撞：用压电元件来检测碰撞
│  ├─Memsic2125 加速度计：两轴加速度计
│  └─Ping 超声波测距：使用超声波来检测物体的远近
├─07.Display 显示
│  ├─barGraph 电位器控制LED光带长度，
│  └─RowColumnScanning 8*8点针扫描控制，
├─08.Strings 字符串
│  ├─CharacterAnalysis 字符串分析：使用操作符(operators )来识别我们正在处理的字符串
│  ├─StringAdditionOperator 字符串连接：以多种方式将字符串连接在一起
│  ├─StringAppendOperator 字符串扩充：使用 += 操作符和concat()方法将字符串扩充
│  ├─StringCaseChanges 字符串大小写转换
│  ├─StringCharacters 得到字符串中特定的字符
│  ├─StringComparisonOperators 字符串比较：用字母表顺序比较字符串
│  ├─StringConstructors 字符串初始化
│  ├─StringIndexOf 字符串索引：获取字符串中第一个/最后一个字符
│  ├─StringLength 字符串长度：获取并且修正字符串长度
│  ├─StringLengthTrim  字符串修剪
│  ├─StringReplace 字符串替换：替换字符串中的字符
│  ├─StringStartsWithEndsWith 检查字符串开始结尾：检查（子）字符串是否是以给定字符开始/结尾的
│  ├─StringSubstring 字符串查找：在指定字符串中找到某个词组
│  └─StringToInt 字符串转换成整数类型
├─09.USB USB设备
│  ├─Keyboard 键盘
│  │  ├─KeyboardLogout 注销电脑
│  │  ├─KeyboardMessage 钮按下时发送字符串
│  │  ├─KeyboardReprogram 控制Arduino IDE：自动打开Arduino IDE并自动给一块Leonardo写简单的blink程序
│  │  └─KeyboardSerial 从串口读取后发回一个按键信息
│  ├─KeyboardAndMouseControl 鼠标和键盘示例
│  └─Mouse 鼠标
│  ├─ButtonMouseControl 控制鼠标移动：用5个按钮控制鼠标移动
│  └─JoystickMouseControl 用摇杆控制鼠标：当按钮按下时用摇杆控制鼠标移动
├─10.StarterKit_BasicKit  初学者套件(Starterkit)和基本套件(BasicKit)
│  ├─p02_SpaceshipInterface
│  ├─p03_LoveOMeter
│  ├─p04_ColorMixingLamp
│  ├─p05_ServoMoodIndicator
│  ├─p06_LightTheremin
│  ├─p07_Keyboard
│  ├─p08_DigitalHourglass
│  ├─p09_MotorizedPinwheel
│  ├─p10_Zoetrope
│  ├─p11_CrystalBall
│  ├─p12_KnockLock
│  ├─p13_TouchSensorLamp
│  ├─p14_TweakTheArduinoLogo
│  └─p15_HackingButtons
└─11.ArduinoISP
   └─ArduinoISP
```

###  较为基础的例程(Basics)

```
    ├─01.Basics
    │  ├─AnalogReadSerial 模拟输入和串口 ，读取电位器的值，并打印它的状态到**Arduino串口监视器**(Serial Monitor)
    │  ├─BareMinimum 最基本的arduino程序结构，
    │  ├─Blink 让13引脚的LED闪烁，
    │  ├─DigitalReadSerial 数字输入，读取按钮的值，并输出到串口监视器，
    │  ├─Fade 模拟输出，呼吸灯，让一个LED的亮度渐弱
    │  └─ReadAnalogVoltage 读取模拟输入的值，并换算成电压，显示到串口监视器，制作一个简易电压表
```

### 数字引脚操作

------

```
   ├─02.Digital 数字引脚操作
    │  ├─BlinkWithoutDelay  不用delay函数闪烁led，
    │  ├─Button 按钮：使用按钮，控制LED，
    │  ├─Debounce 按钮去抖动：读取一个按钮状态，并且滤去干扰
    │  ├─DigitalInputPullup 数字引脚上的拉电阻：pinMode()函数INPUT_PULLUP参数的使用
    │  ├─StateChangeDetection 探测按钮状的态改变：按钮按下次数计数
    │  ├─toneKeyboard 三键电子琴：使用压力传感器和压电扬声器制作三键电子琴
    │  ├─toneMelody 使用tone播放乐曲
    │  ├─toneMultiple 多个扬声器播放乐曲：使用tone()函数操作多个扬声器播放曲调
    │  └─tonePitchFollower 光感琴：根据外界光照的不同，播放不同的曲调，
```

### 模拟信号操作

------

```
    ├─03.Analog 模拟信号操作
    │  ├─AnalogInOutSerial 模拟信号与串口：根据电位器读出的值来控制led的亮暗，
    │  ├─AnalogInput 模拟信号输入：根据电位器的值来控制led闪烁的时间间隔，
    │  ├─AnalogWriteMega 模拟信号输出：12个按照呼吸灯变化的led流水灯，
    │  ├─Calibration 模拟信号的校准：根据光敏电阻的值来调节led的亮暗，
    │  ├─Fading 呼吸灯：使用脉宽引脚（PWM pin）来让一个LED的亮度渐弱
    │  └─Smoothing 输入信号平滑处理：多个模拟引脚的输入值变得更加均匀平滑
```

### 通信

> 这些例子包含Arduino与运行在电脑上的**Processing程序**通信的代码。
> 关于Processing更多信息，请访问其[官方网站](https://processing.org/)
> 例子中也含有能与Arduino工程通信的**Max/MSP**的**程序包**（patch）。想要了解更多信息请看[Cycling 74](https://cycling74.com/)。

> 有与Arduino内容重复的。
> 希望多关注Processing代码，来学习Processing的使用。

------

```
    ├─04.Communication 通信
    │  ├─ASCIITable ASCIl表：通过串口输出ASCII码表，
    │  ├─Dimmer 调光器：与processing通信，通过移动鼠标来改变led的亮度，
    │  ├─Graph 数据图表：与processing通信，绘制电位器的数据图像，
    │  ├─Midi MIDI音乐：串口发送MIDI音符
    │  ├─MultiSerial 多串口：使用Arduino Mega上的两个串口
    │  ├─PhysicalPixel 控制LED：与processing通信，控制led，
    │  ├─ReadASCIIString 读取ASCII字符串：通过串口读的数值控制REG LED，
        │  ├─SerialCallResponse 串口双向调用 (握手连接)：使用握手方式发送多个变量，
    │  ├─SerialCallResponseASCII 串口双向调用(使用ASCII字符串)：使用握手方式发送多个变量，并且在转发之前将这些变量的值通过ASCII解码为字符串。
    │  ├─SerialEvent 串口事件：串口高级用法SerialEvent举例
    │  ├─SerialPassthrough 一个板子上，同时用两个串口通信，
    │  └─VirtualColorMixer  虚拟调色盘：与processing通信，通过串口发送多个数据，来控制电脑端的颜色，
```

### 结构控制

```
    ├─05.Control 结构控制
    │  ├─Arrays 数组举例：通过for循环来展示如何使用数组
    │  ├─ForLoopIteration for循环示例：用for循环控制多个LED
    │  ├─IfStatementConditional if判断语句：使用if语句根据输入的条件的变化改变输出条件
    │  ├─switchCase switchCase语句：从一堆不连续的数字中找到需要的数字
    │  ├─switchCase2 switchCase语句：根据串口的输入值来采取不同的动作
    │  └─WhileStatementConditional While语句：使用while循环来在按钮被按下时校准传感器
```

### 传感器

```
    ├─06.Sensors 传感器
    │  ├─ADXL3xx 加速度计：读取ADXL3xx加速度计
    │  ├─Knock 检测碰撞：用压电元件来检测碰撞
    │  ├─Memsic2125 加速度计：两轴加速度计
    │  └─Ping 超声波测距：使用超声波来检测物体的远近
```

### 显示

```
    ├─07.Display 显示
    │  ├─barGraph 电位器控制LED光带长度，
    │  └─RowColumnScanning 8*8点针扫描控制，
```

### 字符串

```
    ├─08.Strings 字符串
    │  ├─CharacterAnalysis 字符串分析：使用操作符(operators )来识别我们正在处理的字符串
    │  ├─StringAdditionOperator 字符串连接：以多种方式将字符串连接在一起
    │  ├─StringAppendOperator 字符串扩充：使用 += 操作符和concat()方法将字符串扩充
    │  ├─StringCaseChanges 字符串大小写转换
    │  ├─StringCharacters 得到字符串中特定的字符
    │  ├─StringComparisonOperators 字符串比较：用字母表顺序比较字符串
    │  ├─StringConstructors 字符串初始化
    │  ├─StringIndexOf 字符串索引：获取字符串中第一个/最后一个字符
    │  ├─StringLength 字符串长度：获取并且修正字符串长度
    │  ├─StringLengthTrim  字符串修剪
    │  ├─StringReplace 字符串替换：替换字符串中的字符
    │  ├─StringStartsWithEndsWith 检查字符串开始结尾：检查（子）字符串是否是以给定字符开始/结尾的
    │  ├─StringSubstring 字符串查找：在指定字符串中找到某个词组
    │  └─StringToInt 字符串转换成整数类型
```

### USB

有关键鼠操作的例程仅仅能在**Leonardo板、Micro板**和**DUE板**上运行, 下面这些例子展示了仅在这三类板上可用的**代码库**(library)的使用。

```
    ├─09.USB USB设备
    │  ├─Keyboard 键盘
    │  │  ├─KeyboardLogout 注销电脑
    │  │  ├─KeyboardMessage 钮按下时发送字符串
    │  │  ├─KeyboardReprogram 控制Arduino IDE：自动打开Arduino IDE并自动给一块Leonardo写简单的blink程序
    │  │  └─KeyboardSerial 从串口读取后发回一个按键信息
    │  ├─KeyboardAndMouseControl 鼠标和键盘示例
    │  └─Mouse 鼠标
    │  ├─ButtonMouseControl 控制鼠标移动：用5个按钮控制鼠标移动
    │  └─JoystickMouseControl 用摇杆控制鼠标：当按钮按下时用摇杆控制鼠标移动
```

### **初学者套件**([Starterkit](http://www.arduino.cc/en/Tutorial/en/Main/ArduinoStarterKit))和**基本套件**([BasicKit](http://www.arduino.cc/en/Tutorial/en/Main/ArduinoBasicKit))

初学者套件中的实例教程已经写在套件提供的书中了，如果你买了基本套件的话，你将能够在[Project Ignite](https://123d.circuits.io/shop/arduino)上看到它们。

```
    ├─10.StarterKit_BasicKit  初学者套件(Starterkit)和基本套件(BasicKit)
    │  ├─p02_SpaceshipInterface
    │  ├─p03_LoveOMeter
    │  ├─p04_ColorMixingLamp
    │  ├─p05_ServoMoodIndicator
    │  ├─p06_LightTheremin
    │  ├─p07_Keyboard
    │  ├─p08_DigitalHourglass
    │  ├─p09_MotorizedPinwheel
    │  ├─p10_Zoetrope
    │  ├─p11_CrystalBall
    │  ├─p12_KnockLock
    │  ├─p13_TouchSensorLamp
    │  ├─p14_TweakTheArduinoLogo
    │  └─p15_HackingButtons
```

## 四 自己写的函数

```c
pinMode(2, INPUT) // 开启指定端口的输入或者输出
pinMode(2, OUTPUT) // 开启指定端口的输入或者输出

Serial.print("hi~~") // 打印不换行
Serial.println("hi~~") // 打印换行
Serial.begin(9600) // 波特率 9600
// 模拟信号只能由 A0 A1 A2 A3 A4 A5 接口读取
// 数字信号可以有其他的端口读取
// sensor 传感器
// Serial 串口（电脑与开发板通信）
// analog 模拟信号
// digital 数字信号
analogRead(A0) // 读取A0口输入的模拟信号
analogWrite(3,0~255) // 三号针脚写入 0~255 值代表亮度 针脚必须前面带有 ~ 号才可以有这个效果 3,5,6,9,10,11（PWM 脉冲宽度调制）

digitalRead(2) // 读取2口的数字信号
map(sensor,0,1023,0,100) // 将传感器的值 0-1023，映射成 0-100 之间的值
// 0,1 引脚是烧写开发板时使用的脚位，在烧写电路板时，不可使用，得拔起来，上传成功后在使用这两个脚位
```

### PWM作用（脉冲宽度调制）

- 通过简单的滤波电路，就可以生成真正的模拟输出量；
- 控制灯光亮度，调节电机转速；请注意这和1不是重复的，因为不需要滤波就可以实现
- 控制舵机角度，这个请参考 [Arduino开发板实验三：舵机控制](https://www.bilibili.com/video/BV1YW411Z76E?p=10&spm_id_from=pageDriver)
- 输出信号，例如接喇叭的时候可以发声 
- 3,5,6,9,10,11引脚

### 伺服电机（SG90 ）

#### 伺服电机 vs 直流马达

> https://blog.csdn.net/weixin_42645653/article/details/112210095

- 伺服电机
  - 接线：3条接线
  - 电源：5V
  - 效果：转特定角度
- 直流电机
  - 接线：2条接线
  - 电源：5V
  - 效果：一直转动

- SG90 伺服电机 (0-180度)
  - 图片
  - <img src="images\伺服电机SG90.jpeg" alt="img" style="zoom: 50%;" />
  - 红线：正极
  - 棕线：负极
  - 黄线：任意数字信号引脚（这个有人说比较特殊要用PWM接口才可以）

#### 代码

```c
#include <Servo.h> 
 
Servo myservo;  // 创建伺服对象以控制伺服电机
                // 大多数板上可以创建十二个伺服对象
 
void setup() 
{ 
  myservo.attach(2);  // 将GIO2上的伺服器连接到伺服对象
} 
 
void loop() 
{ 
  int pos;

  for(pos = 0; pos <= 180; pos += 1) // 从0度到180度
  {                                  // 一步一度 
    myservo.write(pos);              // 告诉伺服电机转到‘pos’角度
    delay(15);                       // 等待15毫秒
  } 
  for(pos = 180; pos>=0; pos-=1)     // 从180度到0度
  {                                
    myservo.write(pos);              // 告诉伺服电机转到‘pos’角度
    delay(15);                       // 等待15毫秒
  } 
} 
```

```c
// 通过电位器读出的值来控制伺服电机转换角度
# include <Servo.h>

Servo myservo;
int sensordata = 0;
intangel = 0;

void setup(){
    myservo.attch(2);
}

void loop(){
    sensordata = analogRead(A0);
    angel = map(sensordata,0,1023,0,180) // 将获取的电位器的值 映射成0-180 的数赋给舵机使其转动
	myservo.write(angel)
	delay(20)
}
```

### 74HC595（扩展端口）

#### 简介

- 74HC595的最重要的功能就是：串行输入，并行输出。3态高速位移寄存器(好腻害的说)

- 595里面有2个8位寄存器：移位寄存器、存储寄存器

  - 类似大平台就是移位寄存器

  - 存储寄存器

    - 存储寄存器是直接和8个输出引脚相通的，将移位寄存器的数据转移到存储寄存器后，Q0 Q1 Q2 Q3 Q4 Q5 Q6 Q7 就可以接受带到我们

    - 开始输入的一个字节的数据。所谓存储寄存器，就是数据可以存在这个寄存器中，并不会随着一次输出就消失，只要595不断电，也没有新 的

    - 数据从移位寄存器中过来，数据就一直不变且有效。新的数据过来后，存储寄存器中的数据就会被覆盖更新。

- 引脚图

  - 14脚：DS（SER）（资料），串行数据输入引脚
  - 13脚：OE， 输出使能控制脚，它是低电才使能输出，所以接GND
  - 12脚：RCK（ST）（大平台），存储寄存器时钟输入引脚。上升沿时（高电平），数据从移位寄存器转存带存储寄存器。
  - 11脚：SCK（SH）（活塞），移位寄存器时钟引脚，上升沿时（高电平），移位寄存器中的bit 数据整体后移，并接受新的bit（从SER输入）。
  - 10脚：MR,低电平时，清空移位寄存器中已有的bit数据，一般不用，接 高电平即可。
  - 9 脚 ：串行数据出口引脚。当移位寄存器中的数据多于8bit时，会把已有的bit“挤出去”，就是从这里出去的。用于595的级联。
  - Qx：并行输出引脚

![img](images\858860-20151222162518499-418101380.png)

#### 扩展提升（串联595）

- 见识到595的厉害了吧。138译码器通过3个输入口控制8个输出口，而且还只能是特定的8个输出值，

- 而595只用了一个输入口就可以输任意的8位数据。可谓短小精悍。

- 啥？你觉的1位控制8位输出还不够？让你的595串联起来吧！打造成加特林机关枪。

- 在上面的程序中用到的9脚，没用起作用，如果要让2个595串联起来的话，就需要它了。

- 想一下，我们将移位寄存器的8个位填满后，再往移位寄存器中塞一个会怎么样？也许你想到了。

- 对！移位寄存器的最后一个位数据会被挤出去，从哪里出去？就是从9脚输出的。如果我们把第一个595的

- 9脚连接到第二个的串行数据输入脚SER，那么，就形成了595的级联。这样，如果我们用2个595组合成了一个新的超级595，

- 这个草鸡595的移位寄存器和存储寄存器的容量都翻倍了，1口控制16口，有木有！你还可以继续级联下去！

- 最后还遗留2个 595 的脚没说

- 13脚OE  输出使能控制脚，如果它不工作，那么595的输出就是高阻态，595就不受我们程序控制了，这显然违背我们的意愿。

- OE的上面画了一条线，表示他是低电平有效。于是我们将他接GND。

- 10脚MR ，位移寄存器清空脚，他的作用就是将位移寄存器中的数据全部清空，这个很少用到，所以我们一般不让他起作用，他也是低电平有效，于是我们给他接VCC。

![image-20210503123827323](images\image-20210503123827323.png)

![image-20210503123936083](images\image-20210503123936083.png)

#### 代码

```c
int big = 2; // 大平台脚位（ST）
int push = 3; // 活塞脚位（SH）
int datain = 4; // 信号输入脚位（DS）
int datalist[8] = {1,0,1,0,1,0,1,0}

void setup(){
    pinMode(big,OUTPUT);
    pinMode(push,OUTPUT);
    pinMode(datain,OUTPUT);
}

void loop(){
    digitalWrite(big,LOW); // 先放下大平台
    for(int i=0;i<8;i++){
		if(i%2 == 0){
            putone();
        }else{
            putzero();
        }
	}
	digitalWrite(big,HIGH); // 大平台高电平推上去
}

void putone(){
    digitalWrite(push,LOW); // 活塞往后拉，等数据放上去
    digitalWrite(datain,1); // 资料放上1 如下面两张图
    digitalWrite(push,LOW); // 放好资料，活塞推上去
}

void putzero(){
    digitalWrite(push,LOW); // 活塞往后拉，等数据放上去
    digitalWrite(datain,0); // 资料放上1 如下面两张图
    digitalWrite(push,LOW); // 放好资料，活塞推上去
}
```

<img src="images\image-20210503125511872.png" alt="image-20210503125511872"  />

![image-20210503125602242](images\image-20210503125602242.png)

### 步进电机

#### 伺服电机 vs 步进电机

- 伺服电机
  - **转到**指定角度
  - 接线数：3条
- 步进电机
  - **转过**指定角度
  - 接线数：4-6条

![image-20210503134157872](images\image-20210503134157872.png)

<img src="images\ULN2003.jpeg" alt="ULN2003"  />

#### 原理

剩下四个线圈轮流接地生成磁性，吸引磁铁

![image-20210503134842779](images\image-20210503134842779.png)

#### ULN2003

- 左边1-7引脚输入高电平右边对应的引脚输出GND

![image-20210503135413751](images\image-20210503135413751.png)

#### 接线

- 注意GND 要统一

![image-20210503135941129](images\image-20210503135941129.png)

#### 代码

```c
/*
	四相五线步进电机教学
	用arduino的四个脚位控制步进马达的四极
*/

int apin = 8; // 橙色
int bpin = 9; // 黄色
int cpin = 10; // 粉红色
int dpin = 11; // 蓝色
int delatytime = 10; // 运动时间间距

void setup(){
    pinMode(apin,OUTPUT);
    pinMode(bpin,OUTPUT);
    pinMode(cpin,OUTPUT);
    pinMode(dpin,OUTPUT);
}

void loop(){
    digitalWrite(apin,HIGH); // 使橙色GND
    delay(delaytime);
    digitalWrite(apin,LOW); // 关掉橙色
    
    digitalWrite(bpin,HIGH); // 使黄色GND
    delay(delaytime);
    digitalWrite(bpin,LOW); // 关掉黄色
    
    digitalWrite(cpin,HIGH); // 使粉红色GND
    delay(delaytime);
    digitalWrite(cpin,LOW); // 关掉粉红色
    
    digitalWrite(dpin,HIGH); // 使蓝色GND
    delay(delaytime);
    digitalWrite(dpin,LOW); // 关掉蓝色
}
```

### 8x8点矩LED灯

![image-20210503143632790](images\image-20210503143632790.png)

- 想要让第四列第一行的灯亮只需要从L4接正电C1接负电即可
- 这个LED想亮必须line为高电压，col为低电压

![image-20210503143911891](images\image-20210503143911891.png)

#### 代码

```c
/*
	8x8 led灯的脚位如图所示
	因脚位有限，所以使用6x6的灯
*/

int line[6] = {0,1,2,3,4,5}; // line的六个脚位作为阵列式的形式
int col[6] = {8,9,10,11,12,13};

int appear[6][6] = {{0,0,0,1,0,0},
                    {0,0,0,0,0,0},
                    {0,0,1,0,0,0},
                    {0,0,0,0,0,0},
                    {0,0,0,0,0,0},
                    {0,0,0,0,0,0}};

void setup(){
    for(int i=0;i<6;i++){
        pinMode(line[i],OUTPUT);
        pinMode(col[i],OUTPUT);
        digitalWrite(line[i],LOW);
        digitalWrite(col[i],HIGH);
    }
}

void loop(){
    // digitalWrite(line[3],HIGH);
    // digitalWrite(col[0],LOW);
    for(int i=0;i<6;i++){
        for(int j=0;j<6;j++){
            if(appear[j][i] == 1){
                digitalWrite(line[i],HIGH);
                digitalWrite(col[j],LOW);
                dealy(1);
                digitalWrite(line[i],LOW);
                digitalWrite(col[j],HIGH);
            }
        }
	}
}
```

### 无线控制方法

- 蓝牙（hc-05、hc-06）
- 无线电（ NRF24L01）
- WIFI（ESP8266 WeMos D1）
- WeMos D1 是集成了ESP8266 模块的arduino 模块

#### 代码

- 以下代码块是单独的ESP8266模块编程

```c
/*
	本代码体现node mcu 这块板子和arduino 一模一样的开发方式
	先用程序带能量led灯
	数字 13=D7 ; 16=D0 ; 15=D8 ; 14=D5 ; 12=D6 ; 4=D2 ; 3=D9 ; 2=D4 ; 1=D10 ; 0=D3 ;
*/

void setup() {
  pinMode(BUILTIN_LED, OUTPUT);    
}

void loop() {
  digitalWrite(BUILTIN_LED, LOW);   
                                    
                                    
  delay(1000);                      
  digitalWrite(BUILTIN_LED, HIGH);  
  delay(2000);                      
}
```

- 以下代码块是WeMos D1模块编程
- 以下代码是模块作为服务器

```c
/*
    * 这个草图演示了如何设置一个简单的类似HTTP的服务器。
    * 服务器将根据请求设置GPIO pin
    * http://server_ip/gpio/0 将GPIO2设置为低，
    * http://server_ip/gpio/1 会把GPIO2调高
    * 服务器ip是ESP8266模块的ip地址，将
    * 连接模块时打印为串行。
*/

#include <ESP8266WiFi.h>

const char* ssid = "your-ssid";
const char* password = "your-password";

// Create an instance of the server
// specify the port to listen on as an argument
WiFiServer server(80);

void setup() {
  Serial.begin(115200);
  delay(10);

  // prepare GPIO2
  pinMode(2, OUTPUT);
  digitalWrite(2, 0);
  
  // Connect to WiFi network
  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  
  // Start the server
  server.begin();
  Serial.println("Server started");

  // Print the IP address
  Serial.println(WiFi.localIP());
}

void loop() {
  // Check if a client has connected
  WiFiClient client = server.available();
  if (!client) {
    return;
  }
  
  // Wait until the client sends some data
  Serial.println("new client");
  while(!client.available()){
    delay(1);
  }
  
  // Read the first line of the request
  String req = client.readStringUntil('\r');
  Serial.println(req);
  client.flush();
  
  // Match the request
  int val;
  if (req.indexOf("/gpio/0") != -1)
    val = 0;
  else if (req.indexOf("/gpio/1") != -1)
    val = 1;
  else {
    Serial.println("invalid request");
    client.stop();
    return;
  }

  // Set GPIO2 according to the request
  digitalWrite(2, val);
  
  client.flush();

  // Prepare the response
  String s = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<!DOCTYPE HTML>\r\n<html>\r\nGPIO is now ";
  s += (val)?"high":"low";
  s += "</html>\n";

  // Send the response to the client
  client.print(s);
  delay(1);
  Serial.println("Client disonnected");

  // The client will actually be disconnected 
  // when the function returns and 'client' object is detroyed
}

```

### 红外线遥控

#### 红外线接收器（Infrared Radiation）

- https://github.com/Arduino-IRremote/Arduino-IRremote（红外线函数库）
- 下载下来后解压
  - window 直接放到安装目录 **libraries** 文件夹下
  - mac 如下图方式导入
  - ![image-20210503164045599](images\image-20210503164045599.png)

![image-20210503162817757](images\image-20210503162817757.png)

#### 连线

- arduino nano （缩小版的arduino）

![image-20210503162918734](images\image-20210503162918734.png)

#### 代码

```c
#include <IRremote.h>

IRrecv irrecv(11);
decode_results results;

void setup(){
    Serial.begin(9600);
    Serial.print("Enabling IRin");
    irrecv.enableIRIn(); // 启用红外线接收
    Serial.print("Enabled IRin");
    pinMode(7,OUTPUT);
}

void loop(){
    if(irrecv.decode(&results)){
        // Serial.println(results.value,HEX); // 打印出接收的值 HEX代表16进制
        if(results.value == 23..){
            digitalWrite(7,!digitalRead(7));
        }
        irrecv.resume();
    }
    delay(100);
}
```

![image-20210503170825345](images\image-20210503170825345.png)

### Arduino 多种板子（attiny85）

- 正常的开发板
- NANO
- MINI
- attiny85

#### attiny85 烧录

- https://create.arduino.cc/projecthub/arjun/programming-attiny85-with-arduino-uno-afb829
- https://raw.githubusercontent.com/damellis/attiny/ide-1.6.x-boards-manager/package_damellis_attiny_index.json

<img src="images\image-20210503173536082.png" alt="image-20210503173536082"  />

<img src="images\image-20210503173648310.png" alt="image-20210503173648310" style="zoom: 67%;" />

![image-20210503173746084](images\image-20210503173746084.png)

![image-20210503174212514](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210503174212514.png)

把这个烧录到arduino 里面（这时arduino就可以给attiny85 烧录程序了）

- attiny85 的引脚图

![image-20210503174432621](images\image-20210503174432621.png)

- 用arduino 给attiny85烧录程序

![image-20210503174432621](images\Programming ATtiny85 with Arduino Uno_bb.png)

- arduino - attiny85（引脚对应）
  - 13 - 7
  - 12 - 6
  - 11 - 5
  - 10 - 1
- arduino想要给attiny85 烧录程序必须要给个电容
  - 长引脚接 arduino的reset
  - 短的接 GND
  - 大小 10uf （10微法）

![image-20210503175543302](images\image-20210503175543302.png)

- 上传到arduino里面就已经给attiny85 烧录了
- 完结

### 呼吸流水灯

#### 代码

```c
int pin[6] = {3,5,6,9,10,11}; // 流水灯引脚
int index = 0; // 循环索引
int level = 0; // 呼吸灯亮度级别

void setup() {
    for(int i=0;i<6;i++){
  		pinMode(pin[i],OUTPUT);   
    }
}

void loop() {
  	analogWrite(pin[index],level);
    ++level %= 7;
    ++index %= 6;
}
```

