from lib.db.seed import seed_data
from lib.db.student import Student
from lib.db.course import Course
from lib.db.enrollment import Enrollment

def print_students():
    print(f"\n--- Students ---")
    for student in Student.get_all():
        print(f"  • {student}")

def print_courses():
    print(f"\n--- Courses ---")
    for course in Course.get_all():
        print(f"  • {course}")

def print_enrollments():
    print(f"\n--- Enrollments ---")
    for enrollment in Enrollment.get_all():
        print(f"  • {enrollment.student.name} → {enrollment.course.title}")

def run_debug():

    # Seed fresh data
    seed_data()

    print("\n Initial Data Seeded")
    print_students()
    print_courses()
    print_enrollments()

    # Testing Updates
    s1 = Student.find_by_id(1)
    c2 = Course.find_by_id(2)
    e3 = Enrollment.find_by_id(3)

    Student.update(s1.id, name="Alice Johnson", email="alice.j@example.com")
    Course.update(c2.id, credits=5, title="Advanced Physics")
    Enrollment.update(e3.id, course=Course.find_by_id(3)) # Bob now takes History instead of Math

    print("\n After Updates")
    print_students()
    print_courses()
    print_enrollments()

    # Testing Delete
    Student.delete(3) # Delete Charlie
    Course.delete(1) # Delete Mathematics
    Enrollment.delete(1) # Delete Alice's Math Enrollment

    print("\n After Deletes")
    print_students()
    print_courses()
    print_enrollments() 


if __name__ == "__main__":
    run_debug()
