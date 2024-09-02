from pydantic import BaseModel


class ProductsRequest(BaseModel):
    productname: str 
    productdescription: str
    productsize: str
    productcost: float
    modelname: str
    productsku: str
    productcolor: str
    productstyle: str
    productprice: float
    productsubcategorykey: int


class ProductResponse(BaseModel):
    productkey: int
    productname: str 
    productdescription: str
    productsize: str
    productcost: float
    modelname: str
    productsku: str
    productcolor: str
    productstyle: str
    productprice: float
    productsubcategorykey: int
