import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise RuntimeError("GROQ_API_KEY not found in .env")

llm = ChatGroq(
    groq_api_key=api_key,
    model_name="llama-3.1-8b-instant" 
)

response = llm.invoke("What is the capital of France?")

try:
    print(response.content)
except AttributeError:
    print(response)