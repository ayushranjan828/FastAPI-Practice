from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return{
        "message": "Hello Ayush"
    }

@app.get("/add")
def add(a: int, b:int):
    return{
        "return": a+b
    }