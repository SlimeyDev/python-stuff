import json
import requests

chatbot = True


def chatbot():
    
    author_input = input()

    chat_endpoint = f"https://pixel-api-production.up.railway.app/fun/chatbot/?message={author_input}?name="
    chat_response = requests.get(chat_endpoint).json()
    chat_message = chat_response["message"]

    print(chat_message)

if chatbot == True:

    chatbot()