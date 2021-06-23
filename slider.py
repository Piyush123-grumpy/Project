from tkinter import *
root=Tk()
root.title('New title')
vertical=Scale(root,from_=0,to=450)
vertical.pack()
horizontal=Scale(root,from_=0,to=450,orient=HORIZONTAL)
horizontal.pack()
def slide():
    my_label=Label(root,text=horizontal.get()).pack()
    root.geometry(str(horizontal.get())+"x"+str(vertical.get()))
my_btn=Button(root,text="click Me",command=slide).pack()
root.mainloop()