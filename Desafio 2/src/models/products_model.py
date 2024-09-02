from sqlalchemy import Column, Integer, String, Float
from database import Base


class Product(Base):
    __tablename__ = 'products'

    productkey = Column(Integer, primary_key=True)
    productsku = Column(String(50))
    productname = Column(String(100))
    modelname = Column(String(50))
    productdescription = Column(String(500))
    productcolor = Column(String(50))
    productsize = Column(String(2))
    productstyle = Column(String(2))
    productcost = Column(Float)
    productprice = Column(Float)
    productsubcategorykey = Column(Integer)
