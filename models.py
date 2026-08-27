class Products:
    id: int 
    product: str
    discription: str
    price: float
    quantity: int

    def __init__(self, id: int, product: str, discription:str, price: float, quantity: int):
        self.id = id
        self.product = product
        self.discription = discription
        self.price = price
        self.quantity = quantity
    