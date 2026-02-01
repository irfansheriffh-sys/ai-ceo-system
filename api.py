from fastapi import FastAPI
from ceo_ai import ceo_ai

app = FastAPI()

@app.get("/")
def health():
    return {"status": "AI-CEO backend running"}

@app.post("/run")
def run_ai(payload: dict):
    idea = payload.get("idea", "")
    return ceo_ai(idea)
