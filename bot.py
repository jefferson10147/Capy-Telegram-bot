import logging
from telegram.ext import Updater
from telegram.ext import CommandHandler
from request_json import get_ramdon_cat
from request_json import get_ramdon_dog

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

TOKEN = '935538322:AAGJE2zDh2UeTCI2cXC6jBy-0yjdR0DDG34'
updater = Updater(token=TOKEN, use_context=True)

dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text = "hi uwu")

def ramdon_cat(update,context):
    url = get_ramdon_cat()
    context.bot.send_photo(chat_id=update.effective_chat.id, photo = url)

def ramdon_dog(update,context):
    url = get_ramdon_dog()
    context.bot.send_photo(chat_id = update.effective_chat.id, photo =  url)

start_handler = CommandHandler('start', start)
ramdon_cat_handler = CommandHandler('cat',ramdon_cat)
ramdon_dog_handler = CommandHandler('dog',ramdon_dog)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(ramdon_cat_handler)
dispatcher.add_handler(ramdon_dog_handler)

updater.start_polling()
updater.idle()