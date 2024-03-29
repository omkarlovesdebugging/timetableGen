import subprocess
from tkinter import *
from tkinter import ttk
import assets
import sqlite3
import tkinter as tk
from tkinter import messagebox
# Creating the main window
root =  Tk()
root.title("Timetable")
root.geometry("800x600+100+100")

# Creating the left sidebar
sidebar =  Frame(root, width=200, height=600, bg="#4a148c")
sidebar.pack(side= LEFT, fill= Y)

# Create a list of menu items for the sidebar
menu_items = [
    ("TIMETABLE", PhotoImage(file="Images/home_icon(1).png").subsample(2)),
    ("LECTURES", PhotoImage(file="Images/lecture_icon.png").subsample(2)),
    ("TEACHERS", PhotoImage(file="Images/teacher_icon(1).png").subsample(2)),
    ("USER", PhotoImage(file="Images/user_icon(1).png").subsample(2)),
    ("LATEST ACTIVITY", PhotoImage(file="Images/activity_icon(1).png").subsample(2))
]

# Connect to SQLite database
conn = sqlite3.connect('lecture.db')
cursor = conn.cursor()

# Create a table named 'subjects' in the database
cursor.execute('''
    CREATE TABLE IF NOT EXISTS subjects(
        teacher_name TEXT,
        subject_name TEXT,
        room TEXT
    )
''')

def save_details():
    Teacher_Name=teacher_name_entry.get()
    Subject_Name=subject_entry.get()
    New = (Subject_Name,Teacher_Name)

    # check for empty fields
    if not (Teacher_Name.rstrip() and Subject_Name.rstrip()):
        return messagebox.showerror("error","Completion of all fields is mandatory.")

    cursor.execute("select * from subjects")
    rows = cursor.fetchall()

    # check for repetition 
    for row in rows :
        if (row[1] == Teacher_Name) and (row[2] == Subject_Name):
            msg = messagebox.showerror("error","Entry already exists") 
            if msg :
                teacher_name_entry.delete(0,tk.END)
                subject_entry.delete(0,tk.END)

                return ValueError

    assets.subjects.append(New)
    print(assets.subjects)

    
    

    # cursor.executemany("INSERT INTO subjects(subject_name, teacher_name, room) VALUES(?,?,?)", assets.subjects)

    cursor.execute("INSERT INTO subjects (teacher_name, subject_name, room) VALUES (?, ?, ?)", (Teacher_Name, Subject_Name, "None"))
    cursor.execute("SELECT * FROM subjects")
    print(cursor.fetchall())
    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    print("Data Saved")
    

def lecture_page() :
    print("Navigating to lecture page...") #Debug Message
    print("Lecture Page opened")#Debug Message
    root.destroy()
    subprocess.run(["python","lecture.py"])


def timetable_page() :
    print("Navigating to timetable page...") #Debug Message
    print("Timetable Page opened")#Debug Message
    root.destroy()
    subprocess.run(["python","timetable_ADITYA.py"])

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

buttons=[]

for item in menu_items:
    if (item[0] == "LECTURES"):
        button = Button(sidebar, text=item[0], image=item[1], compound=LEFT, fg="#4a148c", bg="white", bd=0, padx=20, pady=10, anchor="w",command=lecture_page)
        button.pack(anchor="w") 
    # Create a button with text and icon
    elif (item[0]=="TEACHERS"):
        button = Button(sidebar, text=item[0], image=item[1], compound=LEFT, fg="white", bg="#4a148c", bd=0, padx=20, pady=10, anchor="w",command=teacher_section)
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
    # Add the button to the list
    buttons.append(button)
    # Pack the button to the sidebar
    button.pack(fill=X)


    # Create a top bar frame
topbar = Frame(root, bg="#C1BBEB", width=600, height=50)
topbar.pack(side=TOP, fill=X)

# Create a label for the title
title = Label(topbar, text="LECTURES", font=("Arial", 20, "bold"), bg="#C1BBEB", fg="#4a148c")
title.pack(side=LEFT, padx=20, pady=10)

# Create a label for the user icon
user_icon_image = PhotoImage(file="Images/settings_icon.png").subsample(2)
user_icon = Label(topbar, image=user_icon_image, bg="#C1BBEB")
user_icon.pack(side=RIGHT, padx=10, pady=10)

# Create a label for the user name
user_name = Label(topbar, text="Vineeta M.", font=("Arial", 16), bg="#C1BBEB", fg="#4a148c")
user_name.pack(side=RIGHT, pady=10)

# Creating the sidebar icons
# timetable_icon =  PhotoImage(file='Images/Timetable.png')
# timetable_icon = timetable_icon.subsample(2, 2)

# Creating the sidebar buttons
# timetable_btn =  Button(sidebar, image=timetable_icon, bg="#4a148c", bd=0)
# timetable_btn.place(x=50, y=50)

# instructions_btn =  Button(sidebar, image=timetable_icon, bg="#4a148c", bd=0)
# instructions_btn.place(x=50, y=150)

# teachers_btn =  Button(sidebar, image=timetable_icon, bg="#4a148c", bd=0, relief= SUNKEN)
# teachers_btn.place(x=50, y=250)

# activity_btn =  Button(sidebar, image=timetable_icon, bg="#4a148c", bd=0)
# activity_btn.place(x=50, y=350)

# Creating the right frame
right_frame =  Frame(root, width=600, height=550, bg="#C1BBEB")
right_frame.pack(side= RIGHT, fill= BOTH, expand=True)

# Creating the add new teacher or update details section
add_section =  LabelFrame(right_frame, text="Lecture Details", font=("Arial", 14), fg="#ffffff", bg="#4a148c",
                             width=705, height=790)
add_section.grid(row=0, column=0, padx=25, pady=25)

# Creating the personal details section
personal_section =  LabelFrame(add_section, font=("Arial", 12), fg="#4a148c", bg="#ffffff", width=500,
                                 height=250)
personal_section.grid(row=0, column=0, padx=10, pady=10)

# Creating the labels and entries for the personal details
teacher_name_label =  Label(personal_section, text="Teacher Name*", font=("Arial", 10), fg="#4a148c",
                            bg="#ffffff")
teacher_name_label.grid(row=0, column=0, padx=10, pady=10, sticky= W)

teacher_name_entry =  Entry(personal_section, font=("Arial", 16), fg="#4a148c", bg="#ffffff", width=35)
teacher_name_entry.grid(row=1, column=0, padx=10, pady=10)



subject_label =  Label(personal_section, text="Subject*", font=("Arial", 10), fg="#4a148c",
                         bg="#ffffff")
subject_label.grid(row=2, column=0, padx=10, pady=10, sticky= W)

subject_entry =  Entry(personal_section, font=("Arial", 16), fg="#4a148c", bg="#ffffff", width=35)
subject_entry.grid(row=3, column=0, padx=10, pady=10)

# subject_code_label =  Label(personal_section, text="Subject Code*", font=("Arial", 10), fg="#4a148c",
#                               bg="#ffffff")
# subject_code_label.grid(row=4, column=0, padx=10, pady=10, sticky= W)

# subject_code_entry =  Entry(personal_section, font=("Arial", 16), fg="#4a148c", bg="#ffffff", width=35)
# subject_code_entry.grid(row=5, column=0, padx=10, pady=10)

# email_label =  Label(personal_section, text="Email*", font=("Arial", 10), fg="#4a148c",
#                        bg="#ffffff")
# email_label.grid(row=6, column=0, padx=10, pady=10, sticky= W)

# email_entry =  Entry(personal_section, font=("Arial", 16), fg="#4a148c", bg="#ffffff", width=35)
# email_entry.grid(row=7, column=0, padx=10, pady=10)


# room_no_label =  Label(personal_section, text="Room No*", font=("Arial", 10), fg="#4a148c",
#                          bg="#ffffff")
# room_no_label.grid(row=0, column=1, padx=10, pady=10, sticky= W)

# # Create a list of room numbers
# room_numbers = ["Room 511", "Room 512", "Room 513", "Room 514"]

# # Create a Combobox widget for room selection
# combobox_room = ttk.Combobox(personal_section, values=room_numbers, font=("Arial", 16), width=33)
# combobox_room.grid(row=1, column=1, padx=10, pady=10)

# Creating the save button
save_btn =  Button(personal_section, text="Save", font=("Arial", 12), fg="#ffffff", bg="#4a148c", width=10,command= save_details)
save_btn.grid(row=14, column=1, padx=10, pady=10)

# Starting the main loop
root.mainloop()
