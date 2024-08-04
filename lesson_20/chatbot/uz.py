from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

# Ваш токен
TOKEN = 'your-telegram-bot-token'

def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Купити квиток", url='https://booking.uz.gov.ua/')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        'Ви хочете купити квиток? Натисніть кнопку нижче, щоб перейти на сайт.',
        reply_markup=reply_markup
    )

def main():
    updater = Updater(TOKEN)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
