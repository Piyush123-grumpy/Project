from tkinter import *
root=Tk()
root.title('New title')
def show():
    myLabel=Label(root,text=clicked.get()).pack()
clicked=StringVar()
clicked.set("Monday")
drop=OptionMenu(root,clicked,"Monday","Tuesday","wednesday","Thursday","friday")
drop.pack()
myButton=Button(root,text="Show selection",command=show).pack()
root.mainloop()