from tkinter import *
import os
import time

#to create new window
root=Tk()
root.geometry("800x600")
localtime=time.asctime(time.localtime(time.time()))

#adding background image
background_label = Label(height=600, width=800)
img=PhotoImage(file="bga.gif")
background_label.config(image=img)
background_label.image = img
background_label.place(x=0, y=0)

#labels on window
lblinfo = Label(root,font=('Times new roman' ,30, 'bold' ),text="Library Management System",fg="Red",bg="cyan",bd=10,anchor='w')
lblinfo.place(x=150,y=10)
lblinfo = Label(font=('Arial' ,20, ),text=localtime,fg="steel blue",anchor=W,bg="cyan")
lblinfo.place(x=220,y=70)

#function for add new student button
def _add_btn_clicked():
    root.destroy()
    os.system('python window_2.py')
#function for add new book button
def _add1_btn_clicked():
    root.destroy()
    os.system('python window_3.py')
#function for issue button
def _issue_btn_clicked():
    root.destroy()
    os.system('python window_4.py')
#function for return book button
def _return_btn_clicked():
    root.destroy()
    os.system('python window_5.py')
#function for back button
def _back_btn_clicked():
    root.destroy()
    os.system('python mainproject.py')

addbtn = Button( text="Add New Student", fg="red", font=("Arial Bold", 20),command=_add_btn_clicked)
addbtn.place(x=200,y=150)

addbtn1 = Button( text="Add New book", fg="red", font=("Arial Bold", 20),command=_add1_btn_clicked)
addbtn1.place(x=200,y=230)

issuebtn = Button( text="Issue Books", fg="red", font=("Arial Bold", 20),command=_issue_btn_clicked)
issuebtn.place(x=200,y=310)

returnbtn = Button( text="Return Books", fg="red", font=("Arial Bold", 20),command=_return_btn_clicked)
returnbtn.place(x=200,y=390)

backbtn = Button( text="Back", fg="red", font=("Arial Bold",20),command =_back_btn_clicked)
backbtn.place(x=200,y=470)

root.mainloop()
