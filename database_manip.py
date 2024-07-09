import sqlite3


# Connect to the SQLite database.
with sqlite3.connect('school.db') as db:
    cursor = db.cursor()

# Create the table.
cursor.execute('''CREATE TABLE IF NOT EXISTS python_programming (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    grade INTEGER NOT NULL
                  )''')

# Create the data for the table.
students = [
    (55, "Carl Davis", 61),
    (66, "Dennis Fredrickson", 88),
    (77, "Jane Richards", 78),
    (12, "Peyton Sawyer", 45),
    (2, "Lucas Brooke", 99)
]

# Insert records into the table.
cursor.executemany('''INSERT OR REPLACE INTO python_programming
                   (id, name, grade)
                      VALUES (?, ?, ?)''', students)

# Commit the changes.
db.commit()

# Selecting the students with the grade of 60-80.
min_range = 60
max_range = 80
cursor.execute('''SELECT * FROM python_programming
                WHERE grade BETWEEN ? AND ?''', (min_range, max_range))

# Printing the result.
for row in cursor:
    print(f"ID: {row[0]}, Name: {row[1]}, Grade: {row[2]}")

# Updating Carl Davis's grade to 65
new_grade = 65
update_name = 'Carl Davis'
cursor.execute('''UPDATE python_programming SET grade = ?
               WHERE name = ?''', (new_grade, update_name))

# Double checking if the changes happened(if the row exists).
cursor.execute('''SELECT * FROM python_programming
               WHERE name = ? AND grade = ?''', (update_name, new_grade))

if not cursor.fetchall():
    # Unsuccessful update message if there is no row under that name.
    print("Update is unsuccessful there is no student under that name.")
else:
    # Print a message about success and commit the changes.
    print("Update is successful")
    db.commit()

# Deleting Dennis Fredrickson from the table.
delete_name = 'Dennis Fredrickson'

# Double checking if the row exists.
cursor.execute('''SELECT * FROM python_programming
               WHERE name = ?''', (delete_name,))
if not cursor.fetchall():
    print("Name cannot be found!")
else:
    # If there is a row like that then delete
    # the row and commit the changes and also
    # prints a successful message.
    cursor.execute('''DELETE FROM python_programming
               WHERE name = ?''', (delete_name,))
    db.commit()
    print(f"{delete_name} has been deleted!")

# Update the grade to 80 of all students who
# has got higher grade than 55.
new_grade = 80
grade_of = 55

# Checking if there are rows with the condition
cursor.execute('''SELECT * FROM python_programming
               WHERE grade > ?''', (grade_of,))

result = cursor.fetchall()
if not result:
    print("No data with the given condition!")
# If there are rows with the condition it
# does the update and commit the changes.
# also the user gets a successful message
else:
    cursor.execute('''UPDATE python_programming SET grade = ?
               WHERE grade > ?''', (new_grade, grade_of))
    db.commit()
    print(f"{len(result)} students have been updated!")
