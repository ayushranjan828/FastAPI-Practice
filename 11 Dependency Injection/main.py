from fastapi import FastAPI, Depends, Header, HTTPException

app = FastAPI()

'''
def common_logic():
    return {
        "Message": "Common logic executed"
    }

@app.get("/home")
def home(data = Depends(common_logic)):
    return data
'''
def verify_token(token: str =  Header(None)):
    if token != "mysecrettoken":
        raise HTTPException(
            status_code=401, 
            detail="Invalid token"
            )
    
    return {
        "User": "Authorized User"
    }

@app.get("/secure-data")
def secure_data(user = Depends(verify_token)):
    return {
        "Message": "Secure data accessed",
        "User": user
    }



def get_current_user():
    return {
        "User": "Ayush"
    }

@app.get("/profile")
def profile(user = Depends(get_current_user)):
    return user

@app.get("/dashboard")
def dashboard(user = Depends(get_current_user)):
    return user