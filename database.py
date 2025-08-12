import sqlite3

conn = sqlite3.connect('timetable_generator.db')

c = conn.cursor()


c.execute(""" DELETE FROM sqlite_sequence WHERE name='teacher';""")
conn.commit()



print(c.fetchall())
conn.commit()

print('Connnection successful')
conn.close()
