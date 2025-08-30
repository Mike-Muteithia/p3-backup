from sqlalchemy import Column, Integer, String, CheckConstraint
from sqlalchemy.orm import relationship, Session as OrmSession
from db.setup import Base
from datetime import datetime

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False, unique=True)
    credits = Column(Integer, nullable=False)
    description = Column(String(500))

    enrollments = relationship("Enrollment", back_populates="course", cascade="all, delete-orphan")

    @property
    def enrolled_students(self):
        return [enrollment.student for enrollment in self.enrollments]
    
    def __repr__(self):
        return f"Course(id={self.id}, title='{self.title}', credits={self.credits})"
    

    # ---- ORM helper methods ----
    @classmethod
    def create(cls, session: OrmSession, title: str, credits: int, description: str = ""):
        instance = cls(title=title, credits=credits, description=description)
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
    
    @classmethod
    def find_by_title(cls, session: OrmSession, title: str):
        return session.query(cls).filter(cls.title.ilike(f"%{title}%")).all()
    
    def delete(self, session: OrmSession):
        session.delete(self)
        session.commit()

