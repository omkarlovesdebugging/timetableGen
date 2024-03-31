# Import tkinter and ttk modules
import subprocess
from tkinter import *
from tkinter import ttk, messagebox
from assets import subjects, rooms
import random
import sqlite3
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph

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
    root.destroy()
    subprocess.run(["python","lecture.py"])


def timetable_page() :
    root.destroy()
    subprocess.run(["python","timetable_ADITYA.py"])

def teacher_section() :
    root.destroy()
    subprocess.run(["python","Teacher_section.py"])

def USER() :
    root.destroy()
    subprocess.run(["python","user.py"])

def activity() :
    root.destroy()
    subprocess.run(["python","notifications.py"])

def timetable_frame(subjects):
    # global calendar
    # if (calendar):
    #     calendar.destroy() 
        
    # calendar = Frame(content, bg="#C1BBEB", width=1000, height=500)
    # calendar.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

    # Create a list of days for the calendar
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    
    # subjects = []

    # Create a variable to keep track of the current subject index
    subject_index = 0
    # subject_index = random.randint(0, len(subjects))

    # Loop through the days and create labels
    for day in days:
        # Create a label for the day
        day_label = Label(calendar, text=day, font=("Arial", 8, "bold"), bg="#C1BBEB", fg="#3a3a3a")
        day_label.grid(row=0, column=days.index(day), padx=50, pady=0)

        # Create a frame for the time slots
        time_frame = Frame(calendar, bg="#C1BBEB")
        time_frame.grid(row=1, column=days.index(day), padx=10, pady=5)

        # Create a list of time slots for the day
        time_slots = ["8:30-9:30", "9:30-10:30", "10:30-11:30", "11:30-12:30", "BREAK", "1:30-2:30", "2:30-3:30"]
        

        # Loop through the time slots and create labels
        for slot in time_slots:

            # Create a label for the time slot
            slot_label = Label(time_frame, text=slot, font=("Arial", 6), bg="#C1BBEB", fg="#3a3a3a")
            
            # Pack the label to the time frame
            slot_label.pack(side=TOP, anchor=W)

            # Check if the time slot is not a break
            if slot != "BREAK":

                # Create a frame for the subject details
                subject_frame = Frame(time_frame, bg="#C1BBEB", width=80, height=6, highlightbackground="#A098AE", highlightthickness=2)
                subject_frame.pack_propagate(1)
                subject_frame.pack(side=TOP, fill=X, padx=6, pady=6)

                data =[]  
                if subjects != []:
                    # if ((subject_index >= len(subjects)) and subjects != []):
                    #     subject_index = random.randint(0, len(subjects) - 1)
                    # Get the current subject from the list
                    # subject = subjects[subject_index]
                    
                    # # Increment the subject index
                    # subject_index += 1

                    # Create a label for the subject name
                    subject_name = Label(subject_frame, text=subjects[subject_index][0], font=("Arial", 8, "bold"), bg="#C1BBEB", fg="#4a148c")
                    subject_name.pack(side=TOP, anchor=W, padx=0, pady=0)
                    


                    # Create a label for the teacher name
                    teacher_name = Label(subject_frame, text=subjects[subject_index][1], font=("Arial", 8, "bold"), bg="#C1BBEB", fg="#4a148c")
                    teacher_name.pack(side=TOP, anchor=W, padx=0, pady=0)
                    

                    # Create a label for the room number
                    room_number = Label(subject_frame, text=subjects[subject_index][2], font=("Arial", 8, "bold"), bg="#C1BBEB", fg="#4a148c")
                    room_number.pack(side=TOP, anchor=W, padx=0, pady=0)
                    
                    subject_index += 1
                    

                    

        # subject_index = 0
        # if ((subject_index >= len(subjects)) and subjects != []):
        #     subject_index = random.randint(0, len(subjects) - 1)    



