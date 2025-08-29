from lib.db.student import Student
from lib.db.course import Course

class Enrollment: 

    _enrollments = []
    _id_counter = 1

    def __init__(self, student, course):
        if not isinstance(student, Student):
            raise ValueError("Invalid student provided")
        if not isinstance(course, Course):
            raise ValueError("Invalid course provided")

        self.id = Enrollment._id_counter
        Enrollment._id_counter += 1
        self.student = student
        self.course = course
        Enrollment._enrollments.append(self)

    # CRUD METHODS
    @classmethod
    def create(cls, student, course):
        for enrollment in cls._enrollments:
            if enrollment.student.id == student.id and enrollment.course.id == course.id:
                print(f"Student {student.name} is already enrolled in {course.title}.")
                return None

        return cls(student, course)
    
    @classmethod
    def get_all(cls):
        return cls._enrollments
    
    @classmethod
    def find_by_id(cls, enrollment_id):
        for enrollment in cls._enrollments:
            if enrollment.id == enrollment_id:
                return enrollment
        return None
    
    @classmethod
    def delete(cls, enrollment_id):
        enrollment = cls.find_by_id(enrollment_id)
        if enrollment:
            cls._enrollments.remove(enrollment)
            return True
        return False
    
    @classmethod
    def update(cls, enrollment_id, student=None, course=None):
        enrollment = cls.find_by_id(enrollment_id)
        if enrollment:
            if student:
                if not isinstance(student, Student):
                    raise ValueError("Invalid student provided")
                enrollment.student = student
            if course:
                if not isinstance(course, Course):
                    raise ValueError("Invalid course provided")
                enrollment.course = course
            return enrollment
        return None

    def __repr__(self):
        return f"{self.student.name} → {self.course.title}"
    
    # Serialization
    def to_dict(self):
        return {
            "id": self.id,
            "student_id": self.student.id,
            "course_id": self.course.id 
        }
    
    # Deserialization
    @classmethod
    def from_dict(cls, data, students_by_id, courses_by_id):
        student = students_by_id.get(data["student_id"])
        course = courses_by_id.get(data["course_id"])
        if not student or not course:
            print(f"Skipping enrollment {data['id']} due to missing student or course.")
            return None
        enrollment = cls.__new__(cls)
        enrollment.id = data["id"]
        enrollment.student = student
        enrollment.course = course
        cls._enrollments.append(enrollment)
        if enrollment.id >= cls._id_counter:
            cls._id_counter = enrollment.id + 1
        return enrollment
