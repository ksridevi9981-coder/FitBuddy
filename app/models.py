from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(100), unique=True, index=True, nullable=False)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    weight = Column(String(50), nullable=False)
    goal = Column(String(100), nullable=False)
    intensity = Column(String(50), nullable=False)

    original_plan = Column(Text, nullable=False)
    updated_plan = Column(Text, nullable=True)
    feedback = Column(Text, nullable=True)
    nutrition_tip = Column(Text, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )
