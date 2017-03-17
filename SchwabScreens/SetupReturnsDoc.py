from googlefinance import getQuotes
from yahoo_finance import Share
import pandas as pd
import time
import os

path = 'Mar16_17/'
#file_name = 'Everything_PE Mar-15-2017'
bad_symbol_list = ['USLV']
symbol_price_map = {}

for file_name in os.listdir(path):
    if file_name.endswith(".csv"): 
        print(os.path.join(path, file_name))

        #df = pd.read_csv( path + file_name + '.csv')
        df = pd.read_csv( os.path.join(path, file_name))

        symbol_list = list(df['Symbol'])
        #remove whitespace from symbols
        for i in range(len(symbol_list)):
            symbol_list[i] = symbol_list[i].strip()


        for i in range(len(symbol_list)):
            print(symbol_list[i])    
            #quote = Share(symbol_list[i])
            #sell_price = quote.get_price()
            #date_time = quote.get_trade_datetime()
            #print('sell_price', sell_price)
            #print('date_time', date_time)
            #print('')
            try:
                sell_price = getQuotes(symbol_list[i])[0]['LastTradePrice']
                index = getQuotes(symbol_list[i])[0]['Index']
            except Exception:
                print('****BAD SYMBOL****')
                bad_symbol_list.append(symbol_list[i])
                continue
            print(index)
            print('')
            time.sleep(.55)


            if (sell_price is None):
                print('****BAD SYMBOL****')
                bad_symbol_list.append(symbol_list[i])
                continue

            if (index == 'NYSE' or index == 'NASDAQ'):
                symbol_price_map[symbol_list[i]] = sell_price
            else:
                bad_symbol_list.append(symbol_list[i])

        columns_list = list(df.columns.values)

        #Loop through all the columns of the csv
        for column in range(len(columns_list)-1):

            #Sort the data frame, biggest numbers first
            df = df.sort_values(columns_list[column], ascending=False)

            symbol_list = list(df['Symbol'])
            for i in range(len(symbol_list)):
                symbol_list[i] = symbol_list[i].strip()

            buy_price_list = list(df['Last Trade'])
            sell_price_list = []
            output_list = []

            for i in range(len(symbol_list)): 
                if (symbol_list[i] not in bad_symbol_list):  
                    output_list.append(symbol_list[i] + ' ' + 
                    str(buy_price_list[i]) + ' ' + str(symbol_price_map[symbol_list[i]]))

            #Remove bad path file symbols      
            output_name = columns_list[column].replace('/', '')
            output_name = output_name.replace(u"\u00AE", '')

            folder_name = file_name.partition(' ')[0]
            directory = path + folder_name + '/'
            
            if not os.path.exists(directory):
                os.makedirs(directory)
            text_file = open(directory + output_name + "_RESULTS.txt", "w")
            for i in range(len(output_list)):

                text_file.write(output_list[i] + '\n')

            text_file.close()
