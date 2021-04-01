import tkinter as tk
from tkinter import messagebox as msgbox

root = tk.Tk()

button = tk.Button(root)

button["text"] = "你好"

button.pack()

def sayHellow(e):
    msgbox.showinfo("sayhellow","hellow world")

button.bind("<Button-1>",sayHellow)

root.geometry("500x500")

root.mainloop()

if __name__ == "__main__":
    pass
