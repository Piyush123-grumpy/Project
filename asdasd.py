from tkinter import *
from tkinter import messagebox
root=Tk()
root.title('New title')
def open():
    top=Toplevel()
    top.title("Check new window")
    btn2=Button(top,text="Close window",command=top.destroy).pack()
btn=Button(root,text="opem",command=open()).pack()
root.mainloop()