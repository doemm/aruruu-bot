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
