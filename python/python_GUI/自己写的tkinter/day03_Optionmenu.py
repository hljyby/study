from tkinter import *

class Application(Frame):

    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.place(x=10,y=10)
        self.createwidget()

    def createwidget(self):
        # 创建组件
        self.v = StringVar()
        self.v.set("上学")
        self.om = OptionMenu(self,self.v,"上学","放学","上课")
        self.om.pack()

if __name__ == '__main__':

    root = Tk()
    root.title("optionmenu测试")
    root.geometry("300x300")
    app = Application(root)
    root.mainloop()