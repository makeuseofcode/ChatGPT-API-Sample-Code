from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

response = client.chat.completions.create(
  model = "gpt-3.5-turbo",
  temperature = 0.8,
  max_tokens = 3000,
  messages = [
    {"role": "system", "content": "You are a poet who creates poems that evoke emotions."},
    {"role": "user", "content": "Write a short poem for programmers."}
  ]
)

print(response.choices[0].message.content)
