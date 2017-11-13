import os
import json
import requests
import telepot
from telepot.exception import TelegramError

CHANNEL_ID = '-1001311613849'

# The main URL for the Telegram API with our bot's token
bot = telepot.Bot(os.environ.get('TELEGRAM_TOKEN'))

""" All the command and chat handlers """

def start(chat_id):
    """ Start Command """
    bot.sendMessage(chat_id, text='Hi! I am a Telegram Bot!!')


def read_message(message):
    """ Returns Message as Dictionary """

    if isinstance(message, dict):
        message = message['message']
    else:
        message = json.loads(message)['message']

    return message


def handle(message):
    """ Handle JSON Message from Telegram 
        
        message - string 
        http://telepot.readthedocs.io/en/latest/reference.html
    """

    message = read_message(message)
    content_type, chat_type, chat_id = telepot.glance(message)

    try:
        if message['text'] == '/start':
            start(chat_id)
            response = "/start"
        else:
            response = "_NOACTION_"
    except TelegramError:
        print("If this is the local enviroment then all is good ;)")

    output = {'content_type':content_type, 'chat_id':chat_id, 'response': response}

    return output
