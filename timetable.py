# Import tkinter and ttk modules
import subprocess
from tkinter import *
from tkinter import ttk
from assets import subjects
import random

# Create a root window
root = Tk()
    
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

def load_timetable(subjects):
        
    # Create a list of days for the calendar
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    
    # # Create a list of subjects for the calendar
    # subjects = []

    # Create a variable to keep track of the current subject index
    subject_index = 0

    # Loop through the days and create labels
    for day in days:
        # Create a label for the day
        day_label = Label(calendar, text=day, font=("Arial", 12, "bold"), bg="#C1BBEB", fg="#3a3a3a")
        # Grid the label to the calendar
        day_label.grid(row=0, column=days.index(day), padx=5, pady=5)

        # Create a frame for the time slots
        time_frame = Frame(calendar, bg="#C1BBEB")
        time_frame.grid(row=1, column=days.index(day), padx=5, pady=5)

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

                if subjects != []:
                    if ((subject_index >= len(subjects)) and subjects != []):
                        subject_index = random.randint(0, 7)
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

                    # Create a label for the room number
                    room_number = Label(subject_frame, text=subject[2], font=("Arial", 8), bg="#C1BBEB", fg="#4a148c")
                    room_number.pack(side=TOP, anchor=W, padx=0, pady=0)
        # subject_index = 0
        if ((subject_index >= len(subjects)) and subjects != []):
            subject_index = random.randint(0, 7)

def fill_timetable():
    load_timetable(subjects=subjects)

# Loop through the menu items and create buttons
for item in menu_items:
    if (item[0] == "TEACHERS"):
        button = Button(sidebar, text=item[0], image=item[1], compound=LEFT, fg="white", bg="#4a148c", bd=0, padx=20, pady=10, anchor="w")
        button.pack(anchor="w") 
    # Create a button with text and icon
    elif (item[0]=="LECTURES"):
        button = Button(sidebar, text=item[0], image=item[1], compound=LEFT, fg="white", bg="#4a148c", bd=0, padx=20, pady=10, anchor="w",command=lecture_page)
        button.pack(anchor="w") 
    elif (item[0]=="TIMETABLE"):
        button = Button(sidebar, text=item[0], image=item[1], compound=LEFT, fg="#4a148c", bg="white", bd=0, padx=20, pady=10, anchor="w",command=timetable_page)
        button.pack(anchor="w") 
    elif (item[0]=="USER"):
        button = Button(sidebar, text=item[0], image=item[1], compound=LEFT, fg="white", bg="#4a148c", bd=0, padx=20, pady=10, anchor="w")
        button.pack(anchor="w") 
    elif (item[0]=="LATEST ACTIVITY"):
        button = Button(sidebar, text=item[0], image=item[1], compound=LEFT, fg="white", bg="#4a148c", bd=0, padx=20, pady=10, anchor="w")
        button.pack(anchor="w") 
    # Add the button to the list
    buttons.append(button)
    # Pack the button to the sidebar
    button.pack(fill=X)

# Create a top bar frame
topbar = Frame(root, bg="#C1BBEB", width=600, height=50)
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

# Create a calendar frame
calendar = Frame(content, bg="#C1BBEB", width=550, height=500)
calendar.pack(side=LEFT, fill=BOTH, expand=True, padx=20, pady=20)

load_timetable([])

# Create a generate button
generate_button = Button(content, text="+", font=("Arial", 20, "bold"), bg="#4a148c", fg="white", bd=0, width=10, height=10, command=fill_timetable)
generate_button.pack(side=RIGHT, anchor=NE, padx=20, pady=20)

# Start the main loop
root.mainloop()
