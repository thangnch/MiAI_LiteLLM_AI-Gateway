from idlelib.run import flush_stdout

from litellm import completion, completion_cost

msgs = [{"role": "user", "content": "Hãy kể về sự xuất hiện của Mì AI trong 100 từ"}]

# 1) Streaming: chữ hiện ra dần như ChatGPT
stream = completion(model="openai/gpt-4o", messages=msgs,
                    stream=True)
for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="")
    print()
    # flush_stdout()

# 2) Biết ngay mỗi lần gọi tốn bao nhiêu
r = completion(model="openai/gpt-4o", messages=msgs)
cost = completion_cost(completion_response=r)
print(f"\nChi phí: ${cost:.6f}")