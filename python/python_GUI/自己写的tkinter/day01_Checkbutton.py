from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master=None):

        super().__init__(master)
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.v1 = IntVar()
        self.v2 = IntVar()
        self.v1.set(1)
        self.v2.set(1)

        # 创建组件
        Checkbutton(self, variable=self.v1,
                    text="视频", onvalue=1,offvalue=0).pack(side="left")
        Checkbutton(self, variable=self.v2,
                    text="音频", onvalue=1,offvalue=0).pack(side="left")

        Button(self, text="确定", command=self.confirm).pack(side="left")

    def confirm(self):
        messagebox.showinfo("测试", "选择爱好为：" + ("视频" if self.v1.get() == 1 else "") + ("音频" if self.v2.get() == 1 else ""))


root = Tk()
root.geometry("500x500+300+300")

root.title("Label 组件的测试")

app = Application(master=root)

root.mainloop()
