import ccxt
from config import binance_id, binance_hash
from binance.client import Client

def spot_balance():
    balance = binance.fetch_balance()['USDT']
    return balance["free"]


def get_current_price():
    price=binance.fetch_ticker("BTC/USDT")
    print(price)


def buy_market_order(symbol, amount):
    order = binance.create_market_buy_order(
        symbol=symbol,
        amount=amount
    )
    return order


def buy_limit_order(symbol,amount,price):
    order = binance.create_limit_buy_order(
        symbol=symbol,
        amount=amount,
        price=price
    )


def stop_loss(symbol, amount, price):
    binance.create_order(symbol=symbol, type='STOP', side='sell', amount=amount, price=price,  params={'stopPrice': price})


def get_position(symbol):
    balance = binance.fetch_balance()
    positions = balance['info']['positions']
    symbol2 = symbol.replace("/", "")
    for position in positions:
        if position["symbol"] == symbol2:
            price = int(position['entryPrice'])
            amount = int(position['positionAmt'])
    return price, amount


binance = ccxt.binance(config={
    'apiKey': binance_id,
    'secret': binance_hash
})

client = Client(binance_id, binance_hash)

