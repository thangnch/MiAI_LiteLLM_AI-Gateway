# pip install litellm python-dotenv
from dotenv import load_dotenv
from litellm import Router

load_dotenv()  # đọc OPENAI_API_KEY, GEMINI_API_KEY từ .env

msgs = [{"role": "user", "content": "Kể tên 5 món đặc sản ngon nhất của Hà Nội trong 100 chữ"}]

router = Router(
    model_list=[
        # Azure "hỏng": cố tình sai model và không có API KEY
        {"model_name": "chat",
         "litellm_params": {"model": "azure/gpt-3"}},
        # Dự phòng 1: OpenAI
        {"model_name": "chat",
         "litellm_params": {"model": "openai/gpt-4o"}},
        # Dự phòng 2: Gemini
        {"model_name": "backup",
         "litellm_params": {"model": "gemini/gemini-2.5-flash"}},
    ],
    fallbacks=[{"chat": ["backup"]}],  # lỗi -> thử lần lượt
    num_retries=1,   # thử lại 1 lần rồi fallback, demo cho nhanh
    timeout=10,
)

r = router.completion(model="chat", messages=msgs)
print("Model trả lời :", r.model)
print(r.choices[0].message.content)