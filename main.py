from fastapi import FastAPI
from models import Products
from db_config import session, engine
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

@app.get('/products')
def get_products():
    return products

#dynamic routing
@app.get('/product/{id}')
def get_product(id: int):
    return products[id-1]


#post method
@app.post('/product')
def get_product(product: Products):
    db = session()
    db.query()
    products.append(product)
    return product

#post method
@app.put('/product')
def update_product(id:int, product: Products):
    for p_index in range(len(products)):
        if products[p_index].id==id:
            products[p_index]=product
            return "Added successfully"
    return "Id not found"


#post method
@app.delete('/product')
def get_product(id: int):
    for p_index in range(len(products)):
        if products[p_index].id==id:
            del products[p_index] #or popout
            return "deleted successfully"
    return "Id not found"