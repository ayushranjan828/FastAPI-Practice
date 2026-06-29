from fastapi import FastAPI, HTTPException, Depends
from jose import jwt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone

# Create FastAPI application instance
app = FastAPI()

# JWT Configuration
SECRET_KEY = "mysecret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Password hashing configuration using bcrypt
pwd_context = CryptContext(schemes=["bcrypt"])

# OAuth2 scheme for extracting Bearer token from requests
oauth_schema = OAuth2PasswordBearer(tokenUrl="login")

# Dummy user database
fake_user_db = {
    "admin": {
        "username": "admin",
        "hashed_password": pwd_context.hash("1234")
    }
}

# Function to hash a plain-text password
def hash_password(password: str):
    return pwd_context.hash(password)

# Function to verify entered password against stored hash
def Verify_Password(plain_password, hash_password):
    return pwd_context.verify(plain_password, hash_password)

# Function to create JWT access token
def create_token(data: dict):
    # Copy user data
    to_encode = data.copy()

    # Set token expiration time
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)

    # Add expiration claim to payload
    to_encode.update({"exp": expire})

    # Generate JWT token
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return token

# Login API using OAuth2 form data
@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):

    # Fetch user from database
    user = fake_user_db.get(form_data.username)

    # Validate username and password
    if not user or not Verify_Password(
        form_data.password,
        user["hashed_password"]
    ):
        raise HTTPException(
            status_code=400,
            detail="Invalid username or password"
        )

    # Generate access token with username stored in "sub" claim
    access_token = create_token(
        {"sub": form_data.username}
    )

    # Return token to client
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

# Function to verify JWT token
def verify_token(token: str = Depends(oauth_schema)):
    try:
        # Decode JWT token
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        # Extract username from token payload
        username: str = payload.get("sub")

        # Check if username exists
        if username is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid Token"
            )

        return username

    except jwt.JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )

# Protected API route
@app.get("/protected")
def protect_route(username: str = Depends(verify_token)):
    return {
        "message": "Hello! you have access to this protected route!",
        "user": username
    }