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
        self.menu = Menu(self.master,tearoff=False)
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
