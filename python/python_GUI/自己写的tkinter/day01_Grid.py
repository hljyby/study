from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master=None):

        super().__init__(master)
        self.pack()
        self.createWidget()

    def createWidget(self):
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


root = Tk()
root.geometry("500x500+300+300")

root.title("Grid 组件的测试")

app = Application(master=root)

root.mainloop()
