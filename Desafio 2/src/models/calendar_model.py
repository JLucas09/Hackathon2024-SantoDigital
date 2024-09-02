from sqlalchemy import Column, Date
from database import Base


class Calendar(Base):
    __tablename__ = 'calendar'
    date = Column(Date)
