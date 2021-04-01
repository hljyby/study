# 开始

文档：https://www.py.cn/manual/python-tkinter.html

```python
import tkinter as tk
from tkinter import messagebox as msgbox

root = tk.Tk()

button = tk.Button(root)

button["text"] = "你好"

button.pack() # 压缩 页面最小

def sayHellow(e):
    msgbox.showinfo("sayhellow","hellow world")

button.bind("<Button-1>",sayHellow) 

root.geometry("500x500+100+100") # 乘为窗口的长宽加/减 为窗口离屏幕边缘的距离

root.mainloop()
```

- bind 方法 为按钮绑定一个方法
- geometry  方法设置窗口的长宽和位置

## Label

```python
width;height
如果是字体，显示的是字体字符大小，如果是图片显示的是像素大小
font
指定字体和字体大小 如：font=(font_name,size)
image
显示在Label上的图像，目前tkinter只支持gif格式
fg;bg
fg（foreground）：前景色、bg（background）：背景色
justify
针对多行文字的对齐，可设置 justify属性，可选值 "left","center","right"

```

## Options 选项详解

我们可以通过三种方式设置Options选项，这在各种GUI组件中的用法都一致

1、创建对象时，使用命名参数（也叫关键字参数）

```python
fred = Button(self,fg="red",bg="blue")
```

2、创建对象都使用字典索引方式

```python
fred["fg"] = "red"
fred["bg"] = "blue"
```

3、创建对象后使用 config() 方法

```python
fred.config(fg="red",bg="blue")
```

## Button

```python
achor # 锚点
default :center (n ne e se s sw w nw)
```

## Entry

> **用户来输入一行字符串的控件，如果需要输入多行文档请使用text**

```python
self.v1 = StringVar()
self.v2 = StringVar()

self.entry01 = Entry(self,textvariable=self.v1,show="*") # 输入内容为* 输入密码时可用
self.entry01.pack()

self.v1.set("admin")

print(self.v1.get()) # 两种办法获取数据，数据双向绑定
print(self.entry01.get())
```

## Text

```python
self.text01 = Text(self, width=40,height=12,bg="gray")
self.text01.pack()

self.text01.insert(1.0,"0123456789\nabcdefg") # 第一行第0列，这两个会起冲突，以标的行列为准，多出来的往下排
self.text01.insert(2.3,"锄禾日当午，汗滴禾下土。谁知盘中餐，粒粒皆辛苦。\n")

self.text01.insert("insert",' Gaoqi ') # "insert" 也可以写成 INSERT
# insert 代表在光标处插入
self.text01.insert("end",'[sxt]') # "end" 也可以写成 END 下面同理
# end 代表在结尾处插入

self.text01.get(1.2,1.6)
# 获取从1.2~1.6的数据
print(self.text01.get(1.0,"end"))
# 返回所有数据

b1 = Button(self.text01,text="你猜")
self.text01.window_create(INSERT,window=b1)

self.text01.delete(1.0,"end")
self.text01.insert(INSERT,"haohaoxuexi\ntiantinaxiangshang \n杨博宇是好人百度一下\n 你就知道")
self.text01.tag_add("goods",1.0,1.9)
self.text01.tag_config("goods",background="yellow",foreground="red")

self.text01.tag_add("baidu",4.0,4.2)
self.text01.tag_config("baidu",underline=True)
self.text01.tag_bind("baidu","<Button-1>",self.webshow)
```

## Radiobutton 和  Checkbutton

```python
# Radiobutton
self.v = StringVar()
self.v.set("f")

# 创建组件
Radiobutton(self, variable=self.v,text="男", value="m").pack(side="left")
            
Radiobutton(self, variable=self.v,text="女", value="f").pack(side="left")

Button(self, text="确定", command=self.confirm).pack(side="left")

# checkbutton

self.v1 = IntVar()
self.v2 = IntVar()
self.v1.set(1)
self.v2.set(1)

# 创建组件
Checkbutton(self, variable=self.v1,
            text="视频", onvalue=1,offvalue=0).pack(side="left")
Checkbutton(self, variable=self.v2,
            text="音频", onvalue=1,offvalue=0).pack(side="left")

Button(self, text="确定", command=self.confirm).pack(side="left")


```

## Canvas