def generate_pdf_from_database(data_a,data_b,data_c):
    pdf_filename = "TIMETABLEGEN_OUTPUT.pdf"
    
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
    elements = []
    i=0
    # Add data to the PDF
    table_data_a = []
    table_data_a.append(["DAY","TIME-SLOT","TEACHER","SUBJECT","ROOM"])
    var = 1
    for row in data_a:
        if var % 6 == 1:
            table_data_a.append(row)
        else:
            new_row = row.copy()
            new_row[0] = ""
            table_data_a.append(new_row)
        var+=1

    # Create table
    table_a = Table(table_data_a)

    # Add style to the table
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Courier-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])
    table_a.setStyle(style)

    styles = getSampleStyleSheet()
    style_heading = styles['Heading1']
    elements.append(Paragraph("D10A", style_heading))
    
    
    # Add table to elements
    elements.append(table_a)
    elements.append(PageBreak())
    
    # Add data to the PDF
    table_data_b = []
    table_data_b.append(["DAY","TIME-SLOT","TEACHER","SUBJECT","ROOM"])
    var = 1
    for row in data_b:    
        if var % 6 == 1:
            table_data_b.append(row)
        else:
            new_row = row.copy()
            new_row[0] = ""
            table_data_b.append(new_row)
        var+=1

    table_b = Table(table_data_b)
    table_b.setStyle(style)

    elements.append(Paragraph("D10B", style_heading))
    elements.append(table_b)   

    elements.append(PageBreak())

    table_data_c = []
    table_data_c.append(["DAY","TIME-SLOT","TEACHER","SUBJECT","ROOM"])
    var = 1
    for row in data_c:    
        if var % 6 == 1:
            table_data_c.append(row)
        else:
            new_row = row.copy()
            new_row[0] = ""
            table_data_c.append(new_row)
        var+=1

    table_c = Table(table_data_c)
    table_c.setStyle(style)

    elements.append(Paragraph("D10C", style_heading))
    elements.append(table_c)   
    elements.append(PageBreak()) 
    # Build PDF
    doc.build(elements)

def save_details():
    cursor.execute("SELECT * FROM timetable")
    data_a=cursor.fetchall()
    new_data_A = []
    for i in data_a:
        new_data_A.append([i[3], i[4], i[1], i[0], i[2]])

    cursor.execute("SELECT * FROM timetable_B")
    data_b=cursor.fetchall()
    new_data_B = []
    for j in data_b:
        new_data_B.append([j[3], j[4], j[1], j[0], j[2]])

    cursor.execute("SELECT * FROM timetable_C")
    data_c=cursor.fetchall()
    new_data_C = []
    for k in data_c:
        new_data_C.append([k[3], k[4], k[1], k[0], k[2]])

    # Create a PDF document
    generate_pdf_from_database(new_data_A,new_data_B,new_data_C)


    if (data_a == [] or data_b == [] or data_c == []):
        msg = messagebox.showerror("ERROR","Please generate a TT for all the classes first") 
        return ValueError

    # with open("TIMETABLE_GEN.txt", "w") as file:
    #     file.write("TIMETABLE GENERATOR\n")
    #     file.write("\nD10A:\n")
    #     for i in data_a:
    #         file.write(f"{i}\n")
    #     file.write("\nD10B:\n")
    #     for j in data_b:
    #         file.write(f"{j}\n")
    #     file.write("\nD10C:\n")
    #     for k in data_c:
    #         file.write(f"{k}\n")

