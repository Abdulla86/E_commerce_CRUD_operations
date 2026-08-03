from sqlalchemy.orm import Session
from model import Product, User
import schema
import bcrypt
from fastapi import HTTPException, Response
import jwt
SECRET_KEY="abcdefghijklmnopqrtuvwxyz"
ALGORITHM="HS256"

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



def user_register(db: Session, user: schema.UserCreate): #validate the iputs that are come from the user and then store the data in the database

    salt = bcrypt.gensalt()   #it is used to generate the salt for the password hashing

    hashed_password = bcrypt.hashpw(   #hashpw is used to hash the password with the salt and then decode it
      user.password.encode("utf-8"),
        salt
    ).decode("utf-8")

    db_user = User(   # in this instatntiation of the User class sqlalchemy recognizes that is base class metadata and create python object and ORM create python objects for columns 
        user_name=user.user_name,
        email=user.email,
        hashed_password=hashed_password
    )

    db.add(db_user)   #it is used to add the new user instance object to the database
    db.commit()
    db.refresh(db_user)

    return db_user

def user_login(db: Session , user: schema.Userlogin, response: Response):
    user_exist = db.query(User).filter(User.email == user.email).first()
    is_same =  bcrypt.checkpw(user.password.encode(),user_exist.hashed_password.encode())
    if is_same:
        payload = {
            "user_name": user_exist.user_name,
            "email": user_exist.email,
            "role": user_exist.role
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
        response.set_cookie(key="access_token",value=token)
        return "login successful!"
    return "Invalid password"
    
    