from googlefinance import getQuotes

sell_price = getQuotes('REI')[0]['LastTradePrice']
print(sell_price)
