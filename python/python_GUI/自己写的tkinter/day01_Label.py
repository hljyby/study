from tkinter import *
from tkinter import messagebox

class Application(Frame):
    def __init__(self, master=None):

        super().__init__(master)
        self.pack()
        self.createWidget()

    def createWidget(self):
        # 创建组件
        self.label01 = Label(self,text="百战程序软",width=10,height=10,bg="black",fg="white",justify="left")
        self.label01.pack()
        # 显示图像
        # global photo
        self.photo = PhotoImage(file="D:\图片\Saved Pictures\下雨.gif")
        self.label02 = Label(self,text="你猜",image=self.photo)
        self.label02.pack()

        self.label03 = Label(self,text="你猜a\n你猜a\n你猜a\n你猜a",borderwidth=1,relief="solid",justify="right")
        self.label03.pack()
root = Tk()
root.geometry("500x500+300+300")

root.title("Label 组件的测试")

app = Application(master=root)

root.mainloop()
