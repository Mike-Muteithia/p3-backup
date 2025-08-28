
class Course: 

    _courses = []

    def __init__(self, title, credits):
        self.id = len(Course._courses) + 1
        self.title = title
        self.credits = credits
        Course._courses.append(self)

    @property
    def enrollments(self):
        from lib.db.enrollment import Enrollment
        return [enrollment for enrollment in Enrollment._enrollments if enrollment.course == self]
    
    @property
    def students(self):
        from lib.db.enrollment import Enrollment
        return [enrollment.student for enrollment in self.enrollments]

    # CRUD METHODS
    @classmethod
    def create(cls, title, credits):
        return cls(title, credits)
    
    @classmethod
    def get_all(cls):
        return cls._courses
    
    @classmethod
    def find_by_id(cls, course_id):
        for course in cls._courses:
            if course.id == course_id:
                return course
        return None
    
    @classmethod
    def delete(cls, course_id):
        course = cls.find_by_id(course_id)
        if course:
            cls._courses.remove(course)
            return True
        return False
    
    @classmethod
    def update(cls, course_id, title=None, credits=None):
        course = cls.find_by_id(course_id)
        if course:
            if title:
                course.title = title
            if credits is not None:
                course.credits = credits
            return course
        return None

    def __repr__(self):
        return f"{self.title} [{self.credits} credits]>"
