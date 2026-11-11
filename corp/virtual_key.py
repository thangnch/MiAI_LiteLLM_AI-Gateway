from openai import OpenAI      # vẫn là thư viện OpenAI!

client = OpenAI(
    api_key="sk-pc0WLFep6d_uV3rsqX9krA",             # virtual key của team
    base_url="http://localhost:4000",  # trỏ về Gateway
)
r = client.chat.completions.create(
    model="openai_gpt",                    # tên trong config.yaml
    messages=[{"role": "user", "content": "Xin chào!"}],
)

print("Model trả lời:", r.model)
print(r.choices[0].message.content)
print("Token đã dùng:", r.usage.total_tokens)
