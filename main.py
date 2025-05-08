from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

class ChatRequest(BaseModel):
    user_input: str
    llm_choice: str

@app.post("/chat/")
async def chat(request: ChatRequest):
    # Call the selected LLM using LiteLLM
    response = requests.post(f"https://api.openrouter.ai/{request.llm_choice}", json={"input": request.user_input})
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="LLM call failed")
    return response.json()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Chat Assistant API!"}