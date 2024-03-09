# Import tkinter and ttk modules
from tkinter import *
from tkinter import ttk

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

# Loop through the menu items and create buttons
for item in menu_items:
    if (item[0] == "TIMETABLE"):
        button = Button(sidebar, text=item[0], image=item[1], compound=LEFT, fg="#4a148c", bg="white", bd=0, padx=20, pady=10, anchor="w")
        button.pack(anchor="w") 
    # Create a button with text and icon
    else:
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

# Create a list of days for the calendar
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Create a list of subjects for the calendar
subjects = [
    ("DBMS", "Vijay Patel", "Room S-11"),
    ("CN Lab", "Lekh Raj", "Room S-12"),
    ("Engg. Mathematics", "Neetu Ji", "Room P-01"),
    ("Engg. Physics", "Rishaveer Ji", "Room G007"),
    ("Car Mechanics", "Vijay Ji", "Room X73"),
    ("Python Lab", "Credits :Palki", "Room X74"),
    ("COA Maths", "Kanan Sir", "Room F14"),
    ("COA Lab", "Kanan Sir/Shanker Sir", "Room F14/F16/F17")
]

# Create a variable to keep track of the current subject index
subject_index = 0

# Loop through the days and create labels
for day in days:
    # Create a label for the day
    day_label = Label(calendar, text=day, font=("Arial", 16, "bold"), bg="#C1BBEB", fg="#3a3a3a")
    # Grid the label to the calendar
    day_label.grid(row=0, column=days.index(day), padx=10, pady=10)

    # Create a frame for the time slots
    time_frame = Frame(calendar, bg="#C1BBEB")
    time_frame.grid(row=1, column=days.index(day), padx=10, pady=10)

    # Create a list of time slots for the day
    time_slots = ["8:30-9:30", "9:30-10:30", "10:30-11:30", "11:-12:-", "12:-1:-", "2:-3:-"]

    # Loop through the time slots and create labels
    for slot in time_slots:
        # Create a label for the time slot
        slot_label = Label(time_frame, text=slot, font=("Arial", 12), bg="#C1BBEB", fg="#3a3a3a")
        # Pack the label to the time frame
        slot_label.pack(side=TOP, anchor=W)

        # Check if the time slot is not a break
        if slot != "11:-12:-":
            # Get the current subject from the list
            subject = subjects[subject_index]
            # Increment the subject index
            subject_index += 1

            # Create a frame for the subject details
            subject_frame = Frame(time_frame, bg="#C1BBEB", width=100, height=50, highlightbackground="#A098AE", highlightthickness=2)
            subject_frame.pack_propagate(1)
            subject_frame.pack(side=TOP, fill=X, padx=10, pady=10)

            # Create a label for the subject name
            subject_name = Label(subject_frame, text=subject[0], font=("Arial", 12, "bold"), bg="#C1BBEB", fg="#4a148c")
            subject_name.pack(side=TOP, anchor=W, padx=10, pady=5)

            # Create a label for the teacher name
            teacher_name = Label(subject_frame, text=subject[1], font=("Arial", 12), bg="#C1BBEB", fg="#4a148c")
            teacher_name.pack(side=TOP, anchor=W, padx=10, pady=5)

            # Create a label for the room number
            room_number = Label(subject_frame, text=subject[2], font=("Arial", 12), bg="#C1BBEB", fg="#4a148c")
            room_number.pack(side=TOP, anchor=W, padx=10, pady=5)
    subject_index = 0

# Create a generate button
generate_button = Button(content, text="+", font=("Arial", 20, "bold"), bg="#4a148c", fg="white", bd=0, width=10, height=10)
generate_button.pack(side=RIGHT, anchor=NE, padx=20, pady=20)

# Start the main loop
root.mainloop()
