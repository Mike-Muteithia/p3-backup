import click
from sqlalchemy.exc import SQLAlchemyError
from db.setup import SessionLocal as Session
from models.student import Student
from models.course import Course
from models.enrollment import Enrollment
from tabulate import tabulate


# Helper functions
def _print_table(rows, headers):
    click.echo(tabulate(rows, headers=headers, tablefmt="fancy_grid"))
    

## CLI Group
@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        click.echo("\nWelcome to CourseFlow CLI!")
        while True:
            click.echo("\nSelect an option:")
            options = [
                "Students",
                "Courses",
                "Enrollments",
                "Exit"
            ]
            for i, label in enumerate(options, start=1):
                click.echo(f"{i}. {label}")
            choice = click.prompt("Enter choice number", type=int)
            if choice == 1:
                _students_menu()
            elif choice == 2:
                _courses_menu()
            elif choice == 3:
                _enrollments_menu()
            elif choice == 4:
                click.echo("Goodbye!")
                break
            else:
                click.echo("Invalid choice.")


## Students Menu
def _students_menu():
    session = Session()
    try:
        while True:
            click.echo("\nStudents Menu:")
            click.echo("1. List all students")
            click.echo("2. Create student")
            click.echo("3. Delete student")
            click.echo("4. View enrolled courses")
            click.echo("5. Back to main menu")
            action = click.prompt("Enter choice number", type=int)

            if action == 1:
                students = session.query(Student).all()
                if not students:
                    click.echo("No students found.")
                    continue
                rows = [[student.id, student.name, student.email] for student in students]
                _print_table(rows, headers=["ID", "Name", "Email"])

            elif action == 2:
                name = click.prompt("Enter student name")
                email = click.prompt("Enter student email")
                student = Student(name=name, email=email)
                session.add(student)
                session.commit()
                click.echo(f"Student '{name}' added.")

            elif action == 3:
                # List students
                students = session.query(Student).all()
                if not students:
                    click.echo("No students found.")
                    continue
                rows = [[student.id, student.name, student.email] for student in students]
                _print_table(rows, ["ID", "Name", "Email"])

                # Prompt for student ID to delete
                student_id = click.prompt("Enter student ID to delete", type=int)
                student = session.get(Student, student_id)
                if not student:
                    click.echo("Student not found.")
                    continue
                session.delete(student)
                session.commit()
                click.echo(f"Student '{student.name}' deleted.")

            elif action == 4:
                # List students
                students = session.query(Student).all()
                if not students:
                    click.echo("No students found.")
                    continue
                rows = [[student.id, student.name, student.email] for student in students]
                _print_table(rows, ["ID", "Name", "Email"])

                # Prompt for student ID to view courses
                student_id = click.prompt("Enter student ID to view courses", type=int)
                student = session.get(Student, student_id)
                if not student:
                    click.echo("Student not found.")
                    continue
                if not student.courses:
                    click.echo("Student is not enrolled in any courses.")
                    continue
                rows = [[course.id, course.title, course.credits] for course in student.courses]
                _print_table(rows, ["Course ID", "Title", "Credits"])

            elif action == 5:
                break

            else:
                click.echo("Invalid choice.")

    except SQLAlchemyError as e:
        session.rollback()
        click.echo(f"Database error: {e}")
    finally:
        session.close()


