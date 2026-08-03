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

class UserCreate(BaseModel):
    user_name : str
    email: str
    password: str
    # is_admin : bool
    # is_active : bool

class Userlogin(BaseModel):
    email: str
    password: str

class UserResponse(UserCreate):
    user_name: str
    email: str
    role: str
    is_active: bool
    model_config = {
        "from_attributes": True
    }