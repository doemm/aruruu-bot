import logging
import json

from helpers import *
from pathlib import Path
from telegram.ext import (
    Updater, CommandHandler
)

# build absolute path from base path
base_path = Path(__file__).parent
# get tokens from file and set global
tokens_path = (base_path/'./tokens.json').resolve()
with open(tokens_path) as f:
    tokens = json.load(f)

# enable logging info
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def init_commands(dispatcher):
    # initialize command handlers
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(CommandHandler('stock', stock, pass_args=True))

def main():
    # pass token into updater
    updater = Updater(token=tokens['tg_token'], use_context=True)

    # register handlers with dispatcher
    dispatcher = updater.dispatcher
    
    # handle all the commands
    init_commands(dispatcher)

    # start the bot
    updater.start_polling()
    print('start running aruruu bot...')

    # bot running until ctrl-c to terminate
    updater.idle()

if __name__ == '__main__':
    main()
