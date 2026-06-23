from fastapi import FastAPI
app = FastAPI()

@app.get("/user/{user_id}")
def get_user(user_id):
    return {"user_id": user_id}

@app.get('/new_user/{user_id}')
def get_new_user(user_id:str):
    return {"new_user_id": user_id}