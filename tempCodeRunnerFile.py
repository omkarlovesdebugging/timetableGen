def save_details():
#     Teacher_Name = teacher_name_entry.get()
#     Subject = subject_entry.get()

#     # Connect to SQLite database
#     conn = sqlite3.connect('lecture.db')
#     cursor = conn.cursor()

#     # Create the 'lectures' table if it doesn't exist
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS lectures (
#             subject TEXT,
#             teacher_name TEXT
#         )
#     ''')

#     # Insert the details into the 'lectures' table
#     cursor.execute("INSERT INTO lectures (subject, teacher_name) VALUES (?, ?)", (Subject, Teacher_Name))

#     # Commit the changes and close the connection
#     conn.commit()
#     conn.close()