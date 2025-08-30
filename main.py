import logging

# Disable SQLAlchemy logging to avoid cluttering the output
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.CRITICAL)


from cli.interface import cli
from db.setup import Base, engine

if __name__ == "__main__":
    # Create all tables if they don't exist
    Base.metadata.create_all(engine)

    # Launch the CLI
    cli()
