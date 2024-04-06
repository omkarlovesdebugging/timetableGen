import subprocess
from tkinter import *
from tkinter import ttk


# Create a root window
root = Tk()

# Set the title and icon of the window
root.title("Timetable")

# Set the size and position of the window
root.geometry("1095x695+209+54")

root.resizable(False,False)
# Connect to the database

Brand_logo=PhotoImage(file="Images/Brand_Logo.png").subsample(4)

# Create a left sidebar frame
sidebar = Frame(root,bg="#190B3E", width=450, height=600)
sidebar.pack(side=LEFT, fill=Y)

Logo_label=Label(sidebar,image=Brand_logo,bg='#190B3E')
Logo_label.pack(side=TOP,fill=BOTH,expand=TRUE,padx=20  )

# # Create a list of menu items for the sidebar
# menu_items = [
#     ("TIMETABLE", PhotoImage(file="Images/home_icon(1).png").subsample(2)),
#     ("LECTURES", PhotoImage(file="Images/lecturer_icon(1).png").subsample(2)),
#     ("TEACHERS", PhotoImage(file="Images/teacher_icon(1).png").subsample(2)),
#     ("USER", PhotoImage(file="Images/user_icon.png").subsample(2)),
#     ("LATEST ACTIVITY", PhotoImage(file="Images/activity_icon(1).png").subsample(2))
# ]

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
# for item in menu_items:
#     if (item[0] == "USER"):
#         button = Button(sidebar, text=item[0], image=item[1], compound=LEFT, fg="#4a148c", bg="white", bd=0, padx=20, pady=10, anchor="w", command=USER)
#         button.pack(anchor="w") 
#     elif (item[0] == "TIMETABLE"):
#         button = Button(sidebar, text=item[0], image=item[1], compound=LEFT, fg="white", bg="#4a148c", bd=0, padx=20, pady=10, anchor="w", command=timetable_page)
#         button.pack(anchor="w") 
#     elif (item[0] == "LATEST ACTIVITY"):
#         button = Button(sidebar, text=item[0], image=item[1], compound=LEFT, fg="white", bg="#4a148c", bd=0, padx=20, pady=10, anchor="w", command=activity)
#         button.pack(anchor="w") 
#     elif (item[0] == "TEACHERS"):
#         button = Button(sidebar, text=item[0], image=item[1], compound=LEFT, fg="white", bg="#4a148c", bd=0, padx=20, pady=10, anchor="w", command=teacher_section)
#         button.pack(anchor="w") 
# #     # Add the button to the list
#     buttons.append(button)
#     # Pack the button to the sidebar
#     button.pack(fill=X)

# Create a top bar frame
Name_of_faculty = "Abhay Kshirsagar"



# Vertical section 1: Classes Information
info_frame = Frame(root, bg="#D1BAFF",width=600,height=500)
info_frame.pack(side=RIGHT, fill=BOTH, expand=True)
info_frame.grid_rowconfigure(0, weight=1)
info_frame.grid_columnconfigure(0, weight=1)
info_frame.grid_columnconfigure(1, weight=1)
# info_frame.grid_columnconfigure(1, weight=1)
info_frame.grid_columnconfigure(2, weight=1)  # Set weight for the second column

Pad_frame=Frame(info_frame,bg="#D1BAFF",height=100,width=600)
Pad_frame.pack(side=TOP,fill=X)
Login_frame=Frame(info_frame,bg="#EEE6FF",height=530,width=600)
Login_frame.pack(side=BOTTOM,pady=50,padx=120)
# Login_frame.grid_rowconfigure(0, weight=1)
# Login_frame.grid_columnconfigure(0, weight=1)

Welcome=Label(Login_frame,text="Welcome To Planify",font=("Times",14),bg="#EEE6FF",width=390,anchor=W)
Welcome.pack(padx=50,pady=15,anchor=W)

W1=Label(Login_frame,text="Log Into your",font=("Times",27),bg="#EEE6FF")
W1.pack(padx=50,pady=0,anchor=W)

W2=Label(Login_frame,text="Account",font=("Times",27),bg="#EEE6FF")
W2.pack(padx=50,pady=5,anchor=W)

Username=Label(Login_frame,text="Username",font=("Times",14),bg="#EEE6FF")
Username.pack(padx=50,pady=10,anchor=W)

User_entry = Entry(Login_frame, font=("Arial", 17), fg="#190B3E", bg="#ffffff",width=330)
User_entry.pack( padx=50,pady=10,anchor=W)

Password=Label(Login_frame,text="Password",font=("Times",14),bg="#EEE6FF")
Password.pack(padx=50,pady=10,anchor=W)

Password_entry = Entry(Login_frame, font=("Arial", 17), fg="#190B3E", bg="#ffffff",width=330)
Password_entry.pack( padx=50, pady=10,anchor=W)

Log_in = Button(Login_frame, text="LOG IN", font=("Times", 16), fg="#ffffff", bg="#28A5FF",width=10)
Log_in.pack( padx=50, pady=25,anchor=W)

student=Label(Login_frame,text = "Are you a student? then                   ",font=("Times",12),bg="#EEE6FF",fg="black")
student.pack(padx=50,pady=10,anchor=W)

button = Button(Login_frame, text="Click Here", relief=FLAT, borderwidth=0, bg="#EEE6FF",font=("Times",12),fg="#28A5FF")
button.place(in_=student,anchor=E,relx=1.0,rely=0.5)
# Function to fetch and display notifications



root.mainloop()
