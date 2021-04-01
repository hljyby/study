from tkinter import *
from tkinter import simpledialog
from tkinter import filedialog
from tkinter import colorchooser

class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.config()
        self.pack(fill=BOTH,expand=True)
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

        self.menuFile.add_command(label="新建",accelerator="Ctrl+N",command=self.newFile)
        self.menuFile.add_command(label="打开",accelerator="Ctrl+O",command=self.openFile)
        self.menuFile.add_command(label="保存",accelerator="Ctrl+S",command=self.saveFile)

        self.menuFile.add_separator() # 添加分割线

        self.menuFile.add_command(label="退出",accelerator="ctrl+q",command=self.exit)

        self.master.config(menu=self.menu)
        
        self.v = StringVar()

        self.text01 = Text(self,font=("宋体",16))
        self.text01.pack(fill=BOTH,expand=True)

        # 绑定 按键
        self.master.bind("<Control-o>",lambda event:self.openFile())
        self.master.bind("<Control-s>",lambda event:self.saveFile())
        self.master.bind("<Control-q>",lambda event:self.exit())
        self.master.bind("<Control-n>",lambda event:self.newFile())

    def createMenu(self):
        self.menubar = Menu(self.master,tearoff=False)
        self.menubar.add_command(label='背景颜色',command=self.openAskcolor)

        self.master.bind("<3>",self.text2)
    
    def openFile(self):
        try:

            with filedialog.askopenfile(title="打开文本文件",initialdir="d:",filetypes=[("文本文件",".txt")]) as f:
                if f:
                    self.text01.delete(1.0,"end")
                    self.text01.insert(1.0,f.read())
                    self.filename = f.name
        except:
            pass

    def saveFile(self):
        with open(self.filename,"wb") as f:
            # print(self.text01.get(1.0,"end"))
            f.write(self.text01.get(1.0,"end").encode('utf8'))

    def newFile(self):
        # defaultextension 默认后缀
        self.filename = filedialog.asksaveasfilename(title="另存文件",initialfile="未命名.txt",filetypes=[("文本文件","*.txt")],defaultextension=".txt")
        self.saveFile()

    def exit(self):
        self.master.quit()

    def openAskcolor(self):
        rgb,hx = colorchooser.askcolor()
        self.text01.config(bg=hx)

    def text2(self,event):
        self.menubar.post(event.x_root,event.y_root)
if __name__ == '__main__':

    root = Tk()
    root.title("yby 的简易记事本")
    root.geometry("300x300")
    app = Application(root)
    root.mainloop()
