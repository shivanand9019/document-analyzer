from fastapi import FastAPI,File, UploadFile
from services.pdf_processing import extract_text_from_pdf

app = FastAPI()

@app.get("/")
def home():
	return {"Backend is running!!"}


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    
    file_location = f"uploads/{file.filename}"

    with open(file_location, "wb") as f:
        f.write(await file.read())

    text = extract_text_from_pdf(file_location)


    return {
        "message": "File uploaded successfully",
        "filename": file.filename,
        "text":text
    }


			
			