```python
# 创建组件
self.canvas = Canvas(self, width=300, height=200, bg="green")
self.canvas.pack()
# 画一条直线
line = self.canvas.create_line(10, 10, 30, 20, 40, 50)
# 画一个矩形
rect = self.canvas.create_rectangle(50, 50, 100, 100)
# 画一个椭圆，坐标两双，为椭圆的边界左下角和底部右下角
oval = self.canvas.create_oval(50, 50, 100, 100)

# self.photo = PhotoImage(file="D:\图片\Saved Pictures\下雨.gif")
# self.canvas.create_image(150, 170, image=self.photo)

Button(self, text="画十个矩形", command=self.draw50Recg).pack(side="left")

def draw50Recg(self):
    for i in range(0, 10):
        x1 = random.randrange(int(self.canvas["width"])/2)
        y1 = random.randrange(int(self.canvas["height"])/2)
        x2 = x1 + random.randrange(int(self.canvas["width"])/2)
        y2 = y1 + random.randrange(int(self.canvas["height"])/2)
        self.canvas.create_rectangle(x1, y1, x2, y2)
```

## Grid

```python
# 创建组件
self.label01 = Label(self, text="用户名")
self.label01.grid(row=0, column=0)
self.entry01 = Entry(self)
self.entry01.grid(row=0, column=1)

self.label02 = Label(self, text="用户名为手机号")
self.label02.grid(row=0, column=2, sticky=E)

self.label03 = Label(self, text="密码")
self.label03.grid(row=1, column=0)
self.entry02 = Entry(self)
self.entry02.grid(row=1, column=1)

Button(self, text="登录").grid(row=2, column=1, sticky=EW)
Button(self, text="取消").grid(row=2, column=2, sticky=E)
```

## 计算器界面

```PYTHON
# 创建组件
Entry(self).grid(row=0, column=0, columnspan=4, sticky=EW,pady=10)

# 第一种写死
# Button(self, text="MC").grid(row=1, column=0, sticky=EW)
# Button(self, text="M+").grid(row=1, column=1, sticky=EW)
# Button(self, text="M-").grid(row=1, column=2, sticky=EW)
# Button(self, text="MR").grid(row=1, column=3, sticky=EW)

# Button(self, text="C").grid(row=2, column=0, sticky=EW)
# Button(self, text="±").grid(row=2, column=1, sticky=EW)
# Button(self, text="x").grid(row=2, column=2, sticky=EW)
# Button(self, text="MR").grid(row=2, column=3, sticky=EW)

# Button(self, text="7").grid(row=3, column=0, sticky=EW)
# Button(self, text="8").grid(row=3, column=1, sticky=EW)
# Button(self, text="9").grid(row=3, column=2, sticky=EW)
# Button(self, text="-").grid(row=3, column=3, sticky=EW)

# Button(self, text="4").grid(row=4, column=0, sticky=EW)
# Button(self, text="5").grid(row=4, column=1, sticky=EW)
# Button(self, text="6").grid(row=4, column=2, sticky=EW)
# Button(self, text="+").grid(row=4, column=3, sticky=EW)

# Button(self, text="1").grid(row=5, column=0, sticky=EW)
# Button(self, text="2").grid(row=5, column=1, sticky=EW)
# Button(self, text="3").grid(row=5, column=2, sticky=EW)

# Button(self, text="+").grid(row=5, column=3, rowspan=2, sticky=NSEW)

# Button(self, text="0").grid(row=6, column=0, columnspan=2, sticky=EW)
# Button(self, text=".").grid(row=6, column=2, sticky=EW)

# 第二种 元祖循环
btnText = (("MC","M+","M-","MR"),("C","±","/","X"),(7,8,8,"-"),(4,5,6,"+"),(1,2,3,"="),(0,"."))

for indexi,i in enumerate(btnText):
    for indexii,ii in enumerate(i):
        print(indexi+1)
        if ii == "=":
            Button(self,text=ii).grid(row=(indexi+1),column=indexii,sticky=NSEW,rowspan=2)
        elif ii == 0:
            Button(self,text=ii).grid(row=(indexi+1),column=indexii,sticky=EW,columnspan=2)
        elif ii == ".":
            Button(self,text=ii).grid(row=(indexi+1),column=indexii+1,sticky=EW)
        else:
            Button(self,text=ii).grid(row=(indexi+1),column=indexii,sticky=EW)
```

## Pack

