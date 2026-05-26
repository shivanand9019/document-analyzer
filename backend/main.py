from fastapi import FastAPI
from fastapi import File, UploadFile

app = FastAPI()

@app.get("/")
def home():
	return {"Backend is running!!"}


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    
    file_location = f"uploads/{file.filename}"

    with open(file_location, "wb") as f:
        f.write(await file.read())

    return {
        "message": "File uploaded successfully",
        "filename": file.filename
    }


			
			
