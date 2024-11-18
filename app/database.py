from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# PostgreSQL connection URL format: 
# postgresql://<username>:<password>@<host>/<database>


DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://doradino:Victoryuche*7@localhost/doradino_db")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
