from googlefinance import getQuotes

sell_price = getQuotes('USLV')[0]['LastTradePrice']
print(sell_price)
