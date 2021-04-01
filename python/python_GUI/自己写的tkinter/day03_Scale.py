from tkinter import *


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.place(x=10, y=10)
        self.createwidget()

    def createwidget(self):
        # 创建组件
        self.label = Label(self, text="引用是怎么实现的")
        self.scale = Scale(self, from_=10, to=50, length=200, tickinterval=5, orient=HORIZONTAL, command=self.text)
        self.scale.pack(anchor=W)
        self.label.pack(anchor=W)

    def text(self, value):
        print("滑块的值", value)
        newFont = ('宋体', value)
        self.label.config(font=newFont)


if __name__ == '__main__':

    root = Tk()
    root.title("scale测试")
    root.geometry("300x300")
    app = Application(root)
    root.mainloop()
