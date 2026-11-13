from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key='any')

messages = [
    {"role": "system", "content": "This is the Chat Application."},
]

print("--- チャットアプリ --- \n")
print("終了するには /quit と入力\n\n")

while True:
    print("あなた: ")
    input_txt = input(">> ")
    
    if input_txt == "/quit":
        break
    if input_txt == "":
        print("終了するには /quit と入力")
        continue
    
    messages.append({"role": "user", "content": input_txt})
    
    res = client.chat.completions.create(
            model="google/gemma-4-e4b",
            messages=messages,
            temperature=0.7,
    ).choices[0].message.content

    print()
    print("AI: ")
    print(res)
    print()
    messages.append({"role": "assistant", "content": res})