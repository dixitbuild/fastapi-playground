from fastapi import FastAPI
from models import Products

app = FastAPI()

@app.get('/')
def greet():
    return "welcome to Fast API"

product = [
    Products(1, 'phone', 'keypad', 1200, 3),
    Products(2, 'phone', 'smart', 12000, 31)
]
@app.get('/products')
def get_products():
    return product
