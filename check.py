from tkinter import *
root=Tk()
root.title('New title')
def show():
    myLabel=Label(root,text=var.get()).pack()
var=StringVar()
checkButton=Checkbutton(root,text="Check this box!",variable=var,onvalue="On",offvalue="Off")
checkButton.deselect()
checkButton.pack()
mybutton=Button(root,text="Show Selection",command=show).pack()
root.mainloop()