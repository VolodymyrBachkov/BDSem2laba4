from sqlalchemy import create_engine
from models import Base
from sqlalchemy.orm import sessionmaker
import os
import logging

# Create database directory if it doesn't exist
DATABASE_DIR = "database"
os.makedirs(DATABASE_DIR, exist_ok=True)

# Database path
DATABASE_PATH = os.path.join(DATABASE_DIR, "university.db")
DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

# Initialize the engine and session
def initialize_engine(logging_state:bool):
    if logging_state:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.disable(logging.CRITICAL)

    engine = create_engine(DATABASE_URL, echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Create tables
    Base.metadata.create_all(engine)
    
    return session
