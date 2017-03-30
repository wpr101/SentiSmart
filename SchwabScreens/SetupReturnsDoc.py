from googlefinance import getQuotes
from yahoo_finance import Share
import pandas as pd
import time
import os

QUOTE_SOURCE = 'GOOGLE' #or YAHOO

path = 'March/Mar29_30/'
bad_symbol_list = ['USLV']
symbol_price_map = {}

for file_name in os.listdir(path):
    #if (file_name.endswith(".csv") and (not ('TRADING' in file_name))): 
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

            #Get real time quotes from GOOGLE
            if (QUOTE_SOURCE == 'GOOGLE'):
                try:
                    sell_price = getQuotes(symbol_list[i])[0]['LastTradePrice']
                    #check for large prices which contain a comma
                    if (',' in sell_price):
                        sell_price = sell_price.replace(',', '')
                    index = getQuotes(symbol_list[i])[0]['Index']
                except Exception:
                    print('****BAD SYMBOL****')
                    bad_symbol_list.append(symbol_list[i])
                    continue
                #Google rate limit, approximately 2 quotes per second allowed
                time.sleep(.55)


                if (sell_price is None):
                    print('****BAD SYMBOL****')
                    bad_symbol_list.append(symbol_list[i])
                    continue

                if (index == 'NYSE' or index == 'NASDAQ'):
                    symbol_price_map[symbol_list[i]] = sell_price
                else:
                    bad_symbol_list.append(symbol_list[i])
            
            #Get real time qutoes from YAHOO
            elif (QUOTE_SOURCE == 'YAHOO'):
                try:
                    quote = Share(symbol_list[i])
                    sell_price = quote.get_price()
                except Exception:
                    print('****BAD SYMBOL****')
                    bad_symbol_list.append(symbol_list[i])
                    continue

                if (sell_price is None):
                    print('****BAD SYMBOL****')
                    bad_symbol_list.append(symbol_list[i])
                    continue

                symbol_price_map[symbol_list[i]] = sell_price
              
                

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