## Courses Menu
def _courses_menu():
    session = Session()
    try:
        while True:
            click.echo("\nCourses Menu:")
            click.echo("1. List all courses")
            click.echo("2. Create course")
            click.echo("3. Delete course")
            click.echo("4. View enrolled students")
            click.echo("5. Back to main menu")
            action = click.prompt("Enter choice number", type=int)

            if action == 1:
                courses = session.query(Course).all()
                if not courses:
                    click.echo("No courses found.")
                    continue
                rows = [[course.id, course.title, course.credits] for course in courses]
                _print_table(rows, ["ID", "Title", "Credits"])

            elif action == 2:
                title = click.prompt("Enter course title")
                credits = click.prompt("Enter course credits", type=int)
                course = Course(title=title, credits=credits)
                session.add(course)
                session.commit()
                click.echo(f"Course '{title}' added.")

            elif action == 3:
                # List courses
                courses = session.query(Course).all()
                if not courses:
                    click.echo("No courses found.")
                    continue
                rows = [[course.id, course.title, course.credits] for course in courses]
                _print_table(rows, ["ID", "Title", "Credits"])

                # Prompt for course ID to delete
                course_id = click.prompt("Enter course ID to delete", type=int)
                course = session.get(Course, course_id)
                if not course:
                    click.echo("Course not found.")
                    continue
                session.delete(course)
                session.commit()
                click.echo(f"Course '{course.title}' deleted.")
            
            elif action == 4:
                # List courses
                courses = session.query(Course).all()
                if not courses:
                    click.echo("No courses found.")
                    continue
                rows = [[course.id, course.title, course.credits] for course in courses]
                _print_table(rows, ["ID", "Title", "Credits"])

                # Prompt for course ID to view students
                course_id = click.prompt("Enter course ID to view students", type=int)
                course = session.get(Course, course_id)
                if not course:
                    click.echo("Course not found.")
                    continue
                if not course.enrolled_students:
                    click.echo(f"No students enrolled in '{course.title}'.")
                    continue
                rows = [[student.id, student.name, student.email] for student in course.enrolled_students]
                _print_table(rows, ["Student ID", "Name", "Email"])

            elif action == 5:
                break

            else:
                click.echo("Invalid choice.")

    except SQLAlchemyError as e:
        session.rollback()
        click.echo(f"Database error: {e}")
    finally:
        session.close()


## Enrollments Menu
def _enrollments_menu():
    session = Session()
    try:
        while True:
            click.echo("\nEnrollments Menu:")
            click.echo("1. List all enrollments")
            click.echo("2. Enroll student in course")
            click.echo("3. Remove enrollment")
            click.echo("4. Back to main menu")
            action = click.prompt("Enter choice number", type=int)

            if action == 1:
                enrollments = session.query(Enrollment).all()
                if not enrollments:
                    click.echo("No enrollments found.")
                    continue
                rows = [[enrollment.id, enrollment.student.name, enrollment.course.title] for enrollment in enrollments]
                _print_table(rows, ["Enrollment ID", "Student", "Course"])

            elif action == 2:
                # Show students
                students = session.query(Student).all()
                if not students:
                    click.echo("No students found. Please create a student first.")
                    continue
                rows = [[student.id, student.name, student.email] for student in students]
                _print_table(rows, ["ID", "Name", "Email"])

                student_id = click.prompt("Enter student ID to enroll", type=int)
                student = session.get(Student, student_id)
                if not student:
                    click.echo("Invalid student ID.")
                    continue

                # Show courses
                courses = session.query(Course).all()
                if not courses:
                    click.echo("No courses found. Please create a course first.")
                    continue
                rows = [[course.id, course.title, course.credits] for course in courses]
                _print_table(rows, ["ID", "Title", "Credits"])

                course_id = click.prompt("Enter course ID to enroll in", type=int)
                course = session.get(Course, course_id)
                if not course:
                    click.echo("Invalid course ID.")
                    continue

                # Create enrollment
                enrollment = Enrollment(student_id=student_id, course_id=course_id)
                session.add(enrollment)
                session.commit()
                click.echo(f"Enrolled '{student.name}' in '{course.title}'.")

            elif action == 3:
                # List enrollments
                enrollments = session.query(Enrollment).all()
                if not enrollments:
                    click.echo("No enrollments found.")
                    continue
                rows = [[enrollment.id, enrollment.student.name, enrollment.course.title] for enrollment in enrollments]
                _print_table(rows, ["Enrollment ID", "Student", "Course"])

                # Prompt for enrollment ID to remove
                enrollment_id = click.prompt("Enter enrollment ID to remove", type=int)
                enrollment = session.get(Enrollment, enrollment_id)
                if not enrollment:
                    click.echo("Enrollment not found.")
                    continue
                session.delete(enrollment)
                session.commit()
                click.echo("Enrollment removed.")

            elif action == 4:
                break

            else:
                click.echo("Invalid choice.")

    except SQLAlchemyError as e:
        session.rollback()
        click.echo(f"Database error: {e}")
    finally:
        session.close()

