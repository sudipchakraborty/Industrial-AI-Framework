from langchain_groq import ChatGroq
from app.config.settings import GROQ_API_KEY

print("GROQ KEY FOUND:", GROQ_API_KEY is not None)

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=GROQ_API_KEY
)