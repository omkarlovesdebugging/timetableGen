import sqlite3

conn = sqlite3.connect('timetable_generator.db')

c = conn.cursor()

c.execute("""
select *  from timetable
""")
print(c.fetchall())
conn.commit()

print('Connnection successful')
conn.close()





# CREATE TABLE timetable (
#     subject_name VARCHAR(45) ,
#     teacher_name VARCHAR(45) ,
#     room_number VARCHAR(45) )
# """)

