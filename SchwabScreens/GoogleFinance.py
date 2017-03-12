from googlefinance import getQuotes

dow_price = getQuotes('DJI')[0]['LastTradePrice']
nasdaq_price = getQuotes('IXIC')[0]['LastTradePrice']
print(nasdaq_price)
