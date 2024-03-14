import subprocess
from tkinter import *
from tkinter import ttk
import sqlite3

def save_details():
    f = first_name_entry.get()
    l = last_name_entry.get()
    s = subject_entry.get()
    e = email_entry.get()

    cursor.execute("INSERT INTO teacher (first_name, last_name, subject_name, email) VALUES (?, ?, ?, ?)", (f, l, s, e))
    cursor.execute("SELECT * FROM teacher")
    print(cursor.fetchall())
    conn.commit()
    tree_insert_details()

def tree_insert_details():
    cursor.execute("SELECT * FROM teacher")
    rows = cursor.fetchall()
    for item in tree.get_children():
        tree.delete(item)
    for row in rows:
        tree.insert("", "end", values=(row[0], row[1] + ' ' + row[2], row[3], row[4]))

def lecture_page() :
    print("Navigating to lecture page...") #Debug Message
    print("Lecture Page opened")#Debug Message
    root.destroy()
    subprocess.run(["python","lecture.py"])

def timetable_page() :
    print("Navigating to timetable page...") #Debug Message
    print("Timetable Page opened")#Debug Message
    root.destroy()
    subprocess.run(["python","timetable.py"])

def teacher_section() :
    print("Navigating to teacher_section page...") #Debug Message
    print("Teacher Section Page opened")#Debug Message
    root.destroy()
    subprocess.run(["python","Teacher_section.py"])

def USER() :
    print("Navigating to lecture page...") #Debug Message
    print("Lecture Page opened")#Debug Message
    root.destroy()
    subprocess.run(["python","user.py"])

def activity() :
    print("Navigating to lecture page...") #Debug Message
    print("Lecture Page opened")#Debug Message
    root.destroy()
    subprocess.run(["python","notifications.py"])
global i 
i=0
root = Tk()
root.title("Timetable")
root.geometry("800x600+100+100")

sidebar = Frame(root, bg="#4a148c", width=200, height=600)
sidebar.pack(side=LEFT, fill=Y)

conn = sqlite3.connect("timetable_generator.db")
cursor = conn.cursor()
# cursor.execute("""
#   CREATE TABLE teacher (
#     teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     first_name VARCHAR(45) NOT NULL,
#     last_name VARCHAR(45) NOT NULL,
#     subject_name VARCHAR(45) NOT NULL,
#     email VARCHAR(45) NOT NULL);
#   """)

menu_items = [
    ("TIMETABLE", PhotoImage(file="Images/home_icon(1).png").subsample(2)),
    ("LECTURES", PhotoImage(file="Images/lecturer_icon(1).png").subsample(2)),
    ("TEACHERS", PhotoImage(file="Images/teacher_icon.png").subsample(2)),
    ("USER", PhotoImage(file="Images/user_icon(1).png").subsample(2)),
    ("LATEST ACTIVITY", PhotoImage(file="Images/activity_icon(1).png").subsample(2))
]

buttons = []

for item in menu_items:
    if (item[0] == "TEACHERS"):
        button = Button(sidebar, text=item[0], image=item[1], compound=LEFT, fg="#4a148c", bg="white", bd=0, padx=20, pady=10, anchor="w",command=teacher_section)
        button.pack(anchor="w") 
    elif (item[0]=="LECTURES"):
        button = Button(sidebar, text=item[0], image=item[1], compound=LEFT, fg="white", bg="#4a148c", bd=0, padx=20, pady=10, anchor="w",command=lecture_page)
        button.pack(anchor="w") 
    elif (item[0]=="TIMETABLE"):
        button = Button(sidebar, text=item[0], image=item[1], compound=LEFT, fg="white", bg="#4a148c", bd=0, padx=20, pady=10, anchor="w",command=timetable_page)
        button.pack(anchor="w") 
    elif (item[0]=="USER"):
        button = Button(sidebar, text=item[0], image=item[1], compound=LEFT, fg="white", bg="#4a148c", bd=0, padx=20, pady=10, anchor="w",command=USER)
        button.pack(anchor="w") 
    elif (item[0]=="LATEST ACTIVITY"):
        button = Button(sidebar, text=item[0], image=item[1], compound=LEFT, fg="white", bg="#4a148c", bd=0, padx=20, pady=10, anchor="w",command=activity)
        button.pack(anchor="w") 
    buttons.append(button)
    button.pack(fill=X)

