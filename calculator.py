from tkinter import *
def buttonclick(Number):
    global operator
    operator=operator+str(Number)
    text_within.set(operator)
def buttonclear():
    global operator
    operator=""
    text_within.set("")
def equals():
    try:
        global operator
        total = str(eval(operator))
        text_within.set(total)
        operator = total
    except ZeroDivisionError:
        text_within.set("Math error")
    except:
        operator = "-" + operator.replace("+-", "")
        total = str(eval(operator))
        text_within.set(total)
        operator = total

root=Tk()
root.title("DOPE CAULIFLOWER")
root.configure(bg="gray16")
root.resizable(0,0)
operator=""
text_within=StringVar()
e=Entry(root,width=8,text=text_within,borderwidth=4,font=("arial",40,))
e.grid(row=0,column=0,columnspan=4,ipadx=25)
button=Button(root,text="7",command=lambda :buttonclick(7),fg="white",bg="gray16",padx=25,pady=2)
button.grid(row=1,column=0,ipadx=5)
button=Button(root,text="8",command=lambda :buttonclick(8),fg="white",bg="gray16",padx=25,pady=2)
button.grid(row=1,column=1,ipadx=5)
button=Button(root,text="9",command=lambda :buttonclick(9),fg="white",bg="gray16",padx=26,pady=2)
button.grid(row=1,column=2,ipadx=5)
button=Button(root,text="4",command=lambda :buttonclick(4),fg="white",bg="gray16",padx=25,pady=2)
button.grid(row=2,column=0,ipadx=5)
button=Button(root,text="5",command=lambda :buttonclick(5),fg="white",bg="gray16",padx=25,pady=2)
button.grid(row=2,column=1,ipadx=5)
button=Button(root,text="6",command=lambda :buttonclick(6),fg="white",bg="gray16",padx=26,pady=2)
button.grid(row=2,column=2,ipadx=5)
button=Button(root,text="1",command=lambda :buttonclick(1),fg="white",bg="gray16",padx=25,pady=2)
button.grid(row=3,column=0,ipadx=5)
button=Button(root,text="2",command=lambda :buttonclick(2),fg="white",bg="gray16",padx=25,pady=2)
button.grid(row=3,column=1,ipadx=5)
button=Button(root,text="3",command=lambda :buttonclick(3),fg="white",bg="gray16",padx=26,pady=2)
button.grid(row=3,column=2,ipadx=5)
button=Button(root,text="0",command=lambda :buttonclick(0),fg="white",bg="gray16",padx=25,pady=2)
button.grid(row=4,column=0,ipadx=5)
button=Button(root,text="A/C",command= buttonclear,fg="white",bg="gray16")
button.grid(row=5,column=0,columnspan=3,ipadx=97.4,ipady=1)
button=Button(root,text="=",command= equals,fg="black",bg="goldenrod",padx=25,pady=2)
button.grid(row=5,column=3,ipadx=5)
button=Button(root,text="+",command=lambda :buttonclick("+"),fg="white",bg="gray20",padx=26,pady=2)
button.grid(row=4,column=3,ipadx=5)
button=Button(root,text="-",command=lambda :buttonclick("-"),fg="white",bg="gray20",padx=27,pady=2)
button.grid(row=3,column=3,ipadx=5)
button=Button(root,text="x",command=lambda :buttonclick("*"),fg="white",bg="gray20",padx=27,pady=2)
button.grid(row=2,column=3,ipadx=5)
button=Button(root,text="÷",command=lambda :buttonclick("//"),fg="white",bg="gray20",padx=25,pady=2)
button.grid(row=1,column=3,ipadx=5.5)
button=Button(root,text=".",command=lambda :buttonclick("."),fg="white",bg="gray16",padx=25.9,pady=2)
button.grid(row=4,column=1,ipadx=5.49)
button=Button(root,text="+-",command=lambda :buttonclick("+-"),fg="white",bg="gray16",padx=22.5,pady=2)
button.grid(row=4,column=2,ipadx=5)

root.mainloop()