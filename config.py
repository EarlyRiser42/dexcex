from dotenv import load_dotenv
import os

load_dotenv()

telegram_id = os.getenv("Telegram_id")
telegram_hash = os.getenv('Telegram_hash')
telegram_upbit_token = os.getenv('Telegram_upbit_token')
telegram_error_token = os.getenv('Telegram_error_token')

binance_id = os.getenv("binance_id")
binance_hash = os.getenv('binance_hash')
