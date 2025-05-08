from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class UserMessage(BaseModel):
    message: str

@app.post("/chat/")
async def chat(user_message: UserMessage):
    # Here you would integrate LiteLLM to get a response
    # For now, we will just echo the message back
    return {"response": f"You said: {user_message.message}"}

@app.get("/")
async def root():
    return {"message": "Welcome to the Chat Assistant!"}