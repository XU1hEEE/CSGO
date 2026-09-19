
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Replace with your MySQL database connection information
DATABASE_URL = "mysql+mysqlconnector://user:password@localhost/csgo_market"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
