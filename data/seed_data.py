import os, sys
CURRENT_DIR = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, os.pardir))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from db.setup import SessionLocal as Session, Base, engine
from models.student import Student
from models.course import Course
from models.enrollment import Enrollment
from sqlalchemy import inspect

# Drop all tables and recreate them
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

inspector = inspect(engine)
print("Tables created:", inspector.get_table_names())

# Start a session
session = Session()

# Seed Students
students_data = [
    ("Alice Johnson", "alice.johnson@email.com"),
    ("Bob Smith", "bob.smith@email.com"),
    ("Carol Davis", "carol.davis@email.com"),
    ("David Wilson", "david.wilson@email.com"),
    ("Eva Brown", "eva.brown@email.com"),
]


students = []
for name, email in students_data:
    student = Student(name=name, email=email)
    session.add(student)
    students.append(student)

session.commit()
print(f"{len(students)} students added.")

# Seed Courses
courses_data = [
    ("Introduction to Python", 3, "Learn the basics of Python programming"),
    ("Advanced SQL", 4, "Master SQL database operations"),
    ("Web Development", 3, "Build modern web applications"),
    ("Data Science Fundamentals", 4, "Introduction to data analysis and visualization"),
    ("Software Engineering", 3, "Best practices in software development")
]

courses = []
for title, credits, description in courses_data:
    course = Course(title=title, credits=credits, description=description)
    session.add(course)
    courses.append(course)

session.commit()
print(f"{len(courses)} courses added.")

# Seed Enrollments
enrollments_data = [
    (0, 0),  # Alice in Python
    (0, 2),  # Alice in Web Development
    (1, 1),  # Bob in SQL
    (1, 3),  # Bob in Data Science
    (2, 0),  # Carol in Python
    (2, 4),  # Carol in Software Engineering
    (3, 1),  # David in SQL
    (3, 2),  # David in Web Development
    (4, 3),  # Eva in Data Science
    (4, 4),  # Eva in Software Engineering
]

for student_id, course_id in enrollments_data:
    enrollment = Enrollment(student_id=students[student_id].id, course_id=courses[course_id].id)
    session.add(enrollment)

session.commit()
print(f"{len(enrollments_data)} enrollments added.")

# Close the session
session.close()
print("Database seeding completed successfully.")