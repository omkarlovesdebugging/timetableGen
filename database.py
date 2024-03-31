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

c.execute(""" DELETE FROM notifications;""")
conn.commit()
# c.execute(""" DELETE FROM teacher where Lec_Type='lab';""")
# conn.commit()
c.execute(""" DELETE FROM sqlite_sequence WHERE name='notifications';""")
conn.commit()

# c.execute("""delete from timetable_B""")
# conn.commit()

# c.execute("""delete from timetable_C""")
# conn.commit()


# c.execute("""ALTER TABLE timetable
# ADD COLUMN day TEXT""")
# c.execute("""ALTER TABLE timetable
# ADD COLUMN time_slot TEXT""")

print(c.fetchall())
conn.commit()

print('Connnection successful')
conn.close()







