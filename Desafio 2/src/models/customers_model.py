from sqlalchemy import Column, Integer, String, Date, Float
from database import Base


class Customer(Base):
    __tablename__ = 'customers'

    customerkey = Column(Integer, primary_key=True)
    prefix = Column(String(5))
    firstname = Column(String(50))
    lastName = Column(String(50))
    birthdate = Column(Date)
    maritalstatus = Column(String(2))
    gender = Column(String(2))
    emailaddress = Column(String(100))
    annualincome = Column(Float)
    totalchildren = Column(Integer)
    educationlevel = Column(String(50))
    occupation = Column(String(50))
    homeowner = Column(String(2))
