from tkinter import *
from tkinter import messagebox
import webbrowser

class Application(Frame):
    def __init__(self, master=None):

        super().__init__(master)
        self.pack()
        self.createWidget()

    def createWidget(self):
        # 创建组件
        self.text01 = Text(self, width=40,height=12,bg="gray")
        self.text01.pack()

        self.text01.insert(1.0,"0123456789\nabcdefg")
        self.text01.insert(2.3,"锄禾日当午，汗滴禾下土。谁知盘中餐，粒粒皆辛苦。\n")

        Button(self,text="重复插入文本",command=self.insertText).pack(side="left")
        Button(self,text="返回文本",command=self.returnText).pack(side="left")
        Button(self,text="添加图片",command=self.addImage).pack(side="left")
        Button(self,text="添加组件",command=self.addWidget).pack(side="left")
        Button(self,text="通过tag精确控制文本",command=self.testTag).pack(side="left")

    def insertText(self):
        self.text01.insert("insert",' Gaoqi ')
        # insert 代表在光标处插入
        self.text01.insert("end",'[sxt]')
        # end 代表在结尾处插入
        self.text01.insert(1.8,"gaoqi")
        # 在一行9列处插入gaoqi

    def returnText(self):
        self.text01.get(1.2,1.6)
        # 获取从1.2~1.6的数据
        print(self.text01.get(1.0,"end"))
        # 返回所有数据

    def addImage(self):
        self.photo = PhotoImage(file=r"D:\\图片\Saved Pictures\\下雨.gif")
        self.text01.image_create("end",image=self.photo)

    def addWidget(self):
        b1 = Button(self.text01,text="你猜")
        self.text01.window_create(INSERT,window=b1)

    def testTag(self):
        self.text01.delete(1.0,"end")
        self.text01.insert(INSERT,"haohaoxuexi\ntiantinaxiangshang \n杨博宇是好人百度一下\n 你就知道")
        self.text01.tag_add("goods",1.0,1.9)
        self.text01.tag_config("goods",background="yellow",foreground="red")

        self.text01.tag_add("baidu",4.0,4.2)
        self.text01.tag_config("baidu",underline=True)
        self.text01.tag_bind("baidu","<Button-1>",self.webshow)

    def webshow(self,event):
        webbrowser.open("http://www.baidu.com")

root = Tk()
root.geometry("500x500+300+300")

root.title("Text 组件的测试")

app = Application(master=root)

root.mainloop()
