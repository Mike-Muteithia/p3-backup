from lib.db.student import Student
from lib.db.course import Course
from lib.db.enrollment import Enrollment
from lib.db.storage import save_to_file

def seed_data():
    # Clear any old data (helps when re-runnung seed)
    Student._students.clear()
    Course._courses.clear()
    Enrollment._enrollments.clear()
    
    # Create Students
    s1 = Student.create("Alice", "alice@example.com")
    s2 = Student.create("Bob", "bob@example.com")

    # Create Courses
    c1 = Course.create("Math 101", 3)
    c2 = Course.create("History 201", 4)

    #Enrollments
    Enrollment.create(s1, c1)
    Enrollment.create(s2, c2)
    Enrollment.create(s1, c2)

    # Debug prints before saving
    print(f"\n Students:")
    for student in Student.get_all():
        print(student.to_dict())

    print(f"\n Courses:")
    for course in Course.get_all():
        print(course.to_dict())

    print(f"\n Enrollments:")
    for enrollment in Enrollment.get_all():
        print(enrollment.to_dict())

    # Save everything to db.json
    save_to_file()
    print("\n✅ Seed data created and saved to db.json")


if __name__ == "__main__":
    seed_data()
    
