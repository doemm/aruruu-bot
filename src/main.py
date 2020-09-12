import logging

from helpers import *
from pathlib import Path
from telegram.ext import (
    Updater, CommandHandler
)

# build absolute path from base path
base_path = Path(__file__).parent

# enable logging info
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def init_commands(dispatcher):
    # initialize command handlers
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help))

def main():
    # get token key from file
    token_path = (base_path/'./TOKEN').resolve()
    with open(token_path) as f:
        token = f.read().rstrip('\n')
    # pass token into updater
    updater = Updater(token=token, use_context=True)

    # register handlers with dispatcher
    dispatcher = updater.dispatcher
    
    # handle all the commands
    init_commands(dispatcher)

    # start the bot
    updater.start_polling()
    print("start running aruruu bot...")

    # bot running until ctrl-c to terminate
    updater.idle()

if __name__ == '__main__':
    main()