def fill_random_tt():
    save_data.clear()
    show_focusA(event=None)

    cursor.execute("SELECT * FROM teacher")
    teachers_data = cursor.fetchall()

    formatted_data_A = []

    for i in teachers_data:
        teacher_fullname = i[1] + " " + i[2]
        subject_fullname = i[3]
        lecture_type=i[5]

        if lecture_type == "lecture":
            room = "514"
        else:
            room = random.randint(509, 513)

        formatted_data_A.append([lecture_type,teacher_fullname, subject_fullname, room, 0])
    # print(formatted_data_B)
    time_slots = ["8:30-9:30", "9:30-10:30", "10:30-11:30", "11:30-12:30", "BREAK", "1:30-2:30", "2:30-3:30"]
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    
    """
    no of labs per subject(4) per week = 1 | no of lectures per subject(6) per week = 3 
    total labs per week = 4 * 2(hrs) = 8 | total lectures per week = 6 * 3 = 18
    total free lectures per week = 30 - 18 - 8 = 4

    free lecture count per day limit = 2
    non free lecture count per day limit = 4
    total free lecture count limit = 7
    total non free lecture count limit = 15
    
    labs count per day limit = 2 * 2(hrs) = 4
    """

    total_free_lecture_count = 0
    total_nonfree_lecture_count = 0
    total_nonfree_lab_count = 0

    total_lab_count = {"Python Lab":0, "COA Lab":0, "OS Lab":0, "CN Lab":0}
    
    print("\nA ka savedata\n")

    for day in days:
        
        free_lecture_count_per_day = 0
        non_free_lecture_count_per_day = 0
        lab_count_per_day = 0

        for slot in time_slots:
            if slot != "BREAK":
                random.shuffle(formatted_data_A)
                # print(total_lab_count)
                if (total_nonfree_lecture_count < 18 and non_free_lecture_count_per_day < 4) and ((save_data == [] and formatted_data_A[0][0] == "lecture") or (formatted_data_A[0][0] == "lecture" and save_data[-1][1].split(" ")[-1] != "Lab") or (formatted_data_A[0][0] == "lecture" and save_data[-1][1].split(" ")[-1] == "Lab" and total_lab_count[save_data[-1][1]] >= 2)):
                    if (formatted_data_A[0][4] < 3 and non_free_lecture_count_per_day < 4):
                        data=[formatted_data_A[0][1],formatted_data_A[0][2],formatted_data_A[0][3], day, slot]
                        formatted_data_A[0][4] += 1
                        non_free_lecture_count_per_day += 1
                        total_nonfree_lecture_count += 1
                        save_data.append(data)
                    else:
                        for i in formatted_data_A:
                            if i[0] == "lecture" and i[4] < 3:
                                data=[i[1],i[2],i[3], day, slot]
                                i[4] += 1
                                # save_data.clear()
                                save_data.append(data)
                                non_free_lecture_count_per_day += 1
                                total_nonfree_lecture_count += 1
                                break
                elif (save_data == [] and formatted_data_A[0][0] == "lab" and slot != "2:30-3:30" and slot != "11:30-12:30" and slot != "9:30-10:30"):
                    if (total_lab_count[formatted_data_A[0][2]] < 2):
                        data=[formatted_data_A[0][1],formatted_data_A[0][2],formatted_data_A[0][3], day, slot]
                        total_lab_count[formatted_data_A[0][2]] += 1
                        save_data.append(data)
                        lab_count_per_day+=1
                        total_nonfree_lab_count+=1
                    else:
                        for lab_name, lab_count in total_lab_count.items():
                            if lab_count < 2:
                                needed_data=[]
                                for i in formatted_data_A:
                                    if i[2] == lab_name:
                                        needed_data=i.copy()
                                        break
                                data=[needed_data[1],needed_data[2], needed_data[3], day, slot]
                                save_data.append(data)
                                total_lab_count[lab_name] += 1
                                lab_count_per_day+=1
                                total_nonfree_lab_count+=1
                                break
                            
                elif (save_data[-1][1].split(" ")[-1] == "Lab" and total_lab_count[save_data[-1][1]] < 2 and lab_count_per_day < 4):
                    data=save_data[-1].copy()
                    data[3]=day
                    data[4]=slot
                    save_data.append(data)
                    total_lab_count[save_data[-1][1]] += 1
                    lab_count_per_day+=1
                    total_nonfree_lab_count+=1

                elif non_free_lecture_count_per_day >= 4 and total_free_lecture_count < 4 and (slot == "8:30-9:30" or slot == "1:30-2:30" or slot == "2:30-3:30"):
                    data=["Free", "", "", day, slot]
                    free_lecture_count_per_day += 1
                    total_free_lecture_count += 1
                    save_data.append(data)

                elif (formatted_data_A[0][0] == "lab" and total_lab_count[formatted_data_A[0][2]] < 2 and lab_count_per_day < 4 and slot != "2:30-3:30" and slot != "11:30-12:30" and slot != "9:30-10:30"):
                    data=[formatted_data_A[0][1],formatted_data_A[0][2],formatted_data_A[0][3], day, slot]
                    save_data.append(data)
                    total_lab_count[formatted_data_A[0][2]] += 1
                    lab_count_per_day+=1
                    total_nonfree_lab_count+=1

                else:
                    if (total_nonfree_lecture_count < 18 and non_free_lecture_count_per_day < 4):
                        for i in formatted_data_A:
                            if i[0] == "lecture" and i[4] < 3:
                                data=[i[1],i[2],i[3], day, slot]
                                i[4] += 1
                                # save_data.clear()
                                save_data.append(data)
                                non_free_lecture_count_per_day += 1
                                total_nonfree_lecture_count += 1
                                break
                    elif (total_nonfree_lab_count < 8 and slot != "2:30-3:30" and slot != "11:30-12:30" and slot != "9:30-10:30"):
                        for lab_name, lab_count in total_lab_count.items():
                            if lab_count < 2:
                                needed_data=[]
                                for i in formatted_data_A:
                                    if i[2] == lab_name:
                                        needed_data=i.copy()
                                        break
                                data=[needed_data[1],needed_data[2], needed_data[3], day, slot]
                                save_data.append(data)
                                total_lab_count[lab_name] += 1
                                lab_count_per_day+=1
                                total_nonfree_lab_count+=1
                                break
                    # else (total_free_lecture_count < 7 and total_nonfree_lecture_count >= 15):
                    elif (total_free_lecture_count < 4 and (slot =="8:30-9:30" or slot == "1:30-2:30" or slot == "2:30-3:30")):    
                        data=["Free", "", "", day, slot]
                        free_lecture_count_per_day += 1
                        total_free_lecture_count += 1
                        save_data.append(data)
                    elif (total_free_lecture_count == 4 and total_nonfree_lab_count == 8 and total_nonfree_lecture_count < 18):
                        for i in formatted_data_A:
                            if i[0] == "lecture" and i[4] < 3:
                                data=[i[1],i[2],i[3], day, slot]
                                i[4] += 1
                                # save_data.clear()
                                save_data.append(data)
                                non_free_lecture_count_per_day += 1
                                total_nonfree_lecture_count += 1
                                break
                    elif (total_nonfree_lecture_count >= 18 and total_nonfree_lab_count == 8 and total_free_lecture_count < 4):
                        while (total_free_lecture_count < 4):
                            data=["Free", "", "", day, slot]
                            free_lecture_count_per_day += 1
                            total_free_lecture_count += 1
                            save_data.append(data)
        # print(save_data, "\n")
        # print(formatted_data_A)

    if (len(teachers_data) < 5 and len(teachers_data) > 0):
        msg = messagebox.showerror("ERROR","You must have atleast 5 teachers to generate a valid TT") 
        return ValueError

    cursor.execute("""delete from timetable""")
    conn.commit()

    cursor.execute("""delete from timetable_B""")
    conn.commit()

    cursor.execute("""delete from timetable_C""")
    conn.commit()

    for i in range(0,len(save_data)):
        cursor.execute("INSERT INTO timetable (teacher_name, subject_name, room_number, day, time_slot) VALUES ( ?, ?, ?, ?, ?)", (save_data[i][0],save_data[i][1],save_data[i][2], save_data[i][3], save_data[i][4]))
        conn.commit()

    # load_timetable(subjects=formatted_data_A)
    if (len(save_data) != 30):
        fill_random_tt()

    timetable_frame(subjects=save_data)


