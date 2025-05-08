from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx

app = FastAPI()

class UserMessage(BaseModel):
    message: str

@app.post("/chat/")
async def chat(user_message: UserMessage):
    # Here you would integrate LiteLLM to get a response
    # For now, we will just echo the message back
    async with httpx.AsyncClient() as client:
        response = await client.post('https://api.openrouter.ai/v1/llm', json={
            'model': 'gpt-3.5-turbo',  # Example model
            'prompt': user_message.message
        })
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error from LLM")
        return response.json()

@app.get("/")
async def root():
    return {"message": "Welcome to the Chat Assistant!"}