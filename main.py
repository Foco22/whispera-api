from fastapi import FastAPI, Request, HTTPException, UploadFile,File
from psycopg2.extras import RealDictCursor
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import requests
from servicewhisper import WhisperClass
from typing import List
from fastapi.responses import JSONResponse, RedirectResponse

load_dotenv()

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/api/whisper")
async def handler(files: List[UploadFile] = File(...)):
    if not files:
        raise HTTPException(status_code=400, detail="Solo un archivo")    

    results_ = []
    for file in files:

        whisper_class = WhisperClass(file)  
        response = whisper_class.main()
        results_.append(
            {
                'duration': response['process'],
                'filename': response['filename'],
                'text': response['text'],
            }
        )
        
    return JSONResponse(content={'results':results_})



