import subprocess
from tkinter import *
from tkinter import ttk
from tkinter import font
import sqlite3


# Create a root window
root = Tk()

def loggingin():
    user=User_entry.get()
    key=Password_entry.get()

    cursor.execute("Select email,password from teacher")
    conn.commit()
    data=cursor.fetchall()

    for i in data:
        if i[0]==user and i[1]==key:
            print("Navigating to lecture page...") #Debug Message
            print("Lecture Page opened")#Debug Message
            root.destroy()
            subprocess.run(["python","user.py"])
            
def student_page():
    print("Navigating to lecture page...") #Debug Message
    print("Lecture Page opened")#Debug Message
    root.destroy()
    subprocess.run(["python","student-pov-web\stu-pov-tt.py"])

conn = sqlite3.connect("timetable_generator.db")
cursor = conn.cursor()

# Set the title and icon of the window
root.title("Timetable")

# Set the size and position of the window
root.geometry("1095x695+209+54")

root.resizable(False,False)
# Connect to the database

Brand_logo=PhotoImage(file="Images/Brand_Logo.png").subsample(4)

# Create a left sidebar frame
sidebar = Frame(root,bg="#190B3E", width=450, height=600)
sidebar.pack(side=LEFT, fill=Y)

Logo_label=Label(sidebar,image=Brand_logo,bg='#190B3E')
Logo_label.pack(side=TOP,fill=BOTH,expand=TRUE,padx=20  )


# Create a top bar frame
Name_of_faculty = "Abhay Kshirsagar"



# Vertical section 1: Classes Information
info_frame = Frame(root, bg="#D1BAFF",width=600,height=500)
info_frame.pack(side=RIGHT, fill=BOTH, expand=True)
info_frame.grid_rowconfigure(0, weight=1)
info_frame.grid_columnconfigure(0, weight=1)
info_frame.grid_columnconfigure(1, weight=1)
# info_frame.grid_columnconfigure(1, weight=1)
info_frame.grid_columnconfigure(2, weight=1)  # Set weight for the second column

Pad_frame=Frame(info_frame,bg="#D1BAFF",height=100,width=600)
Pad_frame.pack(side=TOP,fill=X)
Login_frame=Frame(info_frame,bg="#EEE6FF",height=530,width=600)
Login_frame.pack(side=BOTTOM,pady=50,padx=120)


Welcome=Label(Login_frame,text="Welcome To Planify",font=("Times",14),bg="#EEE6FF",width=390,anchor=W)
Welcome.pack(padx=50,pady=15,anchor=W)

W1=Label(Login_frame,text="Log Into your",font=("Times",27),bg="#EEE6FF")
W1.pack(padx=50,pady=0,anchor=W)

W2=Label(Login_frame,text="Account",font=("Times",27),bg="#EEE6FF")
W2.pack(padx=50,pady=5,anchor=W)

Username=Label(Login_frame,text="Username",font=("Times",14),bg="#EEE6FF")
Username.pack(padx=50,pady=10,anchor=W)

User_entry = Entry(Login_frame, font=("Arial", 17), fg="#868686", bg="#ffffff",width=330)
User_entry.pack( padx=50,pady=10,anchor=W)

Password=Label(Login_frame,text="Password",font=("Times",14),bg="#EEE6FF")
Password.pack(padx=50,pady=10,anchor=W)

Password_entry = Entry(Login_frame, font=("Arial", 17), fg="#868686", bg="#ffffff",width=330)
Password_entry.pack( padx=50, pady=10,anchor=W)

Log_in = Button(Login_frame, text="LOG IN", font=("Times", 16), fg="#ffffff", bg="#28A5FF",width=10,command=loggingin)
Log_in.pack( padx=50, pady=25,anchor=W)

student=Label(Login_frame,text = "Are you a student? then                   ",font=("Times",12),bg="#EEE6FF",fg="black")
student.pack(padx=50,pady=10,anchor=W)

button = Button(Login_frame, text="Click Here", relief=FLAT, borderwidth=0, bg="#EEE6FF",font=("Times",12),fg="#28A5FF",command=student_page)
button.place(in_=student,anchor=E,relx=1.0,rely=0.5)
# Function to fetch and display notifications



root.mainloop()
