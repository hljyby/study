from tkinter import *

class Application(Frame):

    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.place(x=10,y=10)
        self.createwidget()

    def createwidget(self):
        # global c1clear
        self.btn01 = Button(self,text="haaaaaaahaha",bg="red")
        self.btn01.pack()
        self.c1 = Canvas(self, width=200, height=200, bg="green") #创建画布
        self.c1.pack()
        self.c1.bind("<Button-1>", self.mouseTest)   # 当鼠标左键点击时，触发事件
        self.c1.bind("<B1-Motion>", self.testDrag)   # 当按住鼠标左键并拖动时， 触发事件
        self.master.bind("<KeyPress>", self.keyboardTest)   # 当按下键盘时就触发
        self.master.bind("<KeyPress-a>", self.press_a_test)  # 按下a键时，触发事件
        self.master.bind("<KeyRelease-a>", self.release_a_test)  # 释放a键时，触发事件
        self.btn01.bind("<Button-1>", lambda event:self.release_z_test(event,1,2))  # 释放a键时，触发事件

    def mouseTest(self, event):
   		 # 显示鼠标点击点相对于c1的位置
        print("鼠标左键单击位置(相对于父容器)为:{}{}".format(event.x, event.y))  
        # 显示鼠标点击点相对于屏幕的位置
        print("鼠标左键单击位置(相对于屏幕)为:{}{}".format(event.x_root, event.y_root)) 
        # 显示事件触发的控件
        print("事件绑定的组件:{}".format(event.widget))  

    def testDrag(self, event):
        # 在鼠标当前位置与当前位置+2的位置创建一个椭圆，拖动较慢时实现的是画图功能
        self.c1.create_oval(event.x, event.y, event.x+2, event.y+2,fill="black")

    def keyboardTest(self, event):
        print("键的keycode:{}，键的char:{}，键的keysym：{}"
              .format(event.keycode, event.char, event.keysym))

    def press_a_test(self, event):
        print("press a")

    def release_a_test(self, event):
        print("release a")
    
    def release_z_test(self, event,a,b):
        print(a,b)
        print(event.__dict__)
        print(event.widget.winfo_geometry())
        print(event.widget.winfo_height())
        print(event.widget.winfo_y())
        print(event.widget.winfo_x())
        print(event.widget.winfo_rootx())
        print(event.widget.winfo_rooty())
        print(event.widget.winfo_parent())


if __name__ == '__main__':

    root = Tk()
    root.title("event测试")
    root.geometry("300x300")
    app = Application(root)
    root.mainloop()