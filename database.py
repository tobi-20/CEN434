import mysql.connector as con

# Create a database connection
mydb = con.connect(
    host="localhost",
    user="root",
    password="t0b2-i8o"
)

# Create a cursor
mycursor = mydb.cursor()

# Create a database
mycursor.execute("CREATE DATABASE CEN_students")
mycursor.execute("USE CEN_students")

# Create a table
mycursor.execute("CREATE TABLE students (name VARCHAR(255), matno VARCHAR(255))")

# Add data
sql = "INSERT INTO students (name, matno) VALUES (%s, %s)"
val = ("Kathy", "20cj027xxx")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

# Read data
mycursor.execute("SELECT name, matno FROM students")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

# Update data
sql = "UPDATE students SET matno = '20CJ029xxx' WHERE matno = '20CJ027xxx'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")

# Delete data
sql = "DELETE FROM students WHERE matno = '20cj027xxx'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")

# Delete table
sql = "DROP TABLE students"

mycursor.execute(sql)

# Delete database
sql = "DROP DATABASE CEN_students"

mycursor.execute(sql)

# Close connection
mydb.close()
