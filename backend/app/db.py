import os
from sqlalchemy import create_engine, Column, Integer, String, Text, Boolean, DateTime,func
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime
from dotenv import load_dotenv
# Load .env file
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set. Please check your .env file.")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

# ✅ Define a table model for queries
class Query(Base):
    __tablename__ = "queries"

    id = Column(Integer, primary_key=True, index=True)
    message = Column(Text, nullable=False)
    reply = Column(Text, nullable=True)
    crop = Column(String(50), nullable=True)
    city = Column(String(50), nullable=True)  # new
    created_at = Column(DateTime, default=datetime.utcnow)  # new
    escalated = Column(Boolean, default=False)  # new

class Farmer(Base):
    __tablename__ = "farmers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    phone = Column(String(15), unique=True, nullable=False)
    password = Column(String(255), nullable=False)  # store hashed password
    location = Column(String(100), nullable=True)
    crops = Column(String(200), nullable=True)

class Scheme(Base):
    __tablename__ = "schemes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    benefit = Column(String, nullable=True)
    state = Column(String, nullable=True)        # None for central schemes
    scheme_type = Column(String, nullable=False) # "Central" or "State"
    apply_link = Column(String, nullable=True)   # URL to apply


def init_db():
    # Create tables if they don't exist
    Base.metadata.create_all(bind=engine)
