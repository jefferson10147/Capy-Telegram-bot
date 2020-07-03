import random
import logging
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import Filters
from telegram.ext import MessageHandler
from request_json import get_random_cat
from request_json import get_random_dog
from configparser import ConfigParser

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.DEBUG)

config_parser = ConfigParser()
config_parser.read('config.ini')
TOKEN = config_parser['Bot']['Token']
updater = Updater(token=TOKEN, use_context=True)

dispatcher = updater.dispatcher

def start(update, context):
    greet_sticker = 'CAACAgEAAxkBAAL_v17-Nqi0j6rUs3ed4bSxE0K4kgd-AAJ4AAMWxqQJZTrUpaRtkRgaBA'
    context.bot.send_message(chat_id = update.effective_chat.id, text = "*Capy says hi*")
    context.bot.send_sticker(chat_id = update.effective_chat.id, sticker = greet_sticker)

def credit(update,context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = "Programmed by: @coquiUnet")
    context.bot.send_message(chat_id = update.effective_chat.id, text = "Source code at: https://github.com/jefferson10147/Capy-Telegram-bot")

def random_cat(update,context):
    url = get_random_cat()
    context.bot.send_photo(chat_id = update.effective_chat.id, photo = url)

def random_dog(update,context):
    url = get_random_dog()
    context.bot.send_photo(chat_id = update.effective_chat.id, photo =  url)

def get_random_sticker(update,context):
    with open('./stickers/random_stickers_id.txt','r') as file:
        lines = file.readlines()
        sticker_id = random.choice(lines).replace('\n','')
        context.bot.send_sticker(chat_id = update.effective_chat.id, sticker = sticker_id)

def add_sticker(update,context):
    sticker_id = ''.join([update.message.sticker.file_id,'\n'])
    with open('./stickers/random_stickers_id.txt','a') as file:
        file.write(sticker_id)
        context.bot.send_message(chat_id = update.effective_chat.id, text = sticker_id)

def unknow(update,context):
    with open('./stickers/capy_stickers_id.txt','r') as file:
        lines = file.readlines()
        sticker_id = random.choice(lines).replace('\n','')
        context.bot.send_sticker(chat_id = update.effective_chat.id, sticker = sticker_id)
    
start_handler = CommandHandler('start', start)
random_cat_handler = CommandHandler('cat',random_cat)
random_dog_handler = CommandHandler('dog',random_dog)
random_sticker_handler = CommandHandler('sticker',get_random_sticker)
credit_handler = CommandHandler('credits',credit)
add_sticker_handler = MessageHandler(Filters.sticker,add_sticker)
unknow_handler = MessageHandler(Filters.text,unknow)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(random_cat_handler)
dispatcher.add_handler(random_dog_handler)
dispatcher.add_handler(random_sticker_handler)
dispatcher.add_handler(credit_handler)
dispatcher.add_handler(add_sticker_handler)
dispatcher.add_handler(unknow_handler)

updater.start_polling()
updater.idle()