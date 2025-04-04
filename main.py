from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

# Define a Pydantic model for request data
class ChatRequest(BaseModel):
    user_id: str
    message: str

@app.post("/chat")
async def chat(request: ChatRequest):
    return {"response": f"You said: {request.message}"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
