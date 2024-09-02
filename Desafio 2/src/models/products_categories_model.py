from sqlalchemy import Column, Integer, String
from database import Base


class ProductCategory(Base):
    __tablename__ = 'products_categories'

    productcategorykey = Column(Integer, primary_key=True)
    categoryname = Column(String(50))
