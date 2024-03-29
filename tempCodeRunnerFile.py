def fill_random_tt():
    save_data.clear()
    show_focusA(event=None)

    cursor.execute("SELECT * FROM teacher")
    data = cursor.fetchall()

    formatted_data_A = []

    for i in data:
        teacher_fullname = i[1] + " " + i[2]
        subject_fullname = i[3]
        room="514"

        formatted_data_A.append([teacher_fullname, subject_fullname, room, 0])
    
    time_slots = ["8:30-9:30", "9:30-10:30", "10:30-11:30", "11:30-12:30", "BREAK", "1:30-3:30"]
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    
    save_data.clear()

    total_free_lecture_count = 0
    total_nonfree_lecture_count = 0

    for day in days:
        free_lecture_count_per_day = 0
        non_free_lecture_count_per_day = 0
        last_was_free = False  # Variable to keep track of the last lecture

        for slot in time_slots:
            if slot != "BREAK":
                random.shuffle(formatted_data_A)
                if (formatted_data_A[0][3] < 3 and non_free_lecture_count_per_day < 4):
                    data=[formatted_data_A[0][0],formatted_data_A[0][1],formatted_data_A[0][2], day, slot]
                    formatted_data_A[0][3] += 1
                    non_free_lecture_count_per_day += 1
                    total_nonfree_lecture_count += 1
                    last_was_free = False
                    save_data.append(data)
                elif (free_lecture_count_per_day < 3 or non_free_lecture_count_per_day > 3) and total_free_lecture_count < 10:
                    data=["Free", "", "", day, slot]
                    free_lecture_count_per_day += 1
                    total_free_lecture_count += 1
                    last_was_free = True
                    save_data.append(data)
                else:
                    if (total_free_lecture_count < 10):
                        data=["Free", "", "", day, slot]
                        free_lecture_count_per_day += 1
                        total_free_lecture_count += 1
                        last_was_free = True
                        save_data.append(data)
                    else:
                        # If last lecture was free, prioritize a non-free lecture
                        if last_was_free:
                            for i in formatted_data_A:
                                if i[3] < 3:
                                    data=[i[0],i[1],i[2], day, slot]
                                    i[3] += 1
                                    save_data.append(data)
                                    non_free_lecture_count_per_day += 1
                                    total_nonfree_lecture_count += 1
                                    last_was_free = False
                                    break
                        # If last lecture was non-free, prioritize a free lecture
                        else:
                            data=["Free", "", "", day, slot]
                            free_lecture_count_per_day += 1
                            total_free_lecture_count += 1
                            last_was_free = True
                            save_data.append(data)

    if (len(formatted_data_A) < 5 and len(formatted_data_A) > 0):
        msg = messagebox.showerror("ERROR","You must have atleast 5 teachers to generate a valid TT") 
        return ValueError

    cursor.execute("""delete from timetable""")
    conn.commit()

    for i in range(0,len(save_data)):
        cursor.execute("INSERT INTO timetable (subject_name, teacher_name, room_number, day, time_slot) VALUES ( ?, ?, ?, ?, ?)", (save_data[i][0],save_data[i][1],save_data[i][2], save_data[i][3], save_data[i][4]))
        conn.commit()

    timetable_frame(subjects=save_data)