from pydantic import BaseModel


class Products(BaseModel):
    id: int 
    product: str
    discription: str
    price: float
    quantity: int

    