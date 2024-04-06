import sqlite3

conn = sqlite3.connect('timetable_generator.db')

c = conn.cursor()

# c.execute("""
# select *  from timetable
# """)

# c.execute("""CREATE TABLE timetable_C (
#     subject_name VARCHAR(45) ,
#     teacher_name VARCHAR(45) ,
#     room_number VARCHAR(45),
#     day TEXT,
#     time_slot TEXT )
# """)

# c.execute(""" DELETE FROM notifications;""")
# conn.commit()
# c.execute(""" DELETE FROM teacher;""")
# conn.commit()
# c.execute(""" DELETE FROM teacher where Lec_Type='lab';""")
# conn.commit()
c.execute(""" DELETE FROM sqlite_sequence WHERE name='teacher';""")
conn.commit()

# c.execute("""delete from timetable_B""")
# conn.commit()

# c.execute("""delete from timetable_C""")
# conn.commit()


# c.execute("""ALTER TABLE timetable
# ADD COLUMN day TEXT""")
# c.execute("""ALTER TABLE teacher
# ADD COLUMN password TEXT""")

# c.execute("INSERT INTO teacher (password) VALUES ('Jadhav') where first_name = 'Rakhi'")
# conn.commit()

print(c.fetchall())
conn.commit()

print('Connnection successful')
conn.close()