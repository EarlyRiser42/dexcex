from telethon.sync import TelegramClient
from config import telegram_upbit_token, telegram_error_token
import telegram


def telegram_send_message(texts, token):
    bot = telegram.Bot(token)
    bot.sendMessage(chat_id="2138484218", text=texts)


telegram_send_message('tests', telegram_upbit_token)
