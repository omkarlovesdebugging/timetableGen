# Import tkinter and ttk modules
import subprocess
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

# Creating the sidebar icons
# path="Images/Timetable.jpg"
# img = Image  PhotoImage(Image.open(path))

# Create a list of menu items for the sidebar
menu_items = [
    ("TIMETABLE", PhotoImage(file="Images/home_icon(1).png").subsample(2)),
    ("LECTURES", PhotoImage(file="Images/lecturer_icon(1).png").subsample(2)),
    ("TEACHERS", PhotoImage(file="Images/teacher_icon.png").subsample(2)),
    ("USER", PhotoImage(file="Images/user_icon(1).png").subsample(2)),
    ("LATEST ACTIVITY", PhotoImage(file="Images/activity_icon(1).png").subsample(2))
]

# timetable_icon =   PhotoImage(file=r'C:\Users\ghola\OneDrive\Desktop\Mini project\timetableGen\Images\Timetable.png')
# instructions_icon =   PhotoImage(file="instructions.png")
# teachers_icon =   PhotoImage(file="teachers.png")
# activity_icon =   PhotoImage(file="activity.png")
# timetable_icon=timetable_icon.subsample(2,2)

# Creating the sidebar buttons
# timetable_btn =   Button(sidebar, image=timetable_icon, bg="#4a148c", bd=0)
# timetable_btn.place(x=50, y=50)
# 
# instructions_btn =   Button(sidebar, image=timetable_icon, bg="#4a148c", bd=0)
#instructions_btn.place(x=50, y=150)

# teachers_btn =   Button(sidebar, image=timetable_icon, bg="#4a148c", bd=0, relief=  SUNKEN)
# teachers_btn.place(x=50, y=250)

# activity_btn =   Button(sidebar, image=timetable_icon, bg="#4a148c", bd=0)
# activity_btn.place(x=50, y=350)
# Loop through the menu items and create buttons

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

buttons = []

for item in menu_items:
    if (item[0] == "TEACHERS"):
        button = Button(sidebar, text=item[0], image=item[1], compound=LEFT, fg="#4a148c", bg="white", bd=0, padx=20, pady=10, anchor="w")
        button.pack(anchor="w") 
    # Create a button with text and icon
    elif (item[0]=="LECTURES"):
        button = Button(sidebar, text=item[0], image=item[1], compound=LEFT, fg="white", bg="#4a148c", bd=0, padx=20, pady=10, anchor="w",command=lecture_page)
        button.pack(anchor="w") 
    elif (item[0]=="TIMETABLE"):
        button = Button(sidebar, text=item[0], image=item[1], compound=LEFT, fg="white", bg="#4a148c", bd=0, padx=20, pady=10, anchor="w",command=timetable_page)
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


# Creating the right frame
right_frame = Frame(root, bg="#C1BBEB", width=600, height=550)
right_frame.pack(side=TOP, fill=BOTH, expand=True)

# Creating the add new teacher or update details section
add_section =   LabelFrame(right_frame, text="Personal Details", font=("Arial", 14), fg="#ffffff", bg="#4a148c", width=705, height=790)
add_section.grid(row=0, column=0, padx=25, pady=25)

# Creating the personal details section
personal_section =   LabelFrame(add_section, font=("Arial", 12), fg="#4a148c", bg="#ffffff", width=500, height=250)
personal_section.grid(row=0,column=0,padx=10, pady=10)

# Creating the labels and entries for the personal details
first_name_label =   Label(personal_section, text="First Name*", font=("Arial", 10), fg="#4a148c", bg="#ffffff")
first_name_label.grid(row=0, column=0, padx=10, pady=10, sticky=  W)

first_name_entry =   Entry(personal_section, font=("Arial", 16), fg="#4a148c", bg="#ffffff",width=35)
first_name_entry.grid(row=1, column=0, padx=10, pady=10)

last_name_label =   Label(personal_section, text="Last Name*", font=("Arial", 10), fg="#4a148c", bg="#ffffff")
last_name_label.grid(row=2, column=0, padx=10, pady=10, sticky=  W)

