from fastapi import FastAPI
from models import Products

app = FastAPI()

@app.get('/')
def greet():
    return "welcome to Fast API"

product = [
    Products(id=1, product='phone', discription='keypad', price=1200, quantity=3),
    Products(id=2, product='phone', discription='smart', price=12000, quantity=31),
    Products(id=3, product='ipad', discription='from apple', price=12000, quantity=41),
]
@app.get('/products')
def get_products():
    return product

#dynamic routing
@app.get('/product/{id}')
def get_product(id: int):
    return product[id-1]