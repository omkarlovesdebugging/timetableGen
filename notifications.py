import tkinter as tk
import sqlite3
from tkinter import *
from datetime import datetime, timedelta
import subprocess

# Connect to the database
conn = sqlite3.connect("timetable_generator.db")
cursor = conn.cursor()

# cursor.execute("""
#   CREATE TABLE notifications (
#     srno INTEGER PRIMARY KEY AUTOINCREMENT,
#     time VARCHAR(45) NOT NULL,
#     day VARCHAR(45) NOT NULL,
#     message VARCHAR(45) NOT NULL
#     );""")

# Create the tkinter window
root = tk.Tk()
root.title("Timetable")

# Set the size and position of the window
root.geometry("1000x600+100+100")

# Create a left sidebar frame
sidebar = tk.Frame(root, bg="#4a148c", width=200, height=600)
sidebar.pack(side=tk.LEFT, fill=tk.Y)

# Create a list of menu items for the sidebar
menu_items = [
    ("TIMETABLE", PhotoImage(file="Images/home_icon(1).png").subsample(2)),
    ("LECTURES", PhotoImage(file="Images/lecturer_icon(1).png").subsample(2)),
    ("TEACHERS", PhotoImage(file="Images/teacher_icon(1).png").subsample(2)),
    ("USER", PhotoImage(file="Images/user_icon(1).png").subsample(2)),
    ("LATEST ACTIVITY", PhotoImage(file="Images/activity_icon.png").subsample(2))
]

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

# Function to handle button clicks
def handle_click(page):
    print(f"Navigating to {page} page...")  # Debug Message
    root.destroy()
    subprocess.run(["python", f"{page}.py"])

# Create a list of buttons for the sidebar
buttons = []

for item in menu_items:
    if (item[0] == "TEACHERS"):
        button = Button(sidebar, text=item[0], image=item[1], compound=LEFT, fg="white", bg="#4a148c", bd=0, padx=20, pady=10, anchor="w",command=teacher_section)
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
        button = Button(sidebar, text=item[0], image=item[1], compound=LEFT, fg="#4a148c", bg="white", bd=0, padx=20, pady=10, anchor="w",command=activity)
        button.pack(anchor="w") 
    buttons.append(button)
    button.pack(fill=X)


# Create a top bar frame
topbar = tk.Frame(root, bg="#C1BBEB", width=800, height=50)
topbar.pack(side=tk.TOP, fill=tk.X)

# Create a label for the title
title = tk.Label(topbar, text="Activity", font=("Arial", 20, "bold"), bg="#C1BBEB", fg="#4a148c")
title.pack(side=tk.LEFT, padx=20, pady=10)

# Create a label for the user icon
user_icon_image = tk.PhotoImage(file="Images/settings_icon.png").subsample(2)
user_icon = tk.Label(topbar, image=user_icon_image, bg="#C1BBEB")
user_icon.pack(side=tk.RIGHT, padx=10, pady=10)

# Create a label for the user name
user_name = tk.Label(topbar, text="Vineeta M.", font=("Arial", 16), bg="#C1BBEB", fg="#4a148c")
user_name.pack(side=tk.RIGHT, pady=10)

# Create a frame for the main section
main_section = tk.Frame(root, bg="#C1BBEB", width=800, height=500)
main_section.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Add labels for day, date, and time
current_time = datetime.now().strftime("%H:%M:%S")
current_date = datetime.now().strftime("%A, %B %d, %Y")

day_date_time_label = tk.Label(main_section, text=f"Day: {current_date} - Time: {current_time}", font=("Arial", 14), bg="#C1BBEB", fg="#4a148c")
day_date_time_label.pack(pady=(20, 10))

# Example Notifications
timeline_frame = tk.Frame(main_section, bg="#C1BBEB", width=150)
timeline_frame.pack(side=tk.LEFT, fill=tk.Y)

canvas = tk.Canvas(main_section, bg="#C1BBEB", width=600, height=500, highlightbackground="white", highlightthickness=2)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

#

# cursor.execute("DELETE FROM notifications")
# conn.commit()

def make_oval(notifications):

    y_offset = 30
    for count, notification in enumerate(notifications, start=1):
        

        y = count * 80
        canvas.create_oval(90, y - 5, 70, y + 15, outline="white", width=2)
        dayNdate=notification[2].split(', ')
        canvas.create_text(60, y - 20, text=f"{dayNdate[0]}\n{dayNdate[1]}\n{notification[1]}", font=("Arial", 8), anchor="e")
        canvas.create_text(100, y, text=notification[3], font=("Arial", 12), anchor="w")
        y_offset += 40

        # Draw vertical line for the day
        canvas.create_line(80, 0, 80, count*85, fill="white", width=2)

def fetch_data():
    cursor.execute("SELECT * FROM notifications")

    rows = cursor.fetchall()
    print(rows)

    
    # for row in rows:
    #     notifications.append({"faculty":"", "message":row[3], "deadline":True})


    
    make_oval(notifications=rows)

fetch_data()

# Right Section for adding latest notification
right_section = tk.Frame(main_section, bg="#C1BBEB", width=200, height=500)
right_section.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Function to handle sending notification
def send_notification():
    # Get current time and date
    current_time = datetime.now().strftime("%H:%M:%S")
    current_date = datetime.now().strftime("%A, %B %d, %Y")

    # Fetch data from message entry
    message_value = message_entry.get("1.0", tk.END)  # Get message from text widget

    # Insert data into database
    cursor.execute("INSERT INTO notifications (time, day, message) VALUES (?, ?, ?)", (current_time, current_date, message_value))
    conn.commit()

    fetch_data()
    

    
    print("Done!")  # Debug Message

# Label and text widget for message
tk.Label(right_section, text="*Message:", font=("Arial", 12), bg="#C1BBEB", fg="#4a148c").pack(pady=5)
message_entry = tk.Text(right_section, font=("Arial", 12), bg="#C1BBEB", height=5)
message_entry.pack(pady=5)

# Button to send notification
send_button = tk.Button(right_section, text="SEND", font=("Arial",10, "bold"), bg="#4a148c", fg="white", bd=0,width=6,height=1, command=send_notification)
send_button.pack(padx=10, pady=10)


root.mainloop()
