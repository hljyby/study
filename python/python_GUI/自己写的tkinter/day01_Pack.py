from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master=None):

        super().__init__(master)
        self.pack(anchor=W)
        self.createWidget()

    def createWidget(self):
        # 创建组件
        btnText = ("流行风", "中国风", "日本风", "重金属", "轻音乐", "二次元")

        for i in btnText:
            Button(self, text=i).pack(side="left", padx=10)

        self.btn01 = Button(self, text="zhzha")
        self.btn01.bind_class("Button", "<Button-1>", self.handler)
        self.btn01.pack(side="left", padx=10)

    def handler(self, event):
        print(event.x)


class Application02(Frame):
    def __init__(self, master=None):

        super().__init__(master)
        self.pack(anchor=W)
        self.createWidget()

    def createWidget(self):
        # 创建组件
        self.btn01 = Button(self, text="zhzha")
        # self.btn01.bind_class("Button","<Button-1>",self.handler)
        self.btn01.pack(side="left",padx=10)
        for i in range(20):
            Label(self,width=5,height=10,borderwidth=1,relief="solid",bg="black" if i%2 == 0 else "white").pack(side="left",padx=2)

root = Tk()
root.geometry("500x500+300+300")

root.title("Label 组件的测试")

app = Application(master=root)
app02 = Application02(master=root)

root.mainloop()
