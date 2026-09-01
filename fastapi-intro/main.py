from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

products_db = []

class Product(BaseModel):
    id: int
    name: str
    price: float
    available: bool = True

@app.post("/products")
def create_products(product: Product):
    products_db.append(product)
    return product


@app.get("/products")
def list_products():
    return products_db

@app.get("/products/{product_id}")
def show_product(product_id: int):
    for product in products_db:
        if product.id == product_id:
            return product

@app.put("/products/{product_id}")
def edit_product(product_id: int, updated_product: Product):
    for product in products_db:
        if product.id == product_id:
            product.name = updated_product.name
            product.price = updated_product.price
            product.available = updated_product.available
            return product

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for product in products_db:
        if product.id == product_id:
            products_db.remove(product)
            return {"detail": "product removed"}

 