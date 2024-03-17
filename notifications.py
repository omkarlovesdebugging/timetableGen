import tkinter as tk
from tkinter import ttk
import sqlite3
import time

# Connect to the database
conn = sqlite3.connect("timetable_generator.db")
cursor = conn.cursor()

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
    ("TIMETABLE", "Images/home_icon(1).png"),
    ("LECTURES", "Images/lecturer_icon(1).png"),
    ("TEACHERS", "Images/teacher_icon(1).png"),
    ("USER", "Images/user_icon(1).png"),
    ("LATEST ACTIVITY", "Images/activity_icon.png")
]

# Function to handle button clicks
def handle_click(page):
    print(f"Navigating to {page} page...")  # Debug Message
    root.destroy()
    subprocess.run(["python", f"{page}.py"])

# Create a list of buttons for the sidebar
buttons = []

for item in menu_items:
    button = tk.Button(sidebar, text=item[0], compound=tk.LEFT, fg="white", bg="#4a148c", bd=0, padx=20, pady=10, anchor="w",
                       command=lambda page=item[0]: handle_click(page))
    button.pack(anchor="w")
    buttons.append(button)

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
main_section = tk.Frame(root, bg="white", width=800, height=500)
main_section.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Add labels for day, date, and time
current_time = time.strftime("%H:%M:%S")
current_date = time.strftime("%A, %B %d, %Y")
day_date_time_label = tk.Label(main_section, text=f"Day: {current_date}", font=("Arial", 14), bg="white")
day_date_time_label.pack(pady=(20, 10))

# Example Notifications
timeline_frame = tk.Frame(main_section, bg="#C1BBEB", width=150)
timeline_frame.pack(side=tk.LEFT, fill=tk.Y)

canvas = tk.Canvas(main_section, bg="white", width=600, height=500)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

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

# Right Section for adding latest notification
right_section = tk.Frame(main_section, bg="white", width=200, height=500)
right_section.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Function to handle sending notification
def send_notification():
    # Fetch data from input fields
    time_value = time_entry.get()
    day_value = day_entry.get()
    date_value = date_entry.get()
    message_value = message_entry.get("1.0", tk.END)  # Get message from text widget

    # Insert data into database
    cursor.execute("INSERT INTO notifications (time, day, date, message) VALUES (?, ?, ?, ?)", (time_value, day_value, date_value, message_value))
    conn.commit()
    print("Notification sent successfully!")  # Debug Message

# Labels and entry widgets for time, day, date, and message
tk.Label(right_section, text="Time:", font=("Arial", 12), bg="white").pack(pady=(20, 5))
time_entry = tk.Entry(right_section, font=("Arial", 12), bg="white")
time_entry.pack(pady=5)

tk.Label(right_section, text="Day:", font=("Arial", 12), bg="white").pack(pady=5)
day_entry = tk.Entry(right_section, font=("Arial", 12), bg="white")
day_entry.pack(pady=5)

tk.Label(right_section, text="Date:", font=("Arial", 12), bg="white").pack(pady=5)
date_entry = tk.Entry(right_section, font=("Arial", 12), bg="white")
date_entry.pack(pady=5)

tk.Label(right_section, text="Message:", font=("Arial", 12), bg="white").pack(pady=5)
message_entry = tk.Text(right_section, font=("Arial", 12), bg="white", height=5)
message_entry.pack(pady=5)

# Button to send notification
send_button = tk.Button(right_section, text="Send", font=("Arial", 12), bg="#4a148c", fg="white", bd=0, command=send_notification)
send_button.pack(pady=20)

root.mainloop()
