from telegram.ext import Updater
from telegram.ext import CommandHandler
import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

TOKEN = '1122265359:AAHo8OuC5bovxR3uAgI4WWVDVV5czrIv940'
updater = Updater(token=TOKEN, use_context=True)

dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="uwu")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
updater.idle()