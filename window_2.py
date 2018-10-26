from tkinter import *
from tkinter import messagebox as tm
import time
import sqlite3
import os

#connecting database
conn=sqlite3.connect("Library_System.db")
c=conn.cursor()

#creating new table
c.execute("CREATE TABLE IF NOT EXISTS Student(Roll_No TEXT NOT NULL PRIMARY KEY,Student_Name TEXT NOT NULL,Dept_Name TEXT NOT NULL ,Mobile_No INT NOT NULL,Fine INT DEFAULT 0)")

#creating new window
root=Tk()
root.geometry("800x600")
root.title("ADD NEW STUDENT")

#adding background image
log_label = Label(height=600, width=800)
image21 = PhotoImage(file="student.gif")
log_label.config(image=image21)
log_label.image = image21
log_label.place(x=0, y=0)

localtime=time.asctime(time.localtime(time.time()))

lblinfo = Label(root,font=('Times new roman' ,30, 'bold' ),text="Library Management System",fg="Red",bd=10,anchor='w',bg='cyan')
lblinfo.place(x=150,y=10)
lblinfo = Label(font=('Arial' ,20 ),text=localtime,fg="steel blue",anchor=W,bg='cyan')
lblinfo.place(x=220,y=70)
lblinfo = Label(font=( 'Times new roman' ,20, 'bold','italic','underline' ),text="ADD NEW STUDENT",fg="Red",bd=10,anchor='w',bg="cyan")
lblinfo.place(x=250,y=100)


label_rollno = Label( text="Roll No",fg="red",font=("Arial ", 20))
label_studentname = Label( text="Student Name",fg="red",font=("Arial ", 20))
label_mobile = Label( text="Mobile No",fg="red",font=("Arial ", 20))

entry_rollno = Entry(width=20,font=('Times',20))
entry_studentname= Entry(width=20,font=('Times',20))
entry_mobile= Entry(width=20,font=('Times',20))

label_rollno.place(x=100,y=150)
label_studentname.place(x=100,y=220)
label_mobile.place(x=100,y=360)

entry_rollno.place(x=350,y=150)
entry_studentname.place(x=350,y=220)
entry_mobile.place(x=350,y=360)

#to make dropdown list
depts=["COMPUTER","IT","ELECTRONICS","EXTC","INSTRUMENTATION"]
option1=StringVar(root)
option1.set("select department")
select_dept=Label(text="Select Department",fg='red',font=("Arial",20))
select_dept.place(x=100,y=290)
dep=OptionMenu(root,option1,*depts)
dep.config(font=('Times',20))
dep.place(x=350,y=290)

def _submit_btn_clicked():
    if len(entry_mobile.get())!=10:
        tm.showerror("Error","Invalid mobile No")
    else:
        query="INSERT INTO Student (Roll_No,Student_Name,Dept_Name,Mobile_No)VALUES(?,?,?,?)"
        c.execute(query,[entry_rollno.get(),entry_studentname.get(),option1.get(),entry_mobile.get()])
        conn.commit()
        tm.showinfo("Success","Student Registered")
        root.destroy()
        os.system('python window_1.py')

subbtn = Button( text="Submit", fg="red", font=("Arial Bold", 20),command=_submit_btn_clicked)
subbtn.place(x=250,y=450)

def back():
    root.destroy()
    os.system('python window_1.py')

backbtn = Button( text="Back", fg="red", font=("Arial Bold",20),command =back)
backbtn.place(x=400,y=450)

root.mainloop()
