
from dotenv import load_dotenv
import os
from openai import OpenAI

# Load environment variables from .env
load_dotenv()

# Create OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Store conversation history
conversation = []

print("AI Chatbot (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    # Add user message to conversation
    conversation.append({
        "role": "user",
        "content": user_input
    })

    # Send conversation to AI
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=conversation
    )

    # Get AI reply
    ai_reply = response.choices[0].message.content

    # Print AI reply
    print("AI:", ai_reply, "\n")

    # Save AI reply to conversation memory
    conversation.append({
        "role": "assistant",
        "content": ai_reply
    })