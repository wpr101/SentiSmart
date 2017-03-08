from googlefinance import getQuotes
import json
import pandas as pd
import os


path = 'Mar7_8/'
file_name = 'Very_High_Quality Mar-07-2017'

for file_name in os.listdir(path):
    if file_name.endswith(".csv"): 
        print(os.path.join(path, file_name))

        #df = pd.read_csv( path + file_name + '.csv')
        df = pd.read_csv( os.path.join(path, file_name))

        symbol_list = list(df['Symbol'])
        for i in range(len(symbol_list)):
            symbol_list[i] = symbol_list[i].strip()

        buy_price_list = list(df['Last Trade'])
        sell_price_list = []
        output_list = []

        for i in range(len(symbol_list)):
            try:
                sell_price = getQuotes(symbol_list[i])[0]['LastTradeWithCurrency']
                #print(symbol_list[i], str(buy_price_list[i]), sell_price)
                output_list.append(symbol_list[i] + ' ' + str(buy_price_list[i]) + ' ' + str(sell_price))
            except Exception:
                print('bad symbol', symbol_list[i])
          

        text_file = open(path + file_name + "_RESULTS.txt", "w")
        for i in range(len(output_list)):

            text_file.write(output_list[i] + '\n')

        text_file.close()
