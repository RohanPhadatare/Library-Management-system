from tkinter import *
from tkinter import messagebox as tm
import time
import sqlite3
import os
#connecting database
conn=sqlite3.connect("Library_System.db")
c=conn.cursor()
#creating new table
c.execute("CREATE TABLE IF NOT EXISTS Books(Book_ID TEXT NOT NULL PRIMARY KEY,Book_Name TEXT NOT NULL,Book_Author TEXT NOT NULL ,Book_Copies INT NOT NULL,Available INT NOT NULL )")
#creating new window
root=Tk()
root.geometry("800x600")
root.title("ADD A BOOK")
localtime=time.asctime(time.localtime(time.time()))

#adding background image
log_label = Label(height=600, width=800)
image21 = PhotoImage(file="student.gif")
log_label.config(image=image21)
log_label.image = image21
log_label.place(x=0, y=0)

lblinfo = Label(root,font=('Times new roman' ,30, 'bold' ),text="Library Management System",fg="Red",bg="cyan",bd=10,anchor='w')
lblinfo.place(x=150,y=10)
lblinfo = Label(font=('Arial' ,20, ),text=localtime,fg="steel blue",anchor=W,bg="cyan")
lblinfo.place(x=220,y=60)
lblinfo = Label(font=( 'Times new roman' ,20, 'bold','italic','underline' ),text="ADD A BOOK",fg="Red",bg="cyan",bd=10,anchor='w')
lblinfo.place(x=250,y=120)

#labels
label_bookname = Label( text="Book Name",fg="red",font=("Arial ", 20))
label_bookid = Label( text="Book ID",fg="red",font=("Arial ", 20))
label_author = Label( text="Author Name",fg="red",font=("Arial ", 20))
label_copies = Label( text="No of copies",fg="red",font=("Arial ", 20))
#textbox
entry_bookname = Entry(width=20,font=('Times',20))
entry_bookid = Entry(width=20,font=('Times',20))
entry_author = Entry(width=20,font=('Times',20))
entry_copies = Entry(width=20,font=('Times',20))

label_bookname.place(x=150,y=200)
label_bookid.place(x=150,y=250)
label_author.place(x=150,y=300)
label_copies.place(x=150,y=350)

entry_bookname.place(x=350,y=200)
entry_bookid.place(x=350,y=250)
entry_author.place(x=350,y=300)
entry_copies.place(x=350,y=350)

def _submit_btn_clicked():
    query = "INSERT INTO Books (Book_ID,Book_Name,Book_Author,Book_Copies,Available) VALUES (?,?,?,?,?)"
    c.execute(query, [entry_bookid.get(), entry_bookname.get(), entry_author.get(), entry_copies.get(),entry_copies.get()])
    conn.commit()
    tm.showinfo("form info", "Added new book successfully!")
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
