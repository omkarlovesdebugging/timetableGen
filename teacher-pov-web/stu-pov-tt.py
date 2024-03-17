# Import tkinter and ttk modules
import subprocess
from tkinter import *
from tkinter import ttk, messagebox
import random
import sqlite3

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
    ("USER", PhotoImage(file="Images/user_icon(1).png").subsample(2)),
    ("LATEST ACTIVITY", PhotoImage(file="Images/activity_icon(1).png").subsample(2))
]

# Create a list of buttons for the sidebar
buttons = []

# Database code
conn = sqlite3.connect("timetable_generator.db")
cursor = conn.cursor()

def timetable_page() :
    print("Navigating to timetable page...") #Debug Message
    print("Timetable Page opened")#Debug Message
    root.destroy()
    subprocess.run(["python","teacher-pov-web/stu-pov-tt.py"])
    
def USER() :
    print("Navigating to lecture page...") #Debug Message
    print("Lecture Page opened")#Debug Message
    root.destroy()
    subprocess.run(["python","teacher-pov-web/tea-profile.py"])

def activity() :
    print("Navigating to activity page...") #Debug Message
    print("activity Page opened")#Debug Message
    root.destroy()
    subprocess.run(["python","teacher-pov-web/tea-pov-notifications.py"])





def fill_timetable():
    
    cursor.execute("SELECT * FROM teacher")
    data = cursor.fetchall()

    formatted_data = []

    for i in data:
        teacher_fullname = i[1] + " " + i[2]
        subject_fullname = i[3]

        formatted_data.append((teacher_fullname, subject_fullname))
    
    print(formatted_data)

   


# Loop through the menu items and create buttons
for item in menu_items:

    if (item[0]=="TIMETABLE"):
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


# Start the main loop
root.mainloop()
