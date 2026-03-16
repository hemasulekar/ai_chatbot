import ollama

conversation = []

print("Local AI Chatbot (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    conversation.append({
        "role": "user",
        "content": user_input
    })

    response = ollama.chat(
        model="llama3",
        messages=conversation
    )

    ai_reply = response["message"]["content"]

    print("AI:", ai_reply, "\n")

    conversation.append({
        "role": "assistant",
        "content": ai_reply
    })
    