#from googlefinance import getQuotes
from yahoo_finance import Share
import pandas as pd
import time
import os

path = 'Mar15_16/'
file_name = 'Everything_PE Mar-15-2017'
bad_symbol_list = ['USLV']
symbol_price_map = {}

df = pd.read_csv( path + file_name + '.csv')

#Get the sell prices from Yahoo and store in map
symbol_list = list(df['Symbol'])
for i in range(len(symbol_list)):
    print(symbol_list[i])
    quote = Share(symbol_list[i])
    sell_price = quote.get_price()
    #remove whitespace from the symbol
    symbol_list[i] = symbol_list[i].strip()
    symbol_price_map[symbol_list[i]] = sell_price

columns_list = list(df.columns.values)

#Loop through all the columns of the csv
for column in range(len(columns_list)-1):
    print(columns_list[column])
    #Sort the data frame, biggest numbers first
    df = df.sort_values(columns_list[column], ascending=False)
    
    symbol_list = list(df['Symbol'])
    for i in range(len(symbol_list)):
        symbol_list[i] = symbol_list[i].strip()

    buy_price_list = list(df['Last Trade'])
    sell_price_list = []
    output_list = []

    for i in range(len(symbol_list)):    
        output_list.append(symbol_list[i] + ' ' + 
        str(buy_price_list[i]) + ' ' + str(symbol_price_map[symbol_list[i]]))

    
    #Remove bad path file symbols      
    output_name = columns_list[column].replace('/', '')
    output_name = output_name.replace(u"\u00AE", '')

    directory = path + file_name + '/'
    if not os.path.exists(directory):
        os.makedirs(directory)
    text_file = open(directory + output_name + "_RESULTS.txt", "w")
    for i in range(len(output_list)):

        text_file.write(output_list[i] + '\n')

    text_file.close()
