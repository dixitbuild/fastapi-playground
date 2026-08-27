from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def greet():
    return "welcome to Fast API"


@app.get('/product')
def product():
    return "welcome to Fast API Products"

