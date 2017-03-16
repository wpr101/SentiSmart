'''from googlefinance import getQuotes

dow_price = getQuotes('DJI')[0]['LastTradePrice']
nasdaq_price = getQuotes('IXIC')[0]['LastTradePrice']
print(nasdaq_price)'''

from yahoo_finance import Share

yahoo = Share('YHOO')

print(yahoo.get_price())
