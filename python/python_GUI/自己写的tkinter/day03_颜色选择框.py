from tkinter import *
from tkinter import colorchooser

class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.place(x=10, y=10)
        self.createwidget()

    def createwidget(self):
        # 创建组件
        self.btn = Button(self, text="引用是怎么实现的",command=self.text)
        self.btn.pack(anchor=W)
        
    def text(self):
        rgb,hx = colorchooser.askcolor(color="red",title="选择背景颜色")
        print(rgb,hx)

if __name__ == '__main__':

    root = Tk()
    root.title("askcolor测试")
    root.geometry("300x300")
    app = Application(root)
    root.mainloop()
