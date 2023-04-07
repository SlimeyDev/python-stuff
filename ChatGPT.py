import openai

openai.api_key = "####"

messages = []
system_msg = "chat"
messages.append({"role": "system", "content": system_msg})
message = input()
messages.append({"role": "user", "content": message})
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages)
reply = response["choices"][0]["message"]["content"]
messages.append({"role": "assistant", "content": reply})
print("\n" + reply + "\n")