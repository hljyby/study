from tkinter import *
from tkinter import simpledialog

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
        f = simpledialog.askinteger(title="选择数量",initialvalue=1,prompt='请输入年龄：',minvalue=10,maxvalue=20)
        if f:
            self.btn["text"] = f

if __name__ == '__main__':

    root = Tk()
    root.title("filedialog测试")
    root.geometry("300x300")
    app = Application(root)
    root.mainloop()
