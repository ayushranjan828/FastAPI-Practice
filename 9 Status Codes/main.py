from fastapi import FastAPI, status, HTTPException

app = FastAPI()

@app.post("/create_user", status_code = status.HTTP_201_CREATED)
def create_user(name: str):
    return {
        "Message": "User created successfully"
    }

@app.get("/user")
def get_user():
    return {
        "status": "Success",
        "Message": "User Fetched",
        "Data": {
            "name": "Ayush",
            "age": 21
        }
    }

@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id != 1:
        raise HTTPException(
            status_code = 404,
            detail = "User not found"
        )
    
    return {
        "id": 1,
        "name": "Ayush"
    }