import sqlite3

conn = sqlite3.connect('Timetable_Generator.db')

c = conn.cursor()

conn.execute("""

""")

conn.commit()

print('Connnection successful')
conn.close()