from db.setup import engine
from sqlalchemy import inspect

def inspect_database():
    inspector = inspect(engine)
    tables = inspector.get_table_names()

    if tables:
        print("✅ Database tables found:")
        for table in tables:
            print(f" - {table}")
    else:
        print("❌ No tables found in the database. You may need to run Base.metadata.create_all(engine) to create them.")

if __name__ == "__main__":
    inspect_database()