import requests
import os

CHANNEL_ID = '-1001311613849'

# The main URL for the Telegram API with our bot's token
TOKEN = os.environ.get('TELEGRAM_TOKEN')
BASE_URL = "https://api.telegram.org/bot{}".format(TOKEN)

def receive_message(msg):
    """Receive a raw message from Telegram"""
    try:
        message = str(msg["message"]["text"])
        chat_id = msg["message"]["chat"]["id"]
        return message, chat_id
    except Exception as e:
        print(e)
        return (None, None)

def handle_message(message):
    """Calculate a response to the message"""
    return message

def send_message(message, chat_id):
    """Send a message to the Telegram chat defined by chat_id"""
    data = {"text": message.encode("utf8"), "chat_id": chat_id}
    url = BASE_URL + "/sendMessage"
    try:
        response = requests.post(url, data).content
    except Exception as e:
        print(e)

def run(message):
    """Receive a message, handle it, and send a response"""
    try:
        message, chat_id = receive_message(message)
        response = handle_message(message)
        send_message(response, chat_id)
    except Exception as e:
        print(e)
