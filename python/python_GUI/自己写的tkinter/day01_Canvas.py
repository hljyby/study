from tkinter import *
from tkinter import messagebox
import random


class Application(Frame):
    def __init__(self, master=None):

        super().__init__(master)
        self.pack()
        self.createWidget()

    def createWidget(self):
        # 创建组件
        self.canvas = Canvas(self, width=300, height=200, bg="green")
        self.canvas.pack()
        # 画一条直线
        line = self.canvas.create_line(10, 10, 30, 20, 40, 50) # 10,10 就是 x 和 y 后面同理
        # 画一个矩形
        rect = self.canvas.create_rectangle(50, 50, 100, 100)
        # 画一个椭圆，坐标两双，为椭圆的边界左下角和底部右下角
        oval = self.canvas.create_oval(50, 50, 100, 100)

        # self.photo = PhotoImage(file="D:\图片\Saved Pictures\下雨.gif")
        # self.canvas.create_image(250, 250, image=self.photo)

        Button(self, text="画十个矩形", command=self.draw50Recg).pack(side="left")

    def draw50Recg(self):
        for i in range(0, 10):
            x1 = random.randrange(int(self.canvas["width"])/2)
            y1 = random.randrange(int(self.canvas["height"])/2)
            x2 = x1 + random.randrange(int(self.canvas["width"])/2)
            y2 = y1 + random.randrange(int(self.canvas["height"])/2)
            self.canvas.create_rectangle(x1, y1, x2, y2)



root = Tk()

root.geometry("500x500+300+300")

root.title("Label 组件的测试")

app = Application(master=root)

root.mainloop()
