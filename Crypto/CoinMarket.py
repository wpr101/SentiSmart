import json
from coinmarketcap import Market
coin_market = Market()
json_data = coin_market.ticker().decode('utf-8')
data = json.loads(json_data)

for coin in data:
    if coin['percent_change_1h'] is not None:
        #check for volume over $1 million dollars
        if float(coin['24h_volume_usd']) > 1000000:
            percent_change_1h = float(coin['percent_change_1h'])
            if percent_change_1h > 10:
                print (coin['name'])





#HACK
#returns a dictionary with data for that coin
'''def get_coin_data(coin):
    coin_data = {}

    i = 0
    items = []
    while i < len(coin):
        if coin[i] == '\"':
            key = ''
            i += 1
            while(coin[i] != '\"'):
                key += coin[i]
                i += 1
            items.append(key)
        i += 1
        
    j = 0
    while j < len(items):
        coin_data[items[j]] = items[j+1]
        j += 2

    return(coin_data)

coins = ['bitcoin', 'ethereum', 'litecoin', 'monero']
for i in coins:
    coin = coin_market.ticker(i)
    coin = coin.decode("utf-8")
    coin_data = get_coin_data(coin)
    for key, value in coin_data.items():
        print (key, value)
    print('') '''
