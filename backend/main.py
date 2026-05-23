from fastapi import FastAPI
import datetime

app = FastAPI()

@app.get("/")
def home():
	return {"Backend is running!!"}


@app.get("/project")

def project():

	return {"Project name :AI document analyzer",
			"Status: Building",
			"Date:" +str(datetime.datetime.now())
			}

