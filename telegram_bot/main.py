import telegram.ext
import pandas_datareader as web

with open('token.txt', 'r') as f:
    TOKEN = f.read()


def start(update, context):
    update.message.reply_text("Hello, welcome to renshubot !")


def help(update, context):
    update.message.reply_text("""
    The following commands are available:
    /start => Welcome Message
    /help => Help center
    /content => Info about Tele Bot
    /contact => Info about contact
    /stock *** => Stock about company
    """)


def content(update, context):
    update.message.reply_text("Watch me on YouTube!")


def contact(update, context):
    update.message.reply_text("Don't forget to contact me!")


def handle_message(update, context):
    update.message.reply_text(f"You said {update.message.text}")


def stock(update, context):
    ticker = context.args[0]
    data = web.DataReader(ticker, 'yahoo')
    price = data.iloc[-1]['Close']

    update.message.reply_text(f"The current price of {ticker} is ${price:.2f}!")


updater = telegram.ext.Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(telegram.ext.CommandHandler("start", start))
dispatcher.add_handler(telegram.ext.CommandHandler("help", help))
dispatcher.add_handler(telegram.ext.CommandHandler("content", content))
dispatcher.add_handler(telegram.ext.CommandHandler("contact", contact))
dispatcher.add_handler(telegram.ext.CommandHandler("stock", stock))
dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))

updater.start_polling()
updater.idle()
