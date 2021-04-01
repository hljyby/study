import tkinter as tk


root = tk.Tk(className="测试")

root.geometry("500x500") # 长宽500x500
# root.resizable(0,0) # 长宽不可变

photo =  tk.PhotoImage(file="D:\图片\Saved Pictures\下雨.gif")
lable =  tk.Label(root,text="新蔡",fg="blue",bg="red",padx="20",image=photo,compound="center")
root.title("你猜") # 标题
scroll = tk.Scrollbar(root)
lable.grid(row=0,column=0)
scroll.grid()
root.mainloop()
