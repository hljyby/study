from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master=None):

        super().__init__(master)
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.v = StringVar()
        self.v.set("f")

        # 创建组件
        Radiobutton(self, variable=self.v,
                    text="男", value="m").pack(side="left")
        Radiobutton(self, variable=self.v,
                    text="女", value="f").pack(side="left")

        Button(self, text="确定", command=self.confirm).pack(side="left")

    def confirm(self):
        messagebox.showinfo("测试", "选择性别为：" + self.v.get())


root = Tk()
root.geometry("500x500+300+300")

root.title("Label 组件的测试")

app = Application(master=root)

root.mainloop()
