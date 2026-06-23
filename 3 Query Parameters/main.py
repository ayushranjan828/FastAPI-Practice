from fastapi import FastAPI
app = FastAPI()

@app.get("/users")
def get_users(name: str = None):
    return {"name": name}     

@app.get("/products")
def get_users(limit: int = 10):
    return {"limit": limit}

@app.get("/items")
def get_items(name: str = None, price: int = 0):
    return {
        "name" : name,
        "price" : price
    }