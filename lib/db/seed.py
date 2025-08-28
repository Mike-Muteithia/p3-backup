from lib.db.student import Student
from lib.db.course import Course
from lib.db.enrollment import Enrollment

def seed_data():
    # Clear any old data (helps when re-runnung seed)
    Student._students.clear()
    Course._courses.clear()
    Enrollment._enrollments.clear()

    # Create Students
    s1 = Student.create("Alice", "alice@example.com")
    s2 = Student.create("Bob", "bob@example.com")
    s3 = Student.create("Charlie", "charlie@example.com")

    # Create Courses
    c1 = Course.create("Mathematics", 3)
    c2 = Course.create("Physics", 4)
    c3 = Course.create("History", 2)

    #Enrollments
    e1 = Enrollment.create(s1, c1)
    e2 = Enrollment.create(s1, c2)
    e3 = Enrollment.create(s2, c1)
    e4 = Enrollment.create(s3, c3)

    print("✅ Database seeded with sample data!")
    return s1, s2, s3, c1, c2, c3, e1, e2, e3, e4


if __name__ == "__main__":
    seed_data()
