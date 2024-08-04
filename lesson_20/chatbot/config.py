# chatbot/config.py
""" 
Файл налаштування config.py містить: 
 - токен бота 
"""

from os import environ as env

from dotenv import load_dotenv


load_dotenv()

TOKEN = env['TOKEN']