import pypdf
from fastapi import HTTPException

def extract_text_from_pdf(file_path):
   
    try:
        text = ""
        with open(file_path,"rb") as file:
            reader = pypdf.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text()

        return text
    except Exception as e:
        return HTTPException(status_code=500, detail="Error processing the PDF file.")
    