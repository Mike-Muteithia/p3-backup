from lib.db.student import Student
from lib.db.course import Course

class Enrollment: 

    _enrollments = []

    def __init__(self, student, course):
        if not isinstance(student, Student):
            raise ValueError("Invalid student provided")
        if not isinstance(course, Course):
            raise ValueError("Invalid course provided")

        self.id = len(Enrollment._enrollments) + 1
        self.student = student
        self.course = course
        Enrollment._enrollments.append(self)

    # CRUD METHODS
    @classmethod
    def create(cls, student, course):
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
