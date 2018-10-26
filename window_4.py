from tkinter import *
from tkinter import messagebox as tm
import time
import os
import sqlite3
import datetime
#connecting databse
conn=sqlite3.connect("Library_System.db")
c=conn.cursor()
#creating new table
c.execute("CREATE TABLE IF NOT EXISTS Books_Issued(Roll_No TEXT NOT NULL,Dept_Name TEXT NOT NULL,Book_ID INT NOT NULL,Issue_Date DATE NOT NULL,Return_Date DATE NOT NULL,PRIMARY KEY (Roll_No,Book_ID))")

#creating new window
root=Tk()
root.geometry("800x600")
root.title("ISSUE BOOKS")

#adding background image
log_label = Label(height=600, width=800)
image21 = PhotoImage(file="student.gif")
log_label.config(image=image21)
log_label.image = image21
log_label.place(x=0, y=0)

localtime=time.asctime(time.localtime(time.time()))
today=datetime.date.today()    #to get system's current date
tdelta=datetime.timedelta(days=7)
returndate=today+tdelta        #to set return date 7 days after current date

lblinfo = Label(root,font=('Times new roman' ,30, 'bold' ),text="Library Management System",fg="Red",bg="cyan",bd=10,anchor='w')
lblinfo.place(x=150,y=10)
lblinfo = Label(font=('Arial' ,20),text=localtime,fg="steel blue",anchor=W,bg="cyan")
lblinfo.place(x=220,y=70)
lblinfo = Label(font=( 'Times new roman' ,20, 'bold','italic','underline' ),text="ISSUE BOOKS",bg="cyan",fg="Red",bd=10,anchor='w')
lblinfo.place(x=250,y=100)

#labels
label_rollno = Label( text="Roll No",fg="red",font=("Arial ", 20))
label_deptname = Label( text="Department Name",fg="red",font=("Arial ", 20))
label_bookid = Label( text="Book ID",fg="red",font=("Arial ", 20))
label_issuedate = Label( text="Issue Date",fg="red",font=("Arial ", 20))
label_returndate = Label( text="Return Date",fg="red",font=("Arial ", 20))
select_dept=Label(text="Select Department",fg='red',font=("Arial",20))

#textbox
entry_rollno = Entry(width=20,font=('Times',20))
entry_deptname = Entry(width=20,font=('Times',20))
entry_bookid = Entry(width=20,font=('Times',20))
entry_issuedate = Label(text=today,font=('Times',20))
entry_returndate = Label(text=returndate,font=('Times',20))

label_rollno.place(x=120,y=200)
label_bookid.place(x=120,y=300)
label_issuedate.place(x=120,y=350)
label_returndate.place(x=120,y=400)
select_dept.place(x=120,y=250)

entry_rollno.place(x=370,y=200)
entry_bookid.place(x=370,y=300)
entry_issuedate.place(x=370,y=350)
entry_returndate.place(x=370,y=400)

#to show department of student with entered roll no
def _view_():
    global bid1
    bid1 = []
    data = c.execute("SELECT Dept_Name FROM Student WHERE Roll_No=?",[entry_rollno.get()])
    for i in data:
        bid1.extend(i)
    global dep
    dep = Label(text=bid1[0])
    dep.config(font=('Times', 20))
    dep.place(x=370, y=250)

view = Button( text="View", fg="red", font=("Arial Bold",10),command=_view_)
view.place(x=680,y=200)

def _submit_btn_clicked():
    if entry_rollno.get() == "" or entry_bookid.get() == "":
        tm.showerror("Error", "Field cannot be blank")
    else:
        bid=[]
        data=c.execute("SELECT Book_ID FROM Books")
        for i in data:
            bid.extend(i)
        global found
        found=0
        #to check if book with entered book id is present in table
        for i in bid:
            if entry_bookid.get() in bid :
                status=[]
                q = "SELECT Available FROM Books WHERE Book_ID=?"
                a = c.execute(q, [entry_bookid.get()])
                for i in a:
                    status.extend(i)
                global available
                available = status[0]
                if available is 0:
                    tm.showinfo("Out of stock", "Cannot Issue")
                    found=1
                else:
                    query = "INSERT INTO Books_Issued (Roll_No,Dept_Name,Book_ID,Issue_Date,Return_Date) VALUES (?,?,?,?,?)"
                    c.execute(query, [entry_rollno.get(), bid1[0], entry_bookid.get(), today,returndate])
                    conn.commit()

                    found=1

                    available=available-1
                    q="UPDATE Books SET Available=? WHERE Book_ID=?"
                    c.execute(q,[available,entry_bookid.get()])
                    tm.showinfo(title="Success", message="Done!")
                    conn.commit()
            break
        if found!=1:
            tm.showerror(title="Error",message="Invalid Book ID")
    root.destroy()
    os.system('python window_1.py')

subbtn = Button( text="submit", fg="red", font=("Arial Bold", 20),command=_submit_btn_clicked)
subbtn.place(x=200,y=450)

def back():
    root.destroy()
    os.system('python window_1.py')

backbtn = Button( text="Back", fg="red", font=("Arial Bold",20),command =back)
backbtn.place(x=400,y=450)

root.mainloop()
