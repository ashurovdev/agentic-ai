import sqlite3
conn = sqlite3.connect('school.db')
cursor = conn.cursor()

# Table 1: Students
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER,
    grade TEXT,
    address TEXT,
    phone TEXT,
    email TEXT,
    birth_date DATE,
    gender TEXT,
    gpa REAL
)
''')

# Insert students data
students_data = [
    ('John', 'Smith', 15, '9-A', 'New York, Manhattan', '+1-555-0101', 'john@email.com', '2009-03-15', 'Male', 3.8),
    ('Emma', 'Johnson', 16, '10-B', 'Los Angeles, Beverly Hills', '+1-555-0102', 'emma@email.com', '2008-07-22', 'Female', 4.0),
    ('Michael', 'Williams', 14, '8-C', 'Chicago, Lincoln Park', '+1-555-0103', 'michael@email.com', '2010-11-10', 'Male', 3.5),
    ('Sophia', 'Brown', 15, '9-A', 'Houston, Downtown', '+1-555-0104', 'sophia@email.com', '2009-05-18', 'Female', 3.9),
    ('James', 'Davis', 17, '11-A', 'Phoenix, Central', '+1-555-0105', 'james@email.com', '2007-09-25', 'Male', 3.7)
]

cursor.executemany('''
INSERT INTO students (first_name, last_name, age, grade, address, phone, email, birth_date, gender, gpa)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', students_data)

# Table 2: Courses
cursor.execute('''
CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT NOT NULL,
    teacher TEXT,
    hours_per_week INTEGER,
    room_number TEXT,
    schedule_days TEXT,
    start_time TEXT,
    end_time TEXT,
    credits INTEGER,
    level TEXT,
    max_students INTEGER
)
''')

# Insert courses data
courses_data = [
    ('Mathematics', 'Dr. Robert Anderson', 4, '201', 'Mon-Wed-Fri', '09:00', '10:30', 5, 'Advanced', 30),
    ('Physics', 'Dr. Lisa Martinez', 3, '305', 'Tue-Thu-Fri', '10:45', '12:15', 4, 'Intermediate', 25),
    ('English Literature', 'Ms. Sarah Johnson', 5, '102', 'Daily', '14:00', '15:30', 6, 'Beginner', 20),
    ('Chemistry', 'Dr. David Lee', 3, '404', 'Mon-Wed-Fri', '08:00', '09:30', 4, 'Advanced', 28),
    ('World History', 'Mr. Thomas Wilson', 2, '203', 'Tue-Wed', '13:00', '14:30', 3, 'Intermediate', 35)
]

cursor.executemany('''
INSERT INTO courses (course_name, teacher, hours_per_week, room_number, schedule_days, start_time, end_time, credits, level, max_students)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', courses_data)

# Table 3: Library
cursor.execute('''
CREATE TABLE IF NOT EXISTS library (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_title TEXT NOT NULL,
    author TEXT,
    publisher TEXT,
    year INTEGER,
    pages INTEGER,
    language TEXT,
    genre TEXT,
    isbn TEXT,
    price REAL,
    quantity INTEGER
)
''')

# Insert library data
library_data = [
    ('To Kill a Mockingbird', 'Harper Lee', 'HarperCollins', 1960, 336, 'English', 'Fiction', '978-0-06-112008-4', 15.99, 12),
    ('1984', 'George Orwell', 'Penguin Books', 1949, 328, 'English', 'Dystopian', '978-0-452-28423-4', 13.99, 15),
    ('Python Programming', 'Mark Lutz', 'O\'Reilly Media', 2019, 1632, 'English', 'Technical', '978-1-491-94600-8', 59.99, 8),
    ('The Great Gatsby', 'F. Scott Fitzgerald', 'Scribner', 1925, 180, 'English', 'Classic', '978-0-7432-7356-5', 12.99, 20),
    ('Harry Potter and the Sorcerer\'s Stone', 'J.K. Rowling', 'Scholastic', 1997, 309, 'English', 'Fantasy', '978-0-590-35340-3', 10.99, 25)
]

cursor.executemany('''
INSERT INTO library (book_title, author, publisher, year, pages, language, genre, isbn, price, quantity)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', library_data)

# Commit changes
conn.commit()

# Display data
print("=== STUDENTS ===")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

print("\n=== COURSES ===")
cursor.execute("SELECT * FROM courses")
for row in cursor.fetchall():
    print(row)

print("\n=== LIBRARY ===")
cursor.execute("SELECT * FROM library")
for row in cursor.fetchall():
    print(row)

# Close connection
conn.close()

print("\n✅ Database successfully created: school.db")