from tkinter import *
from tkinter import messagebox

class Application(Frame):
    def __init__(self, master=None):

        super().__init__(master)
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.btn1 = Button(self)
        self.btn1["text"] = "nihao "
        self.btn1.pack()
        self.btn1["command"] = self.songhua
        self.btnQuit = Button(self,text="退出",command=root.destroy)
        self.btnQuit.pack()
    def songhua(self):
        messagebox.showinfo("songhua","宋会很骄傲")


root = Tk()
root.geometry("500x500+300+300")

root.title("一个经典的GUI程序类设计")

app = Application(master=root)

root.mainloop()
