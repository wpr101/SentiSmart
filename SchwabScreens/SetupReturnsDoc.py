from googlefinance import getQuotes
import pandas as pd
import time

path = 'Mar14_15/'
file_name = 'BasicPE_Technicals Mar-14-2017'
bad_symbol_list = ['USLV']

df = pd.read_csv( path + file_name + '.csv')

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
        try:
            if (symbol_list[i] in bad_symbol_list):
                continue
            #rate limit on google, appears 2 per second is okay
            time.sleep(.55)
            quote = getQuotes(symbol_list[i])
            sell_price = quote[0]['LastTradeWithCurrency']
            index = quote[0]['Index']
            #Only look at NYSE and NASDAQ
            if (index == 'NYSE' or index == 'NASDAQ'):
                output_list.append(symbol_list[i] + ' ' + 
                str(buy_price_list[i]) + ' ' + str(sell_price))
        except Exception:
            pass
            #print('bad symbol', symbol_list[i])
    
    #Remove bad path file symbols      
    output_name = columns_list[column].replace('/', '')
    output_name = output_name.replace(u"\u00AE", '')

    text_file = open(path + output_name + "_RESULTS.txt", "w")
    for i in range(len(output_list)):

        text_file.write(output_list[i] + '\n')

    text_file.close()
