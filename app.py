import os
import random
import json
import configparser
import requests
import telepot
from telepot.exception import TelegramError

from emoji import emojize

# Set Keys from Config
config = configparser.ConfigParser()
config.sections()
config.read('./enviroment.ini')
shiokapi_url = config['development']['SHIOK_API_HTTP']
channel_id = config['development']['CHANNEL_ID']

# The main URL for the Telegram API with our bot's token
bot = telepot.Bot(os.environ.get('TELEGRAM_TOKEN'))


def ask_shiokapi(endpoint):
    """ helper function to get results from shiokapi """
    return json.loads(requests.get(shiokapi_url + endpoint).text)

def personality(topic):
    """ helper function to get shiokbot's personality! """
    personailty = list(json.load(open("personality.json"))[topic])
    return emojize(random.choice(personailty), use_aliases=True)


""" All the command and chat handlers """

def start(chat_id):
    """ Start Command """
    bot.sendMessage(chat_id, text='Hi! I am a Telegram Bot!!')


def weather(chat_id):
    """ Weather Command """

    bot.sendMessage(chat_id, text=personality("weather"))
    bot.sendChatAction(chat_id, "typing")

    weather1 = ask_shiokapi("weather")
    weather2 = ask_shiokapi("weatherwarning")
    weather3 = ask_shiokapi("weathermap")

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
