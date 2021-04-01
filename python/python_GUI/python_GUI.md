

# Python_GUI

## 电影解析软件

>**tkinter** **GUI编程库** **python自带** 

>**urllib**
>
>**webbrowser**

```python
# url解析 vip视频播放地址的模块 做url加密的
from urllib import parse

# TK 如果出现错误会返回一个消息
import tkinter.messagebox as msgbox

# 做桌面编程的
import tkinter as tk

# 控制浏览器的
import webbrowser

# 正则表达式
import re


class APP:
    # 魔术方法
    # 初始化用的
    def __init__(self, width=500, height=300):
        self.w = width
        self.h = height
        self.title = 'vip视频破解助手'
        # 软件名
        self.root = tk.Tk(className=self.title)

        # vip视频播放地址 StringVar() 定义字符串变量
        self.url = tk.StringVar()

        # 定义选择哪个播放源
        self.v = tk.IntVar()

        # 默认为1
        self.v.set(1)

        # Frame空间
        frame_1 = tk.Frame(self.root)
        frame_2 = tk.Frame(self.root)

        # 控件内容设置
        group = tk.Label(frame_1, text='暂时只有一个视频播放通道：', padx=10, pady=10)
        tb = tk.Radiobutton(frame_1, text='唯一通道', variable=self.v, value=1, width=10, height=3)
        lable = tk.Label(frame_2, text='请输入视频连接：')

        # 输入框声明
        # entry = tk.Entry(frame_2, textvariable=self.url, highlightcolor='Fuchsia', highlightthickness=1, width=35)
        entry = tk.Entry(frame_2, textvariable=self.url, highlightthickness=1, width=35)
        play = tk.Button(frame_2, text='播放', font=('楷体', 12), fg='Purple', width=2, height=1, command=self.video_play)

        # 控件布局 显示控件在你的软件上
        frame_1.pack()
        frame_2.pack()

        # 确定控件的位置 wow 行 column 列
        group.grid(row=0, column=0)
        tb.grid(row=0, column=1)
        lable.grid(row=0, column=0)
        entry.grid(row=0, column=1)

        # ipadx x方向的外部填充 ipady y方向的内部填充
        play.grid(row=0, column=3, ipadx=10, ipady=10)

    def video_play(self):
        # 视频解析网站地址
        port = 'http://www.wmxz.wang/video.php?url='

        # 正则表达式判定是否为合法连接
        if re.match(r'^https?:/{2}\w.+$', self.url.get()):
            # 拿到用户输入的视频网址
            ip = self.url.get()

            # 视频连接加密
            ip = parse.quote_plus(ip)

            # 用浏览器打开网址
            webbrowser.open(port + ip)

        else:
            msgbox.showerror(title='错误', message='视频链接地址无效，请重新输入！')

    # 启动GUI程序的函数
    def loop(self):
        self.root.resizable(True, True)
        self.root.mainloop()


if __name__ == "__main__":
    app = APP()
    app.loop()

```

# Python GUI编程(Tkinter)

Python 提供了多个图形开发界面的库，几个常用 Python GUI 库如下：

- **Tkinter：** Tkinter 模块(Tk 接口)是 Python 的标准 Tk GUI 工具包的接口 .Tk 和 Tkinter 可以在大多数的 Unix 平台下使用,同样可以应用在 Windows 和 Macintosh 系统里。Tk8.0 的后续版本可以实现本地窗口风格,并良好地运行在绝大多数平台中。
- **wxPython：**wxPython 是一款开源软件，是 Python 语言的一套优秀的 GUI 图形库，允许 Python 程序员很方便的创建完整的、功能健全的 GUI 用户界面。
- **Jython：**Jython 程序可以和 Java 无缝集成。除了一些标准模块，Jython 使用 Java 的模块。Jython 几乎拥有标准的Python 中不依赖于 C 语言的全部模块。比如，Jython 的用户界面将使用 Swing，AWT或者 SWT。Jython 可以被动态或静态地编译成 Java 字节码。

------

## Tkinter 编程

Tkinter 是 Python 的标准 GUI 库。Python 使用 Tkinter 可以快速的创建 GUI 应用程序。

由于 Tkinter 是内置到 python 的安装包中、只要安装好 Python 之后就能 import Tkinter 库、而且 IDLE 也是用 Tkinter 编写而成、对于简单的图形界面 Tkinter 还是能应付自如。

> **注意**：Python3.x 版本使用的库名为 tkinter,即首写字母 T 为小写。
>
> ```
> import tkinter
> ```

创建一个GUI程序

- 1、导入 Tkinter 模块
- 2、创建控件
- 3、指定这个控件的 master， 即这个控件属于哪一个
- 4、告诉 GM(geometry manager) 有一个控件产生了。

## 实例(Python3.x)

```python
#!/usr/bin/python3
 
import tkinter
top = tkinter.Tk()
# 进入消息循环
top.mainloop()
```



## 实例(Python2.x)

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import Tkinter
top = Tkinter.Tk()
# 进入消息循环
top.mainloop()
```



以上代码执行结果如下图:

![tkwindow](https://www.runoob.com/wp-content/uploads/2013/12/tkwindow.jpg)

## 实例

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
# Python2.x 导入方法
from Tkinter import *           # 导入 Tkinter 库
# Python3.x 导入方法
#from tkinter import * 
root = Tk()                     # 创建窗口对象的背景色
                                # 创建两个列表
li     = ['C','python','php','html','SQL','java']
movie  = ['CSS','jQuery','Bootstrap']
listb  = Listbox(root)          #  创建两个列表组件
listb2 = Listbox(root)
for item in li:                 # 第一个小部件插入数据
    listb.insert(0,item)
 
for item in movie:              # 第二个小部件插入数据
    listb2.insert(0,item)
 
listb.pack()                    # 将小部件放置到主窗口中
listb2.pack()
root.mainloop()                 # 进入消息循环
```



以上代码执行结果如下图:

