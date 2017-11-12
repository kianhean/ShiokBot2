import requests
import os
import telepot

CHANNEL_ID = '-1001311613849'

# The main URL for the Telegram API with our bot's token
TOKEN = os.environ.get('TELEGRAM_TOKEN')
BASE_URL = "https://api.telegram.org/bot{}".format(TOKEN)

bot = telepot.Bot(TOKEN)


def handle(message):
    message = message['message']
    content_type, chat_type, chat_id = telepot.glance(message)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        bot.sendMessage(chat_id, message['text'])
