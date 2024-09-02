from sqlalchemy import Column, Integer, Date
from database import Base


class Return(Base):
    __tablename__ = 'returns'

    returnid = Column(Integer, primary_key=True)
    returndate = Column(Date)
    territorykey = Column(Integer)
    productkey = Column(Integer)
    returnquantity = Column(Integer)
