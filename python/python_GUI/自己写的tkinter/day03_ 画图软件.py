from tkinter import *
from tkinter import simpledialog
from tkinter import filedialog
from tkinter import colorchooser
import random


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(fill=BOTH, expand=True)
        self.x = 0
        self.y = 0
        self.backgroundcolor = "skyblue"
        self.fillColor = "#ccc"
        self.lastdraw = 0  # 图形的id
        self.startDrawflag = False
        self.createwidget()

    def createwidget(self):
        # 创建组件
        self.cnavas01 = Canvas(self, bg=self.backgroundcolor)
        self.cnavas01.pack(fill=X)

        # 创建按钮
        self.btn01 = Button(self, text="开始", name="开始")
        self.btn01.pack(side="left", padx=10)
        self.btn02 = Button(self, text="画笔", name="画笔")
        self.btn02.pack(side="left", padx=10)
        self.btn03 = Button(self, text="矩形", name="矩形")
        self.btn03.pack(side="left", padx=10)
        self.btn04 = Button(self, text="清屏", name="清屏")
        self.btn04.pack(side="left", padx=10)
        self.btn05 = Button(self, text="橡皮擦", name="橡皮擦")
        self.btn05.pack(side="left", padx=10)
        self.btn06 = Button(self, text="直线", name="直线")
        self.btn06.pack(side="left", padx=10)
        self.btn07 = Button(self, text="箭头直线", name="箭头直线")
        self.btn07.pack(side="left", padx=10)
        self.btn08 = Button(self, text="颜色", name="颜色")
        self.btn08.pack(side="left", padx=10)
        self.btn09 = Button(self, text="椭圆", name="椭圆")
        self.btn09.pack(side="left", padx=10)

        # 绑定事件
        self.btn01.bind_class('Button', "<1>", self.eventManager)
        self.cnavas01.bind("<ButtonRelease-1>", self.stopDraw)

    def eventManager(self, event):
        name = event.widget.winfo_name()
        print(name)
        # event.widget.config(bg="yellow")
        if name == "直线":
            self.cnavas01.bind("<B1-Motion>", self.myline)
        elif name == "箭头直线":
            self.cnavas01.bind("<B1-Motion>", self.mylineArrow)
        elif name == "矩形":
            self.cnavas01.bind("<B1-Motion>", self.myRect)
        elif name == "椭圆":
            self.cnavas01.bind("<B1-Motion>", self.myOval)
        elif name == "画笔":
            self.cnavas01.bind("<B1-Motion>", self.myPen)
        elif name == "橡皮擦":
            self.cnavas01.bind("<B1-Motion>", self.myErasor)
        elif name == "清屏":
            self.cnavas01.delete("all")
        elif name == "颜色":
            rgb,hx = colorchooser.askcolor(title="选择画笔颜色")
            self.fillColor = hx
            print(rgb)
        # event.widget.config(bg="yellow")
    def startDraw(self, event):
        self.cnavas01.delete(self.lastdraw)
        if not self.startDrawflag:
            self.startDrawflag = True
            self.x = event.x
            self.y = event.y

    def myline(self, event):

        self.startDraw(event)
        self.lastdraw = self.cnavas01.create_line(
            self.x, self.y, event.x, event.y, fill=self.fillColor)

    def mylineArrow(self, event):

        self.startDraw(event)
        self.lastdraw = self.cnavas01.create_line(
            self.x, self.y, event.x, event.y, arrow=LAST, fill=self.fillColor)

    def myRect(self, event):

        self.startDraw(event)
        self.lastdraw = self.cnavas01.create_rectangle(self.x, self.y, event.x, event.y, outline=self.fillColor)

    def myOval(self, event):

        self.startDraw(event)
        self.lastdraw = self.cnavas01.create_oval(self.x, self.y, event.x, event.y, outline=self.fillColor)

    def myPen(self, event):

        self.startDraw(event)
        random01 = random.randint(0,255)
        random02 = random.randint(0,255)
        random03 = random.randint(0,255)
        # self.cnavas01.create_line(self.x, self.y, event.x, event.y, fill=self.fillColor,width=5)
        # self.cnavas01.create_line(self.x, self.y, event.x, event.y, fill=f"({random01},{random02},{random03})",width=5)
        self.cnavas01.create_line(self.x, self.y, event.x, event.y, fill=self._from_rgb((random01,random02,random03)),width=5)
        self.x = event.x
        self.y = event.y

    def myErasor(self, event): # 橡皮擦

        self.startDraw(event)
        self.cnavas01.create_rectangle(event.x-4, event.y-4, event.x+4, event.y+4, fill=self.backgroundcolor,width=0)


    def stopDraw(self, event):
        self.lastdraw = 0
        self.startDrawflag = False

    def _from_rgb(self,rgb):
        """translates an rgb tuple of int to a tkinter friendly color code
        """
        return "#%02x%02x%02x" % rgb # %x是十六进制整数 %02x 是2位16进制整数不够用零补

if __name__ == '__main__':

    root = Tk()
    root.title("yby 的简易记事本")
    root.geometry("500x500")
    app = Application(root)
    root.mainloop()
