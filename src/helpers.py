import requests

from main import tokens
from str_prep import *

iex_baseurl = 'https://cloud.iexapis.com'

# reply back to start
def start(update, context):
    print('command /start received')
    # initial bot, receiver, message
    bot = context.bot
    receiver = update.message.chat_id
    message = '<b>aruruu</b> starts serving...'
    # send message
    bot.send_message(receiver, text=message, parse_mode='HTML')

def help(update, context):
    print('command /help received')

def stock(update, context):
    print('command /stock received')
    if (len(context.args) != 2):
        update.message.reply_text('/stock command error')
        return
    # perform actions
    action = context.args[0]
    key = context.args[1]
    if (action == 'search'):
        url = '{}/stable/stock/{}/quote?token={}'\
            .format(iex_baseurl, key, tokens['iex_token'])
        req = requests.get(url)
        if (req.status_code == 200):
            res = req.json()
            if (len(res['companyName']) > 25):
                name = res['companyName'][:25]+'...'
            else:
                name = res['companyName']
            symbol = res['symbol']
            old_price = res['previousClose']
            new_price = res['latestPrice']
            change = res['changePercent']*100
            pretty_res = stock_search_res\
                    .format(name, symbol,
                        old_price,  new_price, change)
            update.message.reply_text(pretty_res)
        else:
            update.message.reply_text('stock search not found')