def fill_timetable_A():
    show_focusA(event=None)

    cursor.execute("SELECT * FROM timetable")
    data=cursor.fetchall()

    if data != []:
        new_data = []
        for i in data:
            new_data.append([i[1], i[0], i[2], i[3], i[4]])
        timetable_frame(subjects=new_data)
        return


def fill_timetable_B():
    save_data.clear()
    
    cursor.execute("SELECT * FROM timetable_B")
    data=cursor.fetchall()
    
    if data != []:
        new_data = []
        for i in data:
            new_data.append([i[1], i[0], i[2], i[3], i[4]])
        timetable_frame(subjects=new_data)
        return

    cursor.execute("SELECT * FROM teacher")
    teachers_data = cursor.fetchall()

    cursor.execute('select *  from timetable')
    tt_of_A = cursor.fetchall()

    if tt_of_A == []:
        msg = messagebox.showerror("ERROR","Please generate TT for the previous classes first.") 
        return ValueError

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    time_slots = ["8:30-9:30", "9:30-10:30", "10:30-11:30", "11:30-12:30", "BREAK", "1:30-2:30", "2:30-3:30"]

    formatted_data_B = []

    for i in teachers_data:
        teacher_fullname = i[1] + " " + i[2]
        subject_fullname = i[3]
        lecture_type=i[5]

        if lecture_type == "lecture":
            room = "513"
        else:
            room = random.randint(509, 513)

        formatted_data_B.append([lecture_type ,teacher_fullname, subject_fullname, room, 0])
    

    total_free_lecture_count = 0
    total_nonfree_lecture_count = 0
    total_nonfree_lab_count = 0

    total_lab_count = {"Python Lab":0, "COA Lab":0, "OS Lab":0, "CN Lab":0}

    print("\nB ka savedata\n")
    for day in days:
        
        
        free_lecture_count_per_day = 0
        non_free_lecture_count_per_day = 0
        lab_count_per_day = 0

        for slot in time_slots:
            if slot != "BREAK":
                random.shuffle(formatted_data_B)
                needed_data_A=()
                for j in tt_of_A:
                    if (j[3] == day and j[4] == slot):
                        needed_data_A = j 

                # for i in formatted_data_B:
                while (formatted_data_B[0][1] == needed_data_A[1] or formatted_data_B[0][2] == needed_data_A[0]):
                    random.shuffle(formatted_data_B)
                print(needed_data_A)
                # print(needed_data_A)
                if (total_nonfree_lecture_count < 18 and non_free_lecture_count_per_day < 4) and ((save_data == [] and formatted_data_B[0][0] == "lecture") or (formatted_data_B[0][0] == "lecture" and save_data[-1][1].split(" ")[-1] != "Lab") or (formatted_data_B[0][0] == "lecture" and save_data[-1][1].split(" ")[-1] == "Lab" and total_lab_count[save_data[-1][1]] >= 2)):
                    if (formatted_data_B[0][4] < 3 and non_free_lecture_count_per_day < 4):
                        data=[formatted_data_B[0][1],formatted_data_B[0][2],formatted_data_B[0][3], day, slot]
                        formatted_data_B[0][4] += 1
                        non_free_lecture_count_per_day += 1
                        total_nonfree_lecture_count += 1
                        save_data.append(data)
                    else:
                        for i in formatted_data_B:
                            if i[0] == "lecture" and i[4] < 3:
                                data=[i[1],i[2],i[3], day, slot]
                                i[4] += 1
                                # save_data.clear()
                                save_data.append(data)
                                non_free_lecture_count_per_day += 1
                                total_nonfree_lecture_count += 1
                                break
                elif (save_data == [] and formatted_data_B[0][0] == "lab" and slot != "2:30-3:30" and slot != "11:30-12:30" and slot != "9:30-10:30"):
                    if (total_lab_count[formatted_data_B[0][2]] < 2):
                        data=[formatted_data_B[0][1],formatted_data_B[0][2],formatted_data_B[0][3], day, slot]
                        total_lab_count[formatted_data_B[0][2]] += 1
                        save_data.append(data)
                        lab_count_per_day+=1
                        total_nonfree_lab_count+=1
                    else:
                        for lab_name, lab_count in total_lab_count.items():
                            if lab_count < 2:
                                needed_data=[]
                                for i in formatted_data_B:
                                    if i[2] == lab_name:
                                        needed_data=i.copy()
                                        break
                                data=[needed_data[1],needed_data[2], needed_data[3], day, slot]
                                save_data.append(data)
                                total_lab_count[lab_name] += 1
                                lab_count_per_day+=1
                                total_nonfree_lab_count+=1
                                break
                            
                elif (save_data[-1][1].split(" ")[-1] == "Lab" and total_lab_count[save_data[-1][1]] < 2 and lab_count_per_day < 4):
                    data=save_data[-1].copy()
                    data[3]=day
                    data[4]=slot
                    save_data.append(data)
                    total_lab_count[save_data[-1][1]] += 1
                    lab_count_per_day+=1
                    total_nonfree_lab_count+=1

                elif non_free_lecture_count_per_day >= 4 and free_lecture_count_per_day < 2 and total_free_lecture_count < 4 and (slot == "8:30-9:30" or slot == "1:30-2:30" or slot == "2:30-3:30"):
                    data=["Free", "", "", day, slot]
                    free_lecture_count_per_day += 1
                    total_free_lecture_count += 1
                    save_data.append(data)

                elif (formatted_data_B[0][0] == "lab" and total_lab_count[formatted_data_B[0][2]] < 2 and lab_count_per_day < 4 and slot != "2:30-3:30" and slot != "11:30-12:30" and slot != "9:30-10:30"):
                    data=[formatted_data_B[0][1],formatted_data_B[0][2],formatted_data_B[0][3], day, slot]
                    save_data.append(data)
                    total_lab_count[formatted_data_B[0][2]] += 1
                    lab_count_per_day+=1
                    total_nonfree_lab_count+=1

                else:
                    if (total_nonfree_lecture_count < 18 and non_free_lecture_count_per_day < 4):
                        for i in formatted_data_B:
                            if i[0] == "lecture" and i[4] < 3:
                                data=[i[1],i[2],i[3], day, slot]
                                i[4] += 1
                                # save_data.clear()
                                save_data.append(data)
                                non_free_lecture_count_per_day += 1
                                total_nonfree_lecture_count += 1
                                break
                    elif (lab_count_per_day < 4 and total_nonfree_lab_count < 8 and slot != "2:30-3:30" and slot != "11:30-12:30" and slot != "9:30-10:30"):
                        for lab_name, lab_count in total_lab_count.items():
                            if lab_count < 2:
                                needed_data=[]
                                for i in formatted_data_B:
                                    if i[2] == lab_name:
                                        needed_data=i.copy()
                                        break
                                data=[needed_data[1],needed_data[2], needed_data[3], day, slot]
                                save_data.append(data)
                                total_lab_count[lab_name] += 1
                                lab_count_per_day+=1
                                total_nonfree_lab_count+=1
                                break
                    # else (total_free_lecture_count < 7 and total_nonfree_lecture_count >= 15):
                    elif (total_free_lecture_count < 4 and free_lecture_count_per_day < 2 and (slot =="8:30-9:30" or slot == "1:30-2:30" or slot == "2:30-3:30")):    
                        data=["Free", "", "", day, slot]
                        free_lecture_count_per_day += 1
                        total_free_lecture_count += 1
                        save_data.append(data)
                    
                    elif (total_free_lecture_count == 4 and total_nonfree_lab_count == 8 and total_nonfree_lecture_count < 18):
                        for i in formatted_data_A:
                            if i[0] == "lecture" and i[4] < 3 and i[1] != needed_data_A[1] and i[2] != needed_data_A[0]:
                                data=[i[1],i[2],i[3], day, slot]
                                i[4] += 1
                                # save_data.clear()
                                save_data.append(data)
                                non_free_lecture_count_per_day += 1
                                total_nonfree_lecture_count += 1
                                break
                    elif (total_nonfree_lecture_count >= 18 and total_nonfree_lab_count == 8 and total_free_lecture_count < 4):
                        while (total_free_lecture_count < 4):
                            data=["Free", "", "", day, slot]
                            free_lecture_count_per_day += 1
                            total_free_lecture_count += 1
                            save_data.append(data)

                    # else:
                    #     for i in formatted_data_B:
                    #         if (i[0] == "lab" and total_lab_count[formatted_data_B[0][2]] < 2):
                    #             save_data.append([formatted_data_B[0][1],formatted_data_B[0][2],formatted_data_B[0][3], day, slot])
                    #             print([formatted_data_B[0][1],formatted_data_B[0][2],formatted_data_B[0][3], day, slot], "\n")
                    #         elif (i[0] == "lecture" and i[4] < 3):
                    #             save_data.append([i[1],i[2],i[3], day, slot])
                    #             print([i[1],i[2],i[3], day, slot], "\n")

        # print(save_data, "\n")
    # print(formatted_data_A)
    # print(formatted_data_B)

    if (len(teachers_data) < 5 and len(teachers_data) > 0):
        msg = messagebox.showerror("ERROR","You must have atleast 5 teachers to generate a valid TT") 
        return ValueError

    # load_timetable(subjects=formatted_data)
    for i in range(0, len(save_data)):
        cursor.execute("INSERT INTO timetable_B (teacher_name, subject_name,room_number, day, time_slot) VALUES ( ?, ?, ?, ?, ?)", (save_data[i][0],save_data[i][1],save_data[i][2], save_data[i][3], save_data[i][4]))
        conn.commit()

    # print(total_lab_count, "\n")
    # print(formatted_data_B, "\n")
    if (len(save_data) != 30):
        fill_timetable_B()

    timetable_frame(subjects=save_data)


