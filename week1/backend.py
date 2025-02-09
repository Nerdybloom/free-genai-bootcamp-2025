from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Translator API is running"}

@app.get("/translate/")
def translate(text: str):
    return {"translated_text": f"Translation of '{text}'", "explanation": "Example explanation"}

