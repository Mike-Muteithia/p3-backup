from sqlalchemy import Column, Integer, String, CheckConstraint
from sqlalchemy.orm import relationship, Session as OrmSession
from db.setup import Base
from datetime import datetime

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, nullable=False)

    enrollments = relationship("Enrollment", back_populates="student", cascade="all, delete-orphan")

    @property
    def courses(self):
        return [enrollment.course for enrollment in self.enrollments]
    
    def __repr__(self):
        return f"Student(id={self.id}, name='{self.name}', email='{self.email}')"
    
    # ---- ORM helper methods ----
    @classmethod
    def get_by_id(cls, session: OrmSession, id_: int):
        return session.get(cls, id_)
    
    @classmethod
    def get_all(cls, session: OrmSession):
        return session.query(cls).all()
    
    @classmethod
    def find_by_name(cls, session: OrmSession, name: str):
        return session.query(cls).filter(cls.name.ilike(f"%{name}%")).all()
    
    def delete(self, session: OrmSession):
        session.delete(self)
        session.commit()