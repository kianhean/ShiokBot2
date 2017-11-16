import os
import json
import requests
import telepot
from telepot.exception import TelegramError

import configparser

# Set Keys from Config
config = configparser.ConfigParser()
config.sections()
config.read('./enviroment.ini')

shiokapi_url = config['development']['SHIOK_API_HTTP']

CHANNEL_ID = '-1001311613849'

# The main URL for the Telegram API with our bot's token
bot = telepot.Bot(os.environ.get('TELEGRAM_TOKEN'))

""" All the command and chat handlers """

def start(chat_id):
    """ Start Command """
    bot.sendMessage(chat_id, text='Hi! I am a Telegram Bot!!')


def weather(chat_id):
    """ Weather Command """
    weather1 = requests.get(shiokapi_url + "weather").text.replace('"','')
    weather2 = requests.get(shiokapi_url + "weatherwarning").text.replace('"','')
    weather3 = requests.get(shiokapi_url + "weathermap").text.replace('"','')

    bot.sendMessage(chat_id, text=weather2, parse_mode="HTML")
    bot.sendMessage(chat_id, text=weather1, parse_mode="HTML")
    bot.sendPhoto(chat_id, photo=weather3)


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
            response = "/start"
            start(chat_id)
        elif message['text'] == '/weather':
            response = "/weather"
            weather(chat_id)
        else:
            response = "_NOACTION_"
    except TelegramError:
        print("If this is the local enviroment then all is good ;)")

    return {'content_type':content_type, 'chat_id':chat_id, 'response': response}
