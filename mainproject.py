from tkinter import *
import time
import tkinter.messagebox as tm
import os

#create new window
root=Tk()
root.geometry("800x600")
root.title("Library management system")

#adding background image
bckground_label = Label(height=600, width=800)
image1 = PhotoImage(file="bg.gif")
bckground_label.config(image=image1)
bckground_label.image = image1
bckground_label.place(x=0, y=0)

#login image
login_label = Label(height=256, width=256)
image2 = PhotoImage(file="1.gif")
login_label.config(image=image2)
login_label.image = image2
login_label.place(x=1, y=150)

#time
localtime=time.asctime(time.localtime(time.time()))

#to add labels on window
lblinfo = Label(root,font=('Times new roman' ,30, 'bold' ),text="Library Management System",fg="Red",bd=10,anchor='w')
lblinfo.place(x=150,y=10)
lblinfo = Label(font=('Arial' ,20, ),text=localtime,fg="steel blue",anchor=W)
lblinfo.place(x=220,y=70)

#labels
label_username = Label(text="Username",fg="red",font=("Arial", 20))
label_password = Label(text="Password",fg="red",font=("Arial", 20))
#textbox
entry_username = Entry(width=20,font=('Times',25))
entry_password = Entry(show="*",width=20,font=('Times',25))
#placing labels and textbox
label_username.place(x=300,y=200)
label_password.place(x=300,y=250)
entry_username.place(x=450,y=200)
entry_password.place(x=450,y=250)

#command for login button
def login_btn_clicked():
    username = entry_username.get()
    password = entry_password.get()

    if username == "admin" and password == "admin123":
        tm.showinfo("Login info", "Welcome to Library")
        root.destroy()
        os.system('python window_1.py')
    elif username != "admin":
        tm.showerror("Login error", "Incorrect username")
    else:
        tm.showerror("Login error", "Incorrect password")

#buttons
logbtn = Button(root,text="Login", fg="red", font=("Arial Bold", 20),command=login_btn_clicked)
logbtn.place(x=400,y=320)
closebtn = Button(root,text="Close", fg="red", font=("Arial Bold",20),command=root.quit)
closebtn.place(x=550,y=320)

root.mainloop()
