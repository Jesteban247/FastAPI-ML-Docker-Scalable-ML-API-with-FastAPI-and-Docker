# main.py

from fastapi import FastAPI, UploadFile, File
import io
from PIL import Image
from model import model_pipeline

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/ask")
async def ask(image: UploadFile = File(...)):
    content = await image.read()
    image = Image.open(io.BytesIO(content)).convert('RGB')
    
    result = model_pipeline(image)
    return {"caption": result}