```python
for i in range(20):
    Label(self,width=5,height=10,borderwidth=1,relief="solid",bg="black" if i%2 == 0 else "white").pack(side="left",padx=2)
```

## Place

```python
class Application(Frame):
    def __init__(self, master=None):

        super().__init__(master)
        self.config(bg="blue",width=200,height=200)
        self.place(x=10,y=10)
        self.createWidget()

    def createWidget(self):
        # 创建组件
        Button(self,text="Vue").place(relx=0.7,rely=0.1,x=10,y=10)
        Button(self,text="Ajax").place(x=10,y=10,relwidth=0.5,relx=0.3)
        Button(self,text="JQuery").place(x=20,y=20)
        Button(self,text="axios").place(x=30,y=30)
```

## Event

```python
from tkinter import *

class Application(Frame):

    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.place(x=10,y=10)
        self.createwidget()

    def createwidget(self):
        # global c1clear
        self.btn01 = Button(self,text="haaaaaaahaha",bg="red")
        self.btn01.pack()
        self.c1 = Canvas(self, width=200, height=200, bg="green") #创建画布
        self.c1.pack()
        self.c1.bind("<Button-1>", self.mouseTest)   # 当鼠标左键点击时，触发事件
        self.c1.bind("<B1-Motion>", self.testDrag)   # 当按住鼠标左键并拖动时， 触发事件
        self.master.bind("<KeyPress>", self.keyboardTest)   # 当按下键盘时就触发
        self.master.bind("<KeyPress-a>", self.press_a_test)  # 按下a键时，触发事件
        self.master.bind("<KeyRelease-a>", self.release_a_test)  # 释放a键时，触发事件
        self.btn01.bind("<Button-1>", self.release_z_test)  # 释放a键时，触发事件

    def mouseTest(self, event):
   		 # 显示鼠标点击点相对于c1的位置
        print("鼠标左键单击位置(相对于父容器)为:{}{}".format(event.x, event.y))  
        # 显示鼠标点击点相对于屏幕的位置
        print("鼠标左键单击位置(相对于屏幕)为:{}{}".format(event.x_root, event.y_root)) 
        # 显示事件触发的控件
        print("事件绑定的组件:{}".format(event.widget))  

    def testDrag(self, event):
        # 在鼠标当前位置与当前位置+2的位置创建一个椭圆，拖动较慢时实现的是画图功能
        self.c1.create_oval(event.x, event.y, event.x+2, event.y+2,fill="black")

    def keyboardTest(self, event):
        print("键的keycode:{}，键的char:{}，键的keysym：{}"
              .format(event.keycode, event.char, event.keysym))

    def press_a_test(self, event):
        print("press a")

    def release_a_test(self, event):
        print("release a")
    
    def release_z_test(self, event):
        print(event.__dict__)
        print(event.widget.winfo_geometry())
        print(event.widget.winfo_height())
        print(event.widget.winfo_y())
        print(event.widget.winfo_x())
        print(event.widget.winfo_rootx())
        print(event.widget.winfo_rooty())
        print(event.widget.winfo_parent())


if __name__ == '__main__':

    root = Tk()
    root.title("event测试")
    root.geometry("300x300")
    app = Application(root)
    root.mainloop()
```

```python
widget.bind(event,handler)
```

## Lambda

```python
lambda 参数（逗号分隔）: 表达式（默认return 表达式结果）

lambda a,b:a+b
# 等于
def xxx(a,b):
    return a+b

# bind 绑定事件
self.btn01.bind("<Button-1>", lambda event:self.release_z_test(event,1,2))# 释放a键时，触发事件,传递参数
def release_z_test(self, event,a,b):
    print(a,b)

# command 绑定事件
self.btn01 = Button(self,text="haaaaaaahaha",bg="red",command=lambda:release_z_test(a,b))
def release_z_test(self,a,b):
    print(a,b)
```

## Bind

> **bind_class** 可以用在**enter** **ctrl-v** **代表粘贴**

```python
# 组件对象绑定（实例化对象绑定事件）
# bind(event,handler) event:事件 handler:触发的函数
btn01.bind("<Button-1>", lambda event:self.release_z_test(event,1,2))
def release_z_test(self, event,a,b):
    print(a,b)
    
# 组件类绑定（所有该类组件全部绑定该事件）
# bind_class(Widget,event,handler) Widget:类 event:事件 handler:触发的函数
btn01.bind_class(Button,"<Button-1>", lambda event:self.release_z_test(event,1,2))
def release_z_test(self, event,a,b):
    print(a,b)

# 全局绑定事件（所有的组件都会绑定）
# bind_all(event,handler)
#不常用
import tkinter
 
root = tkinter.Tk()
root.title('bind_all')
root.minsize(300,300)
 
btn1 = tkinter.Button(root,text = '按钮1')
btn1.pack()
 
entry =tkinter.Entry(root)
entry.pack()
 
text = tkinter.Text(root,width=30,height=5)
text.pack()
 
def changebg(e):
    e.widget['bg']='red'
#虽然仅绑定了按钮，但单击任一控件，都会改变所单击控件的背景色，相当于所有的控件都绑定了changebg函数。
btn1.bind_all('<Button-1>',changebg)
 
root.mainloop()
```

## Unbind

```python
# 解绑

canvas.bind("<Button-1>",some_function)
canvas.unbind("<Button-1>")
```

## Optionmenu

```python
self.v = StringVar()
self.v.set("上学")
self.om = OptionMenu(self,self.v,"上学","放学","上课")
self.om.pack()
```

## Scale

```python
from tkinter import *


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.place(x=10, y=10)
        self.createwidget()

    def createwidget(self):
        # 创建组件
        self.label = Label(self, text="引用是怎么实现的")
        self.scale = Scale(self, from_=10, to=50, length=200, tickinterval=5, orient=HORIZONTAL, command=self.text)
        self.scale.pack(anchor=W)
        self.label.pack(anchor=W)

    def text(self, value):
        print("滑块的值", value)
        newFont = ('宋体', value)
        self.label.config(font=newFont)


if __name__ == '__main__':

    root = Tk()
    root.title("scale测试")
    root.geometry("300x300")
    app = Application(root)
    root.mainloop()
```

## 颜色选择器

```python
from tkinter import *
from tkinter import colorchooser

class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.place(x=10, y=10)
        self.createwidget()

    def createwidget(self):
        # 创建组件
        self.btn = Button(self, text="引用是怎么实现的",command=self.text)
        self.btn.pack(anchor=W)
        
    def text(self):
        rgb,hx = colorchooser.askcolor(color="red",title="选择背景颜色")
        print(rgb,hx)

if __name__ == '__main__':

    root = Tk()
    root.title("askcolor测试")
    root.geometry("300x300")
    app = Application(root)
    root.mainloop()

```

## simpledialog

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

## Menu

```python
from tkinter import *
from tkinter import simpledialog

class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.place(x=10, y=10)
        self.createwidget()
        self.createMenu()

    def createwidget(self):
        # 创建组件
        self.menu = Menu(self.master,tearoff=False) # 是否可以撕下
        self.menuFile = Menu(self.menu,tearoff=False)
        self.menuEdit = Menu(self.menu,tearoff=False)
        self.menuHelp = Menu(self.menu,tearoff=False)

        self.menu.add_cascade(label="文件",menu=self.menuFile)
        self.menu.add_cascade(label="编辑",menu=self.menuEdit)
        self.menu.add_cascade(label="帮助",menu=self.menuHelp)

        self.menuFile.add_command(label="新建",accelerator="ctrl+n",command=self.text)
        self.menuFile.add_command(label="打开",accelerator="ctrl+o",command=self.text)
        self.menuFile.add_command(label="保存",accelerator="ctrl+s",command=self.text)

        self.menuFile.add_separator() # 添加分割线

        self.menuFile.add_command(label="退出",accelerator="ctrl+q",command=self.text)

        self.master.config(menu=self.menu)
        
    def createMenu(self):
        self.menubar = Menu(self.master)
        self.menubar.add_command(label='字体')

        self.master.bind("<3>",self.text2)
    def text(self):
        print(111)
    def text2(self,event):
        self.menubar.post(event.x_root,event.y_root)
if __name__ == '__main__':

    root = Tk()
    root.title("filedialog测试")
    root.geometry("300x300")
    app = Application(root)
    root.mainloop()


备注：accelerator
1. 显示该菜单项的加速键（快捷键）
2. 例如 accelerator = "Ctrl+N"
3. 该选项仅显示，并没有实现加速键的功能（通过按键绑定实现）
```