def fill_timetable_C():
    save_data.clear()

    cursor.execute("SELECT * FROM timetable_C")
    data=cursor.fetchall()

    if data != []:
        new_data = []
        for i in data:
            new_data.append([i[1], i[0], i[2], i[3], i[4]])
        timetable_frame(subjects=new_data)
        return

    cursor.execute("SELECT * FROM teacher")
    teachers_data = cursor.fetchall()

    cursor.execute('select *  from timetable')
    tt_of_A = cursor.fetchall()

    cursor.execute('select *  from timetable_B')
    tt_of_B = cursor.fetchall()

    if (tt_of_B == [] or tt_of_A == []):
        msg = messagebox.showerror("ERROR","Please generate TT for the previous classes first.") 
        return ValueError

    # print(tt_of_A)
    # print(tt_of_B)

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    time_slots = ["8:30-9:30", "9:30-10:30", "10:30-11:30", "11:30-12:30", "BREAK", "1:30-2:30", "2:30-3:30"]

    formatted_data_C = []

    for i in teachers_data:
        teacher_fullname = i[1] + " " + i[2]
        subject_fullname = i[3]
        lecture_type=i[5]

        if lecture_type == "lecture":
            room = "512"
        else:
            room = random.randint(509, 513)

        formatted_data_C.append([lecture_type ,teacher_fullname, subject_fullname, room, 0])
    

    total_free_lecture_count = 0
    total_nonfree_lecture_count = 0
    total_nonfree_lab_count = 0

    total_lab_count = {"Python Lab":0, "COA Lab":0, "OS Lab":0, "CN Lab":0}

    print("\nC ka savedata\n")

    for day in days:
        # print(save_data, "\n")

        free_lecture_count_per_day = 0
        non_free_lecture_count_per_day = 0
        lab_count_per_day = 0

        for slot in time_slots:
            if slot != "BREAK":

                random.shuffle(formatted_data_C)
                needed_data_A=()
                needed_data_B=()
                for j in tt_of_A:
                    if (j[3] == day and j[4] == slot):
                        needed_data_A = j 
                
                for k in tt_of_B:
                    if (k[3] == day and k[4] == slot):
                        needed_data_B = k 

                while (formatted_data_C[0][1] == needed_data_A[1] or formatted_data_C[0][2] == needed_data_A[0] or formatted_data_C[0][1] == needed_data_B[1] or formatted_data_C[0][2] == needed_data_B[0]):
                    random.shuffle(formatted_data_C)
                else:
                # print(needed_data)
                    if (total_nonfree_lecture_count < 18 and non_free_lecture_count_per_day < 4) and ((save_data == [] and formatted_data_C[0][0] == "lecture") or (formatted_data_C[0][0] == "lecture" and save_data[-1][1].split(" ")[-1] != "Lab") or (formatted_data_C[0][0] == "lecture" and save_data[-1][1].split(" ")[-1] == "Lab" and total_lab_count[save_data[-1][1]] >= 2)):
                        if (formatted_data_C[0][4] < 3 and non_free_lecture_count_per_day < 4):
                            data=[formatted_data_C[0][1],formatted_data_C[0][2],formatted_data_C[0][3], day, slot]
                            formatted_data_C[0][4] += 1
                            non_free_lecture_count_per_day += 1
                            total_nonfree_lecture_count += 1
                            save_data.append(data)
                        else:
                            for i in formatted_data_C:
                                if i[0] == "lecture" and i[4] < 3:
                                    data=[i[1],i[2],i[3], day, slot]
                                    i[4] += 1
                                    # save_data.clear()
                                    save_data.append(data)
                                    non_free_lecture_count_per_day += 1
                                    total_nonfree_lecture_count += 1
                                    break
                    elif (save_data == [] and formatted_data_C[0][0] == "lab" and slot != "2:30-3:30" and slot != "11:30-12:30" and slot != "9:30-10:30"):
                        if (total_lab_count[formatted_data_C[0][2]] < 2):
                            data=[formatted_data_C[0][1],formatted_data_C[0][2],formatted_data_C[0][3], day, slot]
                            total_lab_count[formatted_data_C[0][2]] += 1
                            save_data.append(data)
                            lab_count_per_day+=1
                            total_nonfree_lab_count+=1
                        else:
                            for lab_name, lab_count in total_lab_count.items():
                                if lab_count < 2:
                                    needed_data=[]
                                    for i in formatted_data_C:
                                        if i[2] == lab_name:
                                            needed_data=i.copy()
                                            break
                                    data=[needed_data[1],needed_data[2], needed_data[3], day, slot]
                                    save_data.append(data)
                                    total_lab_count[lab_name] += 1
                                    lab_count_per_day+=1
                                    total_nonfree_lab_count+=1
                                    break
                                
                    elif (save_data[-1][1].split(" ")[-1] == "Lab" and total_lab_count[save_data[-1][1]] < 2 and lab_count_per_day < 4):
                        data=save_data[-1].copy()
                        data[3]=day
                        data[4]=slot
                        save_data.append(data)
                        total_lab_count[save_data[-1][1]] += 1
                        lab_count_per_day+=1
                        total_nonfree_lab_count+=1

                    elif non_free_lecture_count_per_day >= 4 and free_lecture_count_per_day < 2 and total_free_lecture_count < 4 and (slot == "8:30-9:30" or slot == "1:30-2:30" or slot == "2:30-3:30"):
                        data=["Free", "", "", day, slot]
                        free_lecture_count_per_day += 1
                        total_free_lecture_count += 1
                        save_data.append(data)

                    elif (formatted_data_C[0][0] == "lab" and total_lab_count[formatted_data_C[0][2]] < 2 and lab_count_per_day < 4 and slot != "2:30-3:30" and slot != "11:30-12:30" and slot != "9:30-10:30"):
                        data=[formatted_data_C[0][1],formatted_data_C[0][2],formatted_data_C[0][3], day, slot]
                        save_data.append(data)
                        total_lab_count[formatted_data_C[0][2]] += 1
                        lab_count_per_day+=1
                        total_nonfree_lab_count+=1

                    else:
                        if (total_nonfree_lecture_count < 18 and non_free_lecture_count_per_day < 4):
                            for i in formatted_data_C:
                                if i[0] == "lecture" and i[4] < 3:
                                    data=[i[1],i[2],i[3], day, slot]
                                    i[4] += 1
                                    # save_data.clear()
                                    save_data.append(data)
                                    non_free_lecture_count_per_day += 1
                                    total_nonfree_lecture_count += 1
                                    break
                        elif (lab_count_per_day < 4 and total_nonfree_lab_count < 8 and slot != "2:30-3:30" and slot != "11:30-12:30" and slot != "9:30-10:30"):
                            for lab_name, lab_count in total_lab_count.items():
                                if lab_count < 2:
                                    needed_data=[]
                                    for i in formatted_data_C:
                                        if i[2] == lab_name:
                                            needed_data=i.copy()
                                            break
                                    data=[needed_data[1],needed_data[2], needed_data[3], day, slot]
                                    save_data.append(data)
                                    total_lab_count[lab_name] += 1
                                    lab_count_per_day+=1
                                    total_nonfree_lab_count+=1
                                    break
                        # else (total_free_lecture_count < 7 and total_nonfree_lecture_count >= 15):
                        elif (total_free_lecture_count < 4 and free_lecture_count_per_day < 2 and (slot =="8:30-9:30" or slot == "1:30-2:30" or slot == "2:30-3:30")):    
                            data=["Free", "", "", day, slot]
                            free_lecture_count_per_day += 1
                            total_free_lecture_count += 1
                            save_data.append(data)
                        
                        elif (total_free_lecture_count == 4 and total_nonfree_lab_count == 8 and total_nonfree_lecture_count < 18):
                            for i in formatted_data_C:
                                if i[0] == "lecture" and i[4] < 3 and i[1] != needed_data_A[1] and i[2] != needed_data_A[0] and i[1] != needed_data_B[1] and i[2] != needed_data_B[0]:
                                    data=[i[1],i[2],i[3], day, slot]
                                    i[4] += 1
                                    # save_data.clear()
                                    save_data.append(data)
                                    non_free_lecture_count_per_day += 1
                                    total_nonfree_lecture_count += 1
                                    break
                        elif (total_nonfree_lecture_count >= 18 and total_nonfree_lab_count == 8 and total_free_lecture_count < 4):
                            while (total_free_lecture_count < 4):
                                data=["Free", "", "", day, slot]
                                free_lecture_count_per_day += 1
                                total_free_lecture_count += 1
                                save_data.append(data)
                                       
    # print(formatted_data_A)
    # print(formatted_data_C)

    if (len(teachers_data) < 5 and len(teachers_data) > 0):
        msg = messagebox.showerror("ERROR","You must have atleast 5 teachers to generate a valid TT") 
        return ValueError

        
    for i in range(0, len(save_data)):
        cursor.execute("INSERT INTO timetable_C (teacher_name, subject_name, room_number, day, time_slot) VALUES ( ?, ?, ?, ?, ?)", (save_data[i][0],save_data[i][1],save_data[i][2], save_data[i][3], save_data[i][4]))
        conn.commit()

    if (len(save_data) != 30):
        fill_timetable_C()
        
    # load_timetable(subjects=formatted_data)
    timetable_frame(subjects=save_data)



