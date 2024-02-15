from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

response = client.chat.completions.create(
  model = "gpt-3.5-turbo-0125",
  temperature = 0.8,
  max_tokens = 3000,
  response_format={ "type": "json_object" },
  messages = [
    {"role": "system", "content": "You are a funny comedian who tells dad jokes. The output should be in JSON format."},
    {"role": "user", "content": "Write a dad joke related to numbers."},
    {"role": "assistant", "content": "Q: How do you make 7 even? A: Take away the s."},
    {"role": "user", "content": "Write one related to programmers."}
  ]
)

print(response.choices[0].message.content)
