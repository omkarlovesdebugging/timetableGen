import sqlite3

conn = sqlite3.connect('Timetable_Generator.db')

c = conn.cursor()
conn.commit()
# CREATE TABLE teacher (
#     teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     first_name VARCHAR(45) NOT NULL,
#     last_name VARCHAR(45) NOT NULL,
#     subject_name VARCHAR(45) NOT NULL,
#     email VARCHAR(45) NOT NULL);
print('Connnection successful')
conn.close()