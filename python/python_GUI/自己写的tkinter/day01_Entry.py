from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master=None):

        super().__init__(master)
        self.pack()
        self.createWidget()

    def createWidget(self):
        # 创建组件
        self.label01 = Label(self, text="用户名", width=10)
        self.label01.pack()

        self.v1 = StringVar()
        self.v2 = StringVar()

        self.entry01 = Entry(self,textvariable=self.v1)
        self.entry01.pack()

        self.v1.set("admin")

        self.label02 = Label(self, text="密码", width=10)
        self.label02.pack()

        self.entry02 = Entry(self,textvariable=self.v2,show="*")
        self.entry02.pack()

        self.button01 = Button(self, text="登录", width=10,bg="#ccc", fg="#333",command=self.login)
        self.button01.pack()

    def login(self):
        messagebox.showinfo(title="欢迎登录", message="欢迎"+self.entry01.get()+"登录")
        print(self.v1.get())
        print(self.entry01.get())


root = Tk()
root.geometry("500x500+300+300")

root.title("Label 组件的测试")

app = Application(master=root)

root.mainloop()
