from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize DeepSeek (using OpenAI SDK setup)
openai.api_key = os.getenv("DEEPSEEK_API_KEY")
openai.api_base = "https://api.deepseek.com"  # Use DeepSeek's base URL

class Query(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(query: Query):
    try:
        # Use DeepSeek to generate a response
        response = openai.ChatCompletion.create(
            model="deepseek-chat",  # Replace with the appropriate DeepSeek model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": query.question},
            ]
        )
        return {"answer": response.choices[0].message.content.strip()}
    except Exception as e:
        # Handle errors and raise an HTTP exception
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while processing the request.")