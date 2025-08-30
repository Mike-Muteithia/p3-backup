
from .lib.db.setup import Base, engine
from .lib.db.models import Student, Course, Enrollment

# This will create all tables in the database
print("Creating database tables...")
Base.metadata.create_all(bind=engine)
print("Database tables created successfully.")


