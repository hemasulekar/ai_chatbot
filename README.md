Local AI Chatbot 🤖

A simple local AI chatbot built with Python and Ollama.
This project allows you to run an AI model locally on your computer and interact with it through the terminal.

Features

- Runs completely locally (no API cost)
- Uses Llama 3 model through Ollama
- Simple command-line chatbot interface
- Maintains conversation history

Requirements

- Python 3.10+
- Ollama installed

Installation

1. Install Ollama from the official website.

2. Pull and run the model:

ollama run llama3

3. Install Python dependencies:

pip install -r requirements.txt

Run the Chatbot

python local_chatbot.py

Example

You: Explain black holes simply
AI: A black hole is a region in space where gravity is so strong that nothing can escape it.

Project Structure

ai-chatbot/
│
├── local_chatbot.py
├── requirements.txt
├── README.md
└── .gitignore

Technologies Used

- Python
- Ollama
- Llama 3

Author

Created as part of learning AI application development.
