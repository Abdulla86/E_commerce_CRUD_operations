from sqlalchemy import Column, Integer, String
from database import Base

class Product(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String(255), nullable=False)
    category = Column(String(50), nullable=False)
    price = Column(Integer, nullable=False)
    stock = Column(Integer, default = 0)


