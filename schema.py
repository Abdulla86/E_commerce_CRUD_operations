from pydantic import BaseModel

class ProductCreate(BaseModel):
    product_name: str
    category: str
    price: int
    stock: int = 0

class ProductResponse(ProductCreate):
    product_id: int

    model_config = {
        "from_attributes": True
    } 