topbar = Frame(root, bg="#C1BBEB", width=600, height=50)
topbar.pack(side=TOP, fill=X)

title = Label(topbar, text="TEACHERS", font=("Arial", 20, "bold"), bg="#C1BBEB", fg="#4a148c")
title.pack(side=LEFT, padx=20, pady=10)

user_icon_image = PhotoImage(file="Images/settings_icon.png").subsample(2)
user_icon = Label(topbar, image=user_icon_image, bg="#C1BBEB")
user_icon.pack(side=RIGHT, padx=10, pady=10)

user_name = Label(topbar, text="Vineeta M.", font=("Arial", 16), bg="#C1BBEB", fg="#4a148c")
user_name.pack(side=RIGHT, pady=10)

right_frame = Frame(root, bg="#C1BBEB", width=600, height=550)
right_frame.pack(side=TOP, fill=BOTH, expand=True)

add_section = LabelFrame(right_frame, text="Personal Details", font=("Arial", 14), fg="#ffffff", bg="#4a148c", width=705, height=790)
add_section.grid(row=0, column=0, padx=25, pady=25)

personal_section = LabelFrame(add_section, font=("Arial", 12), fg="#4a148c", bg="#ffffff", width=500, height=250)
personal_section.grid(row=0,column=0,padx=10, pady=10)

first_name_label = Label(personal_section, text="First Name*", font=("Arial", 10), fg="#4a148c", bg="#ffffff")
first_name_label.grid(row=0, column=0, padx=10, pady=10, sticky=  W)

first_name_entry = Entry(personal_section, font=("Arial", 16), fg="#4a148c", bg="#ffffff",width=35)
first_name_entry.grid(row=1, column=0, padx=10, pady=10)

last_name_label = Label(personal_section, text="Last Name*", font=("Arial", 10), fg="#4a148c", bg="#ffffff")
last_name_label.grid(row=2, column=0, padx=10, pady=10, sticky=  W)

last_name_entry = Entry(personal_section, font=("Arial", 16), fg="#4a148c", bg="#ffffff",width=35)
last_name_entry.grid(row=3, column=0, padx=10, pady=10)

subject_label = Label(personal_section, text="Subject*", font=("Arial", 10), fg="#4a148c", bg="#ffffff")
subject_label.grid(row=4, column=0, padx=10, pady=10, sticky=  W)

subject_entry = Entry(personal_section, font=("Arial", 16), fg="#4a148c", bg="#ffffff",width=35)
subject_entry.grid(row=5, column=0, padx=10, pady=10)

email_label = Label(personal_section, text="Email*", font=("Arial", 10), fg="#4a148c", bg="#ffffff")
email_label.grid(row=8, column=0, padx=10, pady=10, sticky=  W)

email_entry = Entry(personal_section, font=("Arial", 16), fg="#4a148c", bg="#ffffff",width=35)
email_entry.grid(row=9, column=0, padx=10, pady=10)

save_btn = Button(personal_section, text="Save", font=("Arial", 12), fg="#ffffff", bg="#4a148c", width=10, command=save_details)
save_btn.grid(row=12, column=1, padx=10, pady=10)

list_section = LabelFrame(right_frame, text="Teacher List", font=("Arial", 14), fg="#ffffff", bg="#4a148c", width=550, height=600)
list_section.grid(row=0, column=1, padx=10, pady=10)

tree = ttk.Treeview(list_section, columns=("S.NO", "NAME", "SUBJECT", "EMAIL"), show="headings", height=5)
tree.pack(padx=10, pady=10)

tree.column("S.NO", width=25, anchor=CENTER)
tree.column("NAME", width=100, anchor=CENTER)
tree.column("SUBJECT", width=100, anchor=CENTER)
tree.column("EMAIL", width=200, anchor=CENTER)

tree.heading("S.NO", text="S.NO")
tree.heading("NAME", text="NAME")
tree.heading("SUBJECT", text="SUBJECT")
tree.heading("EMAIL", text="EMAIL")

tree_insert_details()


root.mainloop()
