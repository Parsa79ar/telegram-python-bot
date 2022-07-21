#!/usr/bin/python
import logging
import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters



# Loging configuration
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Bot Token
bot_token = "Your bot token"

# Send a message when the command /start is issued.
def start(update, context):
    update.message.reply_text('Hi!')

# Send a message when the command /help is issued.
def help(update, context):
    update.message.reply_text('Help!')


# Echo the user message.
def echo(update, context):
    print(update["message"])
    message = update.message
    logging.info(f'New Message => Channel: "{message.chat.title}" - text: "{message.text}"')


# Log Errors caused by Updates.
def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    updater = Updater(bot_token, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()


if __name__ == '__main__':
    main()