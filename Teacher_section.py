# Importing modules
import tkinter as tk
from tkinter import ttk
# from PIL import ImageTk, Image

# Creating the main window
window = tk.Tk()
window.title("Timetable Management System")
window.geometry("1920x940")
window.configure(bg="#4a148c")

# Creating the left sidebar
sidebar = tk.Frame(window, width=300, height=600, bg="#4a148c")
sidebar.pack(side=tk.LEFT, fill=tk.Y)

# Creating the sidebar icons
# path="Images/Timetable.jpg"
# img = ImageTk.PhotoImage(Image.open(path))

timetable_icon = tk.PhotoImage(file=r'C:\Users\ghola\OneDrive\Desktop\Mini project\timetableGen\Images\Timetable.png')
# instructions_icon = tk.PhotoImage(file="instructions.png")
# teachers_icon = tk.PhotoImage(file="teachers.png")
# activity_icon = tk.PhotoImage(file="activity.png")
timetable_icon=timetable_icon.subsample(2,2)

# Creating the sidebar buttons
timetable_btn = tk.Button(sidebar, image=timetable_icon, bg="#4a148c", bd=0)
timetable_btn.place(x=50, y=50)

instructions_btn = tk.Button(sidebar, image=timetable_icon, bg="#4a148c", bd=0)
instructions_btn.place(x=50, y=150)

teachers_btn = tk.Button(sidebar, image=timetable_icon, bg="#4a148c", bd=0, relief=tk.SUNKEN)
teachers_btn.place(x=50, y=250)

activity_btn = tk.Button(sidebar, image=timetable_icon, bg="#4a148c", bd=0)
activity_btn.place(x=50, y=350)

# Creating the right frame
right_frame = tk.Frame(window, width=600, height=600, bg="#ffffff")
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Creating the add new teacher or update details section
add_section = tk.LabelFrame(right_frame, text="Personal Details", font=("Arial", 14), fg="#ffffff", bg="#4a148c", width=705, height=790)
add_section.grid(row=0, column=0, padx=25, pady=25)

# Creating the personal details section
personal_section = tk.LabelFrame(add_section, font=("Arial", 12), fg="#4a148c", bg="#ffffff", width=500, height=250)
personal_section.grid(row=0,column=0,padx=10, pady=10)

# Creating the labels and entries for the personal details
first_name_label = tk.Label(personal_section, text="First Name*", font=("Arial", 10), fg="#4a148c", bg="#ffffff")
first_name_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

first_name_entry = tk.Entry(personal_section, font=("Arial", 16), fg="#4a148c", bg="#ffffff",width=35)
first_name_entry.grid(row=1, column=0, padx=10, pady=10)

last_name_label = tk.Label(personal_section, text="Last Name*", font=("Arial", 10), fg="#4a148c", bg="#ffffff")
last_name_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

last_name_entry = tk.Entry(personal_section, font=("Arial", 16), fg="#4a148c", bg="#ffffff",width=35)
last_name_entry.grid(row=3, column=0, padx=10, pady=10)

subject_label = tk.Label(personal_section, text="Subject*", font=("Arial", 10), fg="#4a148c", bg="#ffffff")
subject_label.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)

subject_entry = tk.Entry(personal_section, font=("Arial", 16), fg="#4a148c", bg="#ffffff",width=35)
subject_entry.grid(row=5, column=0, padx=10, pady=10)

subject_code_label = tk.Label(personal_section, text="Subject Code*", font=("Arial", 10), fg="#4a148c", bg="#ffffff")
subject_code_label.grid(row=6, column=0, padx=10, pady=10, sticky=tk.W)

subject_code_entry = tk.Entry(personal_section, font=("Arial", 16), fg="#4a148c", bg="#ffffff",width=35)
subject_code_entry.grid(row=7, column=0, padx=10, pady=10)

email_label = tk.Label(personal_section, text="Email*", font=("Arial", 10), fg="#4a148c", bg="#ffffff")
email_label.grid(row=8, column=0, padx=10, pady=10, sticky=tk.W)

email_entry = tk.Entry(personal_section, font=("Arial", 16), fg="#4a148c", bg="#ffffff",width=35)
email_entry.grid(row=9, column=0, padx=10, pady=10)

date_of_birth_label = tk.Label(personal_section, text="Date of Birth*", font=("Arial", 10), fg="#4a148c", bg="#ffffff")
date_of_birth_label.grid(row=10, column=0, padx=10, pady=10, sticky=tk.W)

date_of_birth_entry = tk.Entry(personal_section, font=("Arial", 16), fg="#4a148c", bg="#ffffff",width=35)
date_of_birth_entry.grid(row=11, column=0, padx=10, pady=10)

# Creating the save button
save_btn = tk.Button(personal_section, text="Save", font=("Arial", 12), fg="#ffffff", bg="#4a148c", width=10)
save_btn.grid(row=12, column=1, padx=10, pady=10)

# Creating the teacher list section
list_section = tk.LabelFrame(right_frame, text="Teacher List", font=("Arial", 14), fg="#ffffff", bg="#4a148c", width=550, height=600)
list_section.grid(row=0, column=1, padx=25, pady=25)

# Creating the treeview for the teacher list
tree = ttk.Treeview(list_section, columns=("S.NO", "NAME", "SUB CODE", "EMAIL"), show="headings", height=5)
tree.pack(padx=10, pady=10)

# Configuring the treeview columns
tree.column("S.NO", width=50, anchor=tk.CENTER)
tree.column("NAME", width=200, anchor=tk.CENTER)
tree.column("SUB CODE", width=100, anchor=tk.CENTER)
tree.column("EMAIL", width=200, anchor=tk.CENTER)

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
view_more_btn = tk.Button(list_section, text="View More", font=("Arial", 12), fg="#ffffff", bg="#4a148c", width=10)
view_more_btn.pack()

# Starting the main loop
window.mainloop()






#C:\Users\ghola\OneDrive\Desktop\Mini project\timetableGen\Images\activity_icon.png