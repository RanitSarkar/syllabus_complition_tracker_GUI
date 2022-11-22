from tkinter import *
import json

font_label=("Courier",25, "bold")
font_body=("Courier",18, "bold")
bgcol="dodger blue"

def save():
    session = session_name.get()

win=Tk()
win.config(bg=bgcol)
win.title("Gate 2023")

label1=Label(text="GATE 2023 SYLLABUS TRACKER",font=font_label,bg=bgcol,fg="white")
label1.grid(row=0,column=0,columnspan=4)

session = Label(text="enter session name",font=font_body,bg=bgcol,fg="white")
session.grid(row=1,column=0,pady=0,padx=0)

session_name=Entry(width=20,)
session_name.grid(row=1,column=1,pady=0,padx=0)

subjects = Label(text="enter topic name",font=font_body,bg=bgcol,fg="white")
subjects.grid(row=2,column=0,pady=0,padx=0)

subject_name=Entry(width=20,)
subject_name.grid(row=2,column=1,pady=0,padx=0)


win.mainloop()