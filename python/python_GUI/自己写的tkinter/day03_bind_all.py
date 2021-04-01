#不常用
import tkinter
 
root = tkinter.Tk()
root.title('bind_all')
root.minsize(300,300)
 
btn1 = tkinter.Button(root,text = '按钮1')
btn1.pack()
 
entry =tkinter.Entry(root)
entry.pack()
 
text = tkinter.Text(root,width=30,height=5)
text.pack()
 
def changebg(e):
    e.widget['bg']='red'
#虽然仅绑定了按钮，但单击任一控件，都会改变所单击控件的背景色，相当于所有的控件都绑定了changebg函数。
btn1.bind_all('<Button-1>',changebg)
 
root.mainloop()