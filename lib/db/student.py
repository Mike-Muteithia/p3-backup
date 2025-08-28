
class Student:

    _students = []

    def __init__(self, name, email):
        self.id = len(Student._students) + 1
        self.name = name
        self.email = email
        Student._students.append(self)

    @property
    def enrollments(self):
        from lib.db.enrollment import Enrollment
        return [enrollment for enrollment in Enrollment._enrollments if enrollment.student == self]
    
    @property
    def courses(self):
        from lib.db.enrollment import Enrollment
        return [enrollment.course for enrollment in self.enrollments]

    # CRUD METHODS
    @classmethod
    def create(cls, name, email):
        return cls(name, email)
    
    @classmethod
    def get_all(cls):
        return cls._students
    
    @classmethod
    def find_by_id(cls, student_id):
        for student in cls._students:
            if student.id == student_id:
                return student
        return None
    
    @classmethod
    def delete(cls, student_id):
        student = cls.find_by_id(student_id)
        if student:
            cls._students.remove(student)
            return True
        return False
    
    @classmethod
    def update(cls, student_id, name=None, email=None):
        student = cls.find_by_id(student_id)
        if student:
            if name:
                student.name = name
            if email:
                student.email = email
            return student
        return None

    def __repr__(self):
        return f"{self.name} ({self.email})"
