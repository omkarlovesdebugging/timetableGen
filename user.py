import subprocess
from tkinter import *
from tkinter import ttk
import sqlite3

# Create a root window
root = Tk()

# Set the title and icon of the window
root.title("Timetable")

# Set the size and position of the window
root.geometry("800x600+100+100")

# Connect to the database
conn = sqlite3.connect("timetable_generator.db")
cursor = conn.cursor()

# Create a left sidebar frame
sidebar = Frame(root, bg="#4a148c", width=200, height=600)
sidebar.pack(side=LEFT, fill=Y)

# Create a list of menu items for the sidebar
menu_items = [
    ("TIMETABLE", PhotoImage(file="Images/home_icon(1).png").subsample(2)),
    ("LECTURES", PhotoImage(file="Images/lecturer_icon(1).png").subsample(2)),
    ("TEACHERS", PhotoImage(file="Images/teacher_icon(1).png").subsample(2)),
    ("USER", PhotoImage(file="Images/user_icon.png").subsample(2)),
    ("LATEST ACTIVITY", PhotoImage(file="Images/activity_icon(1).png").subsample(2))
]

# Create a list of buttons for the sidebar
buttons = []

def timetable_page():
    print("Navigating to timetable page...") # Debug Message
    print("Timetable Page opened") # Debug Message
    root.destroy()
    subprocess.run(["python", "timetable_ADITYA.py"])

def teacher_section():
    print("Navigating to teacher_section page...") # Debug Message
    print("Teacher Section Page opened") # Debug Message
    root.destroy()
    subprocess.run(["python", "Teacher_section.py"])

def USER():
    print("Navigating to user page...") # Debug Message
    print("User Page opened") # Debug Message
    root.destroy()
    subprocess.run(["python", "user.py"])

def activity():
    print("Navigating to activity page...") # Debug Message
    print("Activity Page opened") # Debug Message
    root.destroy()
    subprocess.run(["python", "notifications.py"])

# Loop through the menu items and create buttons
for item in menu_items:
    if (item[0] == "USER"):
        button = Button(sidebar, text=item[0], image=item[1], compound=LEFT, fg="#4a148c", bg="white", bd=0, padx=20, pady=10, anchor="w", command=USER)
        button.pack(anchor="w") 
    elif (item[0] == "TIMETABLE"):
        button = Button(sidebar, text=item[0], image=item[1], compound=LEFT, fg="white", bg="#4a148c", bd=0, padx=20, pady=10, anchor="w", command=timetable_page)
        button.pack(anchor="w") 
    elif (item[0] == "LATEST ACTIVITY"):
        button = Button(sidebar, text=item[0], image=item[1], compound=LEFT, fg="white", bg="#4a148c", bd=0, padx=20, pady=10, anchor="w", command=activity)
        button.pack(anchor="w") 
    elif (item[0] == "TEACHERS"):
        button = Button(sidebar, text=item[0], image=item[1], compound=LEFT, fg="white", bg="#4a148c", bd=0, padx=20, pady=10, anchor="w", command=teacher_section)
        button.pack(anchor="w") 
    # Add the button to the list
    buttons.append(button)
    # Pack the button to the sidebar
    button.pack(fill=X)

# Create a top bar frame
Name_of_faculty = "Abhay Kshirsagar"

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
user_name = Label(topbar, text=Name_of_faculty, font=("Arial", 16), bg="#C1BBEB", fg="#4a148c")
user_name.pack(side=RIGHT, pady=10)

# Horizontal section: Faculty Information
faculty_info_frame = Frame(root, bg="#C1BBEB", width=600, height=100)
faculty_info_frame.pack(side=TOP, fill=X)

# Profile picture of faculty

faculty_profile_picture = PhotoImage(file="Images/Profile.png").subsample(5)
faculty_profile_pic = Label(faculty_info_frame, image=faculty_profile_picture, bg="#C1BBEB", padx=20)
faculty_profile_pic.grid(row=0, column=0, padx=10, pady=10)

cursor.execute("SELECT * FROM teacher WHERE first_name=? and last_name=? and Lec_Type=?", ("Abhay","Kshirsagar","lecture"))
lectures = cursor.fetchall()

print(lectures)
# Faculty name, phone number, and email
faculty_details=Frame( faculty_info_frame,bg="#C1BBEB")
faculty_details.grid(row=0,column=1,padx=10,pady=10)

faculty_name = Label(faculty_details, text="Abhay Kshirsagar", font=("Arial", 25, "bold"), bg="#C1BBEB")
faculty_name.grid(row=0, column=1, padx=10, pady=10, sticky=W)

faculty_phone = Label(faculty_details, text="Phone: 123-456-7890", font=("Arial", 10), bg="#C1BBEB")
faculty_phone.grid(row=1, column=1, padx=10, pady=2, sticky=W)

faculty_email = Label(faculty_details, text=f"Email: {lectures[0][4]}", font=("Arial", 10), bg="#C1BBEB")
faculty_email.grid(row=2, column=1, padx=10, pady=2, sticky=W)

# Vertical section 1: Classes Information
info_frame = Frame(root, bg="#A274FF")
info_frame.pack(side=LEFT, fill=BOTH, expand=True)
info_frame.grid_rowconfigure(0, weight=1)
info_frame.grid_columnconfigure(0, weight=1)
info_frame.grid_columnconfigure(1, weight=1)  # Set weight for the second column


classes_info_frame=Frame(info_frame, bg="#D1BAFF",height=1000,width=400 )
classes_info_frame.grid(row=0,column=0,padx=30,pady=30,sticky="nsew")




# Today's classes
today_classes_label = Label(classes_info_frame, text="Classes", font=("Arial", 25, "bold"), bg="#D1BAFF")
today_classes_label.pack(side=TOP, padx=10, pady=10)

# Function to fetch and display today's classes for the faculty
def fetch_and_display_classes():
    # global Name_of_faculty
    print(Name_of_faculty)
    # Fetch the faculty name
      # Update with the actual faculty name
    # Query to fetch today's classes for the faculty
    cursor.execute("SELECT * FROM timetable WHERE teacher_name=?", (Name_of_faculty,))
    lectures = cursor.fetchall()
    # Display the classes along with time slots
    for lecture in lectures:
        lecture_info = Label(classes_info_frame, text=f"{lecture[3]} - {lecture[2]} ({lecture[4]})", bg="#D1BAFF",font=("Arial", 13))
        lecture_info.pack(anchor=W, padx=20, pady=5)

# Fetch and display today's classes
fetch_and_display_classes()

# Vertical section 2: Notices Information

notices_info_frame = Frame(info_frame, bg="#D1BAFF",  height=1000,width=400,)
notices_info_frame.grid(row=0,column=1,padx=30,pady=30,sticky="nsew")
# Notices from Principal/HOD
notices_label = Label(notices_info_frame, text="Notices", font=("Arial", 25, "bold"), bg="#D1BAFF")
notices_label.pack(side=TOP, padx=10, pady=10)

# Function to fetch and display notifications
def fetch_and_display_notifications():
    cursor.execute("SELECT * FROM notifications")
    notifications = cursor.fetchall()
    print(notifications)
    for notification in notifications:
        notice = Label(notices_info_frame, text=f"-> {notification[3]}", bg="#D1BAFF",font=("Arial", 13))
        notice.pack(anchor=W, padx=20, pady=5)

# Fetch and display notifications
fetch_and_display_notifications()

root.mainloop()
