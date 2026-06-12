import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Read values
api_key = os.getenv("API_KEY")
base_url = os.getenv("BASE_URL")
model_name = os.getenv("MODEL_NAME")

# Create client
client = OpenAI(
    api_key=api_key,
    base_url=base_url
)

print("🤖 AI Chatbot Started")
print("Type 'exit' to stop\n")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot stopped.")
        break

    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {
                "role": "system",
                "content": "You are an Azure AI Trainer helping students learn cloud and AI."
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    ai_reply = response.choices[0].message.content

    print("\nAI:")
    print(ai_reply)
    print("\n" + "-"*50 + "\n")