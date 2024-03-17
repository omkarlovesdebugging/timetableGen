import subprocess
from tkinter import *
from tkinter import ttk
import time
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
    ("LATEST ACTIVITY", PhotoImage(file="Images/activity_icon.png").subsample(2))
]

conn = sqlite3.connect("timetable_generator.db")
cursor = conn.cursor()

def activity() :
    print("Navigating to lecture page...") #Debug Message
    print("Lecture Page opened")#Debug Message
    root.destroy()
    subprocess.run(["python","teacher-pov-web/tea-pov-notifications.py"])

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



# Create a list of buttons for the sidebar
buttons = []

# Loop through the menu items and create buttons
for item in menu_items:
    if (item[0] == "LATEST ACTIVITY"):
        button = Button(sidebar, text=item[0], image=item[1], compound=LEFT, fg="#4a148c", bg="white", bd=0, padx=20, pady=10, anchor="w",command=activity)
        button.pack(anchor="w") 
    # Create a button with text and icon
    elif (item[0]=="TIMETABLE"):
        button = Button(sidebar, text=item[0], image=item[1], compound=LEFT, fg="#4a148c", bg="white", bd=0, padx=20, pady=10, anchor="w",command=timetable_page)
        button.pack(anchor="w") 
    elif (item[0]=="USER"):
        button = Button(sidebar, text=item[0], image=item[1], compound=LEFT, fg="white", bg="#4a148c", bd=0, padx=20, pady=10, anchor="w",command=USER)
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

# Create a frame for the main section
main_section = Frame(root, bg="white", width=600, height=500)
main_section.pack(side=TOP, fill=BOTH, expand=True)



# Add labels for day, date, and time
current_time = time.strftime("%H:%M:%S")
current_date = time.strftime("%A, %B %d, %Y")
day_date_time_label = Label(main_section, text=f"Day: {current_date}", font=("Arial", 14), bg="white")
day_date_time_label.pack(pady=(20, 10))

# Example Notifications
timeline_frame = Frame(main_section, bg="#C1BBEB", width=0)
timeline_frame.pack(side=LEFT, fill=Y)

canvas = Canvas(main_section, bg="white", width=550, height=500)
canvas.pack(side=LEFT, fill=BOTH, expand=True)

# Draw vertical line for the day
canvas.create_line(80, 0, 80, 500, fill="#C1BBEB", width=2)

# Add circles and labels for notifications
notifications = [
    {"faculty": "Dr. Smith", "message": "Lecture on Math starts at 10:00 AM", "deadline": False},
    {"faculty": "Prof. Johnson", "message": "Meeting with Teachers at 2:00 PM", "deadline": False},
    {"faculty": "Dr. Parker", "message": "Deadline for assignment submission is tomorrow", "deadline": True}
]

y_offset = 30
for idx, notification in enumerate(notifications, start=1):
    y = idx * 80
    if notification["deadline"]:
        canvas.create_oval(90, y - 5, 70, y + 15, outline="red", width=2)
    else:
        canvas.create_oval(90, y - 5, 70, y + 15, outline="black", width=2)
    canvas.create_text(60, y - 20, text=f"{current_date.split(',')[0]}\n{current_date.split(',')[1]}", font=("Arial", 8), anchor="e")
    canvas.create_text(100, y, text=f"{notification['faculty']}:\n{notification['message']}", font=("Arial", 12), anchor="w")
    y_offset += 40

root.mainloop()


