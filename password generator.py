from tkinter import*
import random
import string
from tkinter import messagebox


def gen_pass():
    length =entry2.get()
    if len(length) <= 0:
        pvar.set("")
        messagebox.showwarning("Alert!","Please press a valid number")

    length = int(length)

    character = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(character) for _ in range(length))
    pvar.set(password)

def reset():
    pvar.set("")


root= Tk()
root.geometry("650x460")
root.title("Password generator")

label1=Label(root,text=" ",bg="green")
label1.place(x=0,y=0,height=420,width=620)

label2=Label(root,text="Password Generator",font=("calibre",15,"underline"),bg="blue")
label2.place(x=210,y=20)

label3=Label(root,text="Enter user name:",font=("calibre"),bg="white")
label3.place(x=50,y=110)

label4=Label(root,text="Enter the length:",font=("calibre"),bg="pink")
label4.place(x=50,y=160)

pvar = StringVar()

label5=Label(root,text="Generated Password:",font=("calibre"),bg="white")
label5.place(x=50,y=210)

#Generate Button
button1=Button(root,text="Generate Password",font=("calibre"),bg="green",command=gen_pass)
button1.place(x=220,y=260,width=200)
button2=Button(root,text="Reset",font=("calibre"),bg="sky blue",command=reset)
button2.place(x=240,y=310,width=150)

#creating entry boxes

entry1=Entry(root,font=('italic',10, 'bold'),relief=GROOVE,bg="white")
entry1.place(x=260,y=115,height=30,width=250)

entry2=Entry(root,font=('italic',10, 'bold'),relief=GROOVE,bg="white")
entry2.place(x=260,y=165,height=30,width=250)

entry3=Entry(root,font=('italic',10, 'bold'),relief=GROOVE,bg="white",textvariable=pvar)
entry3.place(x=260,y=215,height=30,width=250)



root.mainloop()