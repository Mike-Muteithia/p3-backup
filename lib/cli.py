from lib.db.student import Student
from lib.db.course import Course
from lib.db.enrollment import Enrollment
from lib.db.storage import save_to_file, load_from_file

def main_menu():

    load_from_file() # Load existing data

    while True:
        print("\n--- CourseFlow CLI ---")
        print("1. Manage Students")
        print("2. Manage Courses")
        print("3. Manage Enrollments")
        print("4. Exit")

        choice = input("Choose an option: \n").strip()

        if choice == "1":
            student_menu()
        elif choice == "2":
            course_menu()
        elif choice == "3":
            enrollment_menu()
        elif choice == "4":
            save_to_file() # Save before exiting
            print("Exiting CourseFlow CLI. Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

def student_menu():

    while True:
        print("\n--- Student Menu ---")
        print("1. Create Student")
        print("2. View All Students")
        print("3. Find Student by ID")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Back to Main Menu")

        choice = input("Choose an option: \n").strip()

        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            if not name or not email:
                print("Name and email cannot be empty.")
                continue
            Student.create(name, email)
            save_to_file()
            print("✅ Student created.")
        elif choice == "2":
            students = Student.get_all()
            if students:
                for student in students:
                    print(f"  • {student}")
            else:
                print("No students found.")
        elif choice == "3":
            try:
                studentid = int(input("Enter student ID: "))
            except ValueError:
                print("Please enter a number.")
                continue
            student = Student.find_by_id(studentid)
            print(student if student else "Not found.")
        elif choice == "4":
            try:
                studentid = int(input("Enter student ID to update: "))
            except ValueError:
                print("Invalid input. Please enter a numeric ID.")
                continue

            name = input("Enter new name (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")

            updated = Student.update(studentid, name=name or None, email=email or None)
            print("✅ Updated." if updated else " Student not found.")
            save_to_file()
        elif choice == "5":
            try:
                studentid = int(input("Enter student ID to delete: "))
            except ValueError:
                print("Please enter a number.")
                continue
            if Student.delete(studentid):
                print("✅ Student deleted.")
                save_to_file()
            else:
                print("Not found.")
        elif choice == "6":
            break
        else: 
            print("Invalid choice.")
            
def course_menu():

    while True:
        print("\n--- Course Menu ---")
        print("1. Create Course")
        print("2. View All Courses")
        print("3. Find Course by ID")
        print("4. Update Course")
        print("5. Delete Course")
        print("6. View Enrolled Students")
        print("7. Back to Main Menu")

        choice = input("Choose an option: \n").strip()

        if choice == "1":
            title = input("Enter course title: ")
            credits_input = input("Enter course credits: ").strip()
            if not title or not credits_input.isdigit() or int(credits_input) <= 0:
                print("Invalid title or credits (must be a positive number).")
                continue
            credits = int(credits_input)
            Course.create(title, credits)
            save_to_file()
            print("✅ Course created.")
        elif choice == "2":
            courses = Course.get_all()
            if courses:
                for course in courses:
                    print(f"  • {course}")
            else:
                print("No courses found.")
        elif choice == "3":
            try:
                courseid = int(input("Enter course ID: "))
            except ValueError:
                print("Please enter a number")
                continue
            course = Course.find_by_id(courseid)
            print(course if course else "Not found.")
        elif choice == "4":
            try:
                courseid = int(input("Enter course ID to update: "))
            except ValueError:
                print("Invalid input. Please enter a numeric ID.")
                continue

            title = input("Enter new title (leave blank to keep current): ")
            credits_input = input("Enter new credits (leave blank to keep current): ")
            credits = None
            if credits_input:
                if credits_input.isdigit():
                    credits = int(credits_input)
                else:
                    print("Credits must be a number.")
                    continue

            updated = Course.update(courseid, title=title or None, credits=credits)
            print("✅ Updated." if updated else "Not found.")
            save_to_file()
        elif choice == "5":
            try:
                courseid = int(input("Enter course ID to delete: "))
            except ValueError:
                print("Please enter a number.")
                continue
            if Course.delete(courseid):
                print("✅ Course deleted.")
                save_to_file()
            else:
                print("Not found.")
        elif choice == "6":
            try:
                courseid = int(input("Enter course ID to view students: "))
            except ValueError:
                print("Please enter a number.")
                continue
            course = Course.find_by_id(courseid)
            if course:
                enrollments = [enrollment for enrollment in Enrollment.get_all() if enrollment.course.id == course.id]
                if enrollments:
                    print(f"Students enrolled in {course.title}:")
                    for enrollment in enrollments:
                        print(f"  • {enrollment.student}")
                else:
                    print("No students enrolled in this course.")
            else:
                print("Course not found.")
        elif choice == "7":
            break
        else: 
            print("Invalid choice.")

def enrollment_menu():
    
    while True:
        print("\n--- Enrollment Menu ---")
        print("1. Create Enrollment")
        print("2. View All Enrollments")
        print("3. Find Enrollment by ID")
        print("4. Delete Enrollment")
        print("5. Back to Main Menu")

        choice = input("Choose an option: \n").strip()

        if choice == "1":
            # Show students
            print("\nStudents:")
            students = Student.get_all()
            if not students:
                print("No students available. Create students first.")
                continue
            for student in students:
                print(f"  {student.id}: {student.name}")

            try:
                studentid = int(input("Enter student ID to enroll: "))
            except ValueError:
                print("IDs must be numbers.")
                continue
            student = Student.find_by_id(studentid)

            # Show courses
            print("\nCourses:")
            courses = Course.get_all()
            if not courses:
                print("No courses available. Create courses first.")
                continue
            for course in courses:
                print(f"  {course.id}: {course.title}")

            try:
                courseid = int(input("Enter course ID to enroll: "))
            except ValueError:
                print("IDs must be numbers.")
                continue
            course = Course.find_by_id(courseid)

            if student and course:
                Enrollment.create(student, course)
                save_to_file()
                print("✅ Enrollment created.")
            else:
                print("Invalid student or course ID.")
        elif choice == "2":
            enrollments = Enrollment.get_all()
            if enrollments:
                for enrollment in enrollments:
                    print(f"  • {enrollment}")
            else:
                print("No enrollments found.")
        elif choice == "3":
            try:
                enrollmentid = int(input("Enter enrollment ID: "))
            except ValueError:
                print("Please enter a number.")
                continue
            enrollment = Enrollment.find_by_id(enrollmentid)
            print(enrollment if enrollment else "Not found.")
        elif choice == "4":
            try:
                enrollmentid = int(input("Enter enrollment ID to delete: "))
            except ValueError:
                print("Please enter a number.")
                continue
            if Enrollment.delete(enrollmentid):
                print("✅ Enrollment deleted.")
                save_to_file()
            else:
                print("Not found.")
        elif choice == "5":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main_menu()
    