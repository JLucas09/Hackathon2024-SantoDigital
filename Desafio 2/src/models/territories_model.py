from sqlalchemy import Column, Integer, String
from database import Base


class Territory(Base):
    __tablename__ = 'territories'

    salesterritorykey = Column(Integer, primary_key=True)
    region = Column(String(50))
    country = Column(String(50))
    continent = Column(String(50))
