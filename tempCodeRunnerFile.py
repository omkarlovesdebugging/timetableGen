
# # Use the function to connect to your database
# conn, cursor = connect_to_db('lecture.db')

# # Create a table named 'subjects' in the database
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS subjects(
#         subject_name TEXT,
#         teacher_name TEXT,
#         room TEXT
#     )
# ''')

# # Insert the subjects data into the table
# subjects = [
#     ("DBMS", "Vijay Sir", "Room S-11"),
#     ("CN Lab", "Anushree", "Room S-12"),
#     ("Engg. Mathematics", "Netto Mam", "Room P-01"),
#     ("Engg. Physics", "Vidya Puja", "Room G007"),
#     ("Car Mechanics", "Don Vijay", "Room X73"),
#     ("Python Lab", "Sneha Pakka", "Room X74"),
#     ("COA Maths", "Abhay FirseShekhar", "Room F14"),
#     ("COA Lab", "Baburao", "Room F14/F16/F17")
# ]

# cursor.executemany('''
#     INSERT INTO subjects(subject_name, teacher_name, room) VALUES(?,?,?)
# ''', subjects)