from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.staticfiles import StaticFiles
import os
import shutil

app = FastAPI()

# 1 Ensure upload folder exist
UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

# 2 Static file set-up
app.mount("/files", StaticFiles(directory=UPLOAD_DIR), name="files")

# 3 Upload file API
@app.post("/upload")
def upload_file(file: UploadFile = File(...)):
    filename = file.filename
    file_path = os.path.join(UPLOAD_DIR, filename)

    if not filename:
        raise HTTPException(
            status_code = 400,
            detail= "File not selected"
        )
    
    with open(file_path, "wb") as buffer:
        shutil.copyfile(file.file, buffer)

    return {
        "Message": "File uploaded successfully",
        "fileName": filename,
        "file_url": f"http://127.0.0.1:8000/files/{filename}"
    }
    
# 4 Get file URL API
@app.get("/files/{filename}")
def get_file(filename: str):
    file_path = os.path.join(UPLOAD_DIR, filename)

    if not os.path.exists(file_path):
        raise HTTPException(
            status_code=404,
            detail="File not found"
        )
    
    return {
        "file_url": f"http://127.0.0.1:8000/files/{filename}"
    }

@app.get("/")
def home():
    return{
        "message": "File Uploaded API Running"

    }