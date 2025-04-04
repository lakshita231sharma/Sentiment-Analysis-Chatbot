from fastapi import FastAPI, Request
from pydantic import BaseModel
from textblob import TextBlob

app = FastAPI()

class ChatRequest(BaseModel):
    user_id: str
    message: str
@app.get("/")  # 👈 ADD THIS
def root():
    return {"message": "Hello! Chatbot is running 🚀"}

@app.post("/chat")
async def chat(request: ChatRequest):
    text = request.message
    analysis = TextBlob(text)
    sentiment = analysis.sentiment.polarity  # Polarity ranges from -1 (negative) to 1 (positive)

    if sentiment > 0:
        sentiment_label = "Positive 😊"
    elif sentiment < 0:
        sentiment_label = "Negative 😞"
    else:
        sentiment_label = "Neutral 😐"

    return {
        "user_id": request.user_id,
        "message": text,
        "sentiment": sentiment_label
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
