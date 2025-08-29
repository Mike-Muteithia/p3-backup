import json 
from lib.db.student import Student
from lib.db.course import Course
from lib.db.enrollment import Enrollment

DB_FILE = "db.json"

def save_to_file():
    data = {
        "students": [student.to_dict() for student in Student.get_all()],
        "courses": [course.to_dict() for course in Course.get_all()],
        "enrollments": [enrollment.to_dict() for enrollment in Enrollment.get_all()],
    }

    # Debug prints before saving
    print("\n Saving data to db.json...")
    print("Students:", data["students"])
    print("Courses:", data["courses"])
    print("Enrollments:", data["enrollments"])

    with open(DB_FILE, "w") as file:
        json.dump(data, file, indent=4)

    print("✅ Data successfully saved to db.json\n")
    return data

def load_from_file():
    try:
        with open(DB_FILE, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("\n db.json not found. Starting with empty database...")
        return {}

    # Debug prints after loading
    print("\n Loading data from db.json...")
    print("Students:", data["students"])
    print("Courses:", data["courses"])
    print("Enrollments:", data["enrollments"])

    # Clear existing in-memory data (important when reloading)
    Student._students = []
    Course._courses = []
    Enrollment._enrollments = []
    Student._id_counter = 1
    Course._id_counter = 1
    Enrollment._id_counter = 1

    # Rebuild students
    students_by_id = {}
    for student in data["students"]:
        student = Student.from_dict(student)
        students_by_id[student.id] = student

    # Rebuild courses
    courses_by_id = {}
    for course in data["courses"]:
        course = Course.from_dict(course)
        courses_by_id[course.id] = course

    # Rebuild enrollments
    for enrollment in data["enrollments"]:
        Enrollment.from_dict(enrollment, students_by_id, courses_by_id)

    print("✅ Data successfully loaded from db.json\n")
    return data