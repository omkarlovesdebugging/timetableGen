import subprocess
from tkinter import *
from tkinter import ttk
import time

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
    ("USER", PhotoImage(file="Images/user_icon.png").subsample(2)),
    ("LATEST ACTIVITY", PhotoImage(file="Images/activity_icon(1).png").subsample(2))
]

# Create a list of buttons for the sidebar
buttons = []

def USER() :
    print("Navigating to lecture page...") #Debug Message
    print("Lecture Page opened")#Debug Message
    root.destroy()
    subprocess.run(["python","teacher-pov-web/tea-profile.py"])

def activity() :
    print("Navigating to lecture page...") #Debug Message
    print("Lecture Page opened")#Debug Message
    root.destroy()
    subprocess.run(["python","teacher-pov-web/tea-pov-notifications.py"])

# Loop through the menu items and create buttons
for item in menu_items:
    if (item[0] == "USER"):
        button = Button(sidebar, text=item[0], image=item[1], compound=LEFT, fg="#4a148c", bg="white", bd=0, padx=20, pady=10, anchor="w",command=USER)
        button.pack(anchor="w") 
    # Create a button with text and icon
    
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
title = Label(topbar, text="Activity", font=("Arial", 20, "bold"), bg="#C1BBEB", fg="#4a148c")
title.pack(side=LEFT, padx=20, pady=10)

# Create a label for the user icon
user_icon_image = PhotoImage(file="Images/settings_icon.png").subsample(2)
user_icon = Label(topbar, image=user_icon_image, bg="#C1BBEB")
user_icon.pack(side=RIGHT, padx=10, pady=10)

# Create a label for the user name
user_name = Label(topbar, text="Vineeta M.", font=("Arial", 16), bg="#C1BBEB", fg="#4a148c")
user_name.pack(side=RIGHT, pady=10)

# Horizontal section: Faculty Information
faculty_info_frame = Frame(root, bg="white", width=600, height=100)
faculty_info_frame.pack(side=TOP, fill=X)

# Profile picture of faculty
faculty_profile_pic = Label(faculty_info_frame, text="Profile Pic", bg="white", padx=20)
faculty_profile_pic.grid(row=0, column=0, padx=10, pady=10)

# Faculty name, phone number, and email
faculty_name = Label(faculty_info_frame, text="Dr. John Doe", font=("Arial", 14, "bold"), bg="white")
faculty_name.grid(row=0, column=1, padx=10, pady=10, sticky=W)

faculty_phone = Label(faculty_info_frame, text="Phone: 123-456-7890", bg="white")
faculty_phone.grid(row=1, column=1, padx=10, pady=2, sticky=W)

faculty_email = Label(faculty_info_frame, text="Email: john.doe@example.com", bg="white")
faculty_email.grid(row=2, column=1, padx=10, pady=2, sticky=W)

# Vertical section 1: Classes Information
classes_info_frame = Frame(root, bg="white", width=300, height=250)
classes_info_frame.pack(side=LEFT, fill=BOTH, expand=True)

# Today's classes
today_classes_label = Label(classes_info_frame, text="Today's Classes", font=("Arial", 14, "bold"), bg="white")
today_classes_label.pack(side=TOP, padx=10, pady=10)

# Example classes information
class1_info = Label(classes_info_frame, text="Math - Room 101", bg="white")
class1_info.pack(anchor=W, padx=20, pady=5)

class2_info = Label(classes_info_frame, text="Physics - Room 102", bg="white")
class2_info.pack(anchor=W, padx=20, pady=5)

class3_info = Label(classes_info_frame, text="Chemistry - Room 103", bg="white")
class3_info.pack(anchor=W, padx=20, pady=5)

# Vertical section 2: Notices Information
notices_info_frame = Frame(root, bg="white", width=300, height=250)
notices_info_frame.pack(side=LEFT, fill=BOTH, expand=True)

# Notices from Principal/HOD
notices_label = Label(notices_info_frame, text="Notices", font=("Arial", 14, "bold"), bg="white")
notices_label.pack(side=TOP, padx=10, pady=10)

# Example notices
notice1 = Label(notices_info_frame, text="Important meeting tomorrow", bg="white")
notice1.pack(anchor=W, padx=20, pady=5)

notice2 = Label(notices_info_frame, text="Holiday on Friday", bg="white")
notice2.pack(anchor=W, padx=20, pady=5)

notice3 = Label(notices_info_frame, text="Submit progress report by Wednesday", bg="white")
notice3.pack(anchor=W, padx=20, pady=5)

root.mainloop()







