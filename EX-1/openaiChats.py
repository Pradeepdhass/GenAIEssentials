from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

SYSTEM_PROMPT = "You are a helpful assistant. Answer directly and do not show your reasoning."

while True:
    question = input("Ask something: ")

    if question.lower() in ["exit", "quit"]:
        break

    response = client.responses.create(
        model="openai/gpt-oss-20b",
        input=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question}
        ],
    )

    print(response.output[0].content[0].text)