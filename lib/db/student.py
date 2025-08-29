
class Student:

    _students = []
    _id_counter = 1

    def __init__(self, name, email):
        self.id = Student._id_counter
        Student._id_counter += 1
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
        for student in cls._students:
            if student.email.lower() == email.lower():
                print(f"Student with email {email} already exists!")
                return None
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
    
    # Serialization
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }
    
    # Deserialization
    @classmethod
    def from_dict(cls, data):
        student = cls.__new__(cls)
        student.id = data["id"]
        student.name = data["name"]
        student.email = data["email"]
        cls._students.append(student)
        if student.id >= cls._id_counter:
            cls._id_counter = student.id + 1
        return student