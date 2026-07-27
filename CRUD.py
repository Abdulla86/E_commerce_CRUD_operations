from sqlalchemy.orm import Session
from model import Product
import schema

def create_product(db: Session, product: schema.ProductCreate):
    db_product = Product(
        product_name=product.product_name,
        category=product.category,
        price=product.price,
        stock=product.stock
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product
def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.product_id == product_id).first()
def get_all_products(db: Session):
    return db.query(Product).all()
def get_products_by_category(db: Session, category: str):
    return db.query(Product).filter(Product.category == category).all()
def update_product(db: Session, product_id: int, updated_product: schema.ProductCreate):
    db_product = db.query(Product).filter(Product.product_id == product_id).first()
    if db_product:
        db_product.product_name = updated_product.product_name
        db_product.category = updated_product.category
        db_product.price = updated_product.price
        db_product.stock = updated_product.stock
        db.commit()
        db.refresh(db_product)
    return db_product
def delete_product(db: Session, product_id: int):
    db_product = db.query(Product).filter(Product.product_id == product_id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
    return db_product