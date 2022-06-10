from tkinter import *
from tkinter import messagebox

class Application(Frame):
    def __init__(self, master=None):

        super().__init__(master)
        self.pack()
        self.createWidget()

    def createWidget(self):
        # 创建组件
        self.button01 = Button(self,text="百战程序软",width=10,height=10,bg="black",fg="white",state="disabled",anchor="nw")
        self.button01.pack()
        # 显示图像
        # global photo
        self.photo = PhotoImage(file="D:\图片\Saved Pictures\下雨.gif")
        self.button02 = Button(self,text="你猜",image=self.photo)
        self.button02.pack()

        self.button03 = Button(self,text="你猜a\n你猜a\n你猜a\n你猜a",command=self.login)
        self.button03.pack()
    def login(self):
        messagebox.showinfo(title="欢迎登录",message="huanyinghdenglu")
        
root = Tk()
root.geometry("500x500+300+300")

root.title("Label 组件的测试")

app = Application(master=root)

root.mainloop()
