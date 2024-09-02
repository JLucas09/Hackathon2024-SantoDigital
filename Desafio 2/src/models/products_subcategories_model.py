from sqlalchemy import Column, Integer, String
from database import Base


class ProductSubcategory(Base):
    __tablename__ = 'products_subcategories'

    productsubcategorykey = Column(Integer, primary_key=True)
    subcategoryname = Column(String(50))
    productcategorykey = Column(Integer)
