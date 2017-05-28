import json
import os
from datetime import datetime
from coinmarketcap import Market
from apscheduler.schedulers.blocking import BlockingScheduler

coin_market = Market()
json_data = coin_market.ticker().decode('utf-8')
data = json.loads(json_data)

path = 'Data'
poloniex_symbols = ['ETH', 'XRP', 'ETC', 'GNT', 'STR', 'DOGE', 'XEM', 'LTC',
                    'DGB', 'XMR', 'ZEC', 'SC', 'BCN', 'DASH', 'BTS', 'BTM',
                    'FCT', 'STEEM', 'STRAT', 'REP', 'LSK', 'SYS', 'NXT',
                    'MAID', 'GAME', 'ARDR', 'RIC', 'GNO', 'DCR', 'AMP', 'VTC',
                    'CLAM', 'BURST', 'BCY', 'LBC', 'SJCX', 'NAV', 'PINK', 
                    'BTCD', 'EXP', 'PPC', 'XCP', 'NEOS', 'NAUT', 'POT',
                    'PASC', 'BELA', 'EMC2', 'BLK', 'FLO', 'FLDC', 'NMC', 'GRC',
                    'XVC', 'XPM', 'OMNI', 'SBD', 'XBC', 'NXC', 'VRC', 'HUC',
                    'NOTE'
                    ]

def increasing():
    for coin in data:
        if coin['percent_change_1h'] is not None:
            #check for volume over $1 million dollars
            if float(coin['24h_volume_usd']) > 1000000:
                percent_change_1h = float(coin['percent_change_1h'])
                if percent_change_1h > 10:
                    print (coin['name'])



def data_to_file():
    directory = path + '/'
            
    if not os.path.exists(directory):
        os.makedirs(directory)
    text_file = open(directory + 
                str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + "_results.txt", "w")
    text_file.write('Coins meeting the filter' + '\n\n')
    for coin in data:
        change_1h = coin['percent_change_1h']
        rank = coin['rank']
        if (change_1h is None) or (rank is None):
            continue
        elif (float(change_1h) > 5) and (int(rank) <= 100):
            text_file.write(str(coin['name']) + '\n')
            text_file.write('Change_1h: ' + str(coin['percent_change_1h']) + '\n')
            text_file.write('Rank ' + str(coin['rank']))
            text_file.write('\n\n')

    text_file.close()


scheduler = BlockingScheduler()
scheduler.add_job(data_to_file, 'interval', minutes=.5)
scheduler.start()
