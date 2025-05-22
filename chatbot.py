from openai import OpenAI

# Replace with your actual OpenRouter API key (keep it secure!)
api_key = "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"  # DO NOT share this publicly

# Create the OpenRouter client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

messages = []
system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready!")
while True:
    user_input = input()
    if user_input.lower().strip() == "quit()":
        break
    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="openai/gpt-4.1-nano",
        messages=messages
    )
    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")