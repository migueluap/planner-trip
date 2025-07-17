import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

print(os.getenv("OPENAI_API_KEY"))

client = OpenAI(
     api_key = os.getenv("OPENAI_API_KEY")
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Vou viajar para Londres em novembro de 2025. Quero que faça um roteiro de viagem para mim"
        }
    ]
)

print(completion.choices[0].message.content)
# print(completion)

