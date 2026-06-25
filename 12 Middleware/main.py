from fastapi import FastAPI, Request

app = FastAPI()

@app.middleware("http")
async def my_middleware(request: Request, call_next):
    print("Request Received")
    response = await call_next(request)
    print("Response Sent")
    return response