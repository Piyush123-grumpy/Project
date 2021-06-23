from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog
root=Tk()
root.title('New title')
def open():
    global my_image
    root.filename=filedialog.askopenfilename(initialdir="/Downloads",title="Select a file",filetypes=(("png files","*.png"),("all files","**")))
    my_image=ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label=Label(image=my_image).pack()
my_btn=Button(root,text="Open file",command=open).pack()
root.mainloop()