"""
Chatbot backend for Streamlit (and optional CLI).
Copy of chatbot.py refactored for integration: get_response() + CLI under __main__.
"""
from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model

model = init_chat_model("mistral-small-2506", model_provider="mistralai", temperature=0.9)


def get_response(messages: list) -> str:
    """Invoke the model with conversation history and return assistant content."""
    response = model.invoke(messages)
    return response.content


if __name__ == "__main__":
    messages = []

    print("--------------------------------")
    print("Welcome to the Chatbot")
    print("Enter '0' to end the chat")
    print("--------------------------------")

    while True:
        prompt = input("You:")
        messages.append(prompt)
        if prompt == "0":
            print("Thank you for using the Chatbot...")
            print("--------------------------------")
            break

        response_content = get_response(messages)
        messages.append(response_content)
        print("Bot:", response_content)

    print(messages)
