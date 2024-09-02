from sqlalchemy import Column, Integer, String, Date
from database import Base


class Sale(Base):
    __tablename__ = 'sales'

    salesid = Column(Integer, primary_key=True)
    orderdate = Column(Date)
    stockdate = Column(Date)
    ordernumber = Column(String(10))
    productkey = Column(Integer)
    customerkey = Column(Integer)
    territorykey = Column(Integer)
    orderlineitem = Column(Integer)
    orderquantity = Column(Integer)
