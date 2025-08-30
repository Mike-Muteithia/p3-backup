from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Session as OrmSession
from db.setup import Base
from datetime import datetime

class Enrollment(Base):
    __tablename__ = 'enrollments'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)

    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")

    def __repr__(self):
        return f"Enrollment(id={self.id}, student_id={self.student_id}, course_id={self.course_id})"
    
    # ---- ORM helper methods ----
    @classmethod
    def create(cls, session: OrmSession, student_id: int, course_id: int):
        instance = cls(student_id=student_id, course_id=course_id)
        session.add(instance)
        session.commit()
        session.refresh(instance)
        return instance
    
    @classmethod
    def get_by_id(cls, session: OrmSession, id_: int):
        return session.get(cls, id_)
    
    @classmethod
    def get_all(cls, session: OrmSession):
        return session.query(cls).all()
    
    def delete(self, session: OrmSession):
        session.delete(self)
        session.commit()
