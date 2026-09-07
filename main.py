from fastapi import FastAPI, Depends
from models import Products
from db_config import session, engine
from sqlalchemy.orm import Session
import db_models

app = FastAPI()
db_models.Base.metadata.create_all(bind=engine)

products = [
    Products(id=1, name='phone', description='keypad', price=1200, quantity=3),
    Products(id=2, name='phone', description='smart', price=12000, quantity=31),
    Products(id=3, name='ipad', description='from apple', price=12000, quantity=41),
]

def init_db():
    db = session()
    # db.add_all([
    #     db_models.Product(name='phone', description='keypad', price=1200, quantity=3),
    #     db_models.Product(name='phone', description='smart', price=12000, quantity=31),
    #     db_models.Product(name='ipad', description='from apple', price=12000, quantity=41)
    # ])
    count= db.query(db_models.Product).count()
    if count==0:
        for product in products:
            db.add(db_models.Product(**(product.model_dump())))
            print("Database initialized with sample products.")
        db.commit()
    db.close()

init_db()

@app.get('/')
def greet():
    return "welcome to Fast API"

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

@app.get('/products')
def get_products(db: Session = Depends(get_db)):
    products = db.query(db_models.Product).all()
    return products

#dynamic routing
@app.get('/product/{id}')
def get_product(id: int, db: Session = Depends(get_db)):
    product = db.query(db_models.Product).filter(db_models.Product.id == id).first()
    return product

#post method
@app.post('/product')
def create_product(product: Products, db: Session = Depends(get_db)):
    id = product.id
    existing_product = db.query(db_models.Product).filter(db_models.Product.id == id).first()
    if existing_product:
        return "Product with this ID already exists."
    db.add(db_models.Product(**product.model_dump()))
    db.commit()
    return product

#post method
@app.put('/product/{id}')
def update_product(id: int, product: Products, db: Session = Depends(get_db)):
    db.query(db_models.Product).filter(db_models.Product.id == id).update(product.model_dump())
    db.commit()
    return "Product updated successfully"


#post method
@app.delete('/product/{id}')
def delete_product(id: int, db: Session = Depends(get_db)):
    product = db.query(db_models.Product).filter(db_models.Product.id == id).first()
    if product:
        db.delete(product)
        db.commit()
        return "Product deleted successfully"
    return "Product not found"