from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Product(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String(255), nullable=False)
    category = Column(String(50), nullable=False)
    price = Column(Integer, nullable=False)
    stock = Column(Integer, default = 0)

class User(Base):
    __tablename__ = "users"

    user_name = Column(String(100), primary_key=True, index=True)
    email = Column(String(100), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    role = Column(String(100), nullable = False, default = "user")  # Default role is "user"
    is_active = Column(Boolean, default=False, nullable = False)  # False for inactive, True for active

   