# Loop through the menu items and create buttons
for item in menu_items:
    if (item[0] == "TEACHERS"):
        button = Button(sidebar, text=item[0], image=item[1], compound=LEFT, fg="white", bg="#4a148c", bd=0, padx=20, pady=10, anchor="w",command=teacher_section)
        button.pack(anchor="w") 
    # Create a button with text and icon
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
content = Frame(root, bg="#C1BBEB", width=1000, height=550)
content.pack(side=TOP, fill=BOTH, expand=True)

class_1_button = Button(content, text="D10A", font=("Arial", 8, "bold"), bg="#4a148c", fg="white", bd=0, padx=10, pady=5, command=fill_timetable_A)
class_1_button.pack(side=TOP, padx=25, pady=5, anchor="w")

class_2_button = Button(content, text="D10B", font=("Arial", 8, "bold"), bg="#4a148c", fg="white", bd=0, padx=10, pady=5, command=fill_timetable_B)
class_2_button.place(x=class_1_button.winfo_x() + class_1_button.winfo_reqwidth() + 41, y=class_1_button.winfo_y()+5)

class_3_button = Button(content, text="D10C", font=("Arial", 8, "bold"), bg="#4a148c", fg="white", bd=0, padx=10, pady=5, command=fill_timetable_C)
class_3_button.place(x=class_2_button.winfo_x() + class_2_button.winfo_reqwidth() + 115, y=class_2_button.winfo_y()+5)

