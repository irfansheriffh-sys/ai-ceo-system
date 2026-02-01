from fastapi import FastAPI
from ceo_ai import ceo_ai

app = FastAPI()

@app.get("/")
def home():
    return {"status": "AI-CEO backend running"}

@app.post("/run")
def run_ai(data: dict):
    idea = data.get("idea", "")
    result = ceo_ai(idea)
    return result
