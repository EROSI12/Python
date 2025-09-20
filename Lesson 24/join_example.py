import sqlite3

connection = sqlite3.connect('example.db')

cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS employees(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary REAL
)
''')
connection.commit()


cursor.execute("INSERT INTO student (name) VALUES ('Alice')")
cursor.execute("INSERT INTO student (name) VALUES ('Boby')")

cursor.execute("INSERT INTO courses (course_name, student_id) VALUES ('Math, 1')")
cursor.execute("INSERT INTO courses (course_name, student_id) VALUES ('Science, 1')")
cursor.execute("INSERT INTO courses (course_name, student_id) VALUES ('Art, 1')")

conn.commit()
cursor.execute('''
SELECT student.name, course.course_name from students
JOIN courses on students.student_id = course.student_id
''')

rows = coursor.fetchall()
for row in rows:
    print(f"Student:{row[0]}, Course: {row[1]}")
    conn.close()