# Binding click events to buttons
def show_focusA(event):
    class_1_button.config(
        bg='#C1BBEB',
        fg="#4a148c",
        highlightbackground="#4a148c"
    )
    class_2_button.config(
        bg='#4a148c',
        fg="white"
    )
    class_3_button.config(
        bg='#4a148c',
        fg="white"
    )
def show_focusB(event):
    class_2_button.config(
        bg='#C1BBEB',
        fg="#4a148c"
    )
    class_1_button.config(
        bg='#4a148c',
        fg="white"
    )
    class_3_button.config(
        bg='#4a148c',
        fg="white"
    )
def show_focusC(event):
    class_3_button.config(
        bg='#C1BBEB',
        fg="#4a148c"
    )
    class_2_button.config(
        bg='#4a148c',
        fg="white"
    )
    class_1_button.config(
        bg='#4a148c',
        fg="white"
    )
class_1_button.bind('<Button>',show_focusA)
class_2_button.bind('<Button>',show_focusB)
class_3_button.bind('<Button>',show_focusC)

show_focusA(event=None)

# Create a calendar frame
calendar = Frame(content, bg="#C1BBEB", width=1000, height=500)
calendar.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

# load_timetable([])
timetable_frame([])

# Create a generate button
generate_button = Button(content, text="+", font=("Arial", 20, "bold"), bg="#4a148c", fg="white", bd=0, width=10, height=10,command=fill_random_tt)
generate_button.pack(side=RIGHT, anchor=NE, padx=20, pady=20)


save_button = Button(content, text="SAVE", font=("Arial", 10, "bold"), bg="#4a148c", fg="white", bd=0, width=10, height=2,command=save_details)
save_button.pack(side=BOTTOM, anchor=NE, padx=10, pady=10)


# Start the main loop
root.mainloop()
