import random
import logging
import files
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import Filters
from telegram.ext import MessageHandler
from configparser import ConfigParser
from request_json import get_random_cat
from request_json import get_random_dog
from ig_scraper import get_random_ig_images


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.DEBUG)

config_parser = ConfigParser()
config_parser.read('config.ini')
TOKEN = config_parser['Bot']['Token']
USERNAME = config_parser['Credits']['username']
IG_USERNAME = config_parser['Credentials']['username']
IG_PASSWORD = config_parser['Credentials']['password']

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    greet_sticker = 'CAACAgEAAxkBAAL_v17-Nqi0j6rUs3ed4bSxE0K4kgd-AAJ4AAMWxqQJZTrUpaRtkRgaBA'
    context.bot.send_message(chat_id = update.effective_chat.id, text = "*Capy says hi*")
    context.bot.send_sticker(chat_id = update.effective_chat.id, sticker = greet_sticker)


def credit(update,context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = ' '.join(["Programmed by:",USERNAME]))
    context.bot.send_message(chat_id = update.effective_chat.id, text = "Source code at: https://github.com/jefferson10147/Capy-Telegram-bot")


def random_cat(update,context):
    url = get_random_cat()
    context.bot.send_photo(chat_id = update.effective_chat.id, photo = url)


def random_dog(update,context):
    url = get_random_dog()
    context.bot.send_photo(chat_id = update.effective_chat.id, photo =  url)


def get_random_sticker(update,context):
    sticker_id = files.get_random_line('./stickers/random_stickers_id.txt')
    context.bot.send_sticker(chat_id = update.effective_chat.id, sticker = sticker_id)


def add_sticker(update,context):
    sticker_id = ''.join([update.message.sticker.file_id,'\n'])
    files.write_file('./stickers/capy_stickers_id.txt',sticker_id)
    context.bot.send_message(chat_id = update.effective_chat.id, text = "*Capy have saved your sticker*")


def get_random_media(update,context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = "*Capy is searching in ig some images...*")
    parameters = update.message.text.split()
    tag = parameters[1]
    number_images = int(parameters[2])
    
    links = get_random_ig_images(IG_USERNAME,IG_PASSWORD,tag,number_images)
    for link in links:
        context.bot.send_photo(chat_id = update.effective_chat.id, photo = link)

    context.bot.send_message(chat_id = update.effective_chat.id, text = "*Capy have finished*")


def unknow(update,context):
    sticker_id = files.get_random_line('./stickers/random_stickers_id.txt')
    context.bot.send_sticker(chat_id = update.effective_chat.id, sticker = sticker_id)


def start_handlers ():
    start_handler = CommandHandler('start', start)
    random_cat_handler = CommandHandler('cat',random_cat)
    random_dog_handler = CommandHandler('dog',random_dog)
    random_sticker_handler = CommandHandler('sticker',get_random_sticker)
    random_media_handler = CommandHandler('media',get_random_media)
    credit_handler = CommandHandler('credits',credit)
    add_sticker_handler = MessageHandler(Filters.sticker,add_sticker)
    unknow_handler = MessageHandler(Filters.text,unknow)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(random_cat_handler)
    dispatcher.add_handler(random_dog_handler)
    dispatcher.add_handler(random_sticker_handler)
    dispatcher.add_handler(random_media_handler)
    dispatcher.add_handler(credit_handler)
    dispatcher.add_handler(add_sticker_handler)
    dispatcher.add_handler(unknow_handler)


if __name__ == '__main__':
    start_handlers()
    updater.start_polling()
    updater.idle()