last_name_entry =   Entry(personal_section, font=("Arial", 16), fg="#4a148c", bg="#ffffff",width=35)
last_name_entry.grid(row=3, column=0, padx=10, pady=10)

subject_label =   Label(personal_section, text="Subject*", font=("Arial", 10), fg="#4a148c", bg="#ffffff")
subject_label.grid(row=4, column=0, padx=10, pady=10, sticky=  W)

subject_entry =   Entry(personal_section, font=("Arial", 16), fg="#4a148c", bg="#ffffff",width=35)
subject_entry.grid(row=5, column=0, padx=10, pady=10)

subject_code_label =   Label(personal_section, text="Subject Code*", font=("Arial", 10), fg="#4a148c", bg="#ffffff")
subject_code_label.grid(row=6, column=0, padx=10, pady=10, sticky=  W)

subject_code_entry =   Entry(personal_section, font=("Arial", 16), fg="#4a148c", bg="#ffffff",width=35)
subject_code_entry.grid(row=7, column=0, padx=10, pady=10)

email_label =   Label(personal_section, text="Email*", font=("Arial", 10), fg="#4a148c", bg="#ffffff")
email_label.grid(row=8, column=0, padx=10, pady=10, sticky=  W)

email_entry =   Entry(personal_section, font=("Arial", 16), fg="#4a148c", bg="#ffffff",width=35)
email_entry.grid(row=9, column=0, padx=10, pady=10)

date_of_birth_label =   Label(personal_section, text="Date of Birth*", font=("Arial", 10), fg="#4a148c", bg="#ffffff")
date_of_birth_label.grid(row=10, column=0, padx=10, pady=10, sticky=  W)

date_of_birth_entry =   Entry(personal_section, font=("Arial", 16), fg="#4a148c", bg="#ffffff",width=35)
date_of_birth_entry.grid(row=11, column=0, padx=10, pady=10)

# Creating the save button
save_btn =   Button(personal_section, text="Save", font=("Arial", 12), fg="#ffffff", bg="#4a148c", width=10)
save_btn.grid(row=12, column=1, padx=10, pady=10)

# Creating the teacher list section
list_section =   LabelFrame(right_frame, text="Teacher List", font=("Arial", 14), fg="#ffffff", bg="#4a148c", width=550, height=600)
list_section.grid(row=0, column=1, padx=25, pady=25)

# Creating the treeview for the teacher list
tree = ttk.Treeview(list_section, columns=("S.NO", "NAME", "SUB CODE", "EMAIL"), show="headings", height=5)
tree.pack(padx=10, pady=10)

# Configuring the treeview columns
tree.column("S.NO", width=50, anchor=  CENTER)
tree.column("NAME", width=200, anchor=  CENTER)
tree.column("SUB CODE", width=100, anchor=  CENTER)
tree.column("EMAIL", width=200, anchor=  CENTER)

# Configuring the treeview headings
tree.heading("S.NO", text="S.NO")
tree.heading("NAME", text="NAME")
tree.heading("SUB CODE", text="SUB CODE")
tree.heading("EMAIL", text="EMAIL")

# Inserting some sample data into the treeview
tree.insert("", "end", values=("1", "Vineeth M.", "1117", "VineethM@vc.ac.in"))
tree.insert("", "end", values=("2", "Kung Fu Panda", "2341", "bigpanda@vc.ac.in"))
tree.insert("", "end", values=("3", "Superman", "2222", "kryptonite@vc.ac.in"))
tree.insert("", "end", values=("4", "Batman", "7856", "batmobile@gotham.vc.ac.in"))

# Creating the view more button
view_more_btn =   Button(list_section, text="View More", font=("Arial", 12), fg="#ffffff", bg="#4a148c", width=10)
view_more_btn.pack()




# Starting the main loop
root.mainloop()






#C:\Users\ghola\OneDrive\Desktop\Mini project\timetableGen\Images\activity_icon.png