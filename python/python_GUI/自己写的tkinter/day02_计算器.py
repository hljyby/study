from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master=None):

        super().__init__(master)
        self.pack()
        self.createWidget()

    def createWidget(self):
        # 创建组件
        Entry(self).grid(row=0, column=0, columnspan=4, sticky=EW,pady=10)
        # Button(self, text="MC").grid(row=1, column=0, sticky=EW)
        # Button(self, text="M+").grid(row=1, column=1, sticky=EW)
        # Button(self, text="M-").grid(row=1, column=2, sticky=EW)
        # Button(self, text="MR").grid(row=1, column=3, sticky=EW)

        # Button(self, text="C").grid(row=2, column=0, sticky=EW)
        # Button(self, text="±").grid(row=2, column=1, sticky=EW)
        # Button(self, text="x").grid(row=2, column=2, sticky=EW)
        # Button(self, text="MR").grid(row=2, column=3, sticky=EW)

        # Button(self, text="7").grid(row=3, column=0, sticky=EW)
        # Button(self, text="8").grid(row=3, column=1, sticky=EW)
        # Button(self, text="9").grid(row=3, column=2, sticky=EW)
        # Button(self, text="-").grid(row=3, column=3, sticky=EW)

        # Button(self, text="4").grid(row=4, column=0, sticky=EW)
        # Button(self, text="5").grid(row=4, column=1, sticky=EW)
        # Button(self, text="6").grid(row=4, column=2, sticky=EW)
        # Button(self, text="+").grid(row=4, column=3, sticky=EW)

        # Button(self, text="1").grid(row=5, column=0, sticky=EW)
        # Button(self, text="2").grid(row=5, column=1, sticky=EW)
        # Button(self, text="3").grid(row=5, column=2, sticky=EW)

        # Button(self, text="+").grid(row=5, column=3, rowspan=2, sticky=NSEW)

        # Button(self, text="0").grid(row=6, column=0, columnspan=2, sticky=EW)
        # Button(self, text=".").grid(row=6, column=2, sticky=EW)

        btnText = (("MC","M+","M-","MR"),("C","±","/","X"),(7,8,8,"-"),(4,5,6,"+"),(1,2,3,"="),(0,"."))

        for indexi,i in enumerate(btnText):
            for indexii,ii in enumerate(i):
                print(indexi+1)
                if ii == "=":
                    Button(self,text=ii).grid(row=(indexi+1),column=indexii,sticky=NSEW,rowspan=2)
                elif ii == 0:
                    Button(self,text=ii).grid(row=(indexi+1),column=indexii,sticky=EW,columnspan=2)
                elif ii == ".":
                    Button(self,text=ii).grid(row=(indexi+1),column=indexii+1,sticky=EW)
                else:
                    Button(self,text=ii).grid(row=(indexi+1),column=indexii,sticky=EW)

root = Tk()
root.geometry("200x200+300+300")

root.title("计算器")

app = Application(master=root)

root.mainloop()