![img](https://www.runoob.com/wp-content/uploads/2013/12/tk.jpg)

------

## Tkinter 组件

Tkinter的提供各种控件，如按钮，标签和文本框，一个GUI应用程序中使用。这些控件通常被称为控件或者部件。

目前有15种Tkinter的部件。我们提出这些部件以及一个简短的介绍，在下面的表:

| 控件                                                         | 描述                                                         |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [Button](https://www.runoob.com/python/python-tk-button.html) | 按钮控件；在程序中显示按钮。                                 |
| [Canvas](https://www.runoob.com/python/python-tk-canvas.html) | 画布控件；显示图形元素如线条或文本                           |
| [Checkbutton](https://www.runoob.com/python/python-tk-checkbutton.html) | 多选框控件；用于在程序中提供多项选择框                       |
| [Entry](https://www.runoob.com/python/python-tkinter-entry.html) | 输入控件；用于显示简单的文本内容                             |
| [Frame](https://www.runoob.cfillom/python/python-tk-frame.html) | 框架控件；在屏幕上显示一个矩形区域，多用来作为容器           |
| [Label](https://www.runoob.com/python/python-tk-label.html)  | 标签控件；可以显示文本和位图                                 |
| Listbox                                                      | 列表框控件；在Listbox窗口小部件是用来显示一个字符串列表给用户 |
| Menubutton                                                   | 菜单按钮控件，用于显示菜单项。                               |
| Menu                                                         | 菜单控件；显示菜单栏,下拉菜单和弹出菜单                      |
| Message                                                      | 消息控件；用来显示多行文本，与label比较类似                  |
| Radiobutton                                                  | 单选按钮控件；显示一个单选的按钮状态                         |
| Scale                                                        | 范围控件；显示一个数值刻度，为输出限定范围的数字区间         |
| Scrollbar                                                    | 滚动条控件，当内容超过可视化区域时使用，如列表框。.          |
| Text                                                         | 文本控件；用于显示多行文本                                   |
| Toplevel                                                     | 容器控件；用来提供一个单独的对话框，和Frame比较类似          |
| Spinbox                                                      | 输入控件；与Entry类似，但是可以指定输入范围值                |
| PanedWindow                                                  | PanedWindow是一个窗口布局管理的插件，可以包含一个或者多个子控件。 |
| LabelFrame                                                   | labelframe 是一个简单的容器控件。常用与复杂的窗口布局。      |
| tkMessageBox                                                 | 用于显示你应用程序的消息框。                                 |

------

## 标准属性

标准属性也就是所有控件的共同属性，如大小，字体和颜色等等。

| 属性      | 描述       |
| --------- | ---------- |
| Dimension | 控件大小； |
| Color     | 控件颜色； |
| Font      | 控件字体； |
| Anchor    | 锚点；     |
| Relief    | 控件样式； |
| Bitmap    | 位图；     |
| Cursor    | 光标；     |

------

## 几何管理

Tkinter控件有特定的几何状态管理方法，管理整个控件区域组织，以下是Tkinter公开的几何管理类：包、网格、位置

| 几何方法 | 描述   |
| -------- | ------ |
| pack()   | 包装； |
| grid()   | 网格； |
| place()  | 位置； |

最近用tkinter+pyinstaller+python完成了一个小工具的项目，在过程当中对tkinter做了一定的了解，以此作为记录，方便日后进行查阅，也希望对各位论坛朋友有帮助。

一、tkinter简介

   tkinter是python实现gui图形界面的一个库，同时还有wxpython以及qt（本人技术还有待提高，目前就只会点tkinter，哈哈）。在我个人使用tkinter来写gui工具之后，我觉得tkinter还是蛮好理解的。

​    tkinter包含了几种常用类型的控件，包括Label（标签，就是界面上显示的字）、Entry（输入框）、Button（按钮，可以绑定各种封装函数）、Radiobutton（单选框）、Checkbuttion（复选框）、messagebox（消息弹出框）、Text（文本编辑框）、Listbox（列表控件）、Scrollbar（滚条控件）等。下面会进行一些属性参数的总结。

二、tkinter各类控件参数总结

1、title：设置窗口的标题

 

| 属性      | 属性简析                                                     | 实例                                |
| --------- | ------------------------------------------------------------ | ----------------------------------- |
| title     | 设置窗口标题                                                 | title（‘xxxxx’）                    |
| geometry  | 设置窗口大小，中间不能是*，而是x                             | geometry('200x100')                 |
| resizable | 设置窗口是否可以变化高（height）、 宽（width），True为可以变化，False为不可变化 | resizable(width=False, height=True) |

 

 

2、Label：标签

 

| 属性     | 属性简析                                                     | 实例                                                         |
| -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| text     | 需要在界面显示的Label标签内容                                | Label（root,text=‘xxxxx’）                                   |
| height   | 组件的高度（所占行数）                                       | Label（root,text=‘xxxxx’，height=2）                         |
| width    | 组件的宽度（所占字符个数）                                   | Label（root,text=‘xxxxx’，height=2，width=20）               |
| fg       | 前景字体颜色                                                 | Label（root,text=‘xxxxx’，fg='blue'）---显示字体为蓝色       |
| bg       | 背景颜色                                                     | Label（root,text=‘xxxxx’，bg=‘red’）---显示背景为红色        |
| justify  | 多行文本的对齐方式，可选参数为： LEFT、 CENTER、RIGHT，分别是向左、居中、向右对齐 | Label（root,text=‘xxxxx’，justify=tk.LEFT）                  |
| padx     | 文本左右两侧的空格数（默认为1）                              | Label（root,text=‘xxxxx’，padx=5）                           |
| pady     | 文本上下两侧的空格数（默认为1）                              | Label（root,text=‘xxxxx’，pady=5）                           |
| font     | 设置字体格式和大小                                           | Label（root,text=‘xxxxx’，font=("微软雅黑", 12)）            |
| photo    | 设置背景图片，事先需要指定图片路径                           | photo=tk.PhotoImage（file='指定图片路径'）Label（root,text=‘xxxxx’，image=photo） |
| compound | 图像背景图位置，可选参数为：botton、top、right、left、center（下、上、右、左、文字覆盖图像） | photo=tk.PhotoImage（file='指定图片路径'）Label（root,text=‘xxxxx’，image=photo,compound=center） |

3、Button：按钮

 

 

| 属性             | 属性简析                                                     | 实例                                                     |
| ---------------- | ------------------------------------------------------------ | -------------------------------------------------------- |
| text             | 按钮图标显示内容                                             | Button（root,text='xxxx'）                               |
| height           | 组件的高度（所占行数）                                       | Button（root,text='xxxx',height=2）                      |
| width            | 组件的宽度（所占字符个数）                                   | Button（root,text='xxxx',width=20）                      |
| fg               | 前景字体颜色                                                 | Button（text='xxxx',fg='blue'）---显示按钮字体颜色为蓝色 |
| bg               | 背景颜色                                                     | Button（root,text='xxxx',bg='red'）---显示按钮背景为红色 |
| activebackground | 按钮按下时的背景颜色                                         | Button（root,text='xxxx',activebackground='grey'）       |
| activeforeground | 按钮按下时的前景字体颜色                                     | Button（root,text='xxxx',activeforeground='white'）      |
| justify          | 多行文本的对齐方式，可选参数为： LEFT、 CENTER、RIGHT，分别是向左、居中、向右对齐 | Button（root,text=‘xxxxx’，justify=tk.LEFT）             |
| padx             | 文本左右两侧的空格数（默认为1）                              | Button（root,text='xxxx',padx=10）                       |
| pady             | 文本上下两侧的空格数（默认为1）                              | Button（root,text='xxxx',pady=10）                       |
| command          | 按钮触发执行的命令（函数）                                   | Button（root,text='xxxx',command=函数）                  |

4、Entry：输入框

 

| 属性         | 属性简析                                                     | 实例                                                |
| ------------ | ------------------------------------------------------------ | --------------------------------------------------- |
| width        | 组件的宽度（所占字符个数）                                   | Entry（root,width=20）                              |
| fg           | 前景字体颜色                                                 | Entry（root,fg='blue'）                             |
| bg           | 背景颜色                                                     | Entry（root,bg='blue'）                             |
| show         | 将Entry框中的文本替换为指定字符，用于输入密码等，如设置 show="*" | Entry（root,show="*"）                              |
| state        | 设置组件状态，默认为normal，可设置为：disabled—禁用组件，readonly—只读 | Entry（root,state=readonly）                        |
| textvariable | 指定变量，需要事先定义一个变量，在Entry进行绑定获取变量的值  | text=tk.StringVar() Entry（root,textvariable=text） |

5、Radiobutton：单选框

 

| 属性     | 属性简析                                                     | 实例                                                         |
| -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| text     | 单选框文本显示内容                                           | Radiobutton（root,text='xxxx'）                              |
| variable | 单选框索引变量，通过变量的值确定哪个单选框被选中。一组单选框使用同一个索引变量，需要事先设定一个变量 | color=tk.StringVar（） Radiobutton（root,variable=color）    |
| value    | 单选框选中时设定变量的值                                     | color=tk.StringVar（） Radiobutton（root,variable=color,value='red'） |
| command  | 单选框选中时执行的命令（函数）                               | color=tk.StringVar（） Radiobutton（root,variable=color,value='red',command=函数） |

6、Checkbuttion：复选框

 

| 属性     | 属性简析                                                     | 实例                                                         |
| -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| text     | 复选框显示的文本                                             | Checkbutton（root,text='xxxx'）                              |
| variable | 复选框索引变量，通过变量的值确定哪些复选框被选中。每个复选框使用不同的变量，使复选框之间相互独立，事先需要定义不同的变量 | typeBlod=tk.IntVar（） Checkbutton（root,variable=typeBlod） |
| onvalue  | 复选框选中（有效）时变量的值，可以通过计算值来判断分支不同的效果，计算值由自己设定 | typeBlod=tk.IntVar（） Checkbutton（root,variable=typeBlod,onvalue=1） |
| offvalue | 复选框未选中（无效）时变量的值，可以通过计算值来判断分支不同的效果，一般设置为0 | typeBlod=tk.IntVar（） Checkbutton（root,variable=typeBlod,onvalue=1,offvalue=0） |
| command  | 复选框选中时执行的命令（函数）                               | typeBlod=tk.IntVar（） Checkbutton（root,variable=typeBlod,onvalue=1,offvalue=0，command=函数） |

7、Text：文本框



| 属性                   | 属性简析                                  | 实例                                           | 备注                                                         |
| ---------------------- | ----------------------------------------- | ---------------------------------------------- | ------------------------------------------------------------ |
| t.insert(mark, 内容)   | 插入文本信息，mark可以是行号,或者特殊标识 | t=tk.Text（） t.insert（END,'插入的文本信息'） | INSERT:光标的插入点 CURRENT:鼠标的当前位置所对应的字符位置 END:这个Textbuffer的最后一个字符 SEL_FIRST:选中文本域的第一个字符，如果没有选中区域则会引发异常 SEL_LAST：选中文本域的最后一个字符，如果没有选中区域则会引发异常 |
| t.delete(mark1, mark2) | 删除文本信息                              |                                                | INSERT:光标的插入点CURRENT:鼠标的当前位置所对应的字符位置 END:这个Textbuffer的最后一个字符 SEL_FIRST:选中文本域的第一个字符，如果没有选中区域则会引发异常 SEL_LAST：选中文本域的最后一个字符，如果没有选中区域则会引发异常 |

8、Menu



**Menu(master=None, \**options)** (class)

master -- 父组件

**options -- 组件选项，下方表格详细列举了各个选项的具体含义和用法：

| **选项**           | **含义**                                                     |
| ------------------ | ------------------------------------------------------------ |
| activebackground   | 设置当 Menu 处于 "active" 状态（通过 state 选项设置状态）的背景色 |
| activeborderwidth  | 设置当 Menu 处于 "active" 状态（通过 state 选项设置状态）的边框宽度 |
| activeforeground   | 设置当 Menu 处于 "active" 状态（通过 state 选项设置状态）的前景色 |
| background         | 设置背景颜色                                                 |
| bg                 | 跟 background 一样                                           |
| borderwidth        | 指定边框宽度                                                 |
| bd                 | 跟 borderwidth 一样                                          |
| cursor             | 指定当鼠标在 Menu 上飘过的时候的鼠标样式                     |
| disabledforeground | 指定当 Menu 处于 "disabled" 状态的时候的前景色               |
| font               | 指定 Menu 中文本的字体                                       |
| foreground         | 设置 Menu 的前景色                                           |
| fg                 | 跟 foreground 一样                                           |
| postcommand        | 将此选项与一个方法相关联，当菜单被打开的时候该方法将自动被调用 |
| relief             | 1. 指定边框样式 2. 默认值是 "flat" 3. 另外你还可以设置 "sunken"，"raised"，"groove" 或 "ridge" |
| selectcolor        | 指定当菜单项显示为单选按钮或多选按钮时选择中标志的颜色       |
| tearoff            | 1. 默认情况下菜单可以被“撕下”（点击 IDLE 菜单上边的 --------- 试试） 2. 将该选项设置为 Flase 关闭这一特性 |
| tearoffcommand     | 如果你希望当用户“撕下”你的菜单时通知你的程序，那么你可以将该选项与一个方法相关联，那么当用户“撕下”你的菜单时，Tkinter 会带着两个参数去调用你的方法（一个参数是当前窗口的 ID，另一个参数是承载被“撕下”的菜单的窗口 ID） |
| title              | 默认情况下，被“撕下”的菜单标题是其主菜单的名字，不过你也可以通过修改此项的值来修改标题 |

**方法**

**add(type, \**options)**
-- type 参数指定添加的菜单类型，可以是："command"，"cascade"，"checkbutton"，"radiobutton" 或 "separator"
-- 还可以通过 options 选项设置菜单的属性，下表列举了 options 可以使用的选项和具体含义：

| **选项**         | **含义**                                                     |
| ---------------- | ------------------------------------------------------------ |
| accelerator      | 1. 显示该菜单项的加速键（快捷键） 2. 例如 accelerator = "Ctrl+N" 3. 该选项仅显示，并没有实现加速键的功能（通过按键绑定实现） |
| activebackground | 设置当该菜单项处于 "active" 状态（通过 state 选项设置状态）的背景色 |
| activeforeground | 设置当该菜单项处于 "active" 状态（通过 state 选项设置状态）的前景色 |
| background       | 设置该菜单项的背景颜色                                       |
| bitmap           | 指定显示到该菜单项上的位图                                   |
| columnbreak      | 从该菜单项开始另起一列显示                                   |
| command          | 将该选项与一个方法相关联，当用户点击该菜单项时将自动调用此方法 |
| compound         | 1. 控制菜单项中文本和图像的混合模式 2. 如果该选项设置为 "center"，文本显示在图像上（文本重叠图像） 3. 如果该选项设置为 "bottom"，"left"，"right" 或 "top"，那么图像显示在文本的旁边（如 "bottom"，则图像在文本的下方 |
| font             | 指定文本的字体                                               |
| foreground       | 设置前景色                                                   |
| hidemargin       | 是否显示菜单项旁边的空白                                     |
| image            | 1. 指定菜单项显示的图片 2. 该值应该是 PhotoImage，BitmapImage，或者能兼容的对象 |
| label            | 指定菜单项显示的文本                                         |
| menu             | 1. 该选项仅在 cascade 类型的菜单中使用 2. 用于指定它的下级菜单 |
| offvalue         | 1. 默认情况下，variable 选项设置为 1 表示选中状态，反之设置为 0 2. 设置 offvalue 的值可以自定义未选中状态的值 |
| onvalue          | 1. 默认情况下，variable 选项设置为 1 表示选中状态，反之设置为 0 2. 设置 onvalue 的值可以自定义选中状态的值 |
| selectcolor      | 指定当菜单项显示为单选按钮或多选按钮时选择中标志的颜色       |
| selectimage      | 如果你在单选按钮或多选按钮菜单中使用图片代替文本，那么设置该选项指定被菜单项被选中时显示的图片 |
| state            | 1. 跟 text 选项一起使用，用于指定哪一个字符画下划线（例如用于表示键盘快捷键） |
| underline        | 1. 用于指定在该菜单项的某一个字符处画下划线 2. 例如设置为 1，则说明在该菜单项的第 2 个字符处画下划线 |
| value            | 1. 当菜单项为单选按钮时，用于标志该按钮的值 2. 在同一组中的所有按钮应该拥有各不相同的值 3. 通过将该值与 variable 选项的值对比，即可判断用户选中了哪个按钮 4. 如在使用上有不懂具体可以参照 [Radiobutton](https://blog.csdn.net/qq_41556318/article/details/85108309) 组件的说明 |
| variable         | 1. 当菜单项是单选按钮或多选按钮时，与之关联的变量 2. 如在使用上有不懂具体可以参照：[Checkbutton](https://blog.csdn.net/qq_41556318/article/details/85108303) 和 [Radiobutton](https://blog.csdn.net/qq_41556318/article/details/85108309) 组件的说明 |

**add_cascade(\**options)**
-- 添加一个父菜单
-- 相当于 add("cascade", **options)

**add_checkbutton(\**options)**
-- 添加一个多选按钮的菜单项
-- 相当于 add("checkbutton", **options)

**add_command(\**options)**
-- 添加一个普通的命令菜单项
-- 相当于 add("command", **options)

**add_radiobutton(\**options)**
-- 添加一个单选按钮的菜单项
-- 相当于 add("radiobutton", **options)

**add_separator(\**options)**
-- 添加一条分割线
-- 相当于 add("separator", **options)

**delete(index1, index2=None)**
-- 删除 index1 ~ index2（包含）的所有菜单项
-- 如果忽略 index2 参数，则删除 index1 指向的菜单项
-- 注意：对于一个被“撕下”的菜单，你无法使用该方法

**entrycget(index, option)**
-- 获得指定菜单项的某选项的值

**entryconfig(index, \**options)**
-- 设置指定菜单项的选项
-- 选项的参数及具体含义请参考上方 add() 方法

**entryconfigure(index, \**options)**
-- 跟 entryconfig() 一样

**index(index)**
-- 返回与 index 参数相应的选项的序号（例如 e.index("end")）

**insert(index, itemType, \**options)**
-- 插入指定类型的菜单项到 index 参数指定的位置
-- itemType 参数指定添加的菜单类型，可以是："command"，"cascade"，"checkbutton"，"radiobutton" 或 "separator"
-- 选项的参数及具体含义请参考上方 add() 方法

**insert_cascade(index, \**options)**
-- 在 index 参数指定的位置添加一个父菜单
-- 相当于 insert("cascade", **options)

**insert_checkbutton(index, \**options)**
-- 在 index 参数指定的位置添加一个多选按钮
-- 相当于 insert("checkbutton", **options)

**insert_command(index, \**options)**
-- 在 index 参数指定的位置添加一个普通的命令菜单项
-- 相当于 insert("command", **options)

**insert_radiobutton(index, \**options)**
-- 在 index 参数指定的位置添加一个单选按钮
-- 相当于 insert("radiobutton", **options)

**insert_separator(index, \**options)**
-- 在 index 参数指定的位置添加一条分割线
-- 相当于 insert("separator", **options)

**invoke(index)**
-- 调用 index 指定的菜单项相关联的方法
-- 如果是单选按钮，设置该菜单项为选中状态
-- 如果是多选按钮，切换该菜单项的选中状态

**post(x, y)**
-- 在指定的位置显示弹出菜单
-- 参考上方【用法】中的创建弹窗菜单的例子

**type(index)**
-- 获得 index 参数指定菜单项的类型
-- 返回值可以是："command"，"cascade"，"checkbutton"，"radiobutton" 或 "separator"

**unpost()**
-- 移除弹出菜单

**yposition(index)**
-- 返回 index 参数指定的菜单项的垂直偏移位置
-- 该方法的目的是为了让你精确放置相对于当前鼠标的位置弹出菜单

三、tkinter构建gui框架参数

1、frame：

内嵌框架，可以在一个图形界面中设定多个frame框架，也可以在frame再次嵌套frame

frame=tk.Frame（父类框架）

frame.pack（）

2、pack

 

| 属性         | 属性简析                                                     | 备注                                                         | 其他                                                         |
| ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| fill         | 设置组件是否向水平或垂直方向填充，包含X、Y、BOTH、NONE       | fill = X（水平方向填充）fill = Y（垂直方向填充）fill = BOTH（水平和垂直）NONE 不填充 |                                                              |
| expand       | 设置组件是否展开，当值为YES时，side选项无效。组件显示在父容器中心位置；若fill选项为BOTH,则填充父组件的剩余空间。它表示某个控件在fill那个方向，要不要把空白的地方分配给它 | YES 、NO（1、0）                                             | 若expand=True或者expand=1，表示在fill那个方向，把空白处都分给这个控件，让它尽量占满。              若expand=False或者expand=0，表示在fill那个方向，有空也不给它。 |
| side         | 设置组件的对齐方式                                           | LEFT、TOP、RIGHT、BOTTOM                                     | 值为左、上、右、下                                           |
| ipadx、ipady | 设置x方向（或者y方向）内部间隙（子组件之间的间隔），它表示某个控件的内边距，即控件边缘和这个控件内容(文字图片什么的)的间距 | 可设置数值，默认是0                                          | 非负整数，单位为像素                                         |
| padx、pady   | 设置x方向（或者y方向）外部间隙（与之并列的组件之间的间隔），它表示某个控件的外边距，即控件边缘和这个控件所在容器之间的间距 | 可设置数值，默认是0                                          | 非负整数，单位为像素                                         |
| anchor       | 锚选项，当可用空间大于所需求的尺寸时，决定组件被放置于容器的何处，它表示某个控件在容器里的摆放方式，是左还是右，是上还是下 | N、E、S、W、NW、NE、SW、SE、CENTER（默认值为CENTER）         | 表示八个方向以及中心                                         |

3、grid

| 属性                | 属性简析                                                     | 实例                                                         |
| ------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| row和column         | 它表示某个控件要放在第几行网格或第几列网格，下标都是从0开始计的 | xxx.grid（column=1,row=1）                                   |
| rowspan和columnspan | 它表示某个控件将会竖着跨几行或横着跨几列，默认都是1          | xxx.grid（column=1,row=1,columnspan=2）xxx.grid（column=1,row=1,rowspan=2） |
| padx和pady          | 它表示某个控件的外边距，即控件边缘和这个控件所在容器之间的间距，单位是像素 | xxx.grid（column=1,row=1,padx=10）xxx.grid（column=1,row=1,pady=10） |
| ipadx和ipady        | 它表示某个控件的内边距，即控件边缘和这个控件内容(文字图片什么的)的间距，单位是像素 | xxx.grid（column=1,row=1,ipadx=10）xxx.grid（column=1,row=1,ipady=10） |
| sticky              | 它表示某个控件在网格里的摆放方式，是左还是右，是上还是下，即使窗口被拉大也会按照指定方向对齐 | 若sticky=N，表示North，尽可能往北面/上面停靠。 若sticky=S，表示South，尽可能往南面/下面停靠。 若sticky=W，表示West，尽可能往西边/左边停靠。 若sticky=E，表示East，尽可能往东边/右边停靠。 若sticky=NS，表示NorthSouth，尽可能往南北方向/上下拉伸。 若sticky=EW，表示EastWest，尽可能往东西方向/左右拉伸。 若sticky=CENTER，尽可能往中心停靠。 |

4、place

| 参数       | 作用                                                         |
| ---------- | ------------------------------------------------------------ |
| anchor     | 控制组件在 place 分配的空间中的位置 "n", "ne", "e", "se", "s", "sw", "w", "nw", 或 "center" 来定位（ewsn代表东西南北，上北下南左西右东） 默认值是 "nw" |
| bordermode | 指定边框模式（"inside" 或 "outside"） 默认值是 "inside"      |
| height     | 指定该组件的高度（像素）                                     |
| in_        | 将该组件放到该选项指定的组件中 指定的组件必须是该组件的父组件 |
| relheight  | 指定该组件相对于父组件的高度 取值范围 0.0 ~ 1.0              |
| relwidth   | 指定该组件相对于父组件的宽度 取值范围 0.0 ~ 1.0              |
| relx       | 指定该组件相对于父组件的水平位置 取值范围 0.0 ~ 1.0          |
| rely       | 指定该组件相对于父组件的垂直位置 取值范围 0.0 ~ 1.0          |
| width      | 指定该组件的宽度（像素）                                     |
| x          | 指定该组件的水平偏移位置（像素） 如同时指定了 relx 选项，优先实现 relx 选项 |
| y          | 指定该组件的垂直偏移位置（像素） 如同时指定了 rely 选项，优先实现 rely 选项 |



四、消息弹出框messagebox（在这里将messagebox简称为msgbox）

消息弹出框用于info、warning、error提示框的弹出使用的，我们可以根据自己的需求来使用

 

| 属性           | 属性简介                        | 实例                                                         |
| -------------- | ------------------------------- | ------------------------------------------------------------ |
| showinfo       | info信息提示，弹出提示框        | msgbox.showinfo("INFO","Showinfo test")，INFO是提示框title，Showinfo test是提示框内容 |
| showwarning    | warning警告信息提示，弹出警告框 | msgbox.showwarning("WARNING","Warning test")，WARNING是警告框title，Warning test是警告框内容 |
| showerror      | error错误信息提示，弹出错误框   | msgbox.showerror("ERROR","Error test")，ERROR是错误框title，Error test是错误框内容 |
| askquestion    | 提问窗口提示                    | msgbox.askquestion("Question","Askquestion test")            |
| askokcancel    | 确定与取消窗口提示              | msgbox.askokcancel("OkCancel","Askokcancel test")            |
| askyesno       | 确定与取消窗口提示              | msgbox.askretrycancel("Retry","Askretrycancel test")         |
| askretrycancel | 重试与取消窗口提示              | msgbox.askretrycancel("Retry","Askretrycancel test")         |

字母的方位

| 字母   | 方位 |
| ------ | ---- |
| n      | 北   |
| s      | 南   |
| w      | 西   |
| e      | 东   |
| center | 中心 |
| nw     | 西北 |
| ne     | 东北 |
| sw     | 西南 |
| se     | 东南 |

# 以下为付费知识

## **简介**

作为 Python 开发者，图形用户界面（GUI）开发是必备技能之一。目前，市面上支持

Python 的“GUI 工具包”很多，各有特点，虽然大多数工具包的基础类似，但要学习一个
新包并掌握其细节还是非常耗时的，因此，在选用工具包时应仔细权衡。本文将介绍
Python 自带的 GUI 工具包 TKinter。

 

TKinter
Python 的 GUI 库非常多，之所以选择 Tkinter，一是最为简单，二是自带库，不需下载
安装，随时使用，跨平台兼容性非常好，三则是从需求出发的，Python 在实际应用中极
少用于开发复杂的桌面应用，毕竟，Python 的各种 GUI 工具包都“一般得很”，不具备优
势。
关于 GUI，泛泛而谈难免枯燥，鉴于此，本文将基于一系列实例来介绍 Tkinter 控件。

## **窗口创建与布局**

做界面，首先需要创建一个窗口，Python Tkinter 创建窗口很简单，代码如下：

```python
from tkinter import *
#初始化Tk()
myWindow = Tk()
#进入消息循环
myWindow.mainloop()
```

上述程序创建的窗口是非常简陋的，有待进一步美化，设置标题、窗口大小、窗口是否
可变等，涉及属性有：title（设置窗口标题）、 geometry（设置窗口大小）、
resizable（设置窗口是否可以变化长 宽）。请看如下实例：

```python
from tkinter import Tk
#初始化Tk()
myWindow = Tk()
#设置标题
myWindow.title('Python GUI Learning')
#设置窗口大小
myWindow.geometry('380x300')
#设置窗口是否可变长、宽，True：可变，False：不可变
myWindow.resizable(width=False, height=True)
#进入消息循环
myWindow.mainloop()
```

进一步，将窗口放置于屏幕中央，如下实例：

```python
from tkinter import Tk
#初始化Tk()
myWindow = Tk()
#设置标题
myWindow.title('Python GUI Learning')
#设置窗口大小
width = 380
height = 300
#获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
screenwidth = myWindow.winfo_screenwidth()
screenheight = myWindow.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2)
myWindow.geometry(alignstr)
#设置窗口是否可变长、宽，True：可变，False：不可变
myWindow.resizable(width=False, height=True)
#进入消息循环
myWindow.mainloop()
```

## **常用控件**

仅有窗口并不能实现交互，还需要控件，Tkinter 提供了各种控件，如按钮、标签和文本
框。在一个 GUI 应用程序中使用，这些控件通常被称为控件或者部件，目前有15种
Tkinter 部件，如下列表:

**![img](https://img2018.cnblogs.com/blog/1421031/201810/1421031-20181015163828976-1464354755.png)**

 

##  **几何管理**

Tkinter 控件有特定的几何状态管理方法，管理整个控件区域组织，以下是 Tkinter 公开
的几何管理类：包、网格、位置。

**![img](https://img2018.cnblogs.com/blog/1421031/201810/1421031-20181015163918318-1851152297.png)**

------

**Lable控件**标签控件，基本用法为： Lable(root, option...) ，即：Label(根对象, [属性列表])，
其中属性列表如下：

**![img](https://img2018.cnblogs.com/blog/1421031/201810/1421031-20181015163950603-1557363500.png)**

Lable 控件实例
实例1：标签展示文本，代码如下：

```python
from tkinter import*
#初始化Tk()
myWindow = Tk()
#设置标题
myWindow.title('Python GUI Learning')
#创建一个标签，显示文本
Label(myWindow, text="user-name",bg='red',font=('Arial 12 bold'),width=20,height=5).pack()
Label(myWindow, text="password",bg='green',width=20,height=5).pack()
#进入消息循环
myWindow.mainloop()
```

执行结果：

![img](https://img2018.cnblogs.com/blog/1421031/201810/1421031-20181015164039950-2048398092.png)

实例2：标签展示图标，代码如下：

```python
from tkinter import*
#初始化Tk()
myWindow = Tk()
#设置标题
myWindow.title('Python GUI Learning')
#创建一个标签，显示图标
logo = PhotoImage(file="/Users/guojin/book/temp.gif")
Label(myWindow, image=logo).pack(side='left')
#进入消息循环
myWindow.mainloop()
```

运行结果：

![img](https://img2018.cnblogs.com/blog/1421031/201810/1421031-20181015164111629-1650617247.png)

实例3：标签图文混叠，边距控制，代码如下：

```python
from tkinter import*
#初始化Tk()
myWindow = Tk()
#设置标题
myWindow.title('Python GUI Learning')
#创建一个标签，显示文本
logo = PhotoImage(file="/Users/guojin/book/temp.gif")
explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interface
exists to allow additional image file
formats to be added easily."""
Label(myWindow,compound=CENTER,text=explanation,image=logo).pack(side="right")
#进入消息循环
myWindow.mainloop()
```

 运行结果：

![img](https://img2018.cnblogs.com/blog/1421031/201810/1421031-20181015165032697-52472823.png)

 **Button控件**

Button 控件是一个标准的 Tkinter 部件，用于实现各种按钮。按钮可以包含文本或图
像，还可以关联 Python 函数。
Tkinter 的按钮被按下时，会自动调用该函数。
按钮文本可跨越一个以上的行。此外，文本字符可以有下划线，例如标记的键盘快捷
键。默认情况下，使用 Tab 键可以移动到一个按钮部件，用法如下：
Entry(根对象, [属性列表])，即Entry(root, option...)
常用的属性列表如下：

![img](https://img2018.cnblogs.com/blog/1421031/201810/1421031-20181015165113874-2103277383.png)Button 实例：

实例1：创建按钮，代码如下：

```python
from tkinter import*
#初始化Tk()
myWindow = Tk()
#设置标题
myWindow.title('Python GUI Learning')
#创建两个按钮
b1=Button(myWindow, text='button1',bg="red", relief='raised', width=8, height=2)
b1.grid(row=0, column=0, sticky=W, padx=5,pady=5)
b2=Button(myWindow, text='button2', font=('Helvetica 10 bold'),width=8, height=2)
b2.grid(row=0, column=1, sticky=W, padx=5, pady=5)
#进入消息循环
myWindow.mainloop()
```

运行结果：

![img](https://img2018.cnblogs.com/blog/1421031/201810/1421031-20181015165301307-1977481359.png)

实例2：创建按钮并绑定响应函数，输入半径，计算圆面积并输出，代码如下：

```python
from tkinter import *
def printInfo():
　　#清理entry2
　　entry2.delete(0, END)
　　#根据输入半径计算面积
　　R=int(entry1.get())
　　S= 3.1415926*R*R
　　entry2.insert(10, S)
　　#清空entry2控件
　　entry1.delete(0, END)
#初始化Tk()
myWindow = Tk()
#设置标题
myWindow.title('Python GUI Learning')
#标签控件布局
Label(myWindow, text="input").grid(row=0)
Label(myWindow, text="output").grid(row=1)
#Entry控件布局
entry1=Entry(myWindow)
entry2=Entry(myWindow)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
#Quit按钮退出；Run按钮打印计算结果
Button(myWindow, text='Quit', command=myWindow.quit).grid(row=2, column=0,sticky=W, padx=5, pady=5)
Button(myWindow, text='Run', command=printInfo).grid(row=2, column=1, sticky=W, padx=5, pady=5)
#进入消息循环
myWindow.mainloop()
```

 运行结果：

![img](https://img2018.cnblogs.com/blog/1421031/201810/1421031-20181015165456943-2087207397.png)

输入半径：

![img](https://img2018.cnblogs.com/blog/1421031/201810/1421031-20181015165516338-1184754718.png)

点击‘Run’计算面积：

![img](https://img2018.cnblogs.com/blog/1421031/201810/1421031-20181015165548062-131369473.png)

 **Checkbutton控件**

Checkbutton 是复选框，又称为多选按钮，可以表示两种状态。用法为： Checkbutton
( root, option, ... )， 其中可选属性 option 有很多，如下表所示：

**![img](https://img2018.cnblogs.com/blog/1421031/201810/1421031-20181015165630492-2037481845.png)**

 

以下是这个小工具的常用方法：

![img](https://img2018.cnblogs.com/blog/1421031/201810/1421031-20181015165700982-1642211921.png)

实例1：创建一组复选框，代码如下：

```python
from tkinter import*
#初始化Tk()
myWindow = Tk()
#设置标题
myWindow.title('Python GUI Learning')
# 用来获取复选框是否被勾选，通过chVarDis.get()来获取其的状态,其状态值为int类型 勾选为1
chVarDis = IntVar()
# text为该复选框后面显示的名称, variable将该复选框的状态赋值给一个变量，当state='disa
check1 = Checkbutton(myWindow, text="Disabled", variable=chVarDis, state='disabled')# 该复选框是否勾选,select为勾选, deselect为不勾选
check1.select()
# sticky=tk.W 当该列中其他行或该行中的其他列的某一个功能拉长这列的宽度或高度时，
# 设定该值可以保证本行保持左对齐，N：北/上对齐 S：南/下对齐 W：西/左对齐 E：东/右对齐
check1.grid(column=0, row=0, sticky=W)
chvarUn = IntVar()
check2 = Checkbutton(myWindow, text="UnChecked", variable=chvarUn)
check2.deselect()
check2.grid(column=1, row=0, sticky=W)
chvarEn = IntVar()
check3 = Checkbutton(myWindow, text="Enabled", variable=chvarEn)
check3.select()
check3.grid(column=2, row=0, sticky=W)
#进入消息循环
myWindow.mainloop()
```

实例2：绑定响应函数，代码如下：

```python
from tkinter import *
def callCheckbutton():
　　#改变v的值，即改变Checkbutton的显示值
　　v.set('check CheckButton')
#初始化Tk()
myWindow = Tk()
#设置标题
myWindow.title('Python GUI Learning')
v = StringVar()
v.set('check python')
#绑定v到Checkbutton的属性textvariable
Checkbutton(myWindow,textvariable = v,command = callCheckbutton).pack()
#进入消息循环
myWindow.mainloop()
```

 **Radiobutton控件**

单选按钮是一种可在多个预先定义的选项中选择出一项的 Tkinter 控件 。单选按钮可显
示文字或图片，显示文字时只能使用预设字体，该控件可以绑定一个 Python 函数或方
法，当单选按钮被选择时，该函数或方法将被调用。
单选按钮（Radio Button）这个名字来源于收音机（Radio）上的调频按钮， 这些按钮用
来选择特定波段或预设电台，如果一个按钮被按下， 其他同类的按钮就会弹起，即同时
只有一个按钮可被按下。
一组单选按钮控件和同一个变量关联。点击其中一个单选按钮将把这个变量设为某个预
定义的值。一般用法为： Radiobutton(myWindow，options) ，其中 option 与
Checkbutton，Button 大多重合，用法一致。

****![img](https://img2018.cnblogs.com/blog/1421031/201810/1421031-20181015170004345-944702579.png)****

实例：创建单选按钮并绑定响应函数，代码如下：

```python
from tkinter import*
#初始化Tk()
myWindow=Tk()
myWindow.title('Python GUI Learning')
v=IntVar()
#列表中存储的是元素是元组
language=[('python',0),('C++',1),('C',2),('Java',3)]
#定义单选按钮的响应函数
def callRB():
　　for i in range(4):
　　if (v.get()==i):
　　　　root1 = Tk()
　　　　Label(root1,text='你的选择是'+language[i][0]+'!',fg='red',width=20, height=6).pack()
　　　　Button(root1,text='确定',width=3,height=1,command=root1.destroy).pack(side='bottom')
Label(myWindow,text='选择一门你喜欢的编程语言').pack(anchor=W)
#for循环创建单选框
for lan,num in language:
　　Radiobutton(myWindow, text=lan, value=num, command=callRB, variable=v).pack(anchor=W)
#进入消息循环
myWindow.mainloop()
```

 运行结果：

![img](https://img2018.cnblogs.com/blog/1421031/201810/1421031-20181015170540585-873407939.png)

![img](https://img2018.cnblogs.com/blog/1421031/201810/1421031-20181015170557193-1659456318.png)

 

------

 **Menu控件**

Menu被用来创建一个菜单，创建Menu类的实例，然后使用add方法添加命令或者其他
菜单内容。使用方法如下：
Menu(root,option,…)
其中 option 列表如下：

****![img](https://img2018.cnblogs.com/blog/1421031/201810/1421031-20181015170627884-998575912.png)**

特有函数如下：

![img](https://img2018.cnblogs.com/blog/1421031/201810/1421031-20181015170650410-2092007143.png)

实例：创建一个菜单组，代码如下：

```python
from tkinter import *
#创建窗口
myWindow=Tk()
myWindow.title("菜单")
myWindow.geometry("400x300+300+100")
# 创建一个菜单项，类似于导航栏，顶层菜单
menubar=Menu(myWindow)
# 创建菜单项
fmenu1=Menu(myWindow)
for item in ['新建','打开','保存','另存为']:
    # 如果该菜单是顶层菜单的一个菜单项，则它添加的是下拉菜单的菜单项。则他添加的是下拉菜单的菜单项。
    fmenu1.add_command(label=item)

fmenu2=Menu(myWindow)
for item in ['复制','粘贴','剪切']:
    fmenu2.add_command(label=item)

fmenu3=Menu(myWindow)
for item in ['大纲视图','web视图']:
    fmenu3.add_command(label=item)

fmenu4=Menu(myWindow)
for item in ["版权信息","其它说明"]:
    fmenu4.add_command(label=item)

# add_cascade 的一个很重要的属性就是 menu 属性，它指明了要把那个菜单级联到该菜单项上，
# 当然，还必不可少的就是 label 属性，用于指定该菜单项的名称
menubar.add_cascade(label="文件",menu=fmenu1)
menubar.add_cascade(label="编辑",menu=fmenu2)
menubar.add_cascade(label="视图",menu=fmenu3)
menubar.add_cascade(label="关于",menu=fmenu4)

# 最后可以用窗口的 menu 属性指定我们使用哪一个作为它的顶层菜单
myWindow.config(menu=menubar)
#进入消息循环
myWindow.mainloop()
```

运行结果：

 ![img](https://img2018.cnblogs.com/blog/1421031/201810/1421031-20181015170945029-877251031.png)

![img](https://img2018.cnblogs.com/blog/1421031/201810/1421031-20181015170954646-1512359629.png)

 

------

 **Message控件**

Message 控件用来展示一些文字短消息。Message 和 Label 控件有些类似， 但在展示文
字方面比 Label 要灵活，比如 Message 控件可以改变字体，而 Label 控件只能使用一种
字体，它提供了一个换行对象，以使文字可以断为多行。
它可以支持文字的自动换行及对齐，这里要澄清一下前面提到的 Message 控件可以改变
字体的说法: 这是说我们可以为单个控件设置任意字体, 控件内的文字都将显示为该字
体，但我们不能给单个控件内的文字设置多种字体，如果你需要这么做，可以考虑使用
Text 控件。
创建一个 Message 控件的语法如下：
w = Message ( root, option, ... )
其中 option 列表如下：

![img](https://img2018.cnblogs.com/blog/1421031/201810/1421031-20181015171029480-929918395.png)

请看下面实例：

```        for i in range(20):
from tkinter import *
#初始化Tk()
myWindow=Tk()
#创建一个Message
whatever_you_do = "Only those who have the patience to do simple things per
msg = Message(myWindow, text = whatever_you_do)
msg.config(bg='lightgreen', font=('times', 20, 'italic'))
msg.pack( )
#进入消息循环
myWindow.mainloop()
```

## 事件绑定

**事件类型**

用户通过鼠标、键盘、游戏控制设备在与图形界面交互时，就会触发事件。tkinter事件通常采用了将事件名称放置于尖括号内的字符串表示，尖括号中的内容我们称之为事件类型。事件类型有其通用的定义方式。如下

<[modifier-]…type[-detail]>

其中方括号内的内容为可选参数

modifier为组合键的定义，例如，同时按下Ctrl键；

type为通用类型，例如，键盘按键（KeyPress）

detail用于具体信息，如按下键盘中‘B’键

常用事件类型如下：

**【鼠标单击事件】**

<Button-1>：单击鼠标左键

<Button-2>：单击鼠标中间键（如果有）

<Button-3>：单击鼠标右键

<Button-4>：向上滚动滑轮

<Button-5>：向下滚动滑轮

**【鼠标双击事件】**

<Double-Button-1>：鼠标左键双击

<Double-Button-2>：鼠标中键双击

<Double-Button-3>.：鼠标右键双击

**【鼠标释放事件】**

<ButtonRelease-1>：鼠标左键释放

<ButtonRelease-2>：鼠标中键释放

<ButtonRelease-3>：鼠标右键释放

**【鼠标按下并移动事件（即拖动）】**

<B1-Motion>：左键拖动

<B2-Motion>：中键拖动

<B3-Motion>：右键拖动

**【鼠标其他操作】**

<Enter>：鼠标进入控件（放到控件上面）

<FocusIn>：控件获得焦点

<Leave>：鼠标移出控件

<FocusOut>：控件失去焦点

**【键盘按下事件】**

<Key>：键盘按下，事件event中的keycode,char都可以获取按下的键值

<Return>：键位绑定，回车键，其它还有<BackSpace>,<Escape>,<Left>,<Up>,<Right>,<Down>等等

**【控件属性改变事件】**

<Configure>：控件大小改变，新的控件大小会存储在事件event对象中的 width 和 height 属性传递，部分平台上该事件也代表控件位置改变。

**【组合使用】**

<Control-Shift-Alt-KeyPress-A>：同时按下Ctrl+Shift+Alt+A等4个键

<KeyPress-A>：按下键盘中的'A'键游戏设备使用参见设备供应商提供的API函数，这里不再赘述，常用的事件类型就是这些了。大家没有必要全部记住，这些事件都是一种类英文的描述，只要记住主要的几个，按照<[modifier-]…type[-detail]>进行组合就可以了。

**事件绑定**

常见的事件绑定有以下几类

**【创建组件对象实例时指定】**

创建组件对象实例时，可以通过其命名参数command指定事件处理函数，如为Button控件绑定单击时间，当控件被单击时执行clickhandler函数处理

**b = Button(root, text='按钮', command=clickhandler)**

**【实例绑定】**

调用组件对象实例方法bind，可以为指定组件实例绑定事件

**w.bind('', eventhandler, add='')**

其中，<event>为事件类型，eventhandler为事件处理函数，可选参数add默认为''，表示事件处理函数替代其他绑定，如果为‘+’，则加入事件处理队列。

如绑定组件对象，使得Canvas组件实例c可以处理鼠标右键单击事件(处理函数名称为eventhandler)，代码如下：

**c=Canvas(); c.bind('Button-3', eventhandler)**

**【类绑定】**

调用组件对象实例方法bind_class函数，可以为特定类绑定事件

**w.bind_class('Widget', '', eventhandler, add='')**

其中，Widget为组件类；<event>为事件；eventhandler为事件处理函数

如绑定组件类，使得所有Canvas组件实例可以处理鼠标中键事件(事件处理函数为eventhandler)

**c = Canvas(); c.bind_class('Canvas', '', eventhandler)**

**【程序界面绑定】**

调用组件对象实例方法bind_all函数，可以为所有组件类型绑定事件

**w.bind_all('', eventhandler, add='')**

同上，其中<event>为事件；eventhandler为事件处理函数

如将PrintScreen键与程序中所有组件对象绑定，使得程序界面能处理打印屏幕的键盘事件

**c = Canvas(); c.bind('', printscreen)**

**事件处理函数的编写**

【**定义事件函数和事件方法】**

对于能通过command传入的函数，其参数没有必须指定第一个参数为event的要求。但是通过bind（含bind_class、bind_all，当然，bind_class第一个参数为className，但其后必须是Event实例）绑定的事件，在定义函数方法时（事件处理可以定义为函数，也可以定义为对象的方法），两者都带一个参数event。触发事件调用处理函数时，将传递Event对象实例。

\# 函数定义

def handlerName(event):

函数内容

\# 类中定义

def handlerName(self, event):

方法内容

**【Event事件对象参数属性】**

通过传递Event事件对象的属性，可以获取相关参数备程序使用。常用的Event事件参数有以下几种。

widget：产生该事件的控件x, y：当前鼠标位置x_root, y_root：当前鼠标相对于屏幕左上角（0，0）的位置，以像素px为单位。char：字符代码（限键盘事件），作为字符串返回keysym：关键符号（限键盘事件）keycode：关键代码（限键盘事件）num：按钮号码（限鼠标按钮事件）width, height：小部件的新大小（以像素px为单位）（限配置事件）。type：事件类型

### 一、事件序列

事件序列是以字符串的形式表示的，可以表示一个或多个相关联的事件。

事件序列使用以下语法描述：

<modifier-type-detail>

- - 事件序列是包含在尖括号（<...>）中
  - type 部分的内容是最重要的，它通常用于描述普通的事件类型，例如鼠标点击或键盘按键点击（详见下方）。
  - modifier 部分的内容是可选的，它通常用于描述组合键，例如 Ctrl + c，Shift + 鼠标左键点击（详见下方）。
  - detail 部分的内容是可选的，它通常用于描述具体的按键，例如 Button-1 表示鼠标左键。

| **事件序列**               | **含义**                      | 序列   |
| -------------------------- | ----------------------------- | ------ |
| <Button-1>                 | 用户点击鼠标左键              | detail |
| <KeyPress-H>               | 用户点击 H 按键               |        |
| <Control-Shift-KeyPress-H> | 用户同时点击 Ctrl + Shift + H |        |

### 二、type

| Activate      | 当组件的状态从“未激活”变为“激活”的时候触发该事件             |
| ------------- | ------------------------------------------------------------ |
| Button        | 1. 当用户点击鼠标按键的时候触发该事件 2. detail 部分指定具体哪个按键：<Button-1>鼠标左键，<Button-2>鼠标中键，<Button-3>鼠标右键，<Button-4>滚轮上滚（Linux），<Button-5>滚轮下滚（Linux） |
| ButtonRelease | 1. 当用户释放鼠标按键的时候触发该事 2. 在大多数情况下，比 Button 要更好用，因为如果当用户不小心按下鼠标，用户可以将鼠标移出组件再释放鼠标，从而避免不小心触发事件 |
| Configure     | 当组件的尺寸发生改变的时候触发该事件                         |
| Deactivate    | 当组件的状态从“激活”变为“未激活”的时候触发该事件             |
| Destroy       | 当组件被销毁的时候触发该事件                                 |
| Enter         | 1. 当鼠标指针进入组件的时候触发该事件 2. 注意：不是指用户按下回车键 |
| Expose        | 当窗口或组件的某部分不再被覆盖的时候触发该事件               |
| FocusIn       | 1. 当组件获得焦点的时候触发该事件 2. 用户可以用 Tab 键将焦点转移到该组件上（需要该组件的 takefocus 选项为 True） 3. 你也可以调用 focus_set() 方法使该组件获得焦点 |
| FocusOut      | 当组件失去焦点的时候触发该事件                               |
| KeyPress      | 1. 当用户按下键盘按键的时候触发该事件 2. detail 可以指定具体的按键，例如 <KeyPress-H>表示当大写字母 H 被按下的时候触发该事件 3. KeyPress 可以简写为 Key |
| KeyRelease    | 当用户释放键盘按键的时候触发该事件                           |
| Leave         | 当鼠标指针离开组件的时候触发该事件                           |
| Map           | 1. 当组件被映射的时候触发该事件 2. 意思是在应用程序中显示该组件的时候，例如调用 grid() 方法 |
| Motion        | 当鼠标在组件内移动的整个过程均触发该事件                     |
| MouseWheel    | 1. 当鼠标滚轮滚动的时候触发该事件 2. 目前该事件仅支持 Windows 和 Mac 系统，Linux 系统请参考 Button |
| Unmap         | 1. 当组件被取消映射的时候触发该事件 2. 意思是在应用程序中不再显示该组件的时候，例如调用 grid_remove() 方法 |
| Visibility    | 当应用程序至少有一部分在屏幕中是可见的时候触发该事件         |

### 三、modifier

| Alt     | 当按下 Alt 按键的时候                                        |
| ------- | ------------------------------------------------------------ |
| Any     | 1. 表示任何类型的按键被按下的时候 2. 例如 <Any-KeyPress> 表示当用户按下任何按键时触发事件 |
| Control | 当按下 Ctrl 按键的时候                                       |
| Double  | 1. 当后续两个事件被连续触发的时候 2. 例如 <Double-Button-1> 表示当用户双击鼠标左键时触发事件 |
| Lock    | 当打开大写字母锁定键（CapsLock）的时候                       |
| Shift   | 当按下 Shift 按键的时候                                      |
| Triple  | 跟 Double 类似，当后续三个事件被连续触发的时候               |

###  四、Event 对象

| widget         | 产生该事件的组件                                             |
| -------------- | ------------------------------------------------------------ |
| x, y           | 当前的鼠标位置坐标（相对于窗口左上角，像素为单位）           |
| x_root, y_root | 当前的鼠标位置坐标（相对于屏幕左上角，像素为单位）           |
| keysym         | 按键名，见下方 Key names（键盘事件专属）                     |
| keycode        | 按键码，见下方 Key names（键盘事件专属）                     |
| num            | 按钮数字（鼠标事件专属）                                     |
| width, height  | 组件的新尺寸（Configure 事件专属）                           |
| type           | 该事件类型                                                   |
| char           | 按键字符，仅对键盘事件有效                                   |
| keycode        | 按键编码，仅对键盘事件有效                                   |
| keysym         | 按键名称，仅对键盘事件有效 <br />比如按下空格键<br />键的keycode：32<br />键的keysym：space<br />键的char： <br /><br />比如按下a键<br />键的keycode：65<br />键的keysym：a<br />键的char： a |

### 五、Key names

| **按键名（keysym）** | **按键码（keycode）** | **代表的按键**               |
| -------------------- | --------------------- | ---------------------------- |
| Alt_L                | 64                    | 左边的 Alt 按键              |
| Alt_R                | 113                   | 右边的 Alt 按键              |
| BackSpace            | 22                    | Backspace（退格）按键        |
| Cancel               | 110                   | break 按键                   |
| Caps_Lock            | 66                    | CapsLock（大写字母锁定）按键 |
| Control_L            | 37                    | 左边的 Ctrl 按键             |
| Control_R            | 109                   | 右边的 Ctrl 按键             |
| Delete               | 107                   | Delete 按键                  |
| Down                 | 104                   | ↓ 按键                       |
| End                  | 103                   | End 按键                     |
| Escape               | 9                     | Esc 按键                     |
| Execute              | 111                   | SysReq 按键                  |
| F1                   | 67                    | F1 按键                      |
| F2                   | 68                    | F2 按键                      |
| F3                   | 69                    | F3 按键                      |
| F4                   | 70                    | F4 按键                      |
| F5                   | 71                    | F5 按键                      |
| F6                   | 72                    | F6 按键                      |
| F7                   | 73                    | F7 按键                      |
| F8                   | 74                    | F8 按键                      |
| F9                   | 75                    | F9 按键                      |
| F10                  | 76                    | F10 按键                     |
| F11                  | 77                    | F11 按键                     |
| F12                  | 96                    | F12 按键                     |
| Home                 | 97                    | Home 按键                    |
| Insert               | 106                   | Insert 按键                  |
| Left                 | 100                   | ← 按键                       |
| Linefeed             | 54                    | Linefeed（Ctrl + J）         |
| KP_0                 | 90                    | 小键盘数字 0                 |
| KP_1                 | 87                    | 小键盘数字 1                 |
| KP_2                 | 88                    | 小键盘数字 2                 |
| KP_3                 | 89                    | 小键盘数字 3                 |
| KP_4                 | 83                    | 小键盘数字 4                 |
| KP_5                 | 84                    | 小键盘数字 5                 |
| KP_6                 | 85                    | 小键盘数字 6                 |
| KP_7                 | 79                    | 小键盘数字 7                 |
| KP_8                 | 80                    | 小键盘数字 8                 |
| KP_9                 | 81                    | 小键盘数字 9                 |
| KP_Add               | 86                    | 小键盘的 + 按键              |
| KP_Begin             | 84                    | 小键盘的中间按键（5）        |
| KP_Decimal           | 91                    | 小键盘的点按键（.）          |
| KP_Delete            | 91                    | 小键盘的删除键               |
| KP_Divide            | 112                   | 小键盘的 / 按键              |
| KP_Down              | 88                    | 小键盘的 ↓ 按键              |
| KP_End               | 87                    | 小键盘的 End 按键            |
| KP_Enter             | 108                   | 小键盘的 Enter 按键          |
| KP_Home              | 79                    | 小键盘的 Home 按键           |
| KP_Insert            | 90                    | 小键盘的 Insert 按键         |
| KP_Left              | 83                    | 小键盘的 ← 按键              |
| KP_Multiply          | 63                    | 小键盘的 * 按键              |
| KP_Next              | 89                    | 小键盘的 PageDown 按键       |
| KP_Prior             | 81                    | 小键盘的 PageUp 按键         |
| KP_Right             | 85                    | 小键盘的 → 按键              |
| KP_Subtract          | 82                    | 小键盘的 - 按键              |
| KP_Up                | 80                    | 小键盘的 ↑ 按键              |
| Next                 | 105                   | PageDown 按键                |
| Num_Lock             | 77                    | NumLock（数字锁定）按键      |
| Pause                | 110                   | Pause（暂停）按键            |
| Print                | 111                   | PrintScrn（打印屏幕）按键    |
| Prior                | 99                    | PageUp 按键                  |
| Return               | 36                    | Enter（回车）按键            |
| Right                | 102                   | → 按键                       |
| Scroll_Lock          | 78                    | ScrollLock 按键              |
| Shift_L              | 50                    | 左边的 Shift 按键            |
| Shift_R              | 62                    | 右边的 Shift 按键            |
| Tab                  | 23                    | Tab（制表）按键              |
| Up                   | 98                    | ↑ 按键                       |

# 组件布局和事件绑定

## 一. 数据显示

在`tkinter`中的数据展示方式有两种表格数据和树状数据, 但是都用到同一个组件`Treeview`, 下面介绍组建的使用

### 1. 表格数据

- 表格数据, 顾名思义就是用表格形式展示数据
- 要使用`Treeview`首先要引用`tkinter`中的`ttk`模块

```Python
from tkinter import ttk

# 此处省略window的相关代码

# 创建表格
tree = ttk.Treeview(window)
tree.pack()

# 定义列title(接受一个元组)
tree["columns"] = ('name', 'sex', 'age', 'height', 'weight')

# 设置列宽度
tree.column('name', width=100)
tree.column('sex', width=50)
tree.column('age', width=50)
tree.column('height', width=80)
tree.column('weight', width=80)

# 设置表头(列名)
tree.heading('name', text='姓名')
tree.heading('sex', text='性别')
tree.heading('age', text='年龄')
tree.heading('height', text='身高(CM)')
tree.heading('weight', text='体重(KG)')

# 添加数据
tree.insert('', 0, text='line1', values=('Titan', 'M', 20, 180, 80))
tree.insert('', 1, text='line2', values=('Jun', 'M', 19, 170, 65))
tree.insert('', 2, text='line3', values=('Coder', 'M', 20, 170, 70))
tree.insert('', 3, text='line4', values=('Che', 'W', 18, 165, 45))
# 上面第一个参数为第一层级, 这里目前用不到, 后面树状结构中会用到12345678910111213141516171819202122232425262728293031
```

效果图如下

![Treeview1.png](https://upload-images.jianshu.io/upload_images/4122543-6852de768c9564c0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 2. 树状数据

树状数据这里指的是,类似文件夹的层级目录一样

```Python
# 创建表格
tree = ttk.Treeview(window)
tree.pack()

# 添加一级树枝
treeA1 = tree.insert('', 0, '浙', text='浙江', values=('A1'))
treeA2 = tree.insert('', 1, '鲁', text='山东', values=('A2'))
treeA3 = tree.insert('', 2, '苏', text='江苏', values=('A3'))

# 添加二级树枝
treeA1_1 = tree.insert(treeA1, 0, 'H', text='杭州', values=('A1_1'))
treeA1_2 = tree.insert(treeA1, 1, 'Z', text='舟山', values=('A1_2'))
treeA1_3 = tree.insert(treeA1, 2, 'J', text='嘉兴', values=('A1_3'))

treeA2_1 = tree.insert(treeA2, 0, 'N', text='济南', values=('A2_1'))
treeA2_2 = tree.insert(treeA2, 1, 'L', text='临沂', values=('A2_2'))
treeA2_3 = tree.insert(treeA2, 2, 'Q', text='青岛', values=('A2_3'))
treeA2_4 = tree.insert(treeA2, 3, 'Y', text='烟台', values=('A2_4'))


# 三级树枝
treeA1_1_1 = tree.insert(treeA1_1, 0, 'G', text='江干', values=('A1_1_1'))
treeA1_1_1 = tree.insert(treeA1_1, 1, 'X', text='萧山', values=('A1_1_2'))
```

> 注意事项
> \- `insert`: 参数介绍
> \- 参数1: 上一层级的目录
> \- 参数2: 当前数据在当前层级的中的索引值
> \- 参数3: 当前数据的标识, 所有层及数据的该标识不能相同, 否则报错
> \- 参数4: 显示的数据
> \- 注: 所有数据的参数3(标识)不能相同

效果图如下

![Treeview2.png](https://upload-images.jianshu.io/upload_images/4122543-52e077a1441f83fa.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 二. 布局方式

- 所谓布局，就是指控制窗体容器中各个控件（组件）的位置关系。
- 在`tkinter`中目前存在的布局方式有三种: 绝对布局(`place`), 相对布局(`pack`)和表格布局(`grid`)

### 1. 绝对布局

- 绝对布局: 窗口的变化对位置没有影响
- 这里先介绍`place`布局涉及到的相关属性和函数

#### 1-1. 属性介绍

| 属性名                | 属性简析                                                     | 取值                                         | 取值说明                                                     |
| --------------------- | ------------------------------------------------------------ | -------------------------------------------- | ------------------------------------------------------------ |
| `anchor`              | 锚点, 当可用空间大于所需求的尺寸时，决定组件被放置于容器的何处 | N、E、S、W、NW、NE、SW、SE、`CENTER`(默认值) | 表示八个方向以及中心                                         |
| `x、y`                | 组件左上角的x、y坐标                                         | 整数，默认值0                                | 绝对位置坐标，单位像素                                       |
| `relx/rely`           | 组件相对于父容器的x、y坐标                                   | 0~1之间浮点数                                | 相对位置，0.0表示左边缘（或上边缘），1.0表示右边缘（或下边缘） |
| `width/height`        | 组件的宽度、高度                                             | 非负整数                                     | 单位像素                                                     |
| `relwidth、relheight` | 组件相对于父容器的宽度、高度                                 | 0~1之间浮点数                                | 与`relx(rely)`取值相似                                       |
| `bordermode`          | 如果设置为`INSIDE`，组件内部的大小和位置是相对的，不包括边框；如果是`OUTSIDE`，组件的外部大小是相对的，包括边框 | `INSIDE`(默认)、`OUTSIDE`                    | 可以使用常量`INSIDE`、`OUTSIDE`，也可以使用字符串形式`inside`、`outside` |

```Python
# 创建四个label
label1 = Label(window, text='11111', bg='red')
label2 = Label(window, text='22222', bg='yellow')
label3 = Label(window, text='33333', bg='blue')
label4 = Label(window, text='44444', bg='orange')

# 绝对布局
label1.place(x=10, y=10, width=200)
label2.place(x=30, y=30)
label3.place(x=60, y=61)
label4.place(x=91, y=91, width=200, height=50)
```

如下图组件位置固定

![place.png](https://upload-images.jianshu.io/upload_images/4122543-0bd83fa3642d52ea.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

#### 1-2. 相关函数

`place`类提供了下列函数（使用组件实例对象调用）

- `place_slaves()`: 以列表方式返回本组件的所有子组件对象
- `place_configure(option=value)`: 给`place`布局管理器设置属性，使用属性`option=value`方式设置
- `propagate(boolean)`: 设置为`True`表示父组件的几何大小由子组件决定(默认值)，反之则无关
- `place_info()`: 返回`place`提供的选项所对应得值
- `grid_forget()`: `Unpack`组件，将组件隐藏并且忽略原有设置，对象依旧存在，可以用`pack(option, …)`，将其显示
- `location(x, y)`: `x/y`为以像素为单位的点，函数返回此点是否在单元格中，在哪个单元格中。返回单元格行列坐标，(-1, -1)表示不在其中
- `size()`: 返回组件所包含的单元格，揭示组件大小

### 2. 相对布局

#### 2-1. 属性介绍

- 相对布局: 组件位置或大小的变化会随着窗口的变化而变化
- 这里先介绍`pack`布局涉及到的相关属性和函数

| 属性名        | 属性简析                                                     | 取值                                                 | 取值说明                                               |
| ------------- | ------------------------------------------------------------ | ---------------------------------------------------- | ------------------------------------------------------ |
| `fill`        | 设置组件是否向水平或垂直方向填充                             | `X、Y、BOTH和NONE`                                   | `fill=X`(水平方向填充),`BOTH`(水平和垂直),`NONE`不填充 |
| `expand`      | 设置组件是否展开                                             | YES、NO（1、0）                                      | `expand=YES`                                           |
| `side`        | 设置组件的对齐方式                                           | `LEFT、TOP、RIGHT、BOTTOM`                           | 值为左、上、右、下                                     |
| `ipadx/ipady` | 设置x方向（或者y方向）内部间隙（子组件之间的间隔）           | 可设置数值，默认是0                                  | 非负整数，单位为像素                                   |
| `padx/pady`   | 设置x方向（或者y方向）外部间隙（与之并列的组件之间的间隔）   | 可设置数值，默认是0                                  | 非负整数，单位为像素                                   |
| `anchor`      | 锚选项，当可用空间大于所需求的尺寸时，决定组件被放置于容器的何处 | N、E、S、W、NW、NE、SW、SE、CENTER（默认值为CENTER） | 表示八个方向以及中心                                   |

需要注意

> `expand`: 设置组件是否展开，当值为YES时，`side`选项无效。组件显示在父容器中心位置；若`fill`选项为`BOTH`,则填充父组件的剩余空间。默认为不展开

```Python
# 创建四个label
label1 = Label(window, text='11111', bg='red')
label2 = Label(window, text='22222', bg='yellow')
label3 = Label(window, text='33333', bg='blue')
label4 = Label(window, text='44444', bg='orange')


# 布局
label1.pack(side=LEFT, fill=Y)
label2.pack(side=RIGHT, fill=Y)
label3.pack(side=TOP, fill=X)
label4.pack(side=BOTTOM, fill=X)
```

效果如图

![pack.png](https://upload-images.jianshu.io/upload_images/4122543-fdb25319dfb38d3b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

#### 2-2. 函数介绍

`pack`类提供了下列函数（使用组件实例对象调用）
\- `pack_slaves()`: 以列表方式返回本组件的所有子组件对象
\- `pack_configure(option=value)`: 给`pack`布局管理器设置属性，使用属性`option=value`方式设置
\- `propagate(boolean)`: 设置为 True 表示父组件的几何大小由子组件决定（默认值），反之则无关。
\- `ack_info()`: 返回pack提供的选项所对应得值。
\- `pack_forget()`: `Unpack`组件，将组件隐藏并且忽略原有设置，对象依旧存在，可以用`pack(option, …)`，将其显示。
\- `location(x, y)`: x, y为以像素为单位的点，函数返回此点是否在单元格中，在哪个单元格中。返回单元格行列坐标，(-1, -1)表示不在其中
\- `size()`: 返回组件所包含的单元格，揭示组件大小

### 3. 表格布局

- `grid`布局又被称作网格布局，是最被推荐使用的布局。
- 程序大多数都是矩形的界面，我们可以很容易把它划分为一个几行几列的网格，然后根据行号和列号，将组件放置于网格之中
- 使用`grid`布局时，需要在里面指定两个参数，分别用`row` 表示行，`column`表示列
- 需要注意的是`row`和`column`的序号都从0开始

#### 3-1. 属性介绍

| 属性名        | 属性简析                                                   | 取值                                 | 取值说明                         |
| ------------- | ---------------------------------------------------------- | ------------------------------------ | -------------------------------- |
| `row/column`  | `row`为行号，`column`为列号，设置将组件放置于第几行第几列  | 取值为行、列的序号，不是行数与列数   | `row`和`column` 的序号都从0 开始 |
| `sticky`      | 设置组件在网格中的对齐方式                                 | `N、E、S、W、NW、NE、SW、SE、CENTER` | 类似于`pack`布局中的锚选项       |
| `rowspan`     | 组件所跨越的行数                                           | 跨越的行数                           | 取值为跨越占用的行数，而不是序号 |
| `columnspan`  | 组件所跨越的列数                                           | 跨越的列数                           | 取值为跨越占用的列数，而不是序号 |
| `ipadx/ipady` | 设置x方向（或者y方向）内部间隙（子组件之间的间隔）         | 可设置数值，默认是0                  | 非负整数，单位为像素             |
| `padx/pady`   | 设置x方向（或者y方向）外部间隙（与之并列的组件之间的间隔） | 可设置数值，默认是0                  | 非负整数，单位为像素             |

```Python
# 创建四个label
label1 = Label(window, text='11111', bg='red')
label2 = Label(window, text='22222', bg='yellow')
label3 = Label(window, text='33333', bg='blue')
label4 = Label(window, text='44444', bg='orange')

# 布局
label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=1, column=0)
label4.grid(row=1, column=1)
```

效果如图

![grid.png](https://upload-images.jianshu.io/upload_images/4122543-53d892edb51941ad.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

#### 3-2. 函数介绍

`grid`类提供了下列函数（使用组件实例对象调用）：

| 函数名                         | 描述                                                         |
| ------------------------------ | ------------------------------------------------------------ |
| `grid_slaves()`                | 以列表方式返回本组件的所有子组件对象。                       |
| `grid_configure(option=value)` | 给`grid`布局管理器设置属性                                   |
| `grid_propagate(boolean)`      | 设置为`True`表示父组件的几何大小由子组件决定(默认值)，反之则无关。 |
| `grid_info()`                  | 返回`grid`提供的选项所对应得值。                             |
| `grid_forget()`                | 将组件隐藏并且忽略原有设置，对象依旧存在                     |
| `grid_location(x, y)`          | `x/y`为以像素为单位的点，函数返回此点是否在单元格中          |
| `size()`                       | 返回组件所包含的单元格，揭示组件大小                         |

## 三. 鼠标和键盘事件

- 一个`Tkinter`应用生命周期中的大部分时间都处在一个消息循环中
- 它等待事件的发生: 事件可能是按键按下, 鼠标点击, 鼠标移动等.
- `Tkinter`提供了用以处理相关事件的机制, 处理函数可以被绑定给各个控件的各种事件
- 如果相关事件发生, `handler`函数会被触发, 事件对象`event`会传递给`handler`函数

```Python
button.bind(event, handler)
```

### 1. 鼠标点击事件

```Python
def buttonAction(event):
    print(event.x, event.y)

button = Button(window, text='这是一个按钮')
button.bind('<Button-4>', buttonAction)
button.pack()
```

其中`event`的事件类型和描述如下

| Event               | Description  |
| ------------------- | ------------ |
| `<Button-1>`        | 鼠标左键     |
| `<Button-3>`        | 鼠标右键     |
| `<Button-2>`        | 鼠标中键     |
| `<Button-4>`        | 鼠标向上滚动 |
| `<Button-5>`        | 鼠标向下滚动 |
| `<Double-Button-1>` | 鼠标左键双击 |
| `<Double-Button-3>` | 鼠标右键双击 |
| `<Double-Button-2>` | 鼠标中键双击 |
| `<Triple-Button-1>` | 鼠标左键三击 |
| `<Triple-Button-3>` | 鼠标右键三击 |
| `<Triple-Button-2>` | 鼠标中键三击 |

### 2. 鼠标在某个按键被按下后的移动事件

```Python
label = Label(window, text='https://www.titanjun.top', bg='orange')
label.place(x=100, y=50, height=30)

def labelAction(event):
    print(event.x, event.y)
label.bind('<B1-Motion>', labelAction)
```

其中`event`的事件类型和描述如下

| Event         | Description |
| ------------- | ----------- |
| `<B1-Motion>` | 左键移动    |
| `<B3-Motion>` | 右键移动    |
| `<B2-Motion>` | 中键移动    |

### 3. 按钮点击释放事件

```Python
label = Label(window, text='https://www.titanjun.top', bg='orange')
label.place(x=100, y=50, height=30)

def labelAction(event):
    print(event.x, event.y)
label.bind('<ButtonRelease-1>', labelAction)
```

其中`event`的事件类型和描述如下

| Event               | Description  |
| ------------------- | ------------ |
| `<ButtonRelease-1>` | 释放鼠标左键 |
| `<ButtonRelease-3>` | 释放鼠标右键 |
| `<ButtonRelease-2>` | 释放鼠标中键 |

需要注意的是
\- 以上鼠标操作中, 苹果鼠标没有中键这一说, 所以在苹果鼠标操作中
\- 正常鼠标的中键操作(例如``等`-2`操作), 响应苹果鼠标的右键操作
\- 正常鼠标的右键操作(例如``等`-3`操作), 在苹果鼠标中无响应

### 4. 鼠标进入/离开控件事件

```Python
# 按钮点击释放事件
label3 = Label(window, text='加油: https://www.titanjun.top', bg='yellow')
label3.place(x=100, y=150, height=30)

def labelAction(event):
    print(event.x, event.y)
label3.bind('<Leave>', labelAction)
```

其中`event`的事件类型和描述如下

| Event     | Description            |
| --------- | ---------------------- |
| `<Enter>` | 鼠标光标进入控件时触发 |
| `<Leave>` | 鼠标光标离开控件时触发 |

### 5. 键盘响应事件

```Python
# 响应所有的按键
label = Label(window, text='https://www.titanjun.top', bg='orange')
# 设置焦点
label.focus_set()
label.place(x=100, y=50, height=30)

def labelAction(event):
    print(event.char, event.keycode)
label.bind('<Key>', labelAction)
```

其他按键操作

| Event          | Description                              |
| -------------- | ---------------------------------------- |
| `<Key>`        | 响应所有的按键(按下)                     |
| `<KeyRelease>` | 响应所有的按键(松开)                     |
| `<FocusIn>`    | 控件或控件的子空间获得键盘焦点.          |
| `<FocusOut>`   | 控件丢失键盘焦点 (焦点移动到另一个控件). |

### 6. 指定按键操作

| Event                        | Description                                        |
| ---------------------------- | -------------------------------------------------- |
| `<Return>/<Enter>`           | 只有回车键响应                                     |
| `<Escape>`                   | esc键                                              |
| `<space>`                    | 空格键                                             |
| `<Tab>`                      | Tab键                                              |
| `<Up>/<Down>/<Left>/<Right>` | 上下左右键                                         |
| `<Shitf_L>/<Shift_R>`        | 左右`Shift`键(类似有左右两个键的, 添加`_L/_R`区分) |
| `<BackSpace>`                | 退格                                               |
| `<a>/<b>`                    | 指定的小写字母键                                   |
| `<A>/<Z>`                    | 指定的大写字母键                                   |
| `<Control-Alt-a>`            | 组合键(可识别任意组合键)                           |

> 需要注意的是: 识别组合键时, 一般是按下组合键的最后一个键才会触发操作

### 7. `event`事件的相应参数

| 时间属性         | 描述                                         |
| ---------------- | -------------------------------------------- |
| `char`           | 从键盘输入的和按键事件的相关字符             |
| `keycode`        | 从按键输入的和按键事件的键代码(ASCII码)      |
| `keysym`         | 从按键输入的和按键事件的键符号(即字符)       |
| `num`            | 按键数字(1, 2, 3)表明按下的是哪个鼠标键      |
| `widget`         | 触发这个事件的小构件对象                     |
| `x和y`           | 当前鼠标在小构件中以像素为单位的位置         |
| `x_root和y_root` | 当前鼠标相对于屏幕左上角的以像素为单位的位置 |

# Python Tkinter Menu菜单

最近更新时间：2019-07-02 10:32:36

简介

Menu小部件用于在python应用程序中创建各种类型的菜单（顶级，下拉和弹出）。顶级菜单是显示在父窗口标题栏下方的菜单。我们需要创建Menu小部件的新实例，并使用add（）方法向其添加各种命令。

------

Menu小部件用于在python应用程序中创建各种类型的菜单（顶级，下拉和弹出）。

顶级菜单是显示在父窗口标题栏下方的菜单。我们需要创建Menu小部件的新实例，并使用add（）方法向其添加各种命令。

下面给出了使用Menu小部件的语法。

句法

```
w = Menu(top, options)
```

下面给出了可能的选项列表。

| SN   | 选项               | 说明                                                         |
| ---- | ------------------ | ------------------------------------------------------------ |
| 1    | activebackground   | 窗口小部件在焦点下时窗口小部件的背景颜色。                   |
| 2    | activeborderwidth  | 小部件在鼠标下方时边框的宽度。默认值为1像素。                |
| 3    | activeforeground   | 窗口小部件具有焦点时窗口小部件的字体颜色。                   |
| 4    | bg                 | 小部件的背景颜色。                                           |
| 5    | bd                 | 小部件的边框宽度。                                           |
| 6    | cursor             | 鼠标指针在悬停窗口小部件时更改为光标类型。光标类型可以设置为箭头或点。 |
| 7    | disabledforeground | 禁用时窗口小部件的字体颜色。                                 |
| 8    | font               | 小部件文本的字体类型。                                       |
| 9    | fg                 | 小部件的前景色。                                             |
| 10   | postcommand        | 命令可以设置为当mourse悬停菜单时调用的任何函数。             |
| 11   | relief             | 窗口小部件的边框类型。默认类型为RAISED。                     |
| 12   | image              | 用于在菜单上显示图像。                                       |
| 13   | selectcolor        | 用于在选中时显示checkbutton或radiobutton的颜色。             |
| 14   | tearoff            | 默认情况下，菜单中的选项从位置1开始。如果我们设置撕裂= 1，那么它将从第0位开始。 |
| 15   | title              | 如果要更改窗口标题，请将此选项设置为窗口标题。               |



方法

“菜单”窗口小部件包含以下方法。

| SN   | 选项                           | 说明                                                     |
| ---- | ------------------------------ | -------------------------------------------------------- |
| 1    | add_command（options）         | 用于将菜单项添加到菜单中。                               |
| 2    | add_radiobutton（options）     | 此方法将radiobutton添加到菜单中。                        |
| 3    | add_checkbutton（options）     | 此方法用于将复选框添加到菜单中。                         |
| 4    | add_cascade（options）         | 用于通过将给定菜单与父菜单相关联来为父菜单创建分层菜单。 |
| 5    | add_separator（）              | 用于将分隔线添加到菜单中。                               |
| 6    | add（type，options）           | 用于将特定菜单项添加到菜单中。                           |
| 7    | delete（startindex，endindex） | 用于删除指定范围内存在的菜单项。                         |
| 8    | entryconfig（index，options）  | 它用于配置由给定索引标识的菜单项。                       |
| 9    | index（item）                  | 用于获取指定菜单项的索引。                               |
| 10   | insert_seperator（index）      | 用于在指定的索引处插入分隔符。                           |
| 11   | invoke（index）                | 它用于调用与指定索引处给出的选项相关联。                 |
| 12   | type（index）                  | 它用于获取索引指定的选择类型。                           |

**创建顶级菜单**

可以通过实例化Menu小部件并将菜单项添加到菜单来创建顶级菜单。

例1

```python
# !/usr/bin/python3  
  
from tkinter import *  
  
top = Tk()  
  
def hello():  
    print("hello!")  
  
# create a toplevel menu  
menubar = Menu(root)  
menubar.add_command(label="Hello!", command=hello)  
menubar.add_command(label="Quit!", command=top.quit)  
  
# display the menu  
top.config(menu=menubar)  
  
top.mainloop()

备注：accelerator
1. 显示该菜单项的加速键（快捷键）
2. 例如 accelerator = "Ctrl+N"
3. 该选项仅显示，并没有实现加速键的功能（通过按键绑定实现）
```

输出：

![360截图1761061292104120.png](https://img.php.cn/upload/image/221/660/695/1562034318459059.png)

单击hello Menubutton将在控制台上打印hello，而单击Quit Menubutton将退出python应用程序。

例2

```python
from tkinter import Toplevel, Button, Tk, Menu  
  
top = Tk()  
menubar = Menu(top)  
file = Menu(menubar, tearoff=0)  
file.add_command(label="New")  
file.add_command(label="Open")  
file.add_command(label="Save")  
file.add_command(label="Save as...")  
file.add_command(label="Close")  
  
file.add_separator()  
  
file.add_command(label="Exit", command=top.quit)  
  
menubar.add_cascade(label="File", menu=file)  
edit = Menu(menubar, tearoff=0)  
edit.add_command(label="Undo")  
  
edit.add_separator()  
  
edit.add_command(label="Cut")  
edit.add_command(label="Copy")  
edit.add_command(label="Paste")  
edit.add_command(label="Delete")  
edit.add_command(label="Select All")  
  
menubar.add_cascade(label="Edit", menu=edit)  
help = Menu(menubar, tearoff=0)  
help.add_command(label="About")  
menubar.add_cascade(label="Help", menu=help)  
  
top.config(menu=menubar)  
top.mainloop()
```

输出：

![python-tkinter-menu-output2.png](https://img.php.cn/upload/image/209/293/613/1562034306596988.png)

# Python Tkinter Menubutton菜单按钮

最近更新时间：2019-07-02 10:14:54

简介

Menubutton小部件可以定义为始终向用户显示的下拉菜单。它用于为用户提供选择应用程序中存在的适当选择的选项。

------

Menubutton小部件可以定义为始终向用户显示的下拉菜单。它用于为用户提供选择应用程序中存在的适当选择的选项。

Menubutton用于在python应用程序中实现各种类型的菜单。菜单与Menubutton相关联，可以在用户点击时显示Menubutton的选项。

下面给出了使用python tkinter Menubutton的语法。

句法

```python
w = Menubutton(Top,options)
```

下面给出了各种选项的列表。

| SN   | 选项               | 说明                                                         |
| ---- | ------------------ | ------------------------------------------------------------ |
| 1    | activebackground   | 窗口小部件处于焦点时窗口小部件的背景颜色                     |
| 2    | activeforeground   | 窗口小部件处于焦点时窗口小部件文本的字体颜色                 |
| 3    | anchor             | 它指定窗口小部件分配的空间大于所需空间时窗口小部件内容的确切位置 |
| 4    | bg                 | 它指定小部件的背景颜色                                       |
| 5    | bitmap             | 设置为要显示给窗口小部件的图形内容                           |
| 6    | bd                 | 它代表边界的大小。默认值为2像素                              |
| 7    | cursor             | 当小部件位于焦点下时，鼠标指针将更改为指定的光标类型。光标类型的可能值是箭头或点等 |
| 8    | direction          | 可以指定方向，以便菜单可以显示到按钮的指定方向。使用LEFT，RIGHT或ABOVE相应地放置控件 |
| 9    | disabledforeground | 禁用窗口小部件时窗口小部件的文本颜色                         |
| 10   | fg                 | 小部件的正常前景色                                           |
| 11   | height             | Menubutton的垂直尺寸。它被指定为行数                         |
| 12   | highlightcolor     | 显示焦点下小部件的高亮颜色                                   |
| 13   | image              | 小部件上显示的图像                                           |
| 14   | justify            | 当文本无法填充小部件的宽度时，这指定了小部件下文本的确切位置。我们可以使用LEFT进行左对齐，使用右进行右对齐，使用CENTER进行中心对齐 |
| 15   | menu               | 它表示使用Menubutton指定的菜单                               |
| 16   | padx               | 小部件的水平填充                                             |
| 17   | pady               | 小部件的垂直填充                                             |
| 18   | relief             | 此选项指定边框的类型。默认值为RAISED                         |
| 19   | state              | 启用Mousebutton的正常状态。我们可以将其设置为DISABLED以使其无响应 |
| 20   | text               | 随窗口小部件显示的文本                                       |
| 21   | textvariable       | 我们可以将字符串类型的控制变量设置为文本变量，以便我们可以在运行时控制窗口小部件的文本 |
| 22   | underline          | 默认情况下，窗口小部件的文本没有加下划线，但我们可以设置此选项以使窗口小部件的文本加下划线 |
| 23   | width              | 它表示小部件的宽度（以字符为单位）。默认值为20               |
| 24   | wraplength         | 我们可以在行数中打破小部件的文本，以便文本包含不大于指定值的行数 |



例

```python
# !/usr/bin/python3  
  
from tkinter import *  
  
top = Tk()  
  
top.geometry("200x250")  
  
menubutton = Menubutton(top, text = "Language", relief = FLAT)  
  
menubutton.grid()  
  
menubutton.menu = Menu(menubutton)  
  
menubutton["menu"]=menubutton.menu  
  
menubutton.menu.add_checkbutton(label = "Hindi", variable=IntVar())  
  
menubutton.menu.add_checkbutton(label = "English", variable = IntVar())  
  
menubutton.pack()  
  
top.mainloop()
```

输出：

![360截图1761061292104120.png](https://img.php.cn/upload/image/789/706/837/1562033682980803.png)

# Python Tkinter Scale滑块

最近更新时间：2019-07-02 13:55:30

简介

Scale小部件用于实现python应用程序的图形滑块，以便用户可以滑动滑块上显示的值范围并选择其中的一个。 我们可以控制最小值和最大值以及比例的分辨率。当用户被迫从给定的值范围中仅选择一个值时，它提供了Entry小部件的替代方法。

------

Scale小部件用于实现python应用程序的图形滑块，以便用户可以滑动滑块上显示的值范围并选择其中的一个。

我们可以控制最小值和最大值以及比例的分辨率。当用户被迫从给定的值范围中仅选择一个值时，它提供了Entry小部件的替代方法。

下面给出了使用Scale小部件的语法。

句法

```python
w = Scale(top, options)
```

 下面给出了可能的选项列表。

| SN   | 选项                | 说明                                                         |
| ---- | ------------------- | ------------------------------------------------------------ |
| 1    | activebackground    | 具有焦点时窗口小部件的背景颜色。                             |
| 2    | bg                  | 小部件的背景颜色。                                           |
| 3    | bd                  | 小部件的边框大小。默认值为2像素。                            |
| 4    | command             | 设置每次移动滑块时调用的步骤。如果滑块快速移动，则回调在结束时完成。 |
| 5    | cursor              | 鼠标指针更改为分配给此选项的光标类型。它可以是箭头，点等。   |
| 6    | digits              | 如果用于控制比例数据的控制变量是字符串类型，则此选项用于指定将数字比例转换为字符串时的位数。 |
| 7    | font                | 小部件文本的字体类型。                                       |
| 8    | fg                  | 文本的前景色。                                               |
| 9    | from_               | 它用于表示小部件范围的一端。                                 |
| 10   | highlightbackground | 小部件没有焦点时的高亮颜色。                                 |
| 11   | highlighcolor       | 小部件具有焦点时的高亮颜色。                                 |
| 12   | label               | 可以设置为某些文本，可以显示为带标尺的标签。如果刻度是水平的，则显示在左上角;如果刻度是垂直的，则显示在右上角。 |
| 13   | length              | 它表示小部件的长度。如果比例为水平，则表示X维度;如果比例为垂直，则表示y维度。 |
| 14   | orient              | 可根据秤的类型设置为水平或垂直。                             |
| 15   | relief              | 它代表边界的类型。默认值为FLAT。                             |
| 16   | repeatdelay         | 此选项指示在滑块重复开始向该方向移动之前按下按钮的持续时间。默认值为300毫秒。 |
| 17   | resolution          | 设置为对刻度值进行的最小变化。                               |
| 18   | showvalue           | 默认情况下，缩放的值以文本形式显示。我们可以将此选项设置为0以禁止标签。 |
| 19   | sliderlength        | 它表示滑块窗口沿刻度长度的长度。默认值为30像素。但是，我们可以将其更改为适当的值。 |
| 20   | state               | 默认情况下，scale小部件处于活动状态。我们可以将其设置为DISABLED以使其无响应。 |
| 21   | takefocus           | 默认情况下，焦点会循环显示缩放小部件。如果我们不希望这种情况发生，我们可以将此选项设置为0。 |
| 22   | tickinterval        | 比例值显示在指定的滴答间隔的倍数上。 tickinterval的默认值为0。 |
| 23   | to                  | 它表示一个浮点或整数值，它指定由比例表示的范围的另一端。     |
| 24   | troughcolor         | 它代表通过的颜色。                                           |
| 25   | variable            | 它表示比例的控制变量。                                       |
| 26   | width               | 它表示小部件的贯穿部分的宽度。                               |

**方法**



| SN   | 方法         | 说明                     |
| ---- | ------------ | ------------------------ |
| 1    | get（）      | 它用于获取比例的当前值。 |
| 2    | set（value） | 用于设置比例的值。       |

**例**

```python
from tkinter import *  
  
def select():  
   sel = "Value = " + str(v.get())  
   label.config(text = sel)  
     
top = Tk()  
top.geometry("200x100")  
v = DoubleVar()  
scale = Scale( top, variable = v, from_ = 1, to = 50, orient = HORIZONTAL)  
scale.pack(anchor=CENTER)  
  
btn = Button(top, text="Value", command=select)  
btn.pack(anchor=CENTER)  
  
label = Label(top)  
label.pack()  
  
top.mainloop()
```

输出：

![360截图1761061292104120.png](https://img.php.cn/upload/image/189/459/738/1562047207337683.png)

# Python Tkinter Scrollbar滚动条

最近更新时间：2019-07-02 14:06:16

简介

滚动条小部件用于向下滚动其他小部件的内容，如列表框，文本和画布。但是，我们也可以为Entry小部件创建水平滚动条。

------

Python Tkinter滚动条

滚动条小部件用于向下滚动其他小部件的内容，如列表框，文本和画布。但是，我们也可以为Entry小部件创建水平滚动条。

下面给出了使用Scrollbar小部件的语法。

句法

```python
w = Scrollbar(top, options)
```

下面给出了可能的选项列表。

|      |      |      |
| ---- | ---- | ---- |
|      |      |      |
|      |      |      |
|      |      |      |

SN选项说明

1 activebackground具有焦点时窗口小部件的背景颜色。

2 bg小部件的背景颜色。

3 bd小部件的边框宽度。

4command可以将其设置为与列表关联的过程，每次移动滚动条时都可以调用该过程。

5cursor鼠标指针更改为设置为此选项的光标类型，可以是箭头，点等。

6 elementborderwidth它表示箭头和滑块周围的边框宽度。默认值为-1。

7 Highlightbackground当窗口小部件没有焦点时，焦点高亮颜色。

8 highlighcolor当小部件具有焦点时，焦点高亮颜色。

9 highlightthickness它代表焦点高光的厚度。

10 jump它用于控制滚动跳转的行为。如果设置为1，则在用户释放鼠标按钮时调用回调。

11 orient可根据滚动条的方向将其设置为HORIZONTAL或VERTICAL。

12 repeatdelay此选项指示在滑块重复开始向该方向移动之前按下按钮的持续时间。默认值为300毫秒。

13 repeatinterval重复间隔的默认值为100。

14 takefocus默认情况下，我们可以通过此小部件选中焦点。如果我们不想要这种行为，我们可以将此选项设置为0。

15 troughcolor它代表槽的颜色。

16 width表示滚动条的宽度。

方法

小部件提供以下方法。

|      |      |      |
| ---- | ---- | ---- |
|      |      |      |
|      |      |      |
|      |      |      |
|      |      |      |
|      |      |      |

SN方法说明

1 get（）返回两个数字a和b，表示滚动条的当前位置。

2 set（first，last）用于将滚动条连接到其他小部件w。此方法的其他窗口小部件的yscrollcommand或xscrollcommand。

例

```python
from tkinter import *  
  
top = Tk()  
sb = Scrollbar(top)  
sb.pack(side = RIGHT, fill = Y)  
  
mylist = Listbox(top, yscrollcommand = sb.set )  
  
for line in range(30):  
    mylist.insert(END, "Number " + str(line))  
  
mylist.pack( side = LEFT )  
sb.config( command = mylist.yview )  
  
mainloop()
```

输出：

![360截图1761061292104120.png](https://img.php.cn/upload/image/495/343/772/1562047553693557.png)

# Python Tkinter Toplevel顶层窗口

最近更新时间：2019-07-02 15:54:27

简介

Toplevel小部件用于创建和显示由窗口管理器直接管理的顶层窗口。顶层窗口小部件可能有也可能没有父窗口。当python应用程序需要在新窗口中表示一些额外信息，弹出窗口或小组件组时，将使用toplevel小部件。

------

Toplevel小部件用于创建和显示由窗口管理器直接管理的顶层窗口。顶层窗口小部件可能有也可能没有父窗口。

当python应用程序需要在新窗口中表示一些额外信息，弹出窗口或小组件组时，将使用toplevel小部件。

顶层窗户有标题栏，边框和其他窗户装饰。

下面给出了使用Toplevel小部件的语法。

句法

```python
w = Toplevel(options)
```

下面给出了可能的选项列表。

| SN   | 选项   | 说明                                                         |
| ---- | ------ | ------------------------------------------------------------ |
| 1    | bg     | 它代表窗口的背景颜色。                                       |
| 2    | bd     | 表示窗口的边框大小。                                         |
| 3    | cursor | 当鼠标在窗口中时，鼠标指针变为设置为箭头，点等的光标类型。   |
| 4    | class_ | 文本小部件中选择的文本将导出以选择到窗口管理器。我们可以将其设置为0以使此行为为false。 |
| 5    | font   | 插入窗口小部件的文本的字体类型。                             |
| 6    | fg     | 小部件的前景色。                                             |
| 7    | height | 它表示窗口的高度。                                           |
| 8    | relief | 它代表窗口的类型。                                           |
| 9    | width  | 表示窗口的宽度，                                             |

方法

与Toplevel小部件关联的方法在以下列表中给出。

| SN   | 方法                     | 说明                                                         |
| ---- | ------------------------ | ------------------------------------------------------------ |
| 1    | deiconify（）            | 此方法用于显示窗口。                                         |
| 2    | frame（）                | 它用于显示系统相关的窗口标识符。                             |
| 3    | group(window)            | 用于将此窗口添加到指定的窗口组。                             |
| 4    | iconify（）              | 用于将顶层窗口转换为图标。                                   |
| 5    | protocol(name, function) | 用于提及将为特定协议调用的功能。                             |
| 6    | state（）                | 它用于获取窗口的当前状态。可能的值包括normal，iconic，withdrawn和icon。 |
| 7    | transient（[master]）    | 用于将此窗口转换为瞬态窗口（临时）。                         |
| 8    | withdraw（）             | 它用于删除窗口但不会销毁它。                                 |
| 9    | maxsize（width，height） | 用于声明窗口的最大大小。                                     |
| 10   | minsize(width, height)   | 用于声明窗口的最小尺寸。                                     |
| 11   | positionfrom（who）      | 用于定义位置控制器。                                         |
| 12   | resizable(width, height) | 用于控制窗口是否可调整大小。                                 |
| 13   | sizefrom（who）          | 用于定义大小控制器。                                         |
| 14   | title(string)            | 用于定义窗口的标题。                                         |

例

```python
from tkinter import *  
  
root = Tk()  
  
root.geometry("200x200")  
  
def open():  
    top = Toplevel(root)  
    top.mainloop()  
  
btn = Button(root, text = "open", command = open)  
  
btn.place(x=75,y=50)  
  
root.mainloop()
```

输出：

![360截图1761061292104120.png](https://img.php.cn/upload/image/844/137/796/1562054045210115.png)

# Python Tkinter Spinbox自设值

最近更新时间：2019-07-02 16:13:11

简介

Spinbox小部件是Entry小部件的替代方案。它为用户提供了一系列值，用户可以从中选择一个值。它用于给予用户一些固定数量的值以供选择的情况。

------

Spinbox小部件是Entry小部件的替代方案。它为用户提供了一系列值，用户可以从中选择一个值。

它用于给予用户一些固定数量的值以供选择的情况。

我们可以使用Spinbox的各种选项来装饰小部件。下面给出了使用Spinbox的语法。

句法

```python
w = Spinbox(top, options)
```

下面给出了可能的选项列表。

| SN   | 选项               | 说明                                                         |
| ---- | ------------------ | ------------------------------------------------------------ |
| 1    | activebackground   | 具有焦点时窗口小部件的背景颜色。                             |
| 2    | bg                 | 小部件的背景颜色。                                           |
| 3    | bd                 | 小部件的边框宽度。                                           |
| 4    | command            | 与每次调用窗口小部件状态时调用的窗口小部件的关联回调。       |
| 5    | cursor             | 鼠标指针更改为分配给此选项的光标类型。                       |
| 6    | disabledbackground | 禁用时窗口小部件的背景颜色。                                 |
| 7    | disabledforeground | 禁用时窗口小部件的前景色。                                   |
| 8    | fg                 | 小部件的正常前景色。                                         |
| 9    | font               | 小部件内容的字体类型。                                       |
| 10   | format             | 此选项用于格式字符串。它没有默认值。                         |
| 11   | from_              | 用于显示小部件的起始范围。                                   |
| 12   | justify            | 它用于指定多行小部件内容的对齐方式。默认为LEFT。             |
| 13   | relief             | 它用于指定边框的类型。默认 SUNKEN。                          |
| 14   | repeatdelay        | 此选项用于控制按钮自动重复。该值以毫秒为单位。               |
| 15   | repeatinterval     | 类似于repeatdelay。该值以毫秒为单位。                        |
| 16   | state              | 它表示小部件的状态。默认值为NORMAL。可能的值为NORMAL，DISABLED或“readonly”。 |
| 17   | textvariable       | 它就像一个控制变量，用于控制窗口小部件文本的行为。           |
| 18   | to                 | 它指定小部件值的最大限制。另一个由from_选项指定。            |
| 19   | validate           | 此选项控制小部件值的验证方式。                               |
| 20   | validatecommand    | 它与函数回调相关联，用于验证窗口小部件内容。                 |
| 21   | values             | 表示包含此小部件值的元组。                                   |
| 22   | vcmd               | 与验证命令相同。                                             |
| 23   | width              | 表示小部件的宽度。                                           |
| 24   | wrap               | 此选项包含Spinbox的向上和向下按钮。                          |
| 25   | xscrollcommand     | 此选项设置为滚动条的set（）方法，以使此小部件可水平滚动。    |

方法

有与窗口小部件关联的以下方法。

| SN   | 选项                           | 说明                                   |
| ---- | ------------------------------ | -------------------------------------- |
| 1    | delete（startindex，endindex） | 此方法用于删除指定范围内的字符。       |
| 2    | get（startindex，endindex）    | 用于获取指定范围内的字符。             |
| 3    | identify（x，y）               | 它用于标识指定范围内的窗口小部件元素。 |
| 4    | index（index）                 | 用于获取给定索引的绝对值。             |
| 5    | insert（index，string）        | 此方法用于在指定的索引处插入字符串。   |
| 6    | invoke（element）              | 它用于调用与窗口小部件关联的回调。     |

例

```python
from tkinter import *  
  
top = Tk()  
  
top.geometry("200x200")  
  
spin = Spinbox(top, from_= 0, to = 25)  
  
spin.pack()  
  
top.mainloop()
```

输出：

![360截图1761061292104120.png](https://img.php.cn/upload/image/112/186/685/1562055185404049.png)

# Python Tkinter PanedWindow窗口布局管理

最近更新时间：2019-07-02 17:24:25

简介

PanedWindow小部件的作用类似于Container小部件，其中包含一个或多个水平或垂直排列的子窗口小部件（窗格）。通过使用鼠标移动称为框格的分隔线，用户可以调整子窗格的大小。

------

PanedWindow小部件的作用类似于Container小部件，其中包含一个或多个水平或垂直排列的子窗口小部件（窗格）。通过使用鼠标移动称为框格的分隔线，用户可以调整子窗格的大小。

每个窗格仅包含一个窗口小部件PanedWindow用于在python应用程序中实现不同的布局。

下面给出了使用PanedWindow的语法。

句法

```
w= PanedWindow(master, options)
```

下面给出了可能的选项列表。

| SN   | 选项        | 说明                                                         |
| ---- | ----------- | ------------------------------------------------------------ |
| 1    | bg          | 它表示窗口小部件没有焦点时的背景颜色。                       |
| 2    | bd          | 它表示小部件的3D边框大小。默认选项指定槽不包含边框，而箭头和滑块包含2像素边框大小。 |
| 3    | borderwidth | 它表示小部件的边框宽度。默认值为2像素。                      |
| 4    | cursor      | 鼠标指针在窗口上方时更改为指定的光标类型。                   |
| 5    | handlepad   | 此选项表示手柄与窗扇末端之间的距离。对于水平方向，它是窗扇顶部和手柄之间的距离。默认值为8像素。 |
| 6    | handlesize  | 它表示句柄的大小。默认大小为8像素。但是，手柄始终是方形。    |
| 7    | height      | 它表示小部件的高度。如果我们不指定高度，则将通过子窗口的高度来计算。 |
| 8    | orient      | 如果我们想要将子窗口并排放置，则Orient将设置为HORIZONTAL。如果我们想要从上到下放置子窗口，可以将其设置为VERTICAL。 |
| 9    | relief      | 它代表边界的类型。默认值为FLAT。                             |
| 10   | sashpad     | 它代表每个窗扇周围的填充。默认值为0。                        |
| 11   | sashrelief  | 它代表每个窗扇周围的边框类型。默认值为FLAT。                 |
| 12   | sashwidth   | 它表示窗扇的宽度。默认值为2像素。                            |
| 13   | showhandle  | 设置为True以显示手柄。默认值为false。                        |
| 14   | width       | 表示小部件的宽度。如果我们不指定窗口小部件的宽度，则将通过子窗口小部件的大小来计算。 |

方法

有与PanedWindow关联的以下方法。

| SN   | 方法                        | 说明                                 |
| ---- | --------------------------- | ------------------------------------ |
| 1    | add（child，options）       | 用于向父窗口添加窗口。               |
| 2    | get（startindex，endindex） | 此方法用于获取指定范围内的文本。     |
| 3    | config（options）           | 它用于使用指定的选项配置窗口小部件。 |

例

```python
# !/usr/bin/python3  
from tkinter import *  
  
def add():  
    a = int(e1.get())  
    b = int(e2.get())  
    leftdata = str(a+b)  
    left.insert(1,leftdata)  
  
w1 = PanedWindow()  
w1.pack(fill = BOTH, expand = 1)  
  
left = Entry(w1, bd = 5)  
w1.add(left)  
  
w2 = PanedWindow(w1, orient = VERTICAL)  
w1.add(w2)  
  
e1 = Entry(w2)  
e2 = Entry(w2)  
  
w2.add(e1)  
w2.add(e2)  
  
bottom = Button(w2, text = "Add", command = add)  
w2.add(bottom)  
  
mainloop()
```

输出：

![360截图1761061292104120.png](https://img.php.cn/upload/image/810/122/448/1562059483263328.png)

# Python Tkinter LabelFrame标签框架

最近更新时间：2019-07-02 17:43:57

简介

LabelFrame小部件用于在其子小部件周围绘制边框。我们还可以显示LabelFrame小部件的标题。它就像一个容器，可以用来分组相互关联的小部件的数量，如Radiobuttons。

------

LabelFrame小部件用于在其子小部件周围绘制边框。我们还可以显示LabelFrame小部件的标题。它就像一个容器，可以用来分组相互关联的小部件的数量，如Radiobuttons。

此小部件是Frame小部件的变体，具有框架的所有功能。它还可以显示标签。

下面给出了使用LabelFrame小部件的语法。

句法

```
w = LabelFrame(top, options)
```

选项列表如下。

| SN   | 选项                | 说明                                                         |
| ---- | ------------------- | ------------------------------------------------------------ |
| 1    | bg                  | 小部件的背景颜色。                                           |
| 2    | bd                  | 表示指示器周围显示的边框大小。默认值为2像素。                |
| 3    | Class               | 类的默认值是LabelFrame。                                     |
| 4    | colormap            | 此选项用于指定要为此窗口小部件使用哪个colomap。通过colormap，我们指的是用于形成图形的256种颜色。使用此选项，我们可以重复使用此窗口小部件上另一个窗口的颜色映射。 |
| 5    | container           | 如果将其设置为true，LabelFrame将成为容器窗口小部件。默认值为false。 |
| 6    | cursor              | 它可以设置为光标类型，即箭头，点等。鼠标指针在窗口小部件上方时会更改为光标类型。 |
| 7    | fg                  | 它表示小部件的前景色。                                       |
| 8    | font                | 它表示窗口小部件文本的字体类型。                             |
| 9    | height              | 它表示小部件的高度。                                         |
| 10   | labelAnchor         | 它表示小部件中文本的确切位置。默认为NW（西北）               |
| 11   | labelwidget         | 它表示用于标签的小部件。如果未指定值，则框架将使用标签的文本。 |
| 12   | highlightbackground | 当窗口小部件没有焦点时，焦点高亮边框的颜色。                 |
| 13   | highlightcolor      | 当窗口小部件具有焦点时焦点突出显示的颜色。                   |
| 14   | highlightthickness  | 焦点高度边框的宽度。                                         |
| 15   | padx                | 小部件的水平填充。                                           |
| 16   | pady                | 小部件的垂直填充。                                           |
| 17   | relief              | 它代表了边境风格。缺省值是GROOVE。                           |
| 18   | text                | 它表示包含标签文本的字符串。                                 |
| 19   | width               | 表示框架的宽度。                                             |

例

```python
# !/usr/bin/python3  
from tkinter import *  
  
top = Tk()  
top.geometry("300x200")  
  
labelframe1 = LabelFrame(top, text="Positive Comments")  
labelframe1.pack(fill="both", expand="yes")  
  
toplabel = Label(labelframe1, text="Place to put the positive comments")  
toplabel.pack()  
  
labelframe2 = LabelFrame(top, text = "Negative Comments")  
labelframe2.pack(fill="both", expand = "yes")  
  
bottomlabel = Label(labelframe2,text = "Place to put the negative comments")  
bottomlabel.pack()  
  
top.mainloop()
```

 输出：

![360截图1761061292104120.png](https://img.php.cn/upload/image/612/218/273/1562060635622337.png)

# Python Tkinter messagebox消息框

最近更新时间：2019-07-03 09:14:00

简介

消息框模块用于显示python应用程序中的消息框。根据应用要求，有各种功能用于显示相关消息。

------

消息框模块用于显示python应用程序中的消息框。根据应用要求，有各种功能用于显示相关消息。

下面给出了使用消息框的语法。

句法

```
messagebox.function_name（title，message [，options]）
```

参数

function_name：它表示适当的消息框功能。

title：这是一个字符串，显示为消息框的标题。

message：消息框中显示为消息的字符串。

options：有多种选项可用于配置消息对话框。

可以使用的两个选项是default和parent。

**1. default**

默认选项用于提示默认按钮的类型，即消息框中的ABORT，RETRY或IGNORE。

**2. parent**

parent选项指定其上方的父窗口，将显示消息框。

有以下功能之一用于显示相应的消息框。所有函数都使用相同的语法，但具有特定的功能。

**使用方法：**

**1. showinfo（）**

showinfo（）消息框用于我们需要向用户显示一些相关信息的地方。

例

```python
# !/usr/bin/python3  
  
from tkinter import *  
  
from tkinter import messagebox  
  
top = Tk()  
  
top.geometry("100x100")      
  
messagebox.showinfo("information","Information")  
  
top.mainloop()
```

输出：

![360截图1761061292104120.png](https://img.php.cn/upload/image/154/379/794/1562116314946314.png)

**2. showwarning（）**

此方法用于向用户显示警告。

例

```python
# !/usr/bin/python3  
from tkinter import *  
  
from tkinter import messagebox  
  
top = Tk()  
top.geometry("100x100")  
messagebox.showwarning("warning","Warning")  
  
top.mainloop()
```

输出：

![python-tkinter-messagebox-output2.png](https://img.php.cn/upload/image/992/607/915/1562116322166199.png)

**3. showerror()**

此方法用于向用户显示错误消息。

例

```python
# !/usr/bin/python3  
from tkinter import *  
from tkinter import messagebox  
  
top = Tk()  
top.geometry("100x100")  
messagebox.showerror("error","Error")  
top.mainloop()
```

输出：

![python-tkinter-messagebox-output3.png](https://img.php.cn/upload/image/295/124/293/1562116333570756.png)

**4.askquestion()**

该方法用于向用户提出一些问题，可以回答是或否。

例

```python
# !/usr/bin/python3  
from tkinter import *  
from tkinter import messagebox  
  
top = Tk()  
top.geometry("100x100")  
messagebox.askquestion("Confirm","Are you sure?")  
top.mainloop()
```

输出：

![python-tkinter-messagebox-output4.png](https://img.php.cn/upload/image/735/206/115/1562116343940939.png)

**5. askokcancel（）**

此方法用于确认用户对某些应用程序活动的操作。

例

```python
# !/usr/bin/python3  
from tkinter import *  
from tkinter import messagebox  
  
top = Tk()  
top.geometry("100x100")  
messagebox.askokcancel("Redirect","Redirecting you to www.javatpoint.com")  
top.mainloop()
```

输出：

![python-tkinter-messagebox-output5.png](https://img.php.cn/upload/image/460/278/563/1562116351705810.png)

**6. askyesno（）**

此方法用于询问用户某些操作，用户可以回答是或否。

例

```python
# !/usr/bin/python3  
from tkinter import *  
from tkinter import messagebox  
  
top = Tk()  
top.geometry("100x100")  
messagebox.askyesno("Application","Got It?")  
top.mainloop()
```

输出：

![python-tkinter-messagebox-output6.png](https://img.php.cn/upload/image/891/105/753/1562116359771511.png)

**7. askretrycancel（）**

此方法用于询问用户是否再次执行特定任务。

例

```python
# !/usr/bin/python3  
from tkinter import *  
from tkinter import messagebox  
  
top = Tk()  
top.geometry("100x100")  
messagebox.askretrycancel("Application","try again?")  
  
top.mainloop()
```

输出：

![python-tkinter-messagebox-output7.png](https://img.php.cn/upload/image/141/543/820/1562116365886061.png)

# Python Tkinter Listbox列表框

最近更新时间：2019-07-02 10:06:44

简介

列表框小部件用于向用户显示列表项。我们只能在列表框中放置文本项，并且所有文本项都包含相同的字体和颜色。用户可以根据配置从列表中选择一个或多个项目。

------

列表框小部件用于向用户显示列表项。我们只能在列表框中放置文本项，并且所有文本项都包含相同的字体和颜色。

用户可以根据配置从列表中选择一个或多个项目。

下面给出了使用Listbox的语法。

```python
w = Listbox(parent,options)
```

下面给出了可能的选项列表。

| SN   | 选项               | 说明                                                         |
| ---- | ------------------ | ------------------------------------------------------------ |
| 1    | bg                 | 小部件的背景颜色                                             |
| 2    | bd                 | 它代表边界的大小，默认值为2像素                              |
| 3    | cursor             | 鼠标指针看起来像点，箭头等光标类型                           |
| 4    | font               | 列表框项的字体类型                                           |
| 5    | fg                 | 文字的颜色                                                   |
| 6    | height             | 它表示列表框中显示的行数，默认值为10                         |
| 7    | highlightcolor     | 窗口小部件处于焦点时的列表框项目的颜色                       |
| 8    | highlightthickness | 高亮的亮度                                                   |
| 9    | relief             | 边框的类型， 默认为SUNKEN                                    |
| 10   | selectbackground   | 用于显示所选文本的背景颜色                                   |
| 11   | selectmode         | 用于确定可从列表中选择的项目数，它可以设置为BROWSE，SINGLE，MULTIPLE，EXTENDED |
| 12   | width              | 它表示小部件的宽度（以字符为单位）                           |
| 13   | xscrollcommand     | 用于让用户水平滚动列表框                                     |
| 14   | yscrollcommand     | 用于让用户垂直滚动列表框                                     |

方法

有与Listbox关联的以下方法。

| SN   | 方法                         | 说明                                                         |
| ---- | ---------------------------- | ------------------------------------------------------------ |
| 1    | activate（index）            | 用于选择指定索引处的行                                       |
| 2    | curselection（）             | 它返回一个元组，其中包含所选元素的行号，从0开始计数。如果未选择任何元素，则返回一个空元组 |
| 3    | delete（first，last = None） | 用于删除给定范围内的行                                       |
| 4    | get（first，last = None）    | 用于获取给定范围内存在的列表项                               |
| 5    | index（i）                   | 用于将具有指定索引的行放在窗口小部件的顶部                   |
| 6    | insert（index，* elements）  | 用于在指定索引之前插入具有指定数量元素的新行                 |
| 7    | nearest（y）                 | 它返回列表框小部件的y坐标的最近一行的索引                    |
| 8    | see（index）                 | 它用于调整列表框的位置，使索引指定的行可见                   |
| 9    | size（）                     | 它返回Listbox小部件中存在的行数                              |
| 10   | xview（）                    | 这用于使小部件可水平滚动                                     |
| 11   | xview_moveto（fraction）     | 它用于使列表框可以按列表框中存在的最长行的宽度的一小部分水平滚动 |
| 12   | xview_scroll（number，what） | 它用于使列表框可以按指定的字符数水平滚动                     |
| 13   | yview（）                    | 它允许列表框可以垂直滚动                                     |
| 14   | yview_moveto（fraction）     | 它用于使列表框可以按列表框中存在的最长行的宽度分数垂直滚动   |
| 15   | yview_scroll（number，what） | 它用于使列表框可以按指定的字符数垂直滚动                     |

例1

```python
# !/usr/bin/python3  
from tkinter import *  
top = Tk()  
top.geometry("200x250")  
lbl = Label(top,text = "A list of favourite countries...")  
listbox = Listbox(top)  
listbox.insert(1,"India")  
listbox.insert(2, "USA")  
listbox.insert(3, "Japan")  
listbox.insert(4, "Austrelia")  
lbl.pack()  
listbox.pack()  
top.mainloop()
```

输出：

![360截图1761061292104120.png](https://img.php.cn/upload/image/902/574/467/1562032719300056.png)

示例2：从列表中删除活动项目

```python
# !/usr/bin/python3  
from tkinter import *  
top = Tk()  
top.geometry("200x250")  
lbl = Label(top,text = "A list of favourite countries...")  
listbox = Listbox(top)  
listbox.insert(1,"India")  
listbox.insert(2, "USA")  
listbox.insert(3, "Japan")  
listbox.insert(4, "Austrelia")  
#this button will delete the selected item from the list   
btn = Button(top, text = "delete", command = lambda listbox=listbox: listbox.delete(ANCHOR))  
lbl.pack()  
listbox.pack()  
btn.pack()  
top.mainloop()
```

输出：

![python-tkinter-listbox2.png](https://img.php.cn/upload/image/950/756/590/1562032713780073.png)

按下删除按钮后。

![python-tkinter-listbox3.png](https://img.php.cn/upload/image/933/839/128/1562032707110491.png)

# filedialog 文件选择器

## 一、filedialog简介

在tkinter中有三种标准对话框：

- messagebox
- filedialog
- colorchooser

之前我们说了 [messagebox 消息对话框](https://blog.csdn.net/nilvya/article/details/106219106)，再来认识认识 **filedialog 对话框**。

如果你的应用程序会需要到打开文件、保存文件、选择目录等关于文件的操作，那么就必须要用到 filedialog 。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200521130103993.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L25pbHZ5YQ==,size_16,color_FFFFFF,t_70)
下面是所有的 filedialog 的函数。

| 函数                | 用法                                         |
| ------------------- | -------------------------------------------- |
| asksaveasfilename() | 选择以什么文件名保存，返回文件名             |
| asksaveasfile()     | 选择以什么文件保存，创建文件并返回文件流对象 |
| askopenfilename()   | 选择打开什么文件，返回文件名                 |
| askopenfile()       | 选择打开什么文件，返回IO流对象               |
| askopenfiles()      | 选择打开多个文件，以列表形式返回多个IO流对象 |
| askdirectory()      | 选择目录，返回目录名                         |

看上去 filedialog 中的函数挺多的，但是我们常用的也就不外乎 askopenfilename 打开文件、asksaveasfilename 保存文件，顶多加上个askdirectory 选择目录。

## 二、运用实例

我们通过一个实际案例，来看看我们常用的 filedialog 函数是怎么使用的。

```python
import tkinter as tk 
from tkinter.filedialog import *
from PIL import Image
  
def selectFile():
	global img
	filepath = askopenfilename()  # 选择打开什么文件，返回文件名
	filename.set(filepath)             # 设置变量filename的值
	img = Image.open(filename.get())    # 打开图片

def outputFile():
	outputFilePath = askdirectory()   # 选择目录，返回目录名
	outputpath.set(outputFilePath)   # 设置变量outputpath的值

def fileSave():
	filenewpath = asksaveasfilename(defaultextension='.png') # 设置保存文件，并返回文件名，指定文件名后缀为.png
	filenewname.set(filenewpath)  # 设置变量filenewname的值
	img.save(str(filenewname.get())) # 设置保存图片

root = tk.Tk()
filename = tk.StringVar()
outputpath = tk.StringVar()
filenewname = tk.StringVar()

# 构建“选择文件”这一行的标签、输入框以及启动按钮，同时我们希望当用户选择图片之后能够显示原图的基本信息
tk.Label(root, text='选择文件').grid(row=1, column=0, padx=5, pady=5)
tk.Entry(root, textvariable=filename).grid(row=1, column=1, padx=5, pady=5)
tk.Button(root, text='打开文件', command=selectFile).grid(row=1, column=2, padx=5, pady=5)

# 构建“选择目录”这一行的标签、输入框以及启动按钮
tk.Label(root, text='选择目录').grid(row=2, column=0, padx=5, pady=5)
tk.Entry(root, textvariable=outputpath).grid(row=2, column=1, padx=5, pady=5)
tk.Button(root, text='点击选择', command=outputFile).grid(row=2, column=2, padx=5, pady=5)

# 构建“保存文件”这一行的标签、输入框以及启动按钮
tk.Label(root, text='保存文件').grid(row=3, column=0, padx=5, pady=5)
tk.Entry(root, textvariable=filenewname).grid(row=3, column=1, padx=5, pady=5)
tk.Button(root, text='点击保存', command=fileSave).grid(row=3, column=2, padx=5, pady=5)


root.mainloop()
```

运行程序来看一下。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200520223710943.gif#pic_center)

- 第一个按钮是选择文件，我们选择了一张图片，Entry 组件中值为返回的完整文件名
- 第二个按钮是选择目录，Entry 组件中值为返回的目录
- 第三个按钮是保存文件，我们点开自定义输入"111"，然后我们返回到文件夹就看到我们的原图就另存为了一张名为"111.png"的图片

## 三、参数&返回值

——

### 1. 参数

下面列出 filedialog 的各个函数可设置的参数以及用法。

| 参数             | 用法                                                         |
| ---------------- | ------------------------------------------------------------ |
| defaultextension | 1. 指定文件的后缀；2. 例如：defaultextension=".jpg"，那么当用户输入一个文件名 “逆旅鸭” 的时候，文件名会自动添加后缀为 “逆旅鸭.jpg”；3. 注意：如果用户输入文件名包含后缀，那么该选项不生效 |
| filetypes        | 1. 指定筛选文件类型的下拉菜单选项；2. 该选项的值是由 2 元祖构成的列表；3. 每个 2 元祖由（类型名，后缀）构成，例如：filetypes=[(“PNG”, “.png”), (“JPG”, “.jpg”), (“GIF”, “.gif”)] |
| initialdir       | 1. 指定打开/保存文件的默认路径；2. 默认路径是当前文件夹      |
| parent           | 1. 如果不指定该选项，那么对话框默认显示在根窗口上；2. 如果想要将对话框显示在子窗口 w 上，那么可以设置 parent=w |
| title            | 指定文件对话框的标题栏文本                                   |

——

### 2. 返回值

- asksaveasfilename() 选择以什么文件名保存，返回文件名
- asksaveasfile() 选择以什么文件保存，创建文件并返回文件流对象
- askopenfilename() 选择打开什么文件，返回文件名
- askopenfilenames() 选择打开多个文件，以元组形式返回多个文件名
- askopenfile() 选择打开什么文件，返回IO流对象
- askopenfiles() 选择打开多个文件，以列表形式返回多个IO流对象
- askdirectory() 选择目录，返回目录名
- 如果用户点击了取消按钮，那么返回值是空字符串

# colorchooser 颜色选择器

## 一、colorchooser简介

在tkinter中有三种标准对话框：

- messagebox
- filedialog
- colorchooser

认识完了 [messagebox 消息对话框](https://blog.csdn.net/nilvya/article/details/106219106)、 [filedialog 文件对话框](https://blog.csdn.net/nilvya/article/details/106221666)，最后再来看一下 colorchooser 颜色选择对话框。

colorchooser 很简单，它就是提供一个让用户可以根据自己需要选择的颜色界面。

可以说几乎绝大部分人都见过它。

就像这样子。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200521201429367.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L25pbHZ5YQ==,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200220173643303.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L25pbHZ5YQ==,size_16,color_FFFFFF,t_70)

## 二、运用实例

——

### 1. colorchooser基操

我们首先看看 colorchooser 怎么用的。

```python
import tkinter as tk
from tkinter.colorchooser import *

root = tk.Tk()

def colorselect():
    color = askcolor()
    print(color)

tk.Button(root, text="颜色框", command=colorselect).pack(padx=10, pady=10)

root.mainloop()
123456789101112
```

运行程序，我们来简单看下。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200521200650938.gif#pic_center)
——

### 2. 五彩缤纷的自由绘画

在[【tkinter组件专栏】Canvas：发挥你横溢才华的画布](https://blog.csdn.net/nilvya/article/details/105904236) 一文中，我们举了一个自由涂鸦的案例。

接下里我们对这个例子进行升级，结合 colorchooser 实现可以自己改变画笔的颜色。

```python
import tkinter as tk
from tkinter.colorchooser import *

# 创建颜色选择函数
def colorselect():
	global color             # 设置全局变量
	colors = askcolor()
	  # 设置color的颜色（R, G, B）, 因为在后面会传入只能传入整数，所以这里利用int() 进行四舍五入
	color = (int(colors[0][0]),int(colors[0][1]),int(colors[0][2])) 
	choosedcolor.set(str(color))         # 设置choosedcolor 变量的值

# 创建绘制函数
def paint(event):
    x1, y1 = event.x, event.y
    x2, y2 = event.x, event.y
    w.create_oval(x1, y1, x2, y2, fill='#%02x%02x%02x' %color, outline='#%02x%02x%02x' %color)  # 设置颜色为colorchooser所选择的

root = tk.Tk()

color = (0,0,0)
choosedcolor = tk.StringVar()
choosedcolor.set(str(color))   # 设置初始颜色

tk.Label(root, text="自由涂鸦").pack(padx=10,pady=10)

frame1 = tk.Frame(root)
tk.Button(frame1, text="选择颜色", relief='flat',command=colorselect).pack(side='left',padx=3, pady=3)
tk.Label(frame1, textvariable=choosedcolor).pack(side='left',padx=3, pady=3)
frame1.pack(anchor='w')

w = tk.Canvas(root, width=400, height=200)
w.pack()

w.bind("<B1-Motion>", paint)   # 绘制函数绑定鼠标左键

tk.Button(root, text="清除屏幕", command=(lambda a='all':w.delete(a))).pack(padx=5, pady=5)

root.mainloop()
1234567891011121314151617181920212223242526272829303132333435363738
```

运行程序

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200521200722703.gif#pic_center)
我们就可以通过 colorchooser 自己选择喜欢的颜色，从而改变画笔的颜色。

整个代码也不复杂，但是同样也是有需要注意的地方

- 要清楚的知道 colorchooser 的返回值是什么，是一个二元组，其中二元组的第一个是表示RGB值的三元组，这个是我们需要的
- 我们采用 `'#%02x%02x%02x' %(red, green, blue)`的方式实现自定义颜色，但是只能传入整数值
- 所以我们在获取 colorchooser RGB值的时候，需要使用`int()`来进行四舍五入取整

## 三、参数&返回值

——

### 1. 参数

colorchooser 涉及的参数不多。

| 参数   | 用法                                                         |
| ------ | ------------------------------------------------------------ |
| color  | 1. 要显示的初始的颜色；2. 默认颜色是浅灰色（light gray）     |
| parent | 1. 如果不指定该选项，那么对话框默认显示在根窗口上；2. 如果想要将对话框显示在子窗口 w 上，那么可以设置 parent=w |
| title  | 1. 指定颜色选择器标题栏的文本；2. 默认标题是“颜色”           |

——

### 2. 返回值

- 如果用户点击的 ‘确定’ 按钮，返回值是一个二元组 (triple, color)
  - triple 是一个三元组 (R, G, B)，其中 R, G, B 的范围是 [0, 255]（就是该颜色的 RGB 颜色）
  - color 是选中颜色的 16 进制的值
- 如果用户点击的 ‘取消’ 按钮，返回值是（None, None）

# simpledialog 简单输入对话框

| 属性名       | 介绍     |
| ------------ | -------- |
| title        | 标题     |
| initialvalue | 初始值   |
| prompt       | 提示文字 |
| minvalue     | 最小值   |
| maxvalue     | 最大值   |



```python
# 简单对话框，包括字符、整数和浮点数
import tkinter as tk
from tkinter import simpledialog


def input_str():
    r = simpledialog.askstring('字符录入', '请输入字符', initialvalue='hello world!')
    if r:
        print(r)
        label['text'] = '输入的是：' + r


def input_int():
    r = simpledialog.askinteger('整数录入', '请输入整数', initialvalue=100)
    if r:
        print(r)
        label['text'] = '输入的是：' + str(r)


def input_float():
    r = simpledialog.askfloat('浮点数录入', '请输入浮点数', initialvalue=1.01)
    if r:
        print(r)
        label['text'] = '输入的是：' + str(r)


root = tk.Tk()
root.title('对话框')
root.geometry('300x100+300+300')

label = tk.Label(root, text='输入对话框，包括字符、整数和浮点数', font='宋体 -14', pady=8)
label.pack()

frm = tk.Frame(root)
btn_str = tk.Button(frm, text='字符', width=6, command=input_str)
btn_str.pack(side=tk.LEFT)
btn_int = tk.Button(frm, text='整数', width=6, command=input_int)
btn_int.pack(side=tk.LEFT)
btn_int = tk.Button(frm, text='浮点数', width=6, command=input_float)
btn_int.pack(side=tk.LEFT)
frm.pack()

root.mainloop()
```

## **1.messagebox 消息对话框**

### askokcancel

![img](https://img.jbzj.com/file_images/article/202011/2020117153744805.png?2020107153758)

```python
import tkinter
# 导入消息对话框子模块
import tkinter.messagebox

# 创建主窗口
root = tkinter.Tk()
# 设置窗口大小
root.minsize(300,300)

# 声明函数
def okqqq():
  # 弹出对话框
  result = tkinter.messagebox.askokcancel(title = '标题~',message='内容：要吃饭嘛？')　　# 返回值为True或者False
  print(result)
# 添加按钮
btn1 = tkinter.Button(root,text = 'ok',command = okqqq)
btn1.pack()

# 加入消息循环
root.mainloop()
```

### askquestion

![img](https://img.jbzj.com/file_images/article/202011/2020117153827968.png?2020107153835)

```python
import tkinter
# 导入消息对话框子模块
import tkinter.messagebox

# 创建主窗口
root = tkinter.Tk()
# 设置窗口大小
root.minsize(300,300)

# 声明函数
def question():
  # 弹出对话框
  result = tkinter.messagebox.askquestion(title = '标题',message='内容：你吃饭了嘛？')
  # 返回值为：yes/no
  print(result)
# 添加按钮
btn1 = tkinter.Button(root,text = 'question',command = question)
btn1.pack()

# 加入消息循环
root.mainloop()
```

### askretrycancel　　(重试)

![img](https://img.jbzj.com/file_images/article/202011/2020117153906225.png?2020107153915)

```python
import tkinter
# 导入消息对话框子模块
import tkinter.messagebox

# 创建主窗口
root = tkinter.Tk()
# 设置窗口大小
root.minsize(300,300)
# 声明函数
def retry():
  # 弹出对话框
  result = tkinter.messagebox.askretrycancel(title = '标题',message='内容：女生拒绝了你！？')
  # 返回值为：True或者False
  print(result)
# 添加按钮
btn1 = tkinter.Button(root,text = 'retry',command = retry)
btn1.pack()
# 加入消息循环
root.mainloop()
```

### askyesno

![img](https://img.jbzj.com/file_images/article/202011/2020117153952185.png?202010715400)

```python
# 声明函数
def yesno():
  # 弹出对话框
  result = tkinter.messagebox.askyesno(title = '标题',message='内容：你喜欢我吗？')
  # 返回值为：True或者False
  print(result)
# 添加按钮
btn1 = tkinter.Button(root,text = 'yesno',command = yesno)
btn1.pack()
```

### showerror （出错）

![img](https://img.jbzj.com/file_images/article/202011/2020117154029824.png?2020107154037)

```python
# 声明函数
def error():
  # 弹出对话框
  result = tkinter.messagebox.showerror(title = '出错了！',message='内容：你的年龄不符合要求。')
  # 返回值为：ok
  print(result)
# 添加按钮
btn1 = tkinter.Button(root,text = 'error',command = error)
btn1.pack()
```

### showwarning(警告)

![img](https://img.jbzj.com/file_images/article/202011/2020117154108398.png?2020107154117)

```python
# 声明函数
def warning():
  # 弹出对话框
  result = tkinter.messagebox.showwarning(title = '出错了！',message='内容：十八岁以下禁止进入。')
  # 返回值为：ok
  print(result)
# 添加按钮
btn1 = tkinter.Button(root,text = 'warning',command = warning)
btn1.pack()
```

### showinto （信息提示）

![img](https://img.jbzj.com/file_images/article/202011/2020117154222826.png?2020107154229)

```python
# 声明函数
def info():
  # 弹出对话框
  result = tkinter.messagebox.showinfo(title = '信息提示！',message='内容：您的女朋友收到一只不明来历的口红！')
  # 返回值为：ok
  print(result)
# 添加按钮
btn1 = tkinter.Button(root,text = 'info',command = info)
btn1.pack()
```

## **2.simpledialog 简单信息对话框**

### asksting（获取字符串）

![img](https://img.jbzj.com/file_images/article/202011/2020117154301150.png?2020107154311)

```python
import tkinter
# 导入子模块
import tkinter.simpledialog

# 创建主窗口
root = tkinter.Tk()
# 设置窗口大小
root.minsize(300,300)

# 创建函数
def askname():
  # 获取字符串（标题，提示，初始值）
  result = tkinter.simpledialog.askstring(title = '获取信息',prompt='请输入姓名：',initialvalue = '可以设置初始值')
  # 打印内容
  print(result)
# 添加按钮
btn = tkinter.Button(root,text = '获取用户名',command = askname)
btn.pack()

# 加入消息循环
root.mainloop()
```

### askinteger(获取整型)

![img](https://img.jbzj.com/file_images/article/202011/2020117154350805.png?202010715440)

```python
import tkinter
# 导入消息对话框子模块
import tkinter.simpledialog

# 创建主窗口
root = tkinter.Tk()
# 设置窗口大小
root.minsize(300,300)

# 创建函数
def askage():
  # 获取整型（标题，提示，初始值）
  result = tkinter.simpledialog.askinteger(title = '获取信息',prompt='请输入年龄：',initialvalue = '18')
  # 打印内容
  print(result)
# 添加按钮
btn = tkinter.Button(root,text = '获取年龄',command = askage)
btn.pack()

# 加入消息循环
root.mainloop()
```

### askfloat(获取浮点型)

![img](https://img.jbzj.com/file_images/article/202011/2020117154437648.png?2020107154445)

```python
import tkinter
# 导入消息对话框子模块
import tkinter.simpledialog

# 创建主窗口
root = tkinter.Tk()
# 设置窗口大小
root.minsize(300,300)

# 创建函数
def askheight():
  # 获取浮点型数据（标题，提示，初始值）
  result = tkinter.simpledialog.askfloat(title = '获取信息',prompt='请输入身高（单位：米）：',initialvalue = '18.0')
  # 打印内容
  print(result)
# 添加按钮
btn = tkinter.Button(root,text = '获取身高',command = askheight)
btn.pack()

# 加入消息循环
root.mainloop()
```

Canvas（画布）组件为 Tkinter 的图形绘制提供了基础。Canvas 是一个高度灵活的组件，你可以用它绘制图形和图表，创建图形编辑器，并实现各种自定义的小部件。

# **何时使用 Canvas 组件？**

  Canvas 是一个通用的组件，通常用于显示和编辑图形。你可以用它来绘制线段、圆形、多边形，甚至是绘制其它组件。


**Canvas 组件支持对象**

·    arc（弧形、弦或扇形）

·    bitmap（内建的位图文件或 XBM 格式的文件）

·    image（BitmapImage 或PhotoImage 的实例对象）

·    line（线）

·    oval（圆或椭圆形）

·    polygon（多边形）

·    rectangle（矩形）

·    text（文本）

·    window（组件）

其中，弦、扇形、椭圆形、圆形、多边形和矩形这些“封闭式”图形都是由轮廓线和填充颜色组成的，但都可以设置为透明（传入空字符串表示透明）。

**坐标系**
  由于画布可能比窗口大（带有滚动条的 Canvas 组件），因此 Canvas 组件可以选择使用两种坐标系：

·    窗口坐标系：以窗口的左上角作为坐标原点

·    画布坐标系：以画布的左上角作为坐标原点

将窗口坐标系转换为画布坐标系，可以使用 canvasx() 或 canvasy() 方法：

\1. def callback(event):

\2.   canvas = event.widget

\3.   x =canvas.canvasx(event.x)

\4.   y =canvas.canvasy(event.y)

\5.   print canvas.find_closest(x,y)


**画布对象显示的顺序**
  Canvas 组件中创建的画布对象都会被列入显示列表中，越接近背景的画布对象位于显示列表的越下方。显示列表决定当两个画布对象重叠的时候是如何覆盖的（默认情况下新创建的会覆盖旧的画布对象的重叠部分，即位于显示列表上方的画布对象将覆盖下方那个）。当然，显示列表中的画布对象可以被重新排序。

**指定画布对象**
  Canvas 组件提供几种方法让你指定画布对象：

·    Item handles

·    Tags

·    ALL

·    CURRENT

Item handles 事实上是一个用于指定某个画布对象的整型数字（也成为画布对象的 ID）。当你在 Canvas 组件上创建一个画布对象的时候，Tkinter 将自动为其指定一个在该 Canvas 组件中独一无二的整型值。然后各种 Canvas 的方法可以通过这个值操纵该画布对象。
  Tags 是附在画布对象上的标签，Tags 由普通的非空白字符串组成。一个画布对象可以与多个 Tags 相关联，一个 Tag 也可用于描述多个画布对象。然而，与 Text 组件不同，没有指定画布对象的 Tags 不能进行事件绑定和配置样式。也就是说，Canvas 组件的 Tags 是仅为画布对象所拥有。
  Canvas 组件预定义了两个 Tags：ALL 和 CURRENT
  ALL（或"all"）表示 Canvas 组件中的所有画布对象
  CURRENT（或"current"）表示鼠标指针下的画布对象（如果有的话）

**参数
Canvas(master=None, \**options)** (class)
master -- 父组件
**options -- 组件选项，下方表格详细列举了各个选项的具体含义和用法：

| **选项**            | **含义**                                                     |
| ------------------- | ------------------------------------------------------------ |
| background          | 指定 Canvas 的背景颜色                                       |
| bg                  | 跟 background 一样                                           |
| borderwidth         | 指定 Canvas 的边框宽度                                       |
| bd                  | 跟 borderwidth 一样                                          |
| closeenough         | 1. 指定一个距离，当鼠标与画布对象的距离小于该值时，鼠标被认为在画布对象上 2. 该选项是一个浮点类型的值 |
| confine             | 1. 指定 Canvas 组件是否允许滚动超出 scrollregion 选项指定的范围 2. 默认值是 True |
| cursor              | 指定当鼠标在 Canvas 上飘过的时候的鼠标样式                   |
| height              | 1. 指定 Canvas 的高度 2. 单位是像素                          |
| highlightbackground | 指定当 Canvas 没有获得焦点的时候高亮边框的颜色               |
| highlightcolor      | 指定当 Canvas 获得焦点的时候高亮边框的颜色                   |
| highlightthickness  | 指定高亮边框的宽度                                           |
| relief              | 1. 指定 Canvas 的边框样式 2. 默认值是 FLAT 3. 其他可以选择的值是 SUNKEN，RAISED，GROOVE 和 RIDGE |
| scrollregion        | 1. 指定 Canvas 可以被滚动的范围 2. 该选项的值是一个 4 元组（x1, y1, x2, y2）表示的矩形 |
| selectbackground    | 指定当画布对象被选中时的背景色                               |
| selectborderwidth   | 指定当画布对象被选中时的边框宽度（选中边框）                 |
| selectforeground    | 指定当画布对象被选中时的前景色                               |
| state               | 1. 设置 Canvas 的状态：NORMAL 或 DISABLED 2. 默认值是 NORMAL 3. 注意：该值不会影响画布对象的状态 |
| takefocus           | 1. 指定使用 Tab 键可以将焦点移动到输入框中 2. 默认是开启的，可以将该选项设置为 False 避免焦点在此输入框中 |
| width               | 1. 指定 Canvas 的宽度 2. 单位是像素                          |
| xscrollcommand      | 1. 与 scrollbar（滚动条）组件相关联（水平方向） 2. 使用方法可以参考：[Scrollbar 组件](http://bbs.fishc.com/thread-59493-1-1.html) |
| xscrollincrement    | 1. 该选项指定 Canvas 水平滚动的“步长” 2. 例如 '3c' 表示 3 厘米，还可以选择的单位有 'i'（英寸），'m'（毫米）和 'p'（DPI，大约是 '1i' 等于 '72p'） 3. 默认值是 0，表示可以水平滚动到任意位置 |
| yscrollcommand      | 1. 与 scrollbar（滚动条）组件相关联（垂直方向） 2. 使用方法可以参考：[Scrollbar 组件](http://bbs.fishc.com/thread-59493-1-1.html) |
| yscrollincrement    | 1. 该选项指定 Canvas 垂直滚动的“步长” 2. 例如 '3c' 表示 3 厘米，还可以选择的单位有 'i'（英寸），'m'（毫米）和 'p'（DPI，大约是 '1i' 等于 '72p'） 3. 默认值是 0，表示可以水平滚动到任意位置 |


**方法
addtag(tag, method, \*args)**
-- 添加一个 Tag 到一系列画布对象中
-- 指定添加 Tag 的位置，可以是："above"，"all"，"below"，"closest"，"enclosed"，"overlapping" 或"withtag"
-- args 是附加参数，请参考下方等同的方法

**addtag_above(tag, item)**
-- 为显示列表中 item 上方的画布对象添加 Tag
-- 该方法相当于 addtag(tag, "above", item)
-- item 可以是单个画布对象的 ID，也可以是某个Tag

**addtag_all(tag)**
-- 为 Canvas 组件中所有的画布对象添加 Tag
-- 该方法相当于 addtag(tag, "all")

**addtag_below(tag, item)**
-- 为显示列表中 item 下方的画布对象添加 Tag
-- 该方法相当于 addtag(tag, "below", item)
-- item 可以是单个画布对象的 ID，也可以是某个Tag

**addtag_closest(tag, x, y, halo=None, start=None)**
-- 将 Tag 添加到与给定坐标（x, y）相临近的画布对象
-- 可选参数 halo 指定一个距离，表示以（x, y）为中心，该距离内的所有画布对象均添加 Tag
-- 可选参数 start 指定一个画布对象，该方法将为低于但最接近该对象的画布对象添加 Tag
-- 该方法相当于 addtag(tag, "closet", x, y,halo=None, start=None)
-- 注1：使用的是画布坐标系
-- 注2：如果同时由几个画布对象与给定坐标（x, y）的距离相同，则为位于显示列表上方的那个画布对象添加 Tag

**addtag_enclosed(tag, x1, y1, x2, y2)**
-- 为所有坐标在矩形（x1, y1, x2, y2）中的画布对象添加 Tag
-- 该方法相当于 addtag(tag, "enclosed", x1, y1, x2,y2)

**addtag_overlapped(tag, x1, y1, x2, y2)**
-- 跟 addtag_enclosed() 方法相似，不过该方法范围更广（即使画布对象只有一部分在矩形中也算）
-- 该方法相当于 addtag(tag, "overlapping", x1, y1,x2, y2)

**addtag_withtag(tag, item)**
-- 为 item 参数指定的画布对象添加 Tag
-- item 参数如果指定一个 Tag，则为所有拥有此Tag 的画布对象添加新的 Tag
-- item 参数如果指定一个画布对象，那么只为其添加 Tag
-- 该方法相当于 addtag(tag, "withtag", item)
-- item 可以是单个画布对象的 ID，也可以是某个Tag

**bbox(\*args)**
-- 返回一个四元组（x1, y1, x2, y2）用于描述args 指定的画布对象所在的矩形范围
-- 如果 args 参数忽略，返回所有的画布对象所在的矩形范围

**canvasx(screenx, gridspacing=None)**
-- 将窗口坐标系的 X 坐标（screenx）转化为画布坐标系
-- 如果提供 gridspacing 参数，则转换结果将为该参数的整数倍

**canvasy(screeny, gridspacing=None)**
-- 将窗口坐标系的 Y 坐标（screenx）转化为画布坐标系
-- 如果提供 gridspacing 参数，则转换结果将为该参数的整数倍

**coords(\*args)**
-- 如果仅提供一个参数（画布对象），返回该画布对象的坐标 (x1, y1, x2, y2)
-- 你可以通过 coords(item, x1, y1, x2, y2) 来移动画布对象

**create_arc(bbox, \**options)**

-- 根据 bbox (x1, y1, x2, y2) 创建一个扇形（PIESLICE）、弓形（CHORD）或弧形（ARC）
-- 新创建的画布对象位于显示列表的顶端
-- 创建成功后返回该画布对象的 ID
-- 下方表格列举了各个 options 选项的具体含义：

| **选项**               | **含义**                                                     |
| ---------------------- | ------------------------------------------------------------ |
| activedash             | 当画布对象状态为 ACTIVE 的时候，绘制虚线                     |
| activefill             | 当画布对象状态为 ACTIVE 的时候，填充颜色                     |
| activeoutline          | 当画布对象状态为 ACTIVE 的时候，绘制轮廓线                   |
| activeoutlinestipple   | 当画布对象状态为 ACTIVE 的时候，指定填充轮廓的位图           |
| activestipple          | 当画布对象状态为 ACTIVE 的时候，指定填充的位图               |
| activewidth            | 当画布对象状态为 ACTIVE 的时候，指定边框的宽度               |
| dash                   | 1. 指定绘制虚线轮廓 2. 该选项值是一个整数元组，元组中的元素分别代表短线的长度和间隔 3. 例如 (3, 5) 代表 3 个像素的短线和 5 个像素的间隔 |
| dashoffset             | 1. 指定虚线轮廓开始的偏移位置 2. 例如当 dash=(5, 1, 2, 1)，dashoffset=3，则从 2 开始画虚线 |
| disableddash           | 当画布对象状态为 DISABLE 的时候，绘制虚线                    |
| disabledfill           | 当画布对象状态为 DISABLE 的时候，填充颜色                    |
| disabledoutline        | 当画布对象状态为 DISABLE 的时候，绘制轮廓线                  |
| disabledoutlinestipple | 当画布对象状态为 DISABLE 的时候，指定填充轮廓的位图          |
| disabledstipple        | 当画布对象状态为 DISABLE 的时候，指定填充的位图              |
| disabledwidth          | 当画布对象状态为 DISABLE 的时候，指定边框的宽度              |
| extent                 | 1. 指定跨度（从 start 选项指定的位置开始到结束位置的角度） 2. 默认值是 90.0 |
| fill                   | 1. 指定填充的颜色 2. 空字符串表示透明                        |
| offset                 | 1. 指定当点画模式时填充位图的偏移 2. 该选项的值可以是："x,y", "#x,y", N, NE, E, SE, S, SW, W, NW, CENTER |
| outline                | 指定轮廓的颜色                                               |
| outlineoffset          | 1. 指定当点画模式绘制轮廓时位图的偏移 2. 该选项的值可以是："x,y", "#x,y", N, NE, E, SE, S, SW, W, NW, CENTER |
| outlinestipple         | 1. 当 outline 选项被设置时，该选项用于指定一个位图来填充边框 2. 默认值是空字符串，表示黑色 |
| start                  | 指定起始位置的偏移角度                                       |
| state                  | 1. 指定该画布对象的状态 2. 可以是 NORMAL，DISABLED（不可用，不响应事件）和 HIDDEN（隐藏） 3. 默认值是 NORMAL |
| stipple                | 1. 指定一个位图用于填充 2. 默认值是空字符串，表示实心        |
| style                  | 1. 指定该方法创建的是扇形（PIESLICE）、弓形（CHORD）还是弧形（ARC） 2. 默认创建的是扇形 |
| tags                   | 为创建的画布对象添加标签                                     |
| width                  | 指定边框的宽度                                               |


**create_bitmap(position, \**options)**
-- 在 position 指定的位置（x, y）创建一个位图对象
-- 创建成功后返回该位图对象的 ID
-- 下方表格列举了各个 options 选项的具体含义：

| **选项**           | **含义**                                                     |
| ------------------ | ------------------------------------------------------------ |
| activebackground   | 指定当位图对象状态为 ACTIVE 时候的背景颜色                   |
| activebitmap       | 指定当位图对象状态为 ACTIVE 时候填充的位图                   |
| activeforeground   | 指定当位图对象状态为 ACTIVE 时候的前景颜色                   |
| anchor             | 1. 指定位图在 position 参数的相对位置 2. N, NE, E, SE, S, SW, W, NW, 或 CENTER 来定位（EWSN代表东西南北，上北下南左西右东） 3. 默认值是 CENTER |
| background         | 1. 指定背景颜色 2. 即在位图中值为 0 的点的颜色 2. 空字符串表示透明 |
| bitmap             | 指定显示的位图                                               |
| disabledbackground | 指定当位图对象状态为 DISABLED 时候的背景颜色                 |
| disabledbitmap     | 指定当位图对象状态为 DISABLED 时候填充的位图                 |
| disabledforeground | 指定当位图对象状态为 DISABLED 时候的前景颜色                 |
| foreground         | 1. 指定前景颜色 2. 即在位图中值为 1 的点的颜色               |
| state              | 1. 指定该画布对象的状态 2. 可以是 NORMAL，DISABLED（不可用，不响应事件）和 HIDDEN（隐藏） 3. 默认值是 NORMAL |
| tags               | 为创建的位图对象添加标签                                     |


**create_image(position, \**options)**
-- 在 position 指定的位置（x, y）创建一个图片对象
-- 创建成功后返回该图片对象的 ID
-- 下方表格列举了各个 options 选项的具体含义：

| **选项**      | **含义**                                                     |
| ------------- | ------------------------------------------------------------ |
| activeimage   | 指定当图片对象状态为 ACTIVE 时候显示的图片                   |
| anchor        | 1. 指定位图在 position 参数的相对位置 2. N, NE, E, SE, S, SW, W, NW, 或 CENTER 来定位（EWSN代表东西南北，上北下南左西右东） 3. 默认值是 CENTER |
| image         | 指定要显示的图片                                             |
| disabledimage | 指定当图片对象状态为 DISABLED 时候显示的图片                 |
| state         | 1. 指定该图片对象的状态 2. 可以是 NORMAL，DISABLED（不可用，不响应事件）和 HIDDEN（隐藏） 3. 默认值是 NORMAL |
| tags          | 为创建的图片对象添加标签                                     |


**create_line(coords, \**options)**
-- 根据 coords 给定的坐标创建一条或多条线段
-- 如果给定的坐标多余两个点，则会首尾相连变成一条折线
-- 创建成功后返回该画布对象的 ID
-- 下方表格列举了各个 options 选项的具体含义：

| **选项**        | **含义**                                                     |
| --------------- | ------------------------------------------------------------ |
| activedash      | 当画布对象状态为 ACTIVE 的时候，绘制虚线                     |
| activefill      | 当画布对象状态为 ACTIVE 的时候，填充颜色                     |
| activestipple   | 当画布对象状态为 ACTIVE 的时候，指定填充的位图               |
| activewidth     | 当画布对象状态为 ACTIVE 的时候，指定边框的宽度               |
| arrow           | 1. 默认线段是不带箭头的 2. 你可以通过设置该选项添加箭头到线段中 3. FIRST 表示添加箭头到线段开始的位置 4. LAST 表示添加箭头到线段结束的位置 5. BOTH 表示两端均添加箭头 |
| arrowshape      | 1. 用一个三元组 (a, b, c) 来指定箭头的形状 2. a, b, c 分别代表箭头的三条边的长 3. 默认值是 (8, 10, 3) |
| capstyle        | 1. 指定线段两端的样式 2. 该选项的值可以是： -- BUTT（线段的两段平切于起点和终点） -- PROJECTING（线段的两段在起点和终点的位置分别延长一半 width 选项设置的长度） -- ROUND（线段的两段在起点和终点的位置分别延长一半 width 选项设置的长度并以圆角绘制） 3. 默认值是 BUTT 4. 如果还不理解请看小甲鱼下方图解你就秒懂了~ |
| dash            | 1. 绘制虚线 2. 该选项值是一个整数元组，元组中的元素分别代表短线的长度和间隔 3. 例如 (3, 5) 代表 3 个像素的短线和 5 个像素的间隔 |
| dashoffset      | 1. 指定虚线开始的偏移位置 2. 例如当 dash=(5, 1, 2, 1)，dashoffset=3，则从 2 开始画虚线 |
| disableddash    | 当画布对象状态为 DISABLE 的时候，绘制虚线                    |
| disabledfill    | 当画布对象状态为 DISABLE 的时候，填充颜色                    |
| disabledstipple | 当画布对象状态为 DISABLE 的时候，指定填充的位图              |
| disabledwidth   | 当画布对象状态为 DISABLE 的时候，指定边框的宽度              |
| fill            | 1. 指定填充的颜色 2. 空字符串表示透明                        |
| joinstyle       | 1. 指定当绘制两个相邻线段之间接口的样式 2. 该选项的值可以是： -- ROUND（以连接点为圆心，1/2 width 选项设置的长度为半径绘制圆角） -- BEVEL（在连接点处对两线段的夹角平切） -- MITER（沿着两线段的夹角延伸至一个点） 3. 默认值是 ROUND 4. 如果还不理解请看上方 create_line() 函数 joinstyle 选项的图解你就秒懂了~ |
| offset          | 1. 指定当点画模式时填充位图的偏移 2. 该选项的值可以是："x,y", "#x,y", N, NE, E, SE, S, SW, W, NW, CENTER |
| smooth          | 1. 该选项的值为 True 时，将绘制贝塞尔样条曲线代替线段（资料：[戳我](http://zh.wikipedia.org/wiki/貝茲曲線)） 2. 默认值为 False |
| splinesteps     | 1. 当绘制贝塞尔样条曲线的时候，该选项指定由多少条折线来构成曲线 2. 默认值是 12 3. 只有当 smooth 选项为 True 时该选项才能生效 |
| state           | 1. 指定该画布对象的状态 2. 可以是 NORMAL，DISABLED（不可用，不响应事件）和 HIDDEN（隐藏） 3. 默认值是 NORMAL |
| stipple         | 1. 指定一个位图用于填充 2. 默认值是空字符串，表示实心        |
| tags            | 为创建的画布对象添加标签                                     |
| width           | 指定边框的宽度                                               |

**
create_oval(bbox,\**options)**
-- 根据限定矩形 bbox 绘制一个椭圆
-- 新创建的画布对象位于显示列表的顶端
-- 创建成功后返回该画布对象的 ID
-- 下方表格列举了各个 options 选项的具体含义：

| **选项**               | **含义**                                                     |
| ---------------------- | ------------------------------------------------------------ |
| activedash             | 当画布对象状态为 ACTIVE 的时候，绘制虚线                     |
| activefill             | 当画布对象状态为 ACTIVE 的时候，填充颜色                     |
| activeoutline          | 当画布对象状态为 ACTIVE 的时候，绘制轮廓线                   |
| activeoutlinestipple   | 当画布对象状态为 ACTIVE 的时候，指定填充轮廓的位图           |
| activestipple          | 当画布对象状态为 ACTIVE 的时候，指定填充的位图               |
| activewidth            | 当画布对象状态为 ACTIVE 的时候，指定边框的宽度               |
| dash                   | 1. 指定绘制虚线轮廓 2. 该选项值是一个整数元组，元组中的元素分别代表短线的长度和间隔 3. 例如 (3, 5) 代表 3 个像素的短线和 5 个像素的间隔 |
| dashoffset             | 1. 指定虚线轮廓开始的偏移位置 2. 例如当 dash=(5, 1, 2, 1)，dashoffset=3，则从 2 开始画虚线 |
| disableddash           | 当画布对象状态为 DISABLE 的时候，绘制虚线                    |
| disabledfill           | 当画布对象状态为 DISABLE 的时候，填充颜色                    |
| disabledoutline        | 当画布对象状态为 DISABLE 的时候，绘制轮廓线                  |
| disabledoutlinestipple | 当画布对象状态为 DISABLE 的时候，指定填充轮廓的位图          |
| disabledstipple        | 当画布对象状态为 DISABLE 的时候，指定填充的位图              |
| disabledwidth          | 当画布对象状态为 DISABLE 的时候，指定边框的宽度              |
| fill                   | 1. 指定填充的颜色 2. 空字符串表示透明                        |
| offset                 | 1. 指定当点画模式时填充位图的偏移 2. 该选项的值可以是："x,y", "#x,y", N, NE, E, SE, S, SW, W, NW, CENTER |
| outline                | 指定轮廓的颜色                                               |
| outlineoffset          | 1. 指定当点画模式绘制轮廓时位图的偏移 2. 该选项的值可以是："x,y", "#x,y", N, NE, E, SE, S, SW, W, NW, CENTER |
| outlinestipple         | 1. 当 outline 选项被设置时，该选项用于指定一个位图来填充边框 2. 默认值是空字符串，表示黑色 |
| state                  | 1. 指定该画布对象的状态 2. 可以是 NORMAL，DISABLED（不可用，不响应事件）和 HIDDEN（隐藏） 3. 默认值是 NORMAL |
| stipple                | 1. 指定一个位图用于填充 2. 默认值是空字符串，表示实心        |
| tags                   | 为创建的画布对象添加标签                                     |
| width                  | 指定边框的宽度                                               |

 

**create_polygon(coords,\**options)**
-- 根据 coords 给定的坐标绘制一个多边形
-- 新创建的画布对象位于显示列表的顶端
-- 创建成功后返回该画布对象的 ID
-- 下方表格列举了各个 options 选项的具体含义：

| **选项**               | **含义**                                                     |
| ---------------------- | ------------------------------------------------------------ |
| activedash             | 当画布对象状态为 ACTIVE 的时候，绘制虚线                     |
| activefill             | 当画布对象状态为 ACTIVE 的时候，填充颜色                     |
| activeoutline          | 当画布对象状态为 ACTIVE 的时候，绘制轮廓线                   |
| activeoutlinestipple   | 当画布对象状态为 ACTIVE 的时候，指定填充轮廓的位图           |
| activestipple          | 当画布对象状态为 ACTIVE 的时候，指定填充的位图               |
| activewidth            | 当画布对象状态为 ACTIVE 的时候，指定边框的宽度               |
| dash                   | 1. 指定绘制虚线轮廓 2. 该选项值是一个整数元组，元组中的元素分别代表短线的长度和间隔 3. 例如 (3, 5) 代表 3 个像素的短线和 5 个像素的间隔 |
| dashoffset             | 1. 指定虚线轮廓开始的偏移位置 2. 例如当 dash=(5, 1, 2, 1)，dashoffset=3，则从 2 开始画虚线 |
| disableddash           | 当画布对象状态为 DISABLE 的时候，绘制虚线                    |
| disabledfill           | 当画布对象状态为 DISABLE 的时候，填充颜色                    |
| disabledoutline        | 当画布对象状态为 DISABLE 的时候，绘制轮廓线                  |
| disabledoutlinestipple | 当画布对象状态为 DISABLE 的时候，指定填充轮廓的位图          |
| disabledstipple        | 当画布对象状态为 DISABLE 的时候，指定填充的位图              |
| disabledwidth          | 当画布对象状态为 DISABLE 的时候，指定边框的宽度              |
| fill                   | 1. 指定填充的颜色 2. 空字符串表示透明                        |
| joinstyle              | 1. 指定当绘制两个相邻线段之间接口的样式 2. 该选项的值可以是： -- ROUND（以连接点为圆心，1/2 width 选项设置的长度为半径绘制圆角） -- BEVEL（在连接点处对两线段的夹角平切） -- MITER（沿着两线段的夹角延伸至一个点） 3. 默认值是 ROUND 4. 如果还不理解请看小甲鱼下方图解你就秒懂了~ |
| offset                 | 1. 指定当点画模式时填充位图的偏移 2. 该选项的值可以是："x,y", "#x,y", N, NE, E, SE, S, SW, W, NW, CENTER |
| outline                | 指定轮廓的颜色                                               |
| outlineoffset          | 1. 指定当点画模式绘制轮廓时位图的偏移 2. 该选项的值可以是："x,y", "#x,y", N, NE, E, SE, S, SW, W, NW, CENTER |
| outlinestipple         | 1. 当 outline 选项被设置时，该选项用于指定一个位图来填充边框 2. 默认值是空字符串，表示黑色 |
| smooth                 | 1. 该选项的值为 True 时，将绘制贝塞尔样条曲线代替线段（资料：[戳我](http://zh.wikipedia.org/wiki/貝茲曲線)） 2. 默认值为 False |
| splinesteps            | 1. 当绘制贝塞尔样条曲线的时候，该选项指定由多少条折线来构成曲线 2. 默认值是 12 3. 只有当 smooth 选项为 True 时该选项才能生效 |
| state                  | 1. 指定该画布对象的状态 2. 可以是 NORMAL，DISABLED（不可用，不响应事件）和 HIDDEN（隐藏） 3. 默认值是 NORMAL |
| stipple                | 1. 指定一个位图用于填充 2. 默认值是空字符串，表示实心        |
| tags                   | 为创建的画布对象添加标签                                     |
| width                  | 指定边框的宽度                                               |


**create_rectangle(bbox, \**options)**
-- 根据限定矩形 bbox 绘制一个矩形
-- 新创建的画布对象位于显示列表的顶端
-- 创建成功后返回该画布对象的 ID
-- 下方表格列举了各个 options 选项的具体含义：

| **选项**               | **含义**                                                     |
| ---------------------- | ------------------------------------------------------------ |
| activedash             | 当画布对象状态为 ACTIVE 的时候，绘制虚线                     |
| activefill             | 当画布对象状态为 ACTIVE 的时候，填充颜色                     |
| activeoutline          | 当画布对象状态为 ACTIVE 的时候，绘制轮廓线                   |
| activeoutlinestipple   | 当画布对象状态为 ACTIVE 的时候，指定填充轮廓的位图           |
| activestipple          | 当画布对象状态为 ACTIVE 的时候，指定填充的位图               |
| activewidth            | 当画布对象状态为 ACTIVE 的时候，指定边框的宽度               |
| dash                   | 1. 指定绘制虚线轮廓 2. 该选项值是一个整数元组，元组中的元素分别代表短线的长度和间隔 3. 例如 (3, 5) 代表 3 个像素的短线和 5 个像素的间隔 |
| dashoffset             | 1. 指定虚线轮廓开始的偏移位置 2. 例如当 dash=(5, 1, 2, 1)，dashoffset=3，则从 2 开始画虚线 |
| disableddash           | 当画布对象状态为 DISABLE 的时候，绘制虚线                    |
| disabledfill           | 当画布对象状态为 DISABLE 的时候，填充颜色                    |
| disabledoutline        | 当画布对象状态为 DISABLE 的时候，绘制轮廓线                  |
| disabledoutlinestipple | 当画布对象状态为 DISABLE 的时候，指定填充轮廓的位图          |
| disabledstipple        | 当画布对象状态为 DISABLE 的时候，指定填充的位图              |
| disabledwidth          | 当画布对象状态为 DISABLE 的时候，指定边框的宽度              |
| fill                   | 1. 指定填充的颜色 2. 空字符串表示透明                        |
| offset                 | 1. 指定当点画模式时填充位图的偏移 2. 该选项的值可以是："x,y", "#x,y", N, NE, E, SE, S, SW, W, NW, CENTER |
| outline                | 指定轮廓的颜色                                               |
| outlineoffset          | 1. 指定当点画模式绘制轮廓时位图的偏移 2. 该选项的值可以是："x,y", "#x,y", N, NE, E, SE, S, SW, W, NW, CENTER |
| outlinestipple         | 1. 当 outline 选项被设置时，该选项用于指定一个位图来填充边框 2. 默认值是空字符串，表示黑色 |
| state                  | 1. 指定该画布对象的状态 2. 可以是 NORMAL，DISABLED（不可用，不响应事件）和 HIDDEN（隐藏） 3. 默认值是 NORMAL |
| stipple                | 1. 指定一个位图用于填充 2. 默认值是空字符串，表示实心        |
| tags                   | 为创建的画布对象添加标签                                     |
| width                  | 指定边框的宽度                                               |

**create_text(position,\**options)**
-- 在 position 指定的位置（x, y）创建一个文本对象
-- 创建成功后返回该文本对象的 ID
-- 下方表格列举了各个 options 选项的具体含义：

| **选项**        | **含义**                                                     |
| --------------- | ------------------------------------------------------------ |
| activefill      | 指定当文本对象状态为 ACTIVE 时候文本的颜色                   |
| activestipple   | 指定当文本对象状态为 ACTIVE 时候文本填充的位图               |
| anchor          | 1. 指定文本在 position 参数的相对位置 2. N, NE, E, SE, S, SW, W, NW, 或 CENTER 来定位（EWSN代表东西南北，上北下南左西右东） 3. 默认值是 CENTER |
| disabledfill    | 指定当文本对象状态为 DISABLED 时候文本的颜色                 |
| disabledstipple | 指定当文本对象状态为 ACTIVE 时候文本填充的位图               |
| fill            | 指定文本的颜色                                               |
| font            | 指定文本的字体、尺寸等信息                                   |
| justify         | 1. 指定对于多行文本的对齐方式 2. 该选项可以使用的值有：LEFT（默认）、CENTER 和 RIGHT |
| offset          | 1. 指定当点画模式时填充位图的偏移 2. 该选项的值可以是："x,y", "#x,y", N, NE, E, SE, S, SW, W, NW, CENTER |
| state           | 1. 指定该画布对象的状态 2. 可以是 NORMAL，DISABLED（不可用，不响应事件）和 HIDDEN（隐藏） 3. 默认值是 NORMAL |
| stipple         | 1. 指定一个位图用于填充 2. 默认值是空字符串，表示实心        |
| tags            | 为创建的位图对象添加标签                                     |
| text            | 指定该文本对象将要显示的文本内容                             |
| width           | 1. 如果指定该选项，则文本会在该宽度处自动断行 2. 如果不指定该选项，文本对象的宽度等于文本最长行的长度 |


**create_window(position, \**options)**
-- 在 position 指定的位置（x, y）创建一个窗口组件
-- 创建成功后返回该窗口组件的 ID
-- 下方表格列举了各个 options 选项的具体含义：

| **选项** | **含义**                                                     |
| -------- | ------------------------------------------------------------ |
| anchor   | 1. 指定位图在 position 参数的相对位置 2. N, NE, E, SE, S, SW, W, NW, 或 CENTER 来定位（EWSN代表东西南北，上北下南左西右东） 3. 默认值是 CENTER |
| height   | 指定窗口组件的高度                                           |
| state    | 1. 指定该图片的状态 2. 可以是 NORMAL，DISABLED（不可用，不响应事件）和 HIDDEN（隐藏） 3. 默认值是 NORMAL |
| tags     | 为创建的图片对象添加标签                                     |
| width    | 指定窗口组件的宽度                                           |
| window   | 指定一个窗口组件                                             |


**dchars(item, from, to=None)**
-- 删除 item 中从from 到 to（包含）参数中的字符串
-- item 可以是单个画布对象的 ID，也可以是某个Tag

**delete(item)**
-- 删除 item 参数指定的画布对象
-- 如果不存在 item 指定的画布对象，并不会产生错误
-- item 可以是单个画布对象的 ID，也可以是某个Tag

**dtag(item, tag=None)**
-- 在 item 参数指定的画布对象中删除指定的 tag
-- 如果 tag 参数被忽略，则删除指定画布对象所有的tags
-- 如果不存在 item 指定的画布对象，并不会产生错误
-- item 可以是单个画布对象的 ID，也可以是某个Tag

**find_above(item)**
-- 返回在 item 参数指定的画布对象之上的 ID
-- 如果有多个画布对象符合要求，那么返回最顶端的那个
-- 如果 item 参数指定的是最顶层的画布对象，那么返回一个空元组
-- item 可以是单个画布对象的 ID，也可以是某个Tag

**find_all()**
-- 返回 Canvas 组件上所有的画布对象
-- 返回格式是一个元组，包含所有画布对象的 ID
-- 按照显示列表的顺序返回
-- 该方法相当于 find_withtag(ALL)

**find_below(item)**
-- 返回在 item 参数指定的画布对象之下的 ID
-- 如果有多个画布对象符合要求，那么返回最底端的那个
-- 如果 item 参数指定的是最底层的画布对象，那么返回一个空元组
-- item 可以是单个画布对象的 ID，也可以是某个Tag

**find_closest(x, y, halo=None, start=None)**
-- 返回一个元组，包含所有靠近点（x, y）的画布对象的ID
-- 如果没有符合的画布对象，则返回一个空元组
-- 可选参数 halo 用于增加点（x, y）的辐射范围
-- 可选参数 start 指定一个画布对象，该方法仅返回在显示列表中低于但最接近的一个 ID
-- 注意，点（x, y）的坐标是采用画布坐标系来表示

**find_enclosed(x1, y1, x2, y2)**
-- 返回完全包含在限定矩形内所有画布对象的 ID

**find_overlapping(x1, y1, x2, y2)**
-- 返回所有与限定矩形有重叠的画布对象的 ID（让然也包含在限定矩形内的画布对象）

**find_withtag(item)**
-- 返回 item 指定的所有画布对象的 ID
-- item 可以是单个画布对象的 ID，也可以是某个Tag

**focus(item=None)**
-- 将焦点移动到指定的 item
-- 如果有多个画布对象匹配，则将焦点移动到显示列表中第一个可以接受光标输入的画布对象
-- item 可以是单个画布对象的 ID，也可以是某个Tag

**gettags(item)**
-- 返回与 item 相关联的所有 Tags
-- item 可以是单个画布对象的 ID，也可以是某个Tag

**icursor(item, index)**
-- 将光标移动到 item 指定的画布对象
-- 这里要求 item 指定的画布对象支持文本输入和转移焦点
-- item 可以是单个画布对象的 ID，也可以是某个Tag

**index(item, index)**
-- 返回 index 在指定 item 中的位置（沿用 Python 的惯例：0 表示第一）
-- index 参数可以是：INSERT（当前光标的位置），END（最后一个字符的位置），SEL_FIRST（当前选中文本的起始位置），SEL_LAST（当前选中文本的结束位置），还可以使用格式为 "@x, y"（x 和 y 是画布坐标系）来获得与此坐标最接近的位置
-- item 可以是单个画布对象的 ID，也可以是某个Tag

**insert(item, index, text)**
-- 在允许进行文本编辑的画布对象的指定位置插入文本
-- index 参数可以是：INSERT（当前光标的位置），END（最后一个字符的位置），SEL_FIRST（当前选中文本的起始位置），SEL_LAST（当前选中文本的结束位置），还可以使用格式为 "@x, y"（x 和 y 是画布坐标系）来获得与此坐标最接近的位置
-- item 可以是单个画布对象的 ID，也可以是某个Tag

**itemcget(item, option)**
-- 获得指定 item 的选项的当前值
-- item 可以是单个画布对象的 ID，也可以是某个Tag

**itemconfig(item, \**options)**
-- 修改指定 item 的选项的当前值
-- item 可以是单个画布对象的 ID，也可以是某个Tag

**itemconfigure(item, \**options)**
-- 跟 itemconfig() 一样

**lift(item, \**options)**
-- 将指定画布对象移动到显示列表的顶部
-- item 可以是单个画布对象的 ID，也可以是某个Tag
-- 跟 tag_raise 一样

**lower(item, \**options)**
-- 将指定画布对象移动到显示列表的底部
-- item 可以是单个画布对象的 ID，也可以是某个Tag
-- 跟 tag_lower 一样

**move(item, dx, dy)**
-- 将 item 移动到新位置（x, y）
-- item 可以是单个画布对象的 ID，也可以是某个Tag

**postscript(\**options)**
-- 将 Canvas 的当前内容封装成 PostScript格式（[什么是 PostScript](http://baike.baidu.com/view/121488.htm)）表示
-- 下方表格列举了各个 options 选项的具体含义：

| **选项**  | **含义**                                                     |
| --------- | ------------------------------------------------------------ |
| colormode | 该选项的值可以是：'color'（颜色输出），'gray'（灰阶输出）和 'mono'（黑白输出） |
| file      | 1. 该选项指定一个文件，将 PostScript 写入该文件中 2. 如果忽略该选项，PostScript 将以字符串的形式返回 |
| height    | 1. 指定要打印的 Canvas 组件的高度 2. 默认值是 Canvas 组件的整体高度 |
| rotate    | 1. 如果该选项的值为 False，该页面将以纵向呈现 2. 如果该选项的值为 True，该页面将以横向呈现 |
| x         | 开始打印的最左边位置，以画布坐标系表示                       |
| y         | 开始打印的最顶端位置，以画布坐标系表示                       |
| width     | 1. 指定要打印的 Canvas 组件的宽度 2. 默认值是 Canvas 组件的整体宽度 |


**scale(item, xOrigin, yOrigin, xScale, yScale)**
-- 缩放 item 指定的画布对象
-- xOrigin 和 yOrigin 决定要缩放的位置
-- xScale 和 yScale 决定缩放的比例
-- item 可以是单个画布对象的 ID，也可以是某个Tag
-- 注意：该方法无法缩放 Text 画布对象

**scan_dragto(x, y)**
-- 见下方 scan_mark(x, y)

**scan_mark(x, y)**
-- 使用这种方式来实现 Canvas 内容的滚动
-- 需要将鼠标按钮事件及当前鼠标位置绑定到 scan_mark(x, y) 方法，然后再将 <motion> 事件及当前鼠标位置绑定到 scan_dragto(x,y) 方法，就可以实现 Canvas 在当前位置和sacn_mack(x, y) 指定的位置 (x, y) 之间滚动

**select_adjust(item, index)**
-- 调整选中范围，使得给定的 index 参数指定的位置在范围内
-- item 可以是单个画布对象的 ID，也可以是某个Tag

**select_clear()**
-- 取消 Canvas 组件中所有选中的范围

**select_from(item, index)**
-- 调整选中范围的起始位置为 index 参数指定的位置
-- item 可以是单个画布对象的 ID，也可以是某个Tag

**select_item()**
-- 范围在 Canvas 组件中当前文本的选中范围
-- 如果没有则返回 None

**select_to(item, index)**
-- 调整选中范围的结束位置为 index 参数指定的位置

**tag_bind(item, event=None, callback, add=None)**
-- 为 Canvas 组件上的画布对象绑定方法
-- event 参数是绑定的事件名称，callback 是与之关联的方法
-- item 可以是单个画布对象的 ID，也可以是某个Tag
-- 注意：与绑定事件关联的是画布对象，而不是 Tag

**tag_lower(item)**
-- 将一个或多个画布对象移至底部
-- 如果是多个画布对象，将它们都移至底部并保留原有顺序
-- item 可以是单个画布对象的 ID，也可以是某个Tag
-- 注意：该方法对窗口组件无效，请使用 lower 代替

**tag_raise(item)**
-- 将一个或多个画布对象移至顶部
-- 如果是多个画布对象，将它们都移至顶部并保留原有顺序
-- item 可以是单个画布对象的 ID，也可以是某个Tag
-- 注意：该方法对窗口组件无效，请使用 lift 代替

**tag_unbind(item, event, callback=None)**
-- 解除与 item 绑定的事件
-- item 可以是单个画布对象的 ID，也可以是某个Tag

**tkraise(item, \**options)**
-- 将指定画布对象移动到显示列表的顶部
-- item 可以是单个画布对象的 ID，也可以是某个Tag
-- 跟 tag_raise 一样

**type(item)**
-- 返回指定画布对象的类型
-- 返回值可以是："arc", "bitmap","image", "line", "oval", "polygon","rectangle", "text", 或"window"

**xview(\*args)**
-- 该方法用于在水平方向上滚动 Canvas 组件的内容，一般通过绑定 Scollbar 组件的 command 选项来实现（具体操作参考：[Scrollbar](http://bbs.fishc.com/thread-59493-1-1.html)）
-- 如果第一个参数是 MOVETO，则第二个参数表示滚动到指定的位置：0.0 表示最左端，1.0 表示最右端
-- 如果第一个参数是 SCROLL，则第二个参数表示滚动的数量，第三个参数表示滚动的单位（可以是 UNITS 或 PAGES），例如：xview(SCROLL,3, UNITS) 表示向右滚动三行

**xview_moveto(fraction)**
-- 跟 xview(MOVETO, fraction) 一样

**xview_scroll(number, what)**
-- 跟 xview(SCROLL, number, what) 一样

**yview(\*args)**
-- 该方法用于在垂直方向上滚动 Canvas 组件的内容，一般通过绑定 Scollbar 组件的 command 选项来实现（具体操作参考：[Scrollbar](http://bbs.fishc.com/thread-59493-1-1.html)）
-- 如果第一个参数是 MOVETO，则第二个参数表示滚动到指定的位置：0.0 表示最顶端，1.0 表示最底端
-- 如果第一个参数是 SCROLL，则第二个参数表示滚动的数量，第三个参数表示滚动的单位（可以是 UNITS 或 PAGES），例如：yview(SCROLL,3, PAGES) 表示向下滚动三页

**yview_moveto(fraction)**
-- 跟 yview(MOVETO, fraction) 一样

**yview_scroll(number, what)**
-- 跟 yview(SCROLL, number, what) 一样