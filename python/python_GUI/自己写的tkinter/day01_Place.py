from tkinter import *
from tkinter import messagebox

class Application(Frame):
    def __init__(self, master=None):

        super().__init__(master)
        self.config(bg="blue",width=200,height=200)
        self.place(x=10,y=10)
        self.createWidget()

    def createWidget(self):
        # 创建组件
        Button(self,text="Vue").place(relx=0.7,rely=0.1,x=10,y=10)
        Button(self,text="Ajax").place(x=10,y=10,relwidth=0.5,relx=0.3)
        Button(self,text="JQuery").place(x=20,y=20)
        Button(self,text="axios").place(x=30,y=30)

        
root = Tk()
root.geometry("500x500+300+300")

root.title("place 组件的测试")

app = Application(master=root)

root.mainloop()
