import tkinter as tk
from tkinter import ttk

# Creating the main window
window = tk.Tk()
window.title("Timetable Management System")
window.geometry("1920x940")
window.configure(bg="#4a148c")

# Creating the left sidebar
sidebar = tk.Frame(window, width=300, height=600, bg="#4a148c")
sidebar.pack(side=tk.LEFT, fill=tk.Y)

# Creating the sidebar icons
timetable_icon = tk.PhotoImage(file=r'C:\Users\ghola\OneDrive\Desktop\Mini project\timetableGen\Images\Timetable.png')
timetable_icon = timetable_icon.subsample(2, 2)

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
right_frame = tk.Frame(window, width=900, height=600, bg="#ffffff")
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Creating the add new teacher or update details section
add_section = tk.LabelFrame(right_frame, text="Lecture Details", font=("Arial", 14), fg="#ffffff", bg="#4a148c",
                             width=705, height=790)
add_section.grid(row=0, column=0, padx=25, pady=25)

# Creating the personal details section
personal_section = tk.LabelFrame(add_section, font=("Arial", 12), fg="#4a148c", bg="#ffffff", width=500,
                                 height=250)
personal_section.grid(row=0, column=0, padx=10, pady=10)

# Creating the labels and entries for the personal details
teacher_name_label = tk.Label(personal_section, text="Teacher Name*", font=("Arial", 10), fg="#4a148c",
                            bg="#ffffff")
teacher_name_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

teacher_name_entry = tk.Entry(personal_section, font=("Arial", 16), fg="#4a148c", bg="#ffffff", width=35)
teacher_name_entry.grid(row=1, column=0, padx=10, pady=10)



subject_label = tk.Label(personal_section, text="Subject*", font=("Arial", 10), fg="#4a148c",
                         bg="#ffffff")
subject_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

subject_entry = tk.Entry(personal_section, font=("Arial", 16), fg="#4a148c", bg="#ffffff", width=35)
subject_entry.grid(row=3, column=0, padx=10, pady=10)

subject_code_label = tk.Label(personal_section, text="Subject Code*", font=("Arial", 10), fg="#4a148c",
                              bg="#ffffff")
subject_code_label.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)

subject_code_entry = tk.Entry(personal_section, font=("Arial", 16), fg="#4a148c", bg="#ffffff", width=35)
subject_code_entry.grid(row=5, column=0, padx=10, pady=10)

email_label = tk.Label(personal_section, text="Email*", font=("Arial", 10), fg="#4a148c",
                       bg="#ffffff")
email_label.grid(row=6, column=0, padx=10, pady=10, sticky=tk.W)

email_entry = tk.Entry(personal_section, font=("Arial", 16), fg="#4a148c", bg="#ffffff", width=35)
email_entry.grid(row=7, column=0, padx=10, pady=10)


room_no_label = tk.Label(personal_section, text="Room No*", font=("Arial", 10), fg="#4a148c",
                         bg="#ffffff")
room_no_label.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

# Create a list of room numbers
room_numbers = ["Room 511", "Room 512", "Room 513", "Room 514"]

# Create a Combobox widget for room selection
combobox_room = ttk.Combobox(personal_section, values=room_numbers, font=("Arial", 16), width=33)
combobox_room.grid(row=1, column=1, padx=10, pady=10)

# Creating the save button
save_btn = tk.Button(personal_section, text="Save", font=("Arial", 12), fg="#ffffff", bg="#4a148c", width=10)
save_btn.grid(row=14, column=1, padx=10, pady=10)

# Starting the main loop
window.mainloop()
