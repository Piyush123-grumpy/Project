from tkinter import *
from tkinter import messagebox
root=Tk()
root.title('Message Box')
def pop():
    response=messagebox.askyesno("Ths is my pop up","Hello world!")
    Label(root,text=response).pack()
    if response==1:
        Label(root,text="Clicked yes").pack()
    else:
        Label(root,text="Clicked No").pack()
Button(root,text="Popup",command=pop).pack()
root.mainloop()