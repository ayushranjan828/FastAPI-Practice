from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home_page():
    return "This is the home page"

@app.get("/about")
def about_page():
    return {"message" : "This is the about page"}

@app.get("/contact")
def contact_page():
    return {
        "Name" : "Ayush Ranjan",
        "Age" : 22,
        "Email" : "ayushranjan94300@gmail.com"
    }