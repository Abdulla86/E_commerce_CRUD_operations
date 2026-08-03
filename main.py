from fastapi import FastAPI, Depends, HTTPException, Response, Request
from sqlalchemy.orm import Session
import CRUD
import schema
from database import Base, engine, SessionLocal
from auth import authorize_user

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def welcome():
    return "welcome to the Store"

@app.get("/products", response_model=list[schema.ProductResponse])
def get_all_products(request: Request, db: Session = Depends(get_db)):
    authorize_user(request, required_role=["admin"])  # Only admins can access this endpoint
    return CRUD.get_all_products(db)

@app.get("/products/{product_id}", response_model=schema.ProductResponse)
def get_product(product_id: int,request: Request, db: Session = Depends(get_db)):
    db_product = CRUD.get_product(db, product_id=product_id)
    authorize_user(request, required_role=["admin","worker"])  # Only workers can access this endpoint
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@app.put("/products/{product_id}", response_model=schema.ProductResponse)
def update_product(product_id: int, updated_product: schema.ProductCreate, request: Request, db: Session = Depends(get_db)):
    db_product = CRUD.update_product(db, product_id=product_id, updated_product=updated_product)
    authorize_user(request, required_role=["admin", "store manager"])  # Only admins and store managers can access this endpoint
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@app.delete("/products/{product_id}", response_model=schema.ProductResponse)
def delete_product(product_id: int, request: Request, db: Session = Depends(get_db)):
    db_product = CRUD.delete_product(db, product_id=product_id)
    authorize_user(request, required_role=["admin"])  # Only admins can access this endpoint
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@app.get("/category/{category}", response_model=list[schema.ProductResponse])
def get_products_by_category(category: str, request: Request, db: Session = Depends(get_db)):
    authorize_user(request, required_role=["worker","admin"])  # Only workers can access this endpoint
    return CRUD.get_products_by_category(db, category=category)

@app.post("/products", response_model=schema.ProductResponse)
def create_product(product: schema.ProductCreate, request: Request, db: Session = Depends(get_db)):
    authorize_user(request, required_role=["admin","store manager"])  # Only admins and store managers can access this endpoint
    return CRUD.create_product(db, product)

@app.post("/register_user")
def user_register(user: schema.UserCreate, db : Session = Depends(get_db)):
    return CRUD.user_register(db, user) # it is step is used to register the new user based given details

@app.post("/login_user")
def user_login(user: schema.Userlogin, db:Session = Depends(get_db), response: Response = None):
    return CRUD.user_login(db, user, response)