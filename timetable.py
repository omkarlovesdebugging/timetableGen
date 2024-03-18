# Import tkinter and ttk modules
import subprocess
from tkinter import *
from tkinter import ttk, messagebox
from assets import subjects, rooms
import random
import sqlite3


# Create a root window
root = Tk()
 
save_data = []    
# Set the title and icon of the window
root.title("Timetable")

# Set the size and position of the window
root.geometry("800x600+100+100")

# Create a left sidebar frame
sidebar = Frame(root, bg="#4a148c", width=200, height=600)
sidebar.pack(side=LEFT, fill=Y)

# Create a list of menu items for the sidebar
menu_items = [
    ("TIMETABLE", PhotoImage(file="Images/home_icon.png").subsample(2)),
    ("LECTURES", PhotoImage(file="Images/lecturer_icon(1).png").subsample(2)),
    ("TEACHERS", PhotoImage(file="Images/teacher_icon(1).png").subsample(2)),
    ("USER", PhotoImage(file="Images/user_icon(1).png").subsample(2)),
    ("LATEST ACTIVITY", PhotoImage(file="Images/activity_icon(1).png").subsample(2))
]

# Create a list of buttons for the sidebar
buttons = []

# Database code
conn = sqlite3.connect("timetable_generator.db")
cursor = conn.cursor()

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

def load_timetable(subjects):
    
    if (len(subjects) < 5 and len(subjects) > 0):
        msg = messagebox.showerror("ERROR","You must have atleast 5 teachers to generate a valid TT") 
        return ValueError

    # Create a list of days for the calendar
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    
    # subjects = []

    # Create a variable to keep track of the current subject index
    # subject_index = 0
    subject_index = random.randint(0, len(subjects))

    # Loop through the days and create labels
    for day in days:
        # Create a label for the day
        day_label = Label(calendar, text=day, font=("Arial", 12, "bold"), bg="#C1BBEB", fg="#3a3a3a")
        day_label.grid(row=0, column=days.index(day), padx=20, pady=5)

        # Create a frame for the time slots
        time_frame = Frame(calendar, bg="#C1BBEB")
        time_frame.grid(row=1, column=days.index(day), padx=20, pady=5)

        # Create a list of time slots for the day
        time_slots = ["8:30-9:30", "9:30-10:30", "10:30-11:30", "11:30-12:30", "BREAK", "1:30-3:30"]
        
        # Loop through the time slots and create labels
        for slot in time_slots:
            # Create a label for the time slot
            slot_label = Label(time_frame, text=slot, font=("Arial", 8), bg="#C1BBEB", fg="#3a3a3a")
            
            # Pack the label to the time frame
            slot_label.pack(side=TOP, anchor=W)

            # Check if the time slot is not a break
            if slot != "BREAK":

                # Create a frame for the subject details
                subject_frame = Frame(time_frame, bg="#C1BBEB", width=80, height=10, highlightbackground="#A098AE", highlightthickness=2)
                subject_frame.pack_propagate(1)
                subject_frame.pack(side=TOP, fill=X, padx=10, pady=10)

                
                data = []  
                if subjects != []:
                    if ((subject_index >= len(subjects)) and subjects != []):
                        subject_index = random.randint(0, len(subjects) - 1)
                    # Get the current subject from the list
                    subject = subjects[subject_index]
                    
                    # Increment the subject index
                    subject_index += 1

                    # Create a label for the subject name
                    subject_name = Label(subject_frame, text=subject[0], font=("Arial", 8, "bold"), bg="#C1BBEB", fg="#4a148c")
                    subject_name.pack(side=TOP, anchor=W, padx=0, pady=0)
                    

                    # Create a label for the teacher name
                    teacher_name = Label(subject_frame, text=subject[1], font=("Arial", 8), bg="#C1BBEB", fg="#4a148c")
                    teacher_name.pack(side=TOP, anchor=W, padx=0, pady=0)
                    

                    room=rooms[random.randint(0, len(rooms) - 1)]
                    # Create a label for the room number
                    room_number = Label(subject_frame, text=room, font=("Arial", 8), bg="#C1BBEB", fg="#4a148c")
                    room_number.pack(side=TOP, anchor=W, padx=0, pady=0)
                    

                    data=[subject[0],subject[1],room]
                    
                    save_data.append(data)

                    

        # subject_index = 0
        if ((subject_index >= len(subjects)) and subjects != []):
            subject_index = random.randint(0, len(subjects) - 1)    


def save_details():
    
    for i in range(0,len(save_data)):
        cursor.execute("INSERT INTO timetable (subject_name, teacher_name, room_number) VALUES ( ?, ?, ?)", (save_data[i][0],save_data[i][1],save_data[i][2] ))
        conn.commit()
    
    cursor.execute('select *  from timetable')
    print(cursor.fetchall(),"fettching from db")
    

def fill_timetable():
    
    cursor.execute("SELECT * FROM teacher")
    data = cursor.fetchall()

    formatted_data = []

    for i in data:
        teacher_fullname = i[1] + " " + i[2]
        subject_fullname = i[3]

        formatted_data.append((teacher_fullname, subject_fullname))
    
    print(formatted_data)

    load_timetable(subjects=formatted_data)
    
    if (len(formatted_data) == 0):
        msg = messagebox.showerror("ERROR","You must have atleast 5 teachers to generate a valid TT") 
        return ValueError
    # load_timetable(subjects=subjects)

# Loop through the menu items and create buttons
for item in menu_items:
    if (item[0] == "TEACHERS"):
        button = Button(sidebar, text=item[0], image=item[1], compound=LEFT, fg="white", bg="#4a148c", bd=0, padx=20, pady=10, anchor="w",command=teacher_section)
        button.pack(anchor="w") 
    # Create a button with text and icon
    elif (item[0]=="LECTURES"):
        button = Button(sidebar, text=item[0], image=item[1], compound=LEFT, fg="white", bg="#4a148c", bd=0, padx=20, pady=10, anchor="w",command=lecture_page)
        button.pack(anchor="w") 
    elif (item[0]=="TIMETABLE"):
        button = Button(sidebar, text=item[0], image=item[1], compound=LEFT, fg="#4a148c", bg="white", bd=0, padx=20, pady=10, anchor="w",command=timetable_page)
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
topbar = Frame(root, bg="#C1BBEB", width=600, height=30)
topbar.pack(side=TOP, fill=X)

# Create a label for the title
title = Label(topbar, text="TIMETABLE", font=("Arial", 20, "bold"), bg="#C1BBEB", fg="#4a148c")
title.pack(side=LEFT, padx=20, pady=10)

# Create a label for the user icon
user_icon_image = PhotoImage(file="Images/settings_icon.png").subsample(2)
user_icon = Label(topbar, image=user_icon_image, bg="#C1BBEB")
user_icon.pack(side=RIGHT, padx=10, pady=10)

# Create a label for the user name
user_name = Label(topbar, text="Vineeta M.", font=("Arial", 16), bg="#C1BBEB", fg="#4a148c")
user_name.pack(side=RIGHT, pady=10)

# Create a main content frame
content = Frame(root, bg="#C1BBEB", width=600, height=550)
content.pack(side=TOP, fill=BOTH, expand=True)

class_1_button = Button(content, text="D10A", font=("Arial", 10), bg="#4a148c", fg="white", bd=0, padx=10, pady=5)
class_1_button.pack(side=TOP, padx=25, pady=10, anchor="w")

class_2_button = Button(content, text="D10B", font=("Arial", 10), bg="#4a148c", fg="white", bd=0, padx=10, pady=5)
class_2_button.place(x=class_1_button.winfo_x() + class_1_button.winfo_reqwidth() + 41, y=class_1_button.winfo_y()+10)

class_3_button = Button(content, text="D10C", font=("Arial", 10), bg="#4a148c", fg="white", bd=0, padx=10, pady=5)
class_3_button.place(x=class_2_button.winfo_x() + class_2_button.winfo_reqwidth() + 115, y=class_2_button.winfo_y()+10)

# Create a calendar frame
calendar = Frame(content, bg="#C1BBEB", width=550, height=500)
calendar.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

load_timetable([])

# Create a generate button
generate_button = Button(content, text="+", font=("Arial", 20, "bold"), bg="#4a148c", fg="white", bd=0, width=10, height=10, command=fill_timetable)
generate_button.pack(side=RIGHT, anchor=NE, padx=20, pady=20)


save_button = Button(content, text="SAVE", font=("Arial", 10, "bold"), bg="#4a148c", fg="white", bd=0, width=10, height=2,command=save_details)
save_button.pack(side=BOTTOM, anchor=NE, padx=10, pady=10)


# Start the main loop
root.mainloop()
