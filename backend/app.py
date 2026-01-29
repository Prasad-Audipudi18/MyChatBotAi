from fastapi import FastAPI
from pydantic import BaseModel
from assistant import ChatAssistant, answer_query
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv()
assistant = ChatAssistant(api_key=os.getenv("GOOGLE_API_KEY"))
class Query(BaseModel):
    text: str

@app.post("/query")
def get_answer(body: Query):
    try:
        response = answer_query(body.text, assistant)
        return {"answer": response}
    except Exception as e:
        return {"error": str(e)}
