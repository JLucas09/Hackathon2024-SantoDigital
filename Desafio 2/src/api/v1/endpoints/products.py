from fastapi import APIRouter, status, HTTPException
from database import SessionLocal
from models.products_model import Product
from models.sales_model import Sale
from schemas.products_schema import ProductsRequest, ProductResponse
import logging


router = APIRouter()
session = SessionLocal()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ProductResponse)
def create_products(payload: ProductsRequest):
    try:
        updated_product = Product(**payload.model_dump())
        session.add(updated_product)
        session.commit()
        return updated_product
    except Exception as e:
        session.rollback()
        logging.error(f"Error creating the product {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.get("/", status_code=status.HTTP_200_OK)
def get_all_products():
    try:
        products = session.query(Product).all()
        return products
    except Exception as e:
        session.rollback()
        logging.error(f"Error getting the product {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=ProductResponse)
def get_one_product(id: int):
    try:
        product = session.query(Product).filter(Product.productkey == id).first()
        if product:
            return product
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found!")
    except Exception as e:
        session.rollback()
        logging.error(f"Error getting the product {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.put('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def update_product(id: int, payload: ProductsRequest):
    product = session.query(Product).filter(Product.productkey == id).first()
    try:
        if product:

            updated_product = Product(**payload.dict())

            product.productsubcategorykey  = updated_product.productsubcategorykey
            product.productsku = updated_product.productsku
            product.productname = updated_product.productname
            product.modelname = updated_product.modelname
            product.productdescription = updated_product.productdescription
            product.productcolor = updated_product.productcolor
            product.productsize = updated_product.productsize
            product.productstyle = updated_product.productstyle
            product.productcost = updated_product.productcost
            product.productprice = updated_product.productprice

            session.add(product)
            session.commit()
            return {'message': 'Product updated succesfully'}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product not found')
    except Exception as e:
        session.rollback()
        logging.error(f"Error updating the product {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_product(id: int):
    product = session.query(Product).filter(Product.productkey == id).first()
    try:
        if product:
            session.query(Sale).filter(Sale.productkey == id).delete()
            session.delete(product)
            session.commit()
            return {'message': 'Product deleted succesfully'}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product not found')
    except Exception as e:
        session.rollback()
        logging.error(f"Error deleting the product {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
