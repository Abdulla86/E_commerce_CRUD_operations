from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import CRUD
import schema
from database import Base, engine, SessionLocal

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

@app.get("/products/{product_id}", response_model=schema.ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    db_product = CRUD.get_product(db, product_id=product_id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@app.get("/products", response_model=list[schema.ProductResponse])
def get_all_products(db: Session = Depends(get_db)):
    return CRUD.get_all_products(db)

@app.put("/products/{product_id}", response_model=schema.ProductResponse)
def update_product(product_id: int, updated_product: schema.ProductCreate, db: Session = Depends(get_db)):
    db_product = CRUD.update_product(db, product_id=product_id, updated_product=updated_product)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@app.delete("/products/{product_id}", response_model=schema.ProductResponse)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = CRUD.delete_product(db, product_id=product_id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@app.get("/category/{category}", response_model=list[schema.ProductResponse])
def get_products_by_category(category: str, db: Session = Depends(get_db)):
    return CRUD.get_products_by_category(db, category=category)

@app.post("/products", response_model=schema.ProductResponse)
def create_product(product: schema.ProductCreate, db: Session = Depends(get_db)):
    return CRUD.create_product(db, product)