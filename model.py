from sqlalchemy import Column, Numeric, String, Integer, Boolean, Float, Date

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)


class Shower(Base):
    __tablename__ = "meteor_shower" 

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    observation_start_date = Column(Date, nullable=False)  # First day of observation
    observation_end_date = Column(Date, nullable=False)  # Last day of observation
    alpha = Column(Integer, nullable=False)
    beta = Column(Integer, nullable=False) 
    pick_date = Column(Date, nullable=False)
