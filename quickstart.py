# pip install litellm python-dotenv
from dotenv import load_dotenv
from litellm import completion

load_dotenv()  # đọc các biến trong file .env vào biến môi trường

response = completion(
    model="openai/gpt-4o",
    messages=[{"role": "user",
               "content": "Giải thích LLM trong 1 câu"}],
)
print(response.choices[0].message.content)