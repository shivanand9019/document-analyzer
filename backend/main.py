from fastapi import FastAPI,File, UploadFile,HTTPException
from services.pdf_processing import extract_text_from_pdf

app = FastAPI()

@app.get("/")
def home():
	return {"Backend is running!!"}


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    
    
    allowed_types = [
    "application/pdf",
    ]
    if file.content_type not in allowed_types:
         raise HTTPException(status_code=400, detail="Unsupported file type. Please upload a PDF, PNG, JPEG, or DOCX file.")
    
    file_location = f"uploads/{file.filename}"

    with open(file_location, "wb") as f:
        f.write(await file.read())
    text = extract_text_from_pdf(file_location)


    return {
        "message": "File uploaded successfully",
        "filename": file.filename,
        "text":text,
        "content_type": file.content_type,
        "text_length": len(text) if text else 0
    }


			
			
