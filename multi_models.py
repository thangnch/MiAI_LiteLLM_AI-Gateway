# pip install litellm python-dotenv
from dotenv import load_dotenv
from litellm import completion

load_dotenv()  # đọc OPENAI_API_KEY, GEMINI_API_KEY từ file .env

models = [
    "openai/gpt-4o",
    "gemini/gemini-2.5-flash",
]
question = [{"role": "user", "content": "Bún chả là gì? Viết ngắn gọn trong 100 từ thôi."}]

for m in models:
    r = completion(model=m, messages=question)
    print(f"--- {m}\n{r.choices[0].message.content}")