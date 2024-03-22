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

def timetable_frame(subjects):
    

    # Create a list of days for the calendar
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    
    # subjects = []

    # Create a variable to keep track of the current subject index
    subject_index = 0
    # subject_index = random.randint(0, len(subjects))

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

                
                data =[]  
                if subjects != []:
                    # if ((subject_index >= len(subjects)) and subjects != []):
                    #     subject_index = random.randint(0, len(subjects) - 1)
                    # # Get the current subject from the list
                    # subject = subjects[subject_index]
                    
                    # # Increment the subject index
                    # subject_index += 1

                    # Create a label for the subject name
                    subject_name = Label(subject_frame, text=subjects[subject_index][0], font=("Arial", 8, "bold"), bg="#C1BBEB", fg="#4a148c")
                    subject_name.pack(side=TOP, anchor=W, padx=0, pady=0)
                    


                    # Create a label for the teacher name
                    teacher_name = Label(subject_frame, text=subjects[subject_index][1], font=("Arial", 8), bg="#C1BBEB", fg="#4a148c")
                    teacher_name.pack(side=TOP, anchor=W, padx=0, pady=0)
                    

                    # Create a label for the room number
                    room_number = Label(subject_frame, text=subjects[subject_index][2], font=("Arial", 8), bg="#C1BBEB", fg="#4a148c")
                    room_number.pack(side=TOP, anchor=W, padx=0, pady=0)
                    
                    subject_index += 1
                    

                    

        # subject_index = 0
        # if ((subject_index >= len(subjects)) and subjects != []):
        #     subject_index = random.randint(0, len(subjects) - 1)    



def save_details():
    
    for i in range(0,len(save_data)):
        cursor.execute("INSERT INTO timetable (subject_name, teacher_name, room_number, day, time_slot) VALUES ( ?, ?, ?, ?, ?)", (save_data[i][0],save_data[i][1],save_data[i][2], save_data[i][3], save_data[i][4]))
        conn.commit()
    
    cursor.execute('select *  from timetable')
    print(cursor.fetchall())
    

def fill_timetable_A():

    cursor.execute("SELECT * FROM teacher")
    data = cursor.fetchall()

    formatted_data_A = []

    for i in data:
        teacher_fullname = i[1] + " " + i[2]
        subject_fullname = i[3]
        room="514"

        formatted_data_A.append((teacher_fullname, subject_fullname,room))
    
    # print(formatted_data_B)
    time_slots = ["8:30-9:30", "9:30-10:30", "10:30-11:30", "11:30-12:30", "BREAK", "1:30-3:30"]
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    for day in days:
        for slot in time_slots:
            if slot != "BREAK":
                random.shuffle(formatted_data_A)

                data=[formatted_data_A[0][0],formatted_data_A[0][1],formatted_data_A[0][2], day, slot]
                # save_data.clear()
                save_data.append(data)



    if (len(formatted_data_A) < 5 and len(formatted_data_A) > 0):
        msg = messagebox.showerror("ERROR","You must have atleast 5 teachers to generate a valid TT") 
        return ValueError

    print(save_data)

    # load_timetable(subjects=formatted_data_A)
    timetable_frame(subjects=save_data)


def fill_timetable_B():
    save_data.clear()

    cursor.execute("SELECT * FROM teacher")
    teachers_data = cursor.fetchall()

    cursor.execute('select *  from timetable')
    tt_of_A = cursor.fetchall()
    print(tt_of_A)

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    time_slots = ["8:30-9:30", "9:30-10:30", "10:30-11:30", "11:30-12:30", "BREAK", "1:30-3:30"]

    formatted_data_B = []

    for day in days:
        for slot in time_slots:
            if slot != "BREAK":

                random.shuffle(teachers_data)
                needed_data=()
                for j in tt_of_A:
                    if (j[3] == day and j[4] == slot):
                        needed_data = j 

                for i in teachers_data:
                    if ((i[1] + " " + i[2]) != needed_data[0] and i[3] != needed_data[1]):
                        teacher_fullname = i[1] + " " + i[2]
                        subject_fullname = i[3]
                        room="512"

                        formatted_data_B.append((teacher_fullname, subject_fullname, room))
    
                        data=[formatted_data_B[-1][0],formatted_data_B[-1][1],formatted_data_B[-1][2], day, slot]
                        save_data.append(data)
                        break
                
    
    # print(formatted_data_A)
    # print(formatted_data_B)

    if (len(formatted_data_B) < 5 and len(formatted_data_B) > 0):
        msg = messagebox.showerror("ERROR","You must have atleast 5 teachers to generate a valid TT") 
        return ValueError

    # load_timetable(subjects=formatted_data)
    for i in range(0, len(save_data)):
        cursor.execute("INSERT INTO timetable_B (subject_name, teacher_name, room_number, day, time_slot) VALUES ( ?, ?, ?, ?, ?)", (save_data[i][0],save_data[i][1],save_data[i][2], save_data[i][3], save_data[i][4]))
        conn.commit()

    timetable_frame(subjects=save_data)


def fill_timetable_C():
    save_data.clear()

    cursor.execute("SELECT * FROM teacher")
    teachers_data = cursor.fetchall()

    cursor.execute('select *  from timetable')
    tt_of_A = cursor.fetchall()

    cursor.execute('select *  from timetable_B')
    tt_of_B = cursor.fetchall()

    # print(tt_of_A)
    print(tt_of_B)

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    time_slots = ["8:30-9:30", "9:30-10:30", "10:30-11:30", "11:30-12:30", "BREAK", "1:30-3:30"]

    formatted_data_C = []

    for day in days:
        for slot in time_slots:
            if slot != "BREAK":

                random.shuffle(teachers_data)
                needed_data_A=()
                needed_data_B=()
                for j in tt_of_A:
                    if (j[3] == day and j[4] == slot):
                        needed_data_A = j 
                
                for k in tt_of_B:
                    if (k[3] == day and k[4] == slot):
                        needed_data_B = k 

                for i in teachers_data:
                    if ((i[1] + " " + i[2]) != needed_data_A[0] and (i[1] + " " + i[2]) != needed_data_B[0] and i[3] != needed_data_A[1] and i[3] != needed_data_B[1]):
                        teacher_fullname = i[1] + " " + i[2]
                        subject_fullname = i[3]
                        room="512"

                        formatted_data_C.append((teacher_fullname, subject_fullname, room))
    
                        data=[formatted_data_C[-1][0],formatted_data_C[-1][1],formatted_data_C[-1][2], day, slot]
                        save_data.append(data)
                        break
                
    
    # print(formatted_data_A)
    # print(formatted_data_B)

    if (len(formatted_data_C) < 5 and len(formatted_data_C) > 0):
        msg = messagebox.showerror("ERROR","You must have atleast 5 teachers to generate a valid TT") 
        return ValueError

        
    for i in range(0, len(save_data)):
        cursor.execute("INSERT INTO timetable_C (subject_name, teacher_name, room_number, day, time_slot) VALUES ( ?, ?, ?, ?, ?)", (save_data[i][0],save_data[i][1],save_data[i][2], save_data[i][3], save_data[i][4]))
        conn.commit()

    # load_timetable(subjects=formatted_data)
    timetable_frame(subjects=save_data)



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

class_2_button = Button(content, text="D10B", font=("Arial", 10), bg="#4a148c", fg="white", bd=0, padx=10, pady=5, command=fill_timetable_B)
class_2_button.place(x=class_1_button.winfo_x() + class_1_button.winfo_reqwidth() + 41, y=class_1_button.winfo_y()+10)

class_3_button = Button(content, text="D10C", font=("Arial", 10), bg="#4a148c", fg="white", bd=0, padx=10, pady=5, command=fill_timetable_C)
class_3_button.place(x=class_2_button.winfo_x() + class_2_button.winfo_reqwidth() + 115, y=class_2_button.winfo_y()+10)

# Create a calendar frame
calendar = Frame(content, bg="#C1BBEB", width=550, height=500)
calendar.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

# load_timetable([])
timetable_frame([])

# Create a generate button
generate_button = Button(content, text="+", font=("Arial", 20, "bold"), bg="#4a148c", fg="white", bd=0, width=10, height=10,command=fill_timetable_A)
generate_button.pack(side=RIGHT, anchor=NE, padx=20, pady=20)


save_button = Button(content, text="SAVE", font=("Arial", 10, "bold"), bg="#4a148c", fg="white", bd=0, width=10, height=2,command=save_details)
save_button.pack(side=BOTTOM, anchor=NE, padx=10, pady=10)


# Start the main loop
root.mainloop()
