""" Bot entry point script. chatbot/__main__.py"""

from chatbot import __app_name__
from chatbot.app import bot

if __name__ == '__main__':
	print(f'\nStarted telegram bot {__app_name__}\n')
	bot.infinity_polling()