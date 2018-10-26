from tkinter import *
from tkinter import messagebox as tm
import datetime
import time
import os
import sqlite3
#connecting database
conn=sqlite3.connect("Library_System.db")
c=conn.cursor()

#creating new window
root=Tk()
root.geometry("800x800")
root.title("RETURN BOOKS")

#adding background image
log_label = Label(height=800, width=800)
image21 = PhotoImage(file="ret1.gif")
log_label.config(image=image21)
log_label.image = image21
log_label.place(x=0, y=0)

localtime=time.asctime(time.localtime(time.time()))
today=datetime.date.today()    #to get system's current date

lblinfo = Label(root,font=('Times new roman' ,30, 'bold' ),text="Library Management System",fg="Red",bg="cyan",bd=10,anchor='w')
lblinfo.place(x=150,y=10)
lblinfo = Label(font=('Arial' ,20),text=localtime,fg="steel blue",anchor=W,bg="cyan")
lblinfo.place(x=220,y=70)
lblinfo = Label(font=( 'Times new roman' ,20, 'bold','italic','underline' ),text="RETURN BOOKS",bg="cyan",fg="Red",bd=10,anchor='w')
lblinfo.place(x=250,y=120)

#labels
label_rollno = Label( text="Roll No",fg="red",font=("Arial ", 20))
select_dept=Label(text="Select Department",fg='red',font=("Arial",20))
label_bookid = Label( text="Book ID",fg="red",font=("Arial ", 20))
label_issuedate = Label( text="Issue Date",fg="red",font=("Arial ", 20))
label_returndate = Label( text="Return Date",fg="red",font=("Arial ", 20))

#textbox
entry_rollno = Entry(width=20,font=('Times',20))
entry_bookid = Entry(width=20,font=('Times',20))

label_rollno.place(x=120,y=200)
select_dept.place(x=120,y=250)
label_bookid.place(x=120,y=300)
label_issuedate.place(x=120,y=350)
label_returndate.place(x=120,y=400)

entry_rollno.place(x=370,y=200)
entry_bookid.place(x=370,y=300)

#to show department of student with entered roll no
def _view_():
    global bid1
    bid1 = []
    data = c.execute("SELECT Dept_Name FROM Student WHERE Roll_No=?",[entry_rollno.get()])
    for i in data:
        bid1.extend(i)
    global dep
    dep = Label(text=bid1[0],font=('Times', 20))
    dep.place(x=370, y=250)

def _view1_():
    #to check if book with entered book id is present
    bid = []
    data = c.execute("SELECT Book_ID FROM Books")
    for i in data:
        bid.extend(i)
    found = 0
    for i in bid:
        if entry_bookid.get() in bid:
            found=1
            global dates
            global dates1

            #to get issue date from books_issued table
            dates=[]
            q="SELECT Issue_Date From Books_Issued WHERE (Roll_No=? and Book_ID=?)"
            b=c.execute(q,[entry_rollno.get(),entry_bookid.get()])
            for i in b:
                dates.extend(i)

            #to get actual return date from books_issued table
            dates1=[]
            q1 = "SELECT Return_Date From Books_Issued WHERE (Roll_No=? and Book_ID=?)"
            b1 = c.execute(q1, [entry_rollno.get(), entry_bookid.get()])
            for i in b1:
                dates1.extend(i)

            #labels
            entry_issuedate = Label(text=dates[0], font=('Times', 20))
            entry_returndate = Label(text=dates1[0], font=('Times', 20))
            entry_issuedate.place(x=370, y=350)
            entry_returndate.place(x=370, y=400)

            #to find difference between actual return date from table and current date
            rd=datetime.datetime.strptime(dates1[0],"%Y-%m-%d")
            difference = today - rd.date()
            global fine_pay
            #if current date is greater or equal to return date from table
            if difference.days>=0:
                sel="SELECT Fine from Student WHERE Roll_No=?"
                s=c.execute(sel,[entry_rollno.get()])
                m=[]
                for i in s:
                    m.extend(i)
                fine_pay=(difference.days*5)+m[0]

            #if book returned before actual return date
            else:
                sel="SELECT Fine from Student WHERE Roll_No=?"
                s=c.execute(sel,[entry_rollno.get()])
                m=[]
                for i in s:
                    m.extend(i)
                fine_pay=m[0]

            #label to show balance fine
            entry_balfine=Label(text=fine_pay,font=('Times',20))
            entry_balfine.place(x=370,y=450)
            break
    if found != 1:
        tm.showerror(title="Error", message="Invalid Book ID")

view = Button( text="View", fg="red", font=("Arial Bold",10),command=_view_)
view.place(x=680,y=200)
view1 = Button( text="View", fg="red", font=("Arial Bold",10),command=_view1_)
view1.place(x=680,y=300)

label_balfine=Label(text="Bal. Fine",fg="red",font=("Arial ", 20))
label_balfine.place(x=120,y=450)
label_finepaid=Label(text="Fine Paid",fg="red",font=("Arial ", 20))
label_finepaid.place(x=120,y=500)
entry_finepaid=Entry(width=20,font=('Times',20))
entry_finepaid.place(x=370,y=500)

#function for submit button
def _submit_btn_clicked():
    if entry_rollno.get() == "" or entry_bookid.get() == "":
        tm.showerror("Error", "Field cannot be blank")
    else:
        #to update balance fine in students table
        fp=int(fine_pay)
        fip=entry_finepaid.get()
        bal=fp-int(fip)
        if bal<0:
            tm.showerror("Error", "Paid fine cannot be greter than balance")
        else:
            ab="UPDATE Student set Fine=? WHERE Roll_No=?"
            c.execute(ab,[bal,entry_rollno.get()])
            conn.commit()

            #to delete student record from book_issued table
            query = "DELETE from Books_Issued WHERE (Roll_No=? and Book_ID=?)"
            c.execute(query, [entry_rollno.get(), entry_bookid.get()])
            conn.commit()

            #to update no of copies of books available
            status = []
            q = "SELECT Available FROM Books WHERE Book_ID=?"
            a = c.execute(q, [entry_bookid.get()])
            for i in a:
                status.extend(i)
            available = status[0]
            available = available + 1
            q = "UPDATE Books SET Available=? WHERE Book_ID=?"
            c.execute(q, [available, entry_bookid.get()])
            tm.showinfo(title="Success", message="Done!")
            conn.commit()
            root.destroy()
            os.system('python window_1.py')

subbtn = Button(text="submit", fg="red", font=("Arial Bold", 20), command=_submit_btn_clicked)
subbtn.place(x=200, y=650)

def back():
    root.destroy()
    os.system('python window_1.py')

backbtn = Button( text="Back", fg="red", font=("Arial Bold",20),command =back)
backbtn.place(x=400,y=650)

root.mainloop